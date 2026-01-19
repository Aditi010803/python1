def reverse_no(n):
    for i in range(n, 0, -1):
        print(i)

def main():
    n = int(input("Enter number:"))
    reverse_no(n)

if __name__ == "__main__":
    main()
