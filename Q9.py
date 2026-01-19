def even(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

def main():
    n = int(input("Enter number:"))
    even(n)

if __name__ == "__main__":
    main()
