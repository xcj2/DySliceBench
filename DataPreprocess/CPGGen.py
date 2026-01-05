import os
import timeout_decorator
import subprocess
from concurrent.futures import ThreadPoolExecutor
from neo4j import GraphDatabase
import concurrent.futures
from collections import defaultdict

import pandas as pd
import time
import shutil
import tracemalloc

def run_command(command):
    print(f"Executing command: {command}")
    os.system(command)


# 第二个项目读取时，是否要清空当前内容
def loadNeo4j():
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "12345678"
    driver = GraphDatabase.driver(uri, auth=(username, password))
    return driver


def clearNeo4j():
    driver = loadNeo4j()
    deleteCyper = """
                MATCH (n)
                DETACH DELETE n
                """
    with driver.session() as session:
        session.run(deleteCyper)
    print("neo4j dataset clear successfully")


def generateBackSlice(criNum, criFile):  
    driver = loadNeo4j()

   
    criterionNodeIDSet = set([])  # 准则信息
    sliceNodeIdSet = set([]) 
    sliceNodePosSet = set([])  # 最后的结果存储   FIle_line

    # 1定位切片准则所在的节点
    locateCriCyper = """
            MATCH (method:METHOD {FILENAME: '"""+criFile+"""'})-[:CONTAINS]->(criNode)
            WHERE criNode.LINE_NUMBER = """ + str(criNum) + """ and method.NAME <> '<body>'
            RETURN criNode.id as criNodeID
            """
    with driver.session() as session:
        result = session.run(locateCriCyper)
        for record in result:
            # 提取节点
            criterionNodeID = record.get('criNodeID')  # 返回类型是int类型
            if criterionNodeID is not None:
                criterionNodeIDSet.add(criterionNodeID)
    
    # 2根据切片准则节点，进行切片遍历
    intraStartNodeIdList = list(criterionNodeIDSet)
    interStartNodeIdList = list(criterionNodeIDSet) #避免切片准则内就有函数调用

    interCount = 0

    while True:
        #intra遍历
        intraNodeIdList = generateBackSlice_Intra(driver, intraStartNodeIdList)
        
        #inter遍历
        interStartNodeIdList = list(set(interStartNodeIdList + intraNodeIdList))
        interReturnNodeIdList = generateBackSlice_Inter(driver, interStartNodeIdList)

        #结果存储
        sliceNodeIdSet = sliceNodeIdSet.union(set(intraNodeIdList))
        sliceNodeIdSet = sliceNodeIdSet.union(set(interReturnNodeIdList))

        #更新下一轮遍历起点
        intraStartNodeIdList = list(set(interReturnNodeIdList))
        interStartNodeIdList = []
        interCount += 1

        if len(interReturnNodeIdList) == 0 or interCount > 5:
            break
    
    # 3根据切片节点id，获取节点的位置信息
    sliceNodeIdList = list(sliceNodeIdSet)
    sliceNodePosSet = generateSlicePos(driver, sliceNodeIdList)

    # sliceNodePosSet_result.add("temp.java_"+str(criNum))  # 切片准则本身
    sliceNodePosSet.add(str(criFile)+"_"+str(criNum))  # 切片准则本身
    print("sliceNodePosSet")
    print(sliceNodePosSet)
    return sliceNodePosSet


def generateBackSlice_Intra(driver, intraStartNodeIdList):
    #根据函数内的节点id获取函数内可以后向遍历到达的节点
    intraNodeIdList = []
    for id in intraStartNodeIdList:
        cyper = """
                OPTIONAL MATCH (n)
                WHERE n.id=""" + str(id) + """
                OPTIONAL MATCH (intra)-[r1:REACHING_DEF|CDG|CONTAINS|ARGUMENT*1..12]->(n)
                RETURN intra.id as intraID, intra.LINE_NUMBER as intraLineNumber
                """
        with driver.session() as session:
            result = session.run(cyper)
            for record in result:
                intraID = record.get('intraID')
                intraLineNumber = record.get('intraLineNumber')
                if intraID is not None and intraLineNumber is not None and intraID not in intraNodeIdList:
                    intraNodeIdList.append(intraID)
    return intraNodeIdList



