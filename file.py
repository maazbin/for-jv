
''' 
Modes to open a file: 

1) Read the file 
2) Write (into) the file
3) Append
4) Delete the file

 

()) execute the file (run the file)

'''

#saving file path 
path = "files_bank/hello.txt"

# open file in read mode
f = open(path,"r")

for i in range(5):
    # reading first 5 char
    print(f"red#{i+1} : {f.read(5)}")

# # reading first 5 char
# print(f.read(6))

# f.write(" blah blah")

# closing the file
f.close()
