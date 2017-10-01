# utf-8
num = int(input())
roman_num = ''
roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 900:'CM', 400:'CD', 90:'XC', 40:'XL', 9:'IX', 4:'IV'}
for l in sorted(roman.keys(), reverse=True):
    roman_num += str(num // l * roman[l])
    num = num % l
print(roman_num)
