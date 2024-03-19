import math
import numpy as np
import matplotlib.pyplot as plt

def hamtinh(vector):
    norm = math.sqrt(sum([x ** 2 for x in vector]))
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
def Maxtrix_3x3():
    identity_matrix = np.eye(3)
    print(identity_matrix)


# Câu 11
def Matrix_11():
    random_matrix = np.random.randint(1, 10, size=(3, 3))

    # a/ Dùng lệnh
    trace_method1 = np.trace(random_matrix)

    # b/ Dùng vòng loops
    trace_method2 = 0
    for i in range(3):
        trace_method2 += random_matrix[i, i]
    print(random_matrix)
    print("Cong bang lenh: ", trace_method1)
    print("Cong bang vong for: ", trace_method2)


# Câu 12
def Matrix_12():
    diagonal_matrix = np.diag([1, 2, 3])
    print("3x3 Diagonal matrix:")
    print(diagonal_matrix)


# Câu 13
def Matrix_13():
    A = np.array([[1, 1, 2], [2, 4, -3], [3, 6, -5]])
    determinant_A = np.linalg.det(A)
    print("Determinant of A:", determinant_A)


# Câu 14
def Matrix_14():
    a1 = [1, -2, -5]
    a2 = [2, 5, 6]

    M = np.column_stack((a1, a2))

    print("Matrix M:")
    print(M)


# Câu 15
def Matrix_15():
    y = np.arange(-5, 6)
    y_squared = y ** 2
    plt.plot(y, y_squared)
    plt.xlabel('y')
    plt.ylabel('y squared')
    plt.title('Plot of y squared')
    plt.show()


# Câu 16
def Matrix_16():
    values = np.linspace(0, 32, 4)
    print("Evenly spaced values:")
    print(values)


# Câu 17
def Matrix_17():
    x = np.linspace(-5, 5, 50)
    y = x ** 2

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of y = x^2')
    plt.show()


# Câu 18
def Matrix_18():
    x = np.linspace(-5, 5, 100)
    y = np.exp(x)
    plt.plot(x, y, label='y = exp(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Exponential Function')
    plt.legend()
    plt.show()


# Câu 19
def Matrix_19():
    x = np.linspace(0.01, 5, 100)
    y = np.log(x)
    plt.plot(x, y, label='y = log(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Logarithmic Function')
    plt.legend()
    plt.show()


# Câu 20
def Matrix_20():
    x = np.linspace(-5, 5, 100)
    y_exp_x = np.exp(x)
    y_exp_2x = np.exp(2 * x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

    ax1.plot(x, y_exp_x, label='y = exp(x)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Exponential Function (y = exp(x))')
    ax1.legend()

    ax2.plot(x, y_exp_2x, label='y = exp(2*x)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Exponential Function (y = exp(2*x))')
    ax2.legend()

    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    # Matrix_5()
    # TinhVector()
    # TichVoHuong()
    # Matrix_8()
    # Tao_matrix()
    # Maxtrix_3x3()
    # Matrix_11()
    # Matrix_12()
    # Matrix_13()
    # Matrix_14()
    # Matrix_15()
    # Matrix_16()
    # Matrix_17()
    # Matrix_18()
    # Matrix_19()
    Matrix_20()