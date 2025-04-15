values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def main():
    roman = input("Roman number: ").strip()
    if not isValid(roman):
        quit("Invalid roman number.")
    

    arabic = 0
    # next is set as the value of the first character so that curr can be assigned to that at the beginning of the loop
    # makes loop more readable
    next = values[roman[0]]
    for i in range(len(roman) - 1):
        curr = next
        next = values[roman[i + 1]]
        if curr < next:
            arabic -= curr
        elif curr >= next:
            arabic += curr
    arabic += values[roman[len(roman) - 1]]
    print(arabic)

def checkValid(roman):
    for c in roman:
        if c not in values.keys():
            quit("Invalid symbols.")
    for c in values.keys():
        if (c != "I" and roman.count(c) > 1):
            return False
        if c == "I":
            count = roman.count("I")
            match count:
                case 0:
                    pass
                case 1:
                    pass
                case 2 | 3:
                    if roman.find("I" * count) == -1:
                         return False
                case _:
                    return False
    if roman.find("DM") != -1:
        return False

main()
