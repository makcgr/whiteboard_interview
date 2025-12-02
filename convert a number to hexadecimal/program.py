def convertToHex(num: int) -> str:
    if num == 0:
        return "0"
    hexSymbols = "0123456789ABCDEF"
    
    # e.g. 26
    # 26 % 16 = 10 (A)
    # 26 // 16 = 1 (1)
    # 1 % 16 = 0

    # (26 - 10) % 16 = 0 
    # (16 // 16 = 1
    if num < 0:
        num = 2 ** 32 + num
 
    res = ""
    while num > 0:
        rem = num % 16
        res = hexSymbols[rem] + res 
        num = num // 16

    return res

print(convertToHex(26))
print(convertToHex(-1))


# why it works
# we can get our hexadecimal value by iteratively getting a remainder from division to 16
# the remainder is actually the hex digit's index
# and then setting the number to itself divided by 16 (to shift  the register to the left 
# until we get to 0 (then we are done)
# NOTE: we handle the negative numbers by adding 2^32 to our integer (two's complement)
# Negative number -x is stored as 2^32 - x
#          E.g.   -26 would be    2^32 - 26

