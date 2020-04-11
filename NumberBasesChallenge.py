import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    possible_digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    digits = digits.upper()
    output = 0
    array_of_digits = list(digits)
    reversed_list = array_of_digits[::-1]
    for i in range(len(reversed_list)):
        digit = reversed_list[i]
        # print(f'Value Before = {type(digit)}')

        for x in range(len(possible_digits)):
            if digit == possible_digits[x]:
                digit = x
                # print(f'Value After = {type(digit)}')

        position = i
        value = base ** (position)
        result = value * int(digit)
        output = output + result
    return output

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert int(number) >= 0, 'number is negative: {}'.format(number)
    possible_digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    number = int(number)
    mods = []
    while number > 0:
        value = str(number % base)
        for x in range(len(possible_digits)):
            # print(f'Is {type(value)} Equal to {type(x)} ?')
            if value == str(x):
                # print('woweeeeeeee')
                value = possible_digits[x]
                break
        mods.append(str(value).lower())
        number //= base
    mods.reverse()
    # print(mods)
    return ''.join(mods)

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    possible_digits = {
         '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
         'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22,
         'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
         'Y': 34, 'Z': 35, 'a': 36
        }
    digit = 0
    for char in digits:
        char = char.upper()
        assert char in possible_digits, 'Found unknown character!'
        value = possible_digits[char]
        assert value < base1, 'Found digit outside base!'
        digit *= base1
        digit += value

    possible_digits_reversed = dict(map(reversed, possible_digits.items()))

    array = []
    #   Until digit is a falsey number.
    while digit:
        digit, value = divmod(digit, base2)
        array.append(possible_digits_reversed[value])
    result = ''.join(reversed(array))

    return result.lower()

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    #main()
    # print(decode('11', 2))
    print(convert('101010', 2, 16))#'10'
    # print(encode('10', 16))