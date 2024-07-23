def getNoZeroIntegers(n: int) -> list[int]:
    for num1 in range(1, n):
        if '0' not in str(num1) and '0' not in str(n - num1):
            return [num1, n - num1]
    

print(getNoZeroIntegers(11))
print(getNoZeroIntegers(2))
print(getNoZeroIntegers(110))
