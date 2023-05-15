def formatted(nums):
    formatted_list = []
    for i in range(len(nums)):
        formatted_list.append("{0:.2f}".format(nums[i]))
    return formatted_list

if __name__ == "__main__":
    my_list = [1.234]
    new_list = formatted(my_list)
    print(new_list)