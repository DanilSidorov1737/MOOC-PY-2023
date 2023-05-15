# Write your solution here
# Write your solution here


# Write your solution here
def longest_series_of_neighbours(my_list: list) -> list: 
    if len(my_list) == 2 and abs(my_list[1] - my_list[0]) == 1:
        return len(my_list)
    result = []
    current = [my_list[0]]
    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            current.append(my_list[i])
        else:
            if len(current) > len(result):
                result = current
            current = [my_list[i]]
    if len(current) > len(result):
        result = current

    return len(result)


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))