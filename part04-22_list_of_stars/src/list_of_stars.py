# Write your solution here

def list_of_stars(nums):
    for i in range(len(nums)):
        print(nums[i] * '*')



if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])