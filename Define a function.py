# Câu 1
import numpy as np


def return_sum():
    a = int(input("Nhap so a:"))
    b = int(input("Nhap so b:"))
    total = a + b
    print(total)


# Câu 2
def matrix():

    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = np.array([1, 2, 3])
    rank_M = np.linalg.matrix_rank(M)
    shape_M = M.shape
    shape_v = v.shape
    print(rank_M)
    print(shape_M)
    print(shape_v)


# Câu 3
def maxtrix_3():
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    new_matrix = M + 3
    print(M)
    print(new_matrix)


# Câu 4
def transpose():
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = np.array([1, 2, 3])
    M_transpose = np.transpose(M)
    v_transpose = np.transpose(v)
    print(M)
    print(M_transpose)
    print(v)
    print(v_transpose)


if __name__ == '__main__':
    # return_sum()
    # matrix()
    # maxtrix_3()
    transpose()