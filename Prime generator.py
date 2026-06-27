
upper_limit = int(input("Enter the last prime number: "))
i = 0

while i < upper_limit:
    i += 1
    if i == 2 or i == 3 or i == 5 or i == 7:
        print(i)

    elif i % 2 == 1 and i % 3 >= 1 and i % 5 >= 1 and i % 7 >= 1 and i > 1:
        print(i)
