def to_roman_numerals(number): # fuction for converts numbers from arabic numerals to roman numerals
    pass

def to_arabic_numerals(number): # fuction for converts numbers from roman numerals to arabic numerals
    pass

def main(): # main function
    number = input('Write number: ')
    try: # try convert str to int
        number = int(number)
        number = to_roman_numerals(number) # if number is int convert number to roman numerals
        print(number)
    except ValueError: # else
        number = to_arabic_numerals(number) # if number is not int convert number to arabic numerals
        print(number)

if __name__ == '__main__':
    main()
