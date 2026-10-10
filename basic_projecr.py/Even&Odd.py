number = [12,34,354,23,5476,7,4,3,89]
even = 0
odd = 0
for num in number:
    if num%2==0:
        even +=1
    else:
        odd +=1
print("Number of Even are :",even)
print("Number of Odd are :",odd)