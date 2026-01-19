def check_vowel(ch):
    if ch in 'aeiouAEIOU':
        print("Vowel")
    else:
        print("Consonant")

def main():
    ch = input("Enter a character:")
    check_vowel(ch)

if __name__ == "__main__":
    main()
