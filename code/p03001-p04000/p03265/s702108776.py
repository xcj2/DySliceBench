#-*- coding:utf-8 -*-
"""
xy平面上に正方形があり、4つの頂点の座標は反時計回りに順番に(x1,y1),(x2,y2),(x3,y3),(x4,y4)です。
なお、x軸は右向きに、y軸は上向きに取ることにします。
高橋君は、これら4つの座標のうち(x3,y3),(x4,y4)を忘れてしまいました。
x1,x2,y1,y2が与えられるので、x3,y3,x4,y4を復元してください。なお、これらの条件から、
x3,y3,x4,y4は一意に存在し、整数となることが証明できます。
"""
import numpy as np


def get_vector(x1, y1, x2, y2):
    a = np.array([x1, y1])
    b = np.array([x2, y2])
    vector = b - a

    return vector


def get_rotation_matrix(rad):
    """
    指定したradの回転行列を返す
    """
    rot = np.array([[np.cos(rad), -np.sin(rad)],
                  [np.sin(rad), np.cos(rad)]])
    return rot


def main(str):
    coodinate = str.split()

    # 標準入力された座標を整数値として読み込み
    x1 = int(coodinate[0])
    y1 = int(coodinate[1])
    x2 = int(coodinate[2])
    y2 = int(coodinate[3])

    # ABvector(仮)を求める
    vector1 = get_vector(x1, y1, x2, y2)
    # 回転行列を求める
    rotate_matrix = get_rotation_matrix(np.pi/2)
    # BCvector(仮)を求める
    vector2 = np.dot(rotate_matrix, vector1)

    x3 = int(round(vector2[0] + x2))
    y3 = int(round(vector2[1] + y2))
    x4 = int(round(vector2[0] + x1))
    y4 = int(round(vector2[1] + y1))

    print(x3, y3, x4, y4)


if __name__ == "__main__":
    main(input())