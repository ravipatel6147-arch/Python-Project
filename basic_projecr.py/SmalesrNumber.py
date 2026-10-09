number = [23,34,235,657,43,2]
smallest = number[0]

for num in number:
    if num < smallest:
        smallest = num
print("Smallesr number is ",smallest)