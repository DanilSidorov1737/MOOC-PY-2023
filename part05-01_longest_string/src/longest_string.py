# Write your solution here

def longest(strings: list):
    string_len = []
    for i in range(len(strings)):
        string_len.append(len(strings[i]))
    ml = max(string_len)
    for i in range(len(string_len)):
        if len(strings[i]) == ml:
            return strings[i]
    

        

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

