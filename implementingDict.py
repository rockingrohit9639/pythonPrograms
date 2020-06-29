dict = {
    "Variable" : "Variables are the values in a programming language which can be changed during the execution of program.",
    "Constant" : "Constants are the values which once defined in the program cannot be changed.",
    "List" : "List are like our daily life list. We note our items in it and in the same way it works in python.",
    "Tuple" : "Tuple is same as a list but the difference is the values in list can be changed and values in tuple cannot be changed",
    "Dictionary": "It is nothing but key value pairs"
}

print("Enter the word to find its meaning : ")
word = input()
if word in dict:
    print(dict[word])
else:
    print("Sorry the word is not in our dictionary.")