def generateBackSlice_Inter(driver, interStartNodeIdList):
    #根据函数间依赖传递，找到callee函数的起点，也就是return节点
    interNodeIdList = []
    for id in interStartNodeIdList:
        cypher = """
            OPTIONAL MATCH (n)  
            WHERE n.id=""" + str(id) + """
            OPTIONAL MATCH (n)-[:CALL]->(callee1)-[:CONTAINS]->(calleeReturn:RETURN)
            OPTIONAL MATCH (n)-[:CALL]->(callee2)-[:AST]->(paraOut:METHOD_PARAMETER_OUT)
            RETURN calleeReturn.id as calleeReturnID, calleeReturn.LINE_NUMBER as calleeReturnLineNumber, paraOut.id as paraOutID, paraOut.LINE_NUMBER as paraOutLineNumber
            """
        with driver.session() as session:
            result = session.run(cypher)
            for record in result:
                calleeReturnID = record.get('calleeReturnID')
                calleeReturnLineNumber = record.get('calleeReturnLineNumber')
                paraOutID = record.get('paraOutID')
                paraOutLineNumber = record.get('paraOutLineNumber')
                if calleeReturnID is not None and calleeReturnLineNumber is not None and calleeReturnID not in interNodeIdList:
                    interNodeIdList.append(calleeReturnID)
                if paraOutID is not None and paraOutLineNumber is not None and paraOutID not in interNodeIdList:
                    interNodeIdList.append(paraOutID)
    return interNodeIdList


def generateSlicePos(driver,sliceNodeIdList):
    sliceWithPosSet = set([])
    nodesSize = len(sliceNodeIdList)
    for index in range(nodesSize):
        id = sliceNodeIdList[index]
        cyper = """
                OPTIONAL MATCH (n)
                WHERE n.id=""" + str(id) + """
                OPTIONAL MATCH (methodorfile)-[:CONTAINS]->(n)
                WHERE methodorfile.FILENAME is not NULL and methodorfile.FILENAME<>'<empty>'
                RETURN methodorfile.FILENAME as fileName, n.LINE_NUMBER as lineNumber"""
        with driver.session() as session:
            result = session.run(cyper)
            for record in result:
                fileName = record.get('fileName')
                lineNumber = record.get('lineNumber')
                if fileName is not None and lineNumber is not None:
                    # print(fileName)
                    sliceWithPos = str(fileName) + "_" + str(lineNumber)
                    # print(sliceWithPos)
                    sliceWithPosSet.add(sliceWithPos)
                    break
    return sliceWithPosSet






def generateNeo4jCSVs(sourcePath, CPG_DIR):
    outputPath = CPG_DIR
    command1 = 'cd /Users/carryc/Singapore/joernV2/joern; '+'./joern-parse ' + sourcePath +'; ./joern-export --repr=all --format=neo4jcsv'
    command4 = f"find /Users/carryc/Singapore/joernV2/joern/out -name 'nodes_*_cypher.csv' -exec sed -i '' \"s,file:/,file://{outputPath},\" {{}} \\;"
    command5 = f"find /Users/carryc/Singapore/joernV2/joern/out -name 'edges_*_cypher.csv' -exec sed -i '' \"s,file:/,file://{outputPath},\" {{}} \\;"
    command6 = 'cp -R /Users/carryc/Singapore/joernV2/joern/out/* ' + outputPath
    command7 = 'rm -rf' + ' /Users/carryc/Singapore/joernV2/joern/out'



    print("command 1")
    print(command1)
    os.system(command1)  # 创建原始csv文件
    print("command 4")
    print(command4)
    os.system(command4)  # 修改节点csv文件内路径
    print("command 5")
    print(command5)
    os.system(command5)  # 修改边csv文件内路径
    print("command 6")
    print(command6)
    os.system(command6)  # 创建存储路径 并复制
    print("command 7")
    print(command7)
    os.system(command7)  # 删除out文件为后续操作


