import re

def is_dotw(my_string: str) -> bool:
    regex = r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun)"
    return bool(re.search(regex, my_string))

def all_vowels(my_string: str) -> bool:
    regex = r"^[aeiou]+$"
    return bool(re.match(regex, my_string))

def time_of_day(my_string: str) -> bool:
    regex = r"^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$"
    return bool(re.match(regex, my_string))