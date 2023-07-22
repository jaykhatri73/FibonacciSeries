def fibonacci(n):

    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


n = int(input("Enter the lenght of Fibonacci Series here: "))
result = fibonacci(n)
print(result)
