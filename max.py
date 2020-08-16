num = [0, 5, 3, 9, 1, 4, 5, 7, 2]
#1Solution
#print(max(num))
maximum = num[0]
# 2Solution
for numb in num:
    if numb > maximum:
        maximum = numb
print(maximum)        