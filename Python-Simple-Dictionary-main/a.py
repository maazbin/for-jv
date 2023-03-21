#loading the file in read mode
text_file = open("./dictionary.txt","r")

# read the file and save that to a varialble

# words = text_file.read()

words = []

for i in text_file:
    line  = i.rstrip() # removes \n
    words.append(line.lower())
    # print(i)

text_file.close()
# print(words)

#checking if the word is from english
a_word = input("give me a word : ")
if a_word.lower() in words:
    print(a_word, " is a english word")
else :
    print(a_word," is not a English word")