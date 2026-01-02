from typing import List


def stack_push(elems: List[int], value: int) -> None:
    elems.append(value)


def stack_pop(elems: List[int]) -> int:
    value = elems.pop()
    return value


def exec_operation(elems: List[int], operation: str) -> None:
    value2 = elems.pop()
    value1 = elems.pop()
    if ("+" == operation):
        elems.append(value1 + value2)
    elif ("-" == operation):
        elems.append(value1 - value2)
    elif ("*" == operation):
        elems.append(value1 * value2)


if __name__ == "__main__":
    stack: List[int] = []
    input_commands = input().split(" ")

    for command in input_commands:
        if (str.isdecimal(command)):
            stack_push(stack, int(command))
        else:
            exec_operation(stack, command)

    print(f"{stack_pop(stack)}")

