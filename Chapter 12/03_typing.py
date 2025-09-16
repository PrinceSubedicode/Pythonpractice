from typing import List, Tuple, Dict, Union

# 1️⃣ List: a list of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# 2️⃣ Tuple: a fixed pair of values (name, age)
person: Tuple[str, int] = ("Alice", 25)

# 3️⃣ Dict: a dictionary with string keys and int values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# 4️⃣ Union: a value that can be either int or str
result: Union[int, str] = 100  # could also be "Pass"

# Using them together
def describe_person(name_age: Tuple[str, int], marks: Dict[str, int], extra: Union[int, str]):
    name, age = name_age
    print(f"{name} is {age} years old.")
    print(f"Scores: {marks}")
    print(f"Extra info: {extra}")

describe_person(person, scores, result)
