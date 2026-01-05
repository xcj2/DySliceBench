#这个脚本用来提取codeNet的动态切片
# 输入：代码路径，行号，执行路径
# 输出：动态切片：行号集合、代码内容

import os
import csv
import re
import shutil
from typing import List, Tuple, Dict, Optional, Set
from CPGGen import run_slicer 




def load_csv(csv_path: str) -> List[Tuple[str, str]]:
    """
    读取CSV文件，返回[(problem_id, submission_id), ...]
    """
    pairs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)  # ⚠️ 不要写 delimiter='\t'
        for row in reader:
            pairs.append((row['problem_id'], row['submission_id']))
    return pairs



def extract_relevant_traces(path_file_path: str, submission_id: str) -> Tuple[List[str], List[str]]:
    """
    提取路径文件中所有包含 submission_id.py(行号): 的行信息
    返回：
    - relevant_lines: ['submission_id.py_508', ...]，保留原始顺序
    - filed_trace_content: [原始文本行, ...]，保留原始顺序
    """

    relevant_lines = []
    filed_trace_content = []

    # 构造正则表达式匹配 submission_id.py(数字):
    pattern = re.compile(rf"{re.escape(submission_id)}\.py\((\d+)\):")

    with open(path_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                line_number = int(match.group(1))
                relevant_lines.append(f"{submission_id}.py_{line_number}")
                filed_trace_content.append(line.rstrip('\n'))

    return relevant_lines, filed_trace_content

# ==========================================================
# 2. 提取源代码中的切片代码 
# ==========================================================
def slice_code_generator(source_file_path: str, relevant_lines, filed_trace_content, temp_source_path_root, temp_CPG_path_root):
    """
    静态代码切片生成函数，返回slice代码行号集合
    """
    clear_directory(temp_source_path_root)
    clear_directory(temp_CPG_path_root)
    copy_file_to_dir(source_file_path, temp_source_path_root) # 将源代码复制到临时目录，供CPG生成使用
    cri_file = os.path.basename(source_file_path)
    cri_line = select_slicing_criterion_from_trace(relevant_lines, filed_trace_content)
    if cri_line is None:
        raise ValueError("未能从执行路径中选择切片准则！")
    else:
        cri_line = str(cri_line).split('_')[-1]
    print("选择的切片准则：", cri_line)
    backSlicePos = run_slicer(temp_source_path_root, cri_line, cri_file, temp_CPG_path_root)

    return backSlicePos, cri_line, cri_file


def extract_code_from_trace_line(trace_line: str) -> str:
    """
    从 trace 行中提取代码部分，如：
    s000026793.py(15):     print(len(ans))  -> print(len(ans))
    """
    if "):" not in trace_line:
        return ""
    return trace_line.split("):", 1)[1].strip()

def is_valid_return(line: str) -> bool:
    return line.startswith("return") and len(line.split()) > 1

def is_valid_print_with_variable(line: str) -> bool:
    if not line.startswith("print"):
        return False
    match = re.match(r'print\s*\((.*)\)', line)
    if not match:
        return False
    inner = match.group(1).strip()
    if not inner:
        return False
    if (inner.startswith('"') and inner.endswith('"')) or (inner.startswith("'") and inner.endswith("'")):
        return False
    return True

def is_useful_statement(line: str) -> bool:
    if not line:
        return False
    if line.startswith("return") or line.startswith("print"):
        return False
    if "=" in line or re.search(r'\w+\s*\(', line) or line.startswith(("if ", "for ", "while ")):
        return True
    return False

def select_slicing_criterion_from_trace(
    relevant_lines: List[str],
    filed_trace_content: List[str]
) -> Optional[str]:
    """
    选择切片准则，基于 trace 行的真实代码内容：
    1. 优先选择 return xxx 或 print(x)
    2. 否则 fallback 为最近的非 return/print 的有用语句
    """
    candidate_fallback = None

    # 确保两者长度一致
    assert len(relevant_lines) == len(filed_trace_content), "两者长度不一致！"

    for entry, trace in reversed(list(zip(relevant_lines, filed_trace_content))):
        code = extract_code_from_trace_line(trace)

        if is_valid_return(code) or is_valid_print_with_variable(code):
            return entry
        elif is_useful_statement(code) and candidate_fallback is None:
            candidate_fallback = entry

    return candidate_fallback


def copy_file_to_dir(src_file_path: str, dst_dir: str):
    """
    将指定文件复制到目标目录中（保留原文件名）
    """
    if not os.path.isfile(src_file_path):
        raise FileNotFoundError(f"源文件不存在: {src_file_path}")

    os.makedirs(dst_dir, exist_ok=True)

    dst_file_path = os.path.join(dst_dir, os.path.basename(src_file_path))
    shutil.copy2(src_file_path, dst_file_path)  # copy2 保留时间戳等元数据

def clear_directory(dir_path: str) -> None:
    """
    删除目录下的所有文件和子目录，但保留目录本身
    """
    if not os.path.isdir(dir_path):
        raise ValueError(f"Not a directory: {dir_path}")

    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)

        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)



# ==========================================================
# 3. 提取路径的切片内容
# ==========================================================

