# write your solution here



def matrix_sum():
    with open("matrix.txt") as new_file:
        count = 0
        for line in new_file:
            parts = line.split(",")
            for part in parts:
                count += int(part)
        return count


def matrix_max():
    with open("matrix.txt") as new_file:
        nums = []
        for line in new_file:
            parts = line.split(",")
            for part in parts:
                nums.append(part)
        return int(max(nums))

def row_sums():
    with open("matrix.txt") as new_file:
        sums = []
        for line in new_file:
            line = line.strip()
            parts = line.split(",")
            sums_lines = 0
            for num in parts:
                sums_lines += int(num)
            sums.append(sums_lines)
      
        return sums




if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()

