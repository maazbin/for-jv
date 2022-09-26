#open the file

f = open("dictionary.txt")


#read what is in the file

word = input("give me a word : ")

english = f.read()

if word in english:
    print(f'{word} is an english word')
else:
    print(f'{word} is not an english word')

# print(f.read())