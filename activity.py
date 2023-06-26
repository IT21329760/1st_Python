n = (1,2,3,4,5,6,7,8,9)

e_count = 0
o_count = 0

for num in n:
    if num % 2 ==0:
        e_count +=1
    else:
        o_count +=1

print("Number of even nos:",e_count )
print("Number of odd nos:",o_count )
