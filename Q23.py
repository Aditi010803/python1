def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    if sum == n:
        print("Perfect number")
    else:
        print("Not a perfect number")

def main():
    n = int(input("Enter number:"))
    perfect(n)

if __name__ == "__main__":
    main()
