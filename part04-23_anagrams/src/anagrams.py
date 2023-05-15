# Write your solution here

# Write your solution here

def anagrams(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        return True
    else:
        return False
    


if __name__ == "__main__":
    print(anagrams("house", "mouse"))