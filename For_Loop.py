# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Câu 1
from typing import List, Tuple


def for_loop():
    name = input("Nhap ten cua ban: ")
    for i in name:
        print(i)


# Câu 2
def odd_num():
    num = int(input("Nhap so: "))
    if 1 <= num <= 10:
        for i in range(1, num + 1):
            if i % 2 != 0:
                print(i)
    else:
        print("So nhap vao khong hop le")


# Câu 3a
def sum_in_2():
    num = int(input("Nhap so: "))
    total = num * 10 + 1 + num * 10 + 2
    print(total)


# Câu 3b
def sum():
    for i in range(1, 6 + 1):
        print(i)


# Câu 4
def mydict():
    mydict = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}

    # In các chữ trong tập hợp
    for key in mydict:
        print(key)

    # In các số trong tập hợp
    for values in mydict.values():
        print(values)

    # In cả 2
    for key, value in mydict.items():
        print(key, value)


# Câu 5
def tuples():
    courses = [131, 141, 142, 212]
    names = ["Maths", "Pysics", "Chem", "Bio"]

    tuples = [(courses, names) for courses, names in zip(courses, names)]

    for courses, names in tuples:
        print(f"{courses} - {names}")


# Câu 6
def consonants():
    words = ("jabbawocky")
    nguyenam = set("aeiou")
    cases = input("Ban chon cach nao (1/2):")
    total = 0
    if cases == "1":
        for i in words:
            if i not in nguyenam:
                total += 1
        print(f'Tong so phu am la: {total}')
    if cases == "2":
        {}


# Câu 7
def divided():
    a = int(input("Nhap so a: "))
    if -2 <= a <= 3:
        if a == 0 :
            print("Can’t divided by zero")
        else :
            divided = 10/a
            print(divided)
    else:
        print("Nhap so")


# Câu 8
def lamda():
    ages = [23, 10, 80]
    names = ["Hoa", "Lam", "Nam"]
    people = list(zip(ages, names))
    sapxep: list[tuple[int, str]] = sorted(people, key=lambda x: x[0])
    print(sapxep)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # for_loop()
    # odd_num()
    # sum_in_2()
    # sum()
    # mydict()
    # tuples()
    # consonants()
    # divided()
    lamda()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
