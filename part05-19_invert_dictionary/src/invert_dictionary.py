# Write your solution here

def invert(dictionary: dict):
    return {v: k for k, v in dictionary.items()}





if __name__ == "__main__":
    
    inverted = invert({1: 10, 2: 20, 3: 30})
    print(inverted)  
    
   