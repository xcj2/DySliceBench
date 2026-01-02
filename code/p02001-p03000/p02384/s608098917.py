def roll(l, command):
    '''
    return rolled list

    l : string list
    command: string
    '''
    res = []
    i = -1
    if command =='N':
        res = [l[i+2], l[i+6], l[i+3], l[i+4], l[i+1], l[i+5]]
    if command =='S':
        res = [l[i+5], l[i+1], l[i+3], l[i+4], l[i+6], l[i+2]]
    if command =='E':
        res = [l[i+4], l[i+2], l[i+1], l[i+6], l[i+5], l[i+3]]
    if command =='W':
        res = [l[i+3], l[i+2], l[i+6], l[i+1], l[i+5], l[i+4]]

    return res

def spin(l):
    '''
    return right sppined list

    l : string list
    '''

    i = -1
    res = [l[i+1], l[i+3], l[i+5], l[i+2], l[i+4], l[i+6]]

    return res

def check_all(upper, front, faces):
    orig_faces = faces[:]

    #change upper face
    for i in range(6):
        if 1 <= i <= 3:
            faces = roll(faces, "N")
        elif i == 4:
            pass
            faces = orig_faces[:]
            faces = roll(faces, "W")
        elif i == 5:
            faces = orig_faces[:]
            faces = roll(faces, "E")


        # spin 4 times
        for _ in range(4): #spin 3 times
            faces = spin(faces)
            if (faces[0] == upper and (faces[1] == front)):
                return faces[2]

if __name__ == "__main__":
    faces = input().split()
    n = int(input())

    for _ in range(n):

        question = list(input().split())
        answer = check_all(question[0], question[1], faces)

        print(answer)

