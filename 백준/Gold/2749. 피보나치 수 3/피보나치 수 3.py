def matrix_multiply(matrix1, matrix2):
    matrix1_matrix2 = [
        [(matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]) % 1000000,
         (matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]) % 1000000],
        [(matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]) % 1000000,
         (matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]) % 1000000]
    ]
    return matrix1_matrix2

def fib(number):
    if number <= 1:
        return [[1, 1], [1, 0]]

    if number % 2 == 0:
        new = fib(number // 2)
        return matrix_multiply(new, new)
    else:
        new = fib((number - 1) // 2)
        return matrix_multiply(matrix_multiply(new, new), fib(1))

n = int(input())
if n <= 2:
    result = 1
else:
    a = fib(n-2)
    result = (a[0][0] + a[0][1]) % 1000000

print(result)