def generateNEO4J(CPG_DIR):


    outputPath = CPG_DIR

    # Define commands
    command1 = ['/opt/homebrew/Cellar/neo4j/5.25.1/libexec/bin/neo4j', 'start']
    command2 = 'cd /opt/homebrew/Cellar/neo4j/5.25.1/libexec/bin; find ' + outputPath + ' -name \'nodes_*_cypher.csv\' -exec ./cypher-shell -u neo4j -p 12345678 --file {} \;'

    command3 = 'cd /opt/homebrew/Cellar/neo4j/5.25.1/libexec/bin; find ' + outputPath + ' -name \'edges_CALL_cypher.csv\' -exec ./cypher-shell -u neo4j -p 12345678 --file {} \;'
    command4 = 'cd /opt/homebrew/Cellar/neo4j/5.25.1/libexec/bin; find ' + outputPath + ' -name \'edges_REACHING_DEF_cypher.csv\' -exec ./cypher-shell -u neo4j -p 12345678 --file {} \;'
    command5 = 'cd /opt/homebrew/Cellar/neo4j/5.25.1/libexec/bin; find ' + outputPath + ' -name \'edges_CONTAINS_cypher.csv\' -exec ./cypher-shell -u neo4j -p 12345678 --file {} \;'
    command6 = 'cd /opt/homebrew/Cellar/neo4j/5.25.1/libexec/bin; find ' + outputPath + ' -name \'edges_CDG_cypher.csv\' -exec ./cypher-shell -u neo4j -p 12345678 --file {} \;'
    command7 = 'cd /opt/homebrew/Cellar/neo4j/5.25.1/libexec/bin; find ' + outputPath + ' -name \'edges_AST_cypher.csv\' -exec ./cypher-shell -u neo4j -p 12345678 --file {} \;'
    command8 = 'cd /opt/homebrew/Cellar/neo4j/5.25.1/libexec/bin; find ' + outputPath + ' -name \'edges_ARGUMENT_cypher.csv\' -exec ./cypher-shell -u neo4j -p 12345678 --file {} \;'

    # Execute command1 and command2 sequentially
    print("command 1")
    process = subprocess.Popen(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("command 2")
    run_command(command2)



    # Run command3 to command7 in parallel
    commands_to_run_in_parallel = [command3, command4, command5, command6, command7, command8]

    num_processes = min(32, os.cpu_count())

    # Run parallel commands
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:  # Adjust the number of processes based on your CPU
        futures = [executor.submit(run_command, cmd) for cmd in commands_to_run_in_parallel]

    print(f" project constructs successfully!")


def turnSliceToCode(backSlicePos, source_dir, save_Foleder: str):
    os.makedirs(save_Foleder, exist_ok=True)
    # 先把每个文件对应的行号收集起来
    file_to_lines = defaultdict(list)

    for item in backSlicePos:
        file_name, line_num = item.rsplit('_', 1)
        file_to_lines[file_name].append(int(line_num))

    # 对每个源文件，提取需要的行并集中写入
    for file_name, line_nums in file_to_lines.items():
        source_file_path = os.path.join(source_dir, file_name)
        if os.path.exists(source_file_path):
            with open(source_file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 准备要写入的内容
            extracted_contents = []
            for line_num in sorted(line_nums):  # 排个序，按行号顺序
                if 1 <= line_num <= len(lines):
                    line_content = lines[line_num - 1].rstrip('\n')  # 去掉末尾换行
                    extracted_contents.append(f'{line_num}: {line_content}')  # 可以加上行号
                else:
                    extracted_contents.append(f'{line_num}: [Line not found]')

            # 保存到目标文件
            target_file_path = os.path.join(save_Foleder, file_name)
            with open(target_file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(extracted_contents))

            print(f"Saved extracted lines to {file_name}")
        else:
            print(f"Warning: Source file {source_file_path} not found.")





#删除文件夹里所有内容，不包括文件夹本身
def clean_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ 文件夹不存在: {folder_path}")
        return

    for name in os.listdir(folder_path):
        path = os.path.join(folder_path, name)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)
                print(f"🗑️ 删除文件: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"🧹 删除目录及其内容: {path}")
        except Exception as e:
            print(f"⚠️ 无法删除 {path}: {e}")


def run_slicer(code_path: str, line_number: int, fileName:str, CPG_DIR: str):
    try:
        #生成CPG
        generateNeo4jCSVs(code_path, CPG_DIR)
        #生成neo4j数据库文件
        clearNeo4j() #每次生成新的数据库时清空已有数据
        generateNEO4J(CPG_DIR)
        #执行切片
        backSlicePos = generateBackSlice(line_number, fileName)  #fileName = 'test/b.py'
        print("切片结果：", backSlicePos)
        # # #将切片结果转化为代码
        # save_path = '/Users/carryc/Documents/Research3/workspace/Data/StaticSlices'
        # if not os.path.exists(save_path):
        #     os.makedirs(save_path)
        # turnSliceToCode(backSlicePos, code_path, save_path)

        # clean_folder(CPG_DIR)   # 删除每一个solution对应的CPG临时文件
        # clean_folder(code_path) # 删除solution临时文件

        return backSlicePos

    except Exception as e:
        print(f"❌ 切片失败：{e}")
        clean_folder(CPG_DIR)   # 删除每一个solution对应的CPG临时文件
        clean_folder(code_path) # 删除solution临时文件
        return False, f'切片错误：{str(e)}'


'''--------------------new content ------------------'''




def main():

    CPG_DIR = "/Users/carryc/Documents/Research3/workspace/Data/codeNetData/TempFile/CPG/"
    project_root = "/Users/carryc/Documents/Research3/workspace/Data/codeNetData/TempFile/Project/"
    criterion_file = "s328864710.py"
    criterion_line = 37
    run_slicer(project_root, criterion_line, criterion_file, CPG_DIR)

    # clean_folder(Neo4j_DIR)
    # clean_folder(CPG_DIR)



if __name__ == '__main__':
    main()


