#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    rom_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
                'I': 1}
    cont = 0
    ler = len(roman_string)
    for i in range(len(roman_string)):
        j = roman_string[i]
        if j in rom_dict:
            if i < ler - 1 and rom_dict[j] < rom_dict[roman_string[i + 1]]:
                cont -= rom_dict[j]
            else:
                cont += rom_dict[j]
    return cont
