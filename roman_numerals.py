def to_roman_numerals(number): # fuction for converts numbers from arabic numerals to roman numerals
    numbers = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',10000:'H'}
    num = (10000,1000,500,100,50,10,5,1)
    n = ''

    while number != 0:
        for x in num:
            if number >= x:
                number -= x
                n += numbers[x]
                break
            else:
                for y in num[::-1]:
                    if number >= x-y and int(x/y) > 2:
                        number -= (x-y)
                        n+= numbers[y]
                        n += numbers[x]
                        break
                else:
                    continue

                break

    return n


def to_arabic_numerals(number): # fuction for converts numbers from roman numerals to arabic numerals
    try:
        numbers = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'H':10000}
        now = 'I'
        n = 0
        a = [None,0]
        for x in number[::-1]:
            if numbers[x] >= numbers[now]:
                now = x
                n += numbers[x]
                a[1] = 0
            else:
                if a[1] > 0 or ( a[1] == 1 and a[0] != x ) or int(numbers[now] / numbers[x]) <= 2:
                    return 'Error!'
                else:
                    a[0] = x
                    a[1] += 1
                    n -= numbers[x]
        return n
    except KeyError:
        return 'Error!'

def main(): # main function
    number = input('Write number: ')
    try: # try convert str to int
        number = int(number)
        number = to_roman_numerals(number) # if number is int convert number to roman numerals
        print(number)
    except ValueError: # else
        number = number.upper()
        number = to_arabic_numerals(number) # if number is not int convert number to arabic numerals
        print(number)

if __name__ == '__main__':
    main()
