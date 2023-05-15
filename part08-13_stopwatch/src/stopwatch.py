# Write your solution here:

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    
    def __str__(self):
        return f"{self.format_digit(self.minutes)}:{self.format_digit(self.seconds)}"
    
    def tick(self):
        self.seconds += 1
        if self.seconds > 59:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > 59:
                self.minutes = 0
                
    def format_digit(self, number):
        if number < 10:
            return f"0{number}"
        else:
            return f"{number}"


if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()