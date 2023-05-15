def histogram(string: str) -> str:
    groups = {}
    for i in string:
        if i not in groups:
            groups[i] = 0
        groups[i] += 1
    
    result = ""
    for i, j in groups.items():
        result += f"{i} {j * '*'}\n"
    
    print(result)
    return result

if __name__ == "__main__":
    histogram("historgram")
   