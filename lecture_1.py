
from lecture_1_utilities import add_two_numbers
#sudo pip install names
import names 

print("Python code is running")

def loop_addition():
    max_number_to_add = 10
    for i in range(max_number_to_add):
        result = add_two_numbers(3, i)
        print(result)


def square_numbers():
    num_names_to_generate = 10
    for i in range(num_names_to_generate):
        print(i**2)


def generate_random_names():
    i = 0
    while i < 10:
        one_name = names.get_full_name()
        print(F"One example name: {one_name}")
        i += 1
    


if __name__ == "__main__":
    generate_random_names()
