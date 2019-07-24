import csv

def forward(so,no):
    sum = 0
    for counter in range(1,no+1):
        sum += (1/(counter**so))
    print("n: ", no, "s: ", so, "Forward Sum: ", sum)
    return sum 

def backward(so,no):
    sum = 0
    for counter in range(1,no+1):
        sum += (1/((no+1-counter)**so))
    print("n: ", no, "s: ", so, "Backward Sum: ", sum)
    return sum

def main():
    s = int(input("Enter your value for s: "))
    n = 10**int(input("Enter your value for n: "))
    z2 = 1.6449340668482264
    z1 = 1.20205690315959
    with open('machine.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['S', 'N', 'Forward', 'Backward', 'Difference', 'Zeta - Forward', 'Zeta - Backward', 'Absolute Error Ratio'])
        for x in range(4,7):
           writer.writerow([2, 10**x, forward(2,10**x), backward(2,10**x), abs(forward(2,10**x)-backward(2,10**x)), z2 - forward(2,10**x), z2 - backward(2,10**x), (z2 - forward(2,10**x))/(z2 - backward(2,10**x))])
        for x in range(4,7):
            writer.writerow([3, 10**x, forward(3,10**x), backward(3,10**x), abs(forward(3,10**x)-backward(3,10**x)), z1 - forward(3,10**x), z1 - backward(3,10**x), (z1 - forward(3,10**x))/(z1 - backward(3,10**x))])

if __name__ == "__main__":
    main()