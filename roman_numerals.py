def to_roman_numerals(number):
    pass

def to_arabic_numerals(number):
    pass

def main():
    number = input('Write number: ')
    try:
        number = int(number)
        number = to_roman_numerals(number)
        print(number)
    except ValueError:
        number = to_arabic_numerals(number)
        print(number)

if __name__ == '__main__':
    main()
