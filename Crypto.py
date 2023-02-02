def caesar(message , key):
    result = []
    for char in message:
        if not char.isupper() and not char.islower(): 
            result.append(char)
            continue

        if char.islower():
            base = ord("a")
        else :
            base = ord('A') 
        a = chr(((ord(char) - base) + key)%26 + base ) 
        result.append(a)      
    return ''.join(result)

print(caesar(input("Enter :" ),1))