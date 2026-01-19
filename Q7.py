
def natural(n):
    sum = 0
    for i in range(1, n + 1):
        sum =sum + i
    print(sum)

def main():
    n = int(input("Enter number: "))
    natural(n)

if __name__ == "__main__":
    main()
