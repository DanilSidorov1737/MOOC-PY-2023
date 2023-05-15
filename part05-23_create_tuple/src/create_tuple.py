# Write your solution here

def create_tuple(x: int, y: int, z: int):
    lst = [x, y, z]
    mini = min(lst)
    maxx = max(lst)
    sumi = x + y + z
    tuple_rst = (mini, maxx, sumi)
    return tuple_rst




if __name__ == "__main__":
    print(create_tuple(1,2,3))