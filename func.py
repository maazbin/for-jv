
# #hello function
def hello():
    print('hello,world')


# returning a string
def helloReeturn():
    return "I am a function which returns hello !"


# takes input
def loundryBoy(dirty_cloth): # dirty cloths are -ve

    # washed cloths
    washed_cloths =   dirty_cloth
    #when we wash them they become +ve
    washed_cloths = washed_cloths * (-1)
    # returns washed cloths
    return washed_cloths



#calling loundry boy
# consider a -ve number as dirty cloths

x = loundryBoy(-1)

print(x)



#calling function
# x = helloReeturn()

# print(x)

# def sum_of_numbers(number):
#     return number + number


# sums = sum_of_numbers(10)
# print(sums)

    # print("hi",name)





#call the function

# hello()
# sum_of_fives()

# sums = sum_of_fives()
# print(sum_of_fives())