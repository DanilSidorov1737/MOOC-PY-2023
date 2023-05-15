# Write your solution here
import math

# Write your solution here

def factorials(n: int):
    facts = {}
    for i in range(1, n+1):
        facts[i] = math.factorial(i)
    return facts




if __name__ == "__main__":
    k = factorials(5)
    print(k)