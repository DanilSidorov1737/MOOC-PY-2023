# Write your solution here

def line(num, string):
    if string == "":
        print(num * "*")
    else:
        string = string[0]        
        print(num * string)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")