#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    result = 0
    if isinstance(roman_string, str):
        for e in range(len(roman_string)):
            if e > 0:
                if roman.get(roman_string[e-1]) < roman.get(roman_string[e]):
                    prev = roman.get(roman_string[e-1])
                    result += roman.get(roman_string[e])-(prev*2)
                else:
                    result = result + roman.get(roman_string[e])
            else:
                result = result+roman.get(roman_string[e])
    return result
