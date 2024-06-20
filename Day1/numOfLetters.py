# This will print the number of letters/characters of the text you input
# print(len(input("What is your name? ")))

# This will store the input in a variable called name
name = input("What is your name? ")
'''
This will count the number of letters/characters of the text you input
and store it in a variable called numOfLetters
'''
numOfLetters = len(name)
# This will print what is stored in the variable name
print(name)
# This will print what is stoed in the variable numOfLetters
print(numOfLetters)
'''
This will print a nice output displaying the name and numOfLetters
(I googled this because I like things to be neat, to display an int
output with other content it needs to be converted to a string)
(I also googled how to have multi-line comments because *pretty*)
(Final note, the tester in me came out and it doesn't matter
what the input is it counts it, spaces, symbols, numbers. All counted.)
'''
print(name + " is " + str(numOfLetters) + " letters long.")

