def prime(n):
    if n <= 1:
        print("No Prime Number")
        return
    for i in range(2, n):
        if n % i == 0:
            print("No Prime Number")
            return
    print("Prime Number")

def main():
    n = int(input("Enter number:"))
    prime(n)

if __name__ == "__main__":
    main()
