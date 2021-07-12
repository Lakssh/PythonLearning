"""
file handling -

Open("<file path>","<mode>")  - To open a file
file.close()                - To close a file
mode    : "r" - read only mode
        : "w" - write only mode
        : "r+" - read and write mode
        : "a" - append file
read a file             -   file.read()
read file line by line  - file.readline()
"""

my_list = ["My First File",1,2,3,]
my_dict = {"product":{"Category1":["a","b","c"],"Category2":["d","e"]},"product2":{"category1":[1,2,3],"category3":[4,5,6]}}

my_file = open("NewFile.txt","w")           # To write a file
my_json = open("NewJsonFile.json",'w')

for item in my_list:
    my_file.write(str(item) + "\t")        # only string can be written to a file. So Type cast to Str
my_file.close()

for key,item in my_dict.items():
    my_json.write(str(key)+":"+str(item))

my_json.close()                             # close the file after the write action

my_file = open("NewFile.txt","r")           # To read a file
my_read_list = my_file.read()

print(my_read_list)

"""
with as Keyword can be used to read/write a file without want to call file.open and close
"""

print("****"*10,"Using With as","****"*10)

with open("NewFile_with_as.txt","w") as write_temp:
    for item in my_list:
        write_temp.write(str(item) + "\n")

with open("NewFile_with_as.txt","r") as read_temp:
    print(read_temp.read())