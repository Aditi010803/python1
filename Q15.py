def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

def main():
    n = int(input("Enter number:"))
    palindrome(n)

if __name__ == "__main__":
    main()
