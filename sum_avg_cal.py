n = int(input("Enter number of integers: "))
sum = 0 
count = 0
for i in range(n):
    num = int(input("Enter integer no: "))
    sum = sum + num
    count = count +1

avg = sum / count

print("Sum = ",sum)
print("Avarage = ",avg)

