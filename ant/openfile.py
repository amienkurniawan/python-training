# file = open("doc_3.txt","r")
# appending
# file = open("doc_3.txt","a")
# overwrite
file = open("doc_3.txt","w")
file.write("\nangle human resurces")
# r => read
# w -> write change the file
# a -> append the file
# r+ => read and write
file = open("doc_3.txt","r")
# check file is readable
# print(file.readable())

# read all line
print(file.read())

# read individual line and moving to next line
# for files in file.readlines():
#     print(files)

# read firstline and the second character
# print(file.readline()[2])
# read next line and the first character
# print(file.readline()[1])

file.close()