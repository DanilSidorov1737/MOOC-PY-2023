def smallest_average(person1: dict, person2: dict, person3: dict):
    personone = 0
    persontwo = 0
    personthree = 0
    for i in range(1,4):
        personone += person1["result" + str(i)]
        persontwo += person2["result" + str(i)]
        personthree += person3["result" + str(i)]
        
    if personone <= persontwo and personone <= personthree:
        return person1
    elif persontwo <= personone and persontwo <= personthree:
        return person2
    else:
        return person3   
        
        

if __name__ == "__main__":
    person1 = {"name": "Larry", "result1": 5, "result2": 4, "result3": 3}
    person2 = {"name": "Danil", "result1": 7, "result2": 7 , "result3": 7}
    person3 = {"name": "Greg", "result1": 1, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))
