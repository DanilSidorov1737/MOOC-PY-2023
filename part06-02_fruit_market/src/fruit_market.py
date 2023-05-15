# write your solution here

# write your solution here



def read_fruits():
    with open("fruits.csv") as new_file:
        fruit_dict = {}
        
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name =  parts[0]
            price = parts[1]
            fruit_dict[name] = float(price)
        return fruit_dict
        



if __name__ == "__main__":
    read_fruits()