import math
import numpy as np

def hamtinh(vector):
    norm = math.sqrt(sum([x**2 for x in vector]))
    return norm


def hamchuanhoa(vector):
    norm = hamtinh(vector)
    ham_chuanhoa = [x / norm for x in vector]
    return ham_chuanhoa

def vector_cong(a, b):
    return [x + y for x, y in zip(a, b)]

def vector_tru(a, b):
    return [x - y for x, y in zip(a, b)]

# Câu 5
def Matrix_5():
    x = [3, 7]
    norm_x = hamtinh(x)
    print("Norm of x:", norm_x)
    chuanhoa_x = hamchuanhoa(x)
    print("Normalized vector x:", chuanhoa_x)


# Câu 6
def TinhVector():
    a = [10, 15]
    b = [8, 2]
    c = [1, 2, 3]

    sum_ab = vector_cong(a, b)
    print("a + b:", sum_ab)

    diff_ab = vector_tru(a, b)
    print("a - b:", diff_ab)

    diff_ac = vector_tru(a, c)
    print("a - c:", diff_ac)


# Câu 7
def TichVoHuong():
    a = [10, 15]
    b = [8, 2]

    dot_product = np.dot(a, b)
    print("Tích vô hướng của a và b:", dot_product)


# Câu 8
def Matrix_8():
    # a)
    A = np.array([[2, 4, 9], [3, 6, 7]])
    hang_A = np.linalg.matrix_rank(A)
    dang_a = A.shape

    print("Hang cua A:", hang_A)
    print("Dang cua A:", dang_a)

    # b)
    giatri7 = A[1, 2]
    print("Gia tri 7 trong A:", giatri7)

    # c)
    cot2 = A[:, 1]
    print("Cot 2 trong A:", cot2)


# Câu 9
def Tao_matrix():
    matrix = np.random.randint(-10, 10, (3, 3))
    print("Ma tran:")
    print(matrix)


# Câu 10


if __name__ == '__main__':
    # Matrix_5()
    # TinhVector()
    # TichVoHuong()
    # Matrix_8()
    # Tao_matrix()
