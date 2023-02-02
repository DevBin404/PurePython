# import random
# a = random.randint(1,6)
# s = random.randint(1,6)

# print(f"(A) Got {a} and (S) Got {s}")


# if a>s : print("It's A Turns...")
# elif a<s : print("It's S Turns...")
# else : print ("Another Round...")

#Update

import random
a = random.randint(1,6)
s = random.randint(1,6)

Question = input("More Or Less ? ")
print(f"(A) GOT {a} and (S) GOT {s} : ") 

if Question == "More":
    if a > s : print ("It's A's Turn...")
    elif s > a : print("It's S's Turn...")
    else : print("Another Round")

if Question == "Less":
    if a > s : print ("It's S's Turn...")
    elif s > a : print("It's A's Turn...")
    else : print("Another Round")
   

