
def odd(n):
    for i in range(1, n + 1):
        if (i % 2==1):
            print(i)

def main():
    n = int(input("Enter number: "))
    odd(n)

if __name__ == "__main__":
    main()
