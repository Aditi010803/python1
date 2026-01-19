def count_digits(n):
    count = 0
    while n > 0:
        count =count + 1
        n //= 10
    print(count)

def main():
    n = int(input("Enter number:"))
    count_digits(n)

if __name__ == "__main__":
    main()
