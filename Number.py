# Use the if statement to check the numbers
def two_numbers(a, b, c):
    if (a > 0 and b > 0) or (a > 0 and c > 0) or (b > 0 and c > 0):
        return True
    else:
        return False

print(two_numbers(1, 2, -8))
