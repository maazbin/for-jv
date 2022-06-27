answer = input("Pyramids are made by aliens , Do you agree ?")

# Hint if answer == 'yes' : print('person agrees')

x = ['Yes','yes','y','Y']

# if answer == 'yes' or answer == 'Yes' or answer == 'y' or answer == 'Y':
if answer in x:  
    print('person agrees')
else : 
    print('not agreed') 