import datetime
t_1 = datetime.datetime.now()

# ---------------------------------------------------------
last_number = 500000

# A LIST OF NUMBERS FROM 2 TO last_number
numbers = []
for i in range(2, last_number):
    numbers.append(i)

# THIS FUNCTION RETURN NUMBER IF IS PRIME ELSE RETURN NONE


def prime(arg):
    factors = []
    for i in range(2, (int(arg**0.5)+1)):
        if arg % i == 0:
            factors.append(i)

        else:
            pass
    if len(factors) == 0:
        return(arg)


# FILTERING PRIMES IN NUMBERS
result = list(filter(prime, numbers))
# OUTPUT
print(result)
print("-------------------")
print(f"Prime Numbers Before {last_number} : {len(result)}")
#INDEX OF PRIME NUMBER
print(result[10000])
print("-------------------")
# ---------------------------------------------------------
t_2 = datetime.datetime.now()
t = t_2 - t_1
print(f"{int(t.total_seconds() * 1000) } ms")
