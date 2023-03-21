




name = input('What is your name : ')
age = int(input('How old are you ? '))
years = int(input('Check how old you will be with the number u enter: '))
# print('hellow,',name,'and bye!')

#Another way
# print('Another way')

print(f'hellow, {name}')
print(f'Hello, {name}, you are {age}, years old.')
print(f'you will be {age + 5}, in 5 years.')
print(f'you will be {age + years} years old in {years} years')

if (age+years)%2==0:
    print('your age is evn')
else:
    print('odd')


