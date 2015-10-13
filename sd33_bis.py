def print_while(step, stop):
    i = 0
    numbers = []

    for i in range(0, stop, step):
        print("At the top i is %d" % i)
        numbers.append(i)
        print("Numbers now:", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers:")
    for num in numbers:
        print(num)
