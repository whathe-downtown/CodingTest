list = input()

count = 0
for i in range(len(list)):

    if  i == 0:
        count += 10
    elif list[i] == "(":
        if list[i-1] == "(":
            count += 5
        else:
           count += 10

    elif list[i] == ")":
        if list[i-1] == ")":
            count += 5
        else:
           count += 10

print(count)