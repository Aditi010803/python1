def sum_digits(n):
    total = 0
    while n > 0:
        total = total + n % 10
        n //= 10
    print(total)

def main():
    n = int(input("Enter number:"))
    sum_digits(n)

if __name__ == "__main__":
    main()
