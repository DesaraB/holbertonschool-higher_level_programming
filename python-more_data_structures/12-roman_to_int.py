#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    sum = 0
    i = 0

    thisdict = {"I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M": 1000,
                "IX": 9, "IV": 4, "XL": 40, "XC": 90,
                "CD": 400, "CM": 900}
    while i < len(roman_string):
        if roman_string[i:i + 2] in thisdict:
            sum += thisdict[roman_string[i:i + 2]]
            i = i + 2
        else:
            sum += thisdict[roman_string[i]]
            i = i + 1
    return sum
