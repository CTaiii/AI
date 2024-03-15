# Câu 9
def readfile():
    with open('Cau9.txt', 'w') as file:
        file.write("hs1\n")
        file.write("hs2\n")
        file.write("hs3\n")

# b)
    with open('Cau9.txt', 'r') as file:
        for line in file:
            print(line.strip())

# c)
    with open('Cau9.txt', 'r') as file:
        content = file.read()
        print(content)


if __name__ == '__main__':
    readfile()