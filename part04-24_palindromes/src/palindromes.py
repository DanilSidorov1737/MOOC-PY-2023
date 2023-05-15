# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!


# Write your solution here

# Write your solution here

def palindromes():
    while True:
        string = input("Please type in a palindrome: ")
        if string[::-1] == string:
            print(f"{string} is a palindrome")
        elif string[::-1] != string:
            print("that wasn't a palindrome")
   
    


if __name__ == "__main__":
    palindromes()
