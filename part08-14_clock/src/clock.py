# Write your solution here:


# Write your solution here:

class Clock:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.seconds = seconds
        self.minutes = minutes
    
    def __str__(self):
        return f"{self.format_digit(self.hours)}:{self.format_digit(self.minutes)}:{self.format_digit(self.seconds)}"
        
    def set(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0
    
    def tick(self):
        self.seconds += 1
        if self.seconds > 59:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > 59:
                self.minutes = 0
                self.hours += 1
                if self.hours > 23:
                    self.minutes = 0
                    self.hours = 0
                
    def format_digit(self, number):
        if number < 10:
            return f"0{number}"
        else:
            return f"{number}"


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)    