def extract_dynamicSlice_by_dependency(
    exec_list: List[str],
    dep_set: Set[str],
    criterion_stmt: str
) -> List[str]:
    """
    从执行顺序列表中提取切片：
    - 不去重
    - 不排序
    - 严格保持 exec_list 中的原始顺序
    """

    # 1. 找最后一次出现的切片准则
    start_idx = -1
    for i in range(len(exec_list) - 1, -1, -1):
        if exec_list[i] == criterion_stmt:
            start_idx = i
            break

    if start_idx == -1:
        return []

    # 2. 向前扫描，只做“是否在 dep_set 中”的过滤
    result = []
    for stmt in exec_list[: start_idx + 1]:
        if stmt in dep_set:
            result.append(stmt)   # ❗保留重复、保留顺序

    return result
    

# ==========================================================
# 4. 存储模块
# ==========================================================

def save_static_slice_to_txt(slice_set, save_dir, filename):
    """
    将结果集合写入指定目录下的 txt 文件（一行一个元素）
    slice_set如：{'s000026793.py_1', 's000026793.py_8', 's000026793.py_10', 's000026793.py_9', 's000026793.py_13', 's000026793.py_14', 's000026793.py_6', 's000026793.py_15', 's000026793.py_7', 's000026793.py_11'}
    """
    file_path = os.path.join(save_dir, filename)
    slice_str = "\n".join(slice_set)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(slice_str)   


def save_dynamic_slice_to_txt(slice_list, save_dir, filename):  
    file_path = os.path.join(save_dir, filename)
    slice_str = "\n".join(slice_list)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(slice_str)   


# ==========================
# 主执行逻辑
# ==========================

def main(
    csv_path: str,
    source_path_root: str,
    trace_path_root: str,
    save_root: str,
    temp_source_path_root: str,  #CPG生成参数，因为CPG要以项目处理
    temp_CPG_path_root: str #CPG生成参数
):
    """
    主函数：根据CSV中问题ID和提交ID，提取路径信息、读取源代码并存储切片结果
    """
    records = load_csv(csv_path)
    failed_records = []

    for problem_id, submission_id in records:
        try:
            # 读取文件路径
            source_file = os.path.join(source_path_root, problem_id, f"{submission_id}.py")
            trace_file = os.path.join(trace_path_root, f"{submission_id}.trace")

            if not os.path.exists(source_file) or not os.path.exists(trace_file):
                print(f"跳过：{submission_id} 文件不存在")
                failed_records.add(f"{submission_id}_{submission_id}")
                continue

            # 1. 提取路径中的相关行号
            dynamic_relevant_lines, dynamic_trace_content = extract_relevant_traces(trace_file, submission_id)
            # print(f"处理 {submission_id}，提取到 {len(relevant_lines)} 条相关路径行")
            if len(dynamic_relevant_lines) == 0:
                print(f"跳过：{submission_id} 未提取到相关路径行")
                failed_records.add(f"{submission_id}_{submission_id}")
                continue
            print(dynamic_trace_content)
            print("相关路径行号：")
            print(dynamic_relevant_lines)

            # 2. 提取源代码中的静态切片代码
            staic_sliced_code_set, dynamic_cri_line, dynamic_cri_file = slice_code_generator(source_file, dynamic_relevant_lines, dynamic_trace_content, temp_source_path_root, temp_CPG_path_root)

            # # 3. 提取路径的动态切片内容
            # criterion_stmt = f"{dynamic_cri_file}_{dynamic_cri_line}"
            # sliced_trace_lines = extract_dynamicSlice_by_dependency(dynamic_relevant_lines, staic_sliced_code_set, criterion_stmt)
            # print("动态切片结果行号：")
            # print(sliced_trace_lines)

            # # # 4. 存储结果
            # # 存储动态结果
            # save_dynamic_slice_to_txt(sliced_trace_lines, save_root + 'Dynamic', submission_id+str(dynamic_cri_line)+".txt")
            # # 存储静态结果
            # save_static_slice_to_txt(staic_sliced_code_set, save_root + 'Static', submission_id+str(dynamic_cri_line)+".txt")
        except Exception as e:
            print(f"处理 {submission_id} 时出错: {e}")
            failed_records.add(f"{submission_id}_{submission_id}")


# ==========================
# 示例调用（根据你的文件路径设置）
# ==========================

if __name__ == "__main__":
    csv_path = "/Users/carryc/Documents/Research3/workspace/Data/codeNetData/filtered_python_data.csv"
    source_path_root = "/Users/carryc/Documents/Research3/workspace/Data/codeNetData/SolutionCode"
    trace_path_root = "/Users/carryc/Documents/Research3/workspace/Data/codeNetData/CodeTrace"
    save_root = "/Users/carryc/Documents/Research3/workspace/Data/codeNetData/Slices/"
    temp_source_path_root = "/Users/carryc/Documents/Research3/workspace/Data/codeNetData/TempFile/Project/" # 临时源代码路径，供CPG建项目分析的
    temp_CPG_path_root = "/Users/carryc/Documents/Research3/workspace/Data/codeNetData/TempFile/CPG/"
    main(csv_path, source_path_root, trace_path_root, save_root, temp_source_path_root, temp_CPG_path_root)