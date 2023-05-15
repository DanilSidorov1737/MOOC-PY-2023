# Write your solution here
def everything_reversed(my_list: list):
    rlist = []
    for i in range(len(my_list)):
        x = my_list[i][::-1]
        rlist.append(x)
    return rlist


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
