# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:
    def __init__(self, week, correct_numbers):
        self.week = week
        self.correct_numbers = correct_numbers
    
    def number_of_hits(self, my_numbers: list):
        return len([num for num in my_numbers if num in self.correct_numbers])
    
    def hits_in_place(self, my_numbers: list):
        return [num if num in self.correct_numbers else -1 for num in my_numbers]








