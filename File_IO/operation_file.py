# # f = open("File_IO/demo.txt", "w+")
# # # data = f.read()
# # # print(data)
# # print(f.read())
# # f.write("appended...")
# # f.close()

# # a = open("File_IO/demo.txt", "r+")

# # a.write("Now ")
# # print(a.read())

# # with open("File_IO/demo.txt", "r") as f :
# #     print(f.read())

# with open("File_IO/prac.txt", "r") as f :
#     # f.write("Hey this is practice task")
#     data = f.read()

# new = data.replace("this", "that")
# print(new)

# with open("File_IO/prac.txt", "w") as f :
#     f.write(new)

###########
def check_for_word():
    word = "task"
    with open("File_IO/prac.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("word Found")
        else:
            print("not found")

def check_for_line():
    word = "line"
    data = True
    line = 1
    with open("File_IO/prac.txt", "r") as f:
        while data :
            data = f.readline()
            if (word in data):
                print(line)
                return
            line += 1
    
    return -1

# check_for_line()

#######
c = 0
with open("File_IO/prac.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for i in nums:
        if(int(i) % 2 == 0):
            c += 1

print(c)