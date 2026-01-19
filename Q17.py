def factors(n):
    print("Factors are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

def main():
    n = int(input("Enter number:"))
    factors(n)

if __name__ == "__main__":
    main()
