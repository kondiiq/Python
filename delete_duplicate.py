num = [6, 9, 2, 3, 6, 9, 1, 2, 0]
final = []
num.sort()
for number in num:
    if number not in final:
        final.append(number)
print(final)


               