sales = [[[0 for i in range(2)] for j in range(4)] for k in range(5)]
while True:
    year = -1
    while not(0<=year<=4):
        try:
            year = int(input("Enter a year (first year is 0, last is 4): "))
        except TypeError:
            year = -1
    quarter = -1
    while not(0<=quarter<=3):
        try:
            quarter = int(input("Enter a quarter (first quarter is 0, last is 3): "))
        except TypeError:
            quarter = -1
    dep = -1
    while not(0<=dep<=1):
        try:
            dep = int(input("Enter a department (hardware is 0, software is 1): "))
        except TypeError:
            dep = -1
    if sales[year][quarter][dep] == 0:
        profit = ""
        while profit == "":
            try:
                profit = int(input("Enter amount of profit. If overall loss, enter -ve number: "))
            except TypeError:
                profit = ""
        sales[year][quarter][dep] = profit
    else:
        print(sales[year][quarter][dep])