# a = input("GO (A)... ")
# s = input("You're Turn (S)... ")

# if a == "S" and s == "K":
#     print("S WINS...")
# elif a == "S" and s == "G":
#     print("A WINS...")
# elif a == "K" and s == "G":
#     print("S WINS...")
# elif a == "K" and s == "S":
#     print("A WINS...")
# elif a == "G" and s == "S":
#     print("S WINS...")
# elif a == "G" and s == "K":
#     print("A WINS...")
# elif a == s :
#     print("It's a Tie")
# else :
#     print("Something Went Wrong")

#Another Type Of Coding

a = input("GO (A)... ")
s = input("You're Turn (S)... ")

if a == s :
    print("It's a Tie")

elif a == "S" :
    if s == "K" : print("S WINS ...")
    elif s == "G" : print("A WINS ...")    

elif a == "K" :
    if s == "S" : print("A WINS ...")
    elif s == "G" : print("S WINS ...") 

elif a == "G" :
    if s == "K" : print("A WINS ...")
    elif s == "S" : print("S WINS ...")


else :
    print("Something Went Wrong")
    

