import os
os.system("cls")

user_input = input("Enter: ")

if len(user_input) % 2 == 1:
    word = int((len(user_input)-1)/2)
    print(user_input[word])
else:
    word = int(len(user_input)/2)
    word_1 = int((len(user_input)/2)-1)
    print(user_input[word],
          user_input[word_1])
