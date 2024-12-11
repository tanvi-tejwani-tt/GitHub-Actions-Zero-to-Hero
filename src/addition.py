

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

for i in range(a,b+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print()
