import datetime
t = datetime.datetime.now()
# code 
a = 123456321
b = int(a/2)
counts = []

for i in range(2, b):
    if a % i != 0:
        continue
    else:
        counts.append(i)
if len(counts)== 0:
    print("It's a PRIME number...")
else:
    print(f"{a} is dividable to {counts}")

x = datetime.datetime.now()
c = x-t
print(f"{int(c.total_seconds() * 1000) } ms")