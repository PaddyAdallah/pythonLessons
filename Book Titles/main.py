if __name__ == "main":

    file = open("/usercode/files/books.txt", "r")
    output = file.readlines()

    for i in output:
        print(i[0] + str(len(i.strip())))

    file.close()
