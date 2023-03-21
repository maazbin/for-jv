#saving file path 
path = "files_bank/hello.txt"

# open file in write mode
f = open(path,"w")

#wrting into the file
f.write(" blah blah new write")

# closing the file
f.close()