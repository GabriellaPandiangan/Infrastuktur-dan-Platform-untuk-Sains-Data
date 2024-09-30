def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def generate_factorials(n):
    result = []
    for i in range(1, n + 1):
        result.append(factorial(i))
    return result

# Contoh penggunaan
n = 4
output = generate_factorials(n)
print(output)  # Output: [1, 1, 2, 6, 24]
