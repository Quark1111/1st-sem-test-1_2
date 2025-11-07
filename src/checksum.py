def modulo11Checksum(ISBNNumber: str):
    digits = [int(char) for char in ISBNNumber if char.isdigit()]
    if len(digits) != 10:
        return -1  
    checkDigit = digits[-1]
    total = 0
    for i in range(len(digits) - 1):
        weight = 10 - i
        digit = digits[i]
        total += digit * weight
    checksum = total + checkDigit
    return checksum % 11 == 0

ISBNNumber = input()

while ISBNNumber != '-1':
    res = modulo11Checksum(ISBNNumber)
    if res == 1:
        print('correct')
    elif res == -1:
        print('Incorrect number length')
    else:
        print('incorrect')
    ISBNNumber = input()
    
