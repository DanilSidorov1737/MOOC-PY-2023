def remove_smallest(numbers: list):
   mn = min(numbers)
   for num in numbers[:]:  # iterate over a copy of the list
       if num == mn:
           numbers.remove(num)
    



if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)