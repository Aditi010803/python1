def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    print(rev)

def main():
    n = int(input("Enter number:"))
    reverse_number(n)

if __name__ == "__main__":
    main()
