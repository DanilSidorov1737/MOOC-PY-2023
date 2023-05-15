# Write your solution here


def filter_solutions():

    with open("solutions.csv") as input_file, \
         open("correct.csv", "w") as correct_file, \
         open("incorrect.csv", "w") as incorrect_file:
        
        for line in input_file:
            name, problem, result = line.strip().split(";")
            if eval(problem) == int(result):
                correct_file.write(line)
            else:
                incorrect_file.write(line)





if __name__ == "__main__":
    filter_solutions()