#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    numberDict = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000
    }
    resulList = []
    for val in roman_string:
        for key, value in numberDict.items():
            if val == key:
                resulList.append(value)
    nElem = len(resulList)
    if nElem <= 0:
        return None
    ans = 0
    for i in range(nElem):
        if i > 0 and resulList[i] > resulList[i-1]:
            ans += resulList[i] - 2 * resulList[i-1]
        else:
            ans += resulList[i]
    return ans
