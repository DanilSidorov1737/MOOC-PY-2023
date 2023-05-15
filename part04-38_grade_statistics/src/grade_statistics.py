# Write your solution here

def ask():
    plist = []
    while True:
        points = input("Exam points and exercises completed: ")
        if points != "":
            plist.append(points)
        else:
            break
    return plist
    
def calculate(plist: list):
    five = 0
    four = 0
    three = 0
    two = 0
    one = 0
    zero = 0
    
    points_sum = 0
    passes = 0
    
    for i in plist:

        parts = i.split()
        num1 = int(parts[0])
        num2 = int(parts[1])
        
        x = num1 + ((num2 / 100) * 10)
        points_sum += x
        
        if num1 >= 10:
            passes += 1

            if x > 0 and x <= 14:
                zero += 1
            elif x > 14 and x <= 17:
                one += 1
            elif x > 17 and x <= 20:
                two += 1
            elif x > 20 and x <= 23:
                three += 1
            elif x > 23 and x <= 26:
                four += 1
            elif x > 26 and x <= 30:
                five += 1
        else:
            zero += 1
        
        
    #point_sum =
    total_students = len(plist)
    points_average = (points_sum / total_students)
    pass_percentage = (passes / total_students) * 100
    
    print(f"Statistics:\nPoints average: {points_average:.1f}\nPass percentage: {pass_percentage:.1f}")
    print("Grade distribution:\n  5:", "*" * five, "\n  4:", "*" * four, "\n  3:", "*" * three, "\n  2:", "*" * two, "\n  1:", "*" * one, "\n  0:", "*" * zero)

        
        
      
        
        
def main():
    plist = ask()
    calculate(plist)

main()        
  

