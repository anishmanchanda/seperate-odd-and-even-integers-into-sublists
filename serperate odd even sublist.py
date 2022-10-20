#to find average of odd and even numbers seperately

n=int(input("enter number of numbers"))
list=[]
even=[]
odd=[]
for i in range (n):
    num = int(input("enter a number"))
    list.append(num)

    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print(list)
print("even:",even)
print("odd:",odd)
