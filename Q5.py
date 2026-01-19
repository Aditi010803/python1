def Divisible(No):
    if ((No % 3==0)and(No % 5==0)):
        print("Number Divisble 3 and 5")
    else:
        print("Number Not Divisble 3 and 5")

def main():
    value = 0
    print("enter number:")
    value =int(input())
    Divisible(value) 
   

if __name__ == "__main__":
    main()