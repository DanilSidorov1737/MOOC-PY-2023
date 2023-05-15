# write your solution here



def largest():
    with open("numbers.txt") as new_file:
        nums = []
        for line in new_file:
            nums.append(line)
        x = max(nums)
        return int(x)



if __name__ == "__main__":
    largest()