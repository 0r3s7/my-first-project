
# This is for testing Github Flow uploading a simple *.py file

a=0
b=0

while (a<=10):
    print(f"While a is {a}, b equals {b}")
    b+=1
    a+=1

print("\nCycle terminated!")

# First modification to *.py file to be pushed to edit branch

c=a+b

if (a<=20):
    print(f"Now a equals {a}, if we sum with b that equals {b} we obtain {c}")


