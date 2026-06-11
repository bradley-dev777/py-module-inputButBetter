# -*- coding: utf-8 -*-

def inputstr(prompt):
    return input(prompt)

def inputint(prompt, min_val=None, max_val=None, err_msg="Please enter a valid integer.", range_msg="Please enter a value between {min_val} and {max_val}."):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(range_msg.format(min_val=min_val, max_val=max_val))
                continue
            if max_val is not None and value > max_val:
                print(range_msg.format(min_val=min_val, max_val=max_val))
                continue
            return value
        except ValueError:
            print(err_msg)

def inputfloat(prompt, min_val=None, max_val=None, err_msg="Please enter a valid number.", range_msg="Please enter a value between {min_val} and {max_val}."):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(range_msg.format(min_val=min_val, max_val=max_val))
                continue
            if max_val is not None and value > max_val:
                print(range_msg.format(min_val=min_val, max_val=max_val))
                continue
            return value
        except ValueError:
            print(err_msg)

def inputbool(prompt, err_msg="Please enter a value in {true_values} or {false_values}.", true_values=['yes', 'y'], false_values=['no', 'n']):
    while True:
        value = input(prompt).strip().lower()
        if value in true_values:
            return True
        elif value in false_values:
            return False
        else:
            print(err_msg.format(true_values=true_values, false_values=false_values))
            
def inputarr(prompt, delimiter=',', err_msg="Please enter values separated by {delimiter}."):
    while True:
        value = input(prompt).strip()
        if value:
            return [item.strip() for item in value.split(delimiter)]
        else:
            print(err_msg.format(delimiter=delimiter))
            
def inputarrlooping(prompt, endsignal='done', err_msg="Please enter values one by one. Type '{endsignal}' to finish."):
    print(err_msg.format(endsignal=endsignal))
    values = []
    while True:
        value = input(prompt).strip()
        if value.lower() == endsignal.lower():
            break
        values.append(value)
    return values

def inputchoice(prompt, choices, err_msg="Please enter one of the following: {choices}."):
    choices_str = ', '.join(choices)
    while True:
        value = input(prompt).strip()
        if value in choices:
            return value
        else:
            print(err_msg.format(choices=choices_str))
            
if __name__ == "__main__":
    # Example usage
    name = inputstr("Enter your name: ")
    age = inputint("Enter your age: ", min_val=0)
    height = inputfloat("Enter your height in meters: ", min_val=0)
    likes_python = inputbool("Do you like Python? (yes/no): ")
    hobbies = inputarr("Enter your hobbies separated by commas: ")
    favorite_colors = inputarrlooping("Enter your favorite colors one by one (type 'done' to finish): ")
    choice = inputchoice("Choose a fruit (apple, banana, orange): ", choices=['apple', 'banana', 'orange'])
    
    print(f"Name: {name}, Age: {age}, Height: {height}, Likes Python: {likes_python}, Hobbies: {hobbies}, Favorite Colors: {favorite_colors}, Chosen Fruit: {choice}")