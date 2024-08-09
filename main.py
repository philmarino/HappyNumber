def isHappy(n):
    previousSubtotals = []

    while True:
        subTotal = 0
        for digit in str(n):
            subTotal += int(digit) * int(digit)
        if subTotal == 1:
            return True
        if subTotal in previousSubtotals:
            return False
        previousSubtotals.append(subTotal)
        n = subTotal


# Example 1:
# Input:
n = 19
print(isHappy(n))
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Example 2:
# Input:
n = 2
print(isHappy(n))
# Output: false
