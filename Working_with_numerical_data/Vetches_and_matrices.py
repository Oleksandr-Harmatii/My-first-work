import numpy as np

vector_1 = np.array([1, 2, 3])
vector_2 = np.array([4, 5, 6])

matrix_1 = np.array([[1, 2], [3, 4], [5, 6]])
matrix_2 = np.array([[7, 8], [9, 10], [11, 12]])

print(f"Розмірність vector_1: {vector_1.shape}")
print(f"Розмірність vector_2: {vector_2.shape}")
print(f"Розмірність matrix_1: {matrix_1.shape}")
print(f"Розмірність matrix_2: {matrix_2.shape}")


vector_sum = vector_1 + vector_2
print(f"Сума векторів: {vector_sum}")

vector_diff = vector_1 - vector_2
print(f"Різниця векторів: {vector_diff}")

matrix_sum = matrix_1 + matrix_2
print(f"Сума матриць: \n{matrix_sum}")

matrix_product = np.dot(matrix_1, matrix_2.T)  
print(f"Множення матриць: \n{matrix_product}")

scalar_multiplication = vector_1 * 2
print(f"Множення вектора на число: {scalar_multiplication}")

matrix_scalar_multiplication = matrix_1 * 3
print(f"Множення матриці на число: \n{matrix_scalar_multiplication}")
