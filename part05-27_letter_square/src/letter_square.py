# Write your solution here

def print_square(layers):
    n = layers * 2 + 1
    center = n // 2

    # create a 2D array of letters
    letters = [['C' for i in range(n)] for j in range(n)]
    for i in range(layers):
        letter = chr(ord('B') + i)
        for j in range(center - i, center + i + 1):
            letters[center - i][j] = letter
            letters[center + i][j] = letter
            letters[j][center - i] = letter
            letters[j][center + i] = letter
    
    # print the array
    for row in letters:
        print(''.join(row))

if __name__ == "__main__":
    print_square(5)