def isharshad(num):
    def sumdigits(num):
        digits = str(num)
        sum = 0
        for dgt in digits:
            # print dgt,
            if dgt.isdigit():
                sum += int(dgt)
        return sum
    return num % sumdigits(num) == 0
