# Financial application: compute commissions


def computeCommission(salesAmount):
    commission = 0.0
    if salesAmount <= 5000:
        commission = salesAmount * 0.08
    elif 5000 < salesAmount <= 10000:
        commission = 400 + (salesAmount - 5000)*0.1
    elif salesAmount > 10000:
        commission = 400 + 500 + (salesAmount - 10000)*0.12
    return commission


def main():
    print("{0:8}  {1:8}".format("Sales Amount", "Commission"))
    for i in range(10000, 100001, 5000):
        print("{0:<15}{1:9}".format(i, computeCommission(i)))


if __name__ == '__main__':
    main()
