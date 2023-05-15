# Write your solution here

def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]




if __name__ == "__main__":
    print(transpose())