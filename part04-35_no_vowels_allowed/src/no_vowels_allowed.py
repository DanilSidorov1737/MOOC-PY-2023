# Write your solution here


# Write your solution here
def no_vowels(my_string: str) -> str: 
    vowels = ['a', 'e', 'i', 'o', 'u']

    for v in vowels:
        if my_string.count(v) > 0:
            my_string = my_string.replace(v, "")
            
    return my_string
            

    


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string)) 
