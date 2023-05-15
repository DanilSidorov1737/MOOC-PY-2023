# Write your solution here

def row_sums(my_matrix: list):
    for i in range(len(my_matrix)):
        row_sum = sum(my_matrix[i])
        my_matrix[i].append(row_sum)
    print(my_matrix)
  
    
    print(my_matrix)
        

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)