# -*- coding: utf-8 -*-

def inputstr(prompt: str, accept_blank: bool = True, err_msg: str = "Input cannot be blank. Please try again.") -> str: 
    """Improved function for getting a string input.

    Args: 
        prompt (str): The prompt to show to the user.
        accept_blank (bool, optional): Whether to accept a blank/whitespace-only value. Defaults to True.
        err_msg (str, optional): Error message to show if input is blank/whitespace-only. Defaults to "Input cannot be blank. Please try again.".

    Returns: 
        str: The user input string.
    """
    inp = input(prompt)
    if not accept_blank and inp.strip() == "": 
        print(err_msg)
        return inputstr(prompt, accept_blank)
    return inp

def inputint(prompt: str, min_val: int|None = None, max_val: int|None = None, err_msg: str = "Please enter a valid integer.", range_msg: str = "Please enter a value between {min_val} and {max_val}.") -> int: 
    """Input function that only accepts integers.

    Args: 
        prompt (str): The prompt to show to the user.
        min_val (int | None, optional): Minimum allowed value. Defaults to None.
        max_val (int | None, optional): Maximum allowed value. Defaults to None.
        err_msg (str, optional): Error message to display if input is not an integer. Defaults to "Please enter a valid integer.".
        range_msg (str, optional): Error message to display if input is out of the allowed range (processed with the minimum and maximum values above). Defaults to "Please enter a value between {min_val} and {max_val}.".

    Returns: 
        int: The user input integer.
    """
    while True: 
        try: 
            value = int(input(prompt))
            if min_val is not None and value < min_val: 
                print(range_msg.format(min_val = min_val, max_val = max_val))
                continue
            if max_val is not None and value > max_val: 
                print(range_msg.format(min_val = min_val, max_val = max_val))
                continue
            return value
        except ValueError: 
            print(err_msg)

def inputfloat(prompt: str, min_val: int|None = None, max_val: int|None = None, err_msg: str = "Please enter a valid number.", range_msg: str = "Please enter a value between {min_val} and {max_val}.") -> float:  
    """Input function that only accepts integers and floating-point numbers.

    Args:
        prompt (str): The prompt to show to the user.
        min_val (int | None, optional): Minimum allowed value. Defaults to None.
        max_val (int | None, optional): Maximum allowed value. Defaults to None.
        err_msg (str, optional): Error message to display if input is not a valid integer or floating-point number. Defaults to "Please enter a valid number.".
        range_msg (str, optional): Error message to display if input is out of the allowed range (processed with the minimum and maximum values above). Defaults to "Please enter a value between {min_val} and {max_val}.".

    Returns:
        float: The user input number presented as a floating-point number.
    """
    while True: 
        try: 
            value = float(input(prompt))
            if min_val is not None and value < min_val: 
                print(range_msg.format(min_val = min_val, max_val = max_val))
                continue
            if max_val is not None and value > max_val: 
                print(range_msg.format(min_val = min_val, max_val = max_val))
                continue
            return value
        except ValueError: 
            print(err_msg)

def inputbool(prompt: str, err_msg: str = "Please enter a value in {true_values} or {false_values}.", true_values: list = ['yes', 'y'], false_values: list = ['no', 'n']) -> bool: 
    """Input function for getting a boolean value from arrays.

    Args:
        prompt (str): The prompt to show to the user.
        err_msg (str, optional): Error message to display if input is not in either arrays below (processed with the arrays below). Defaults to "Please enter a value in {true_values} or {false_values}.".
        true_values (list, optional): Values to return True if recieved. Defaults to ['yes', 'y'].
        false_values (list, optional): Values to return False if recieved. Defaults to ['no', 'n'].

    Returns:
        bool: The user input boolean from the arrays.
    """
    while True: 
        value = input(prompt).strip().lower()
        if value in true_values: 
            return True
        elif value in false_values: 
            return False
        else: 
            print(err_msg.format(true_values = true_values, false_values = false_values))
            
def inputarr(prompt: str, delimiter: str = ',', err_msg: str = "Please enter values separated by {delimiter}.") -> list: 
    """Input function for lists using a delimiter

    Args:
        prompt (str): The prompt to show to the user.
        delimiter (str, optional): The delimiter used to split the input. Defaults to ','.
        err_msg (str, optional): The error message to display if input is invalid. Defaults to "Please enter values separated by {delimiter}.".

    Returns:
        list: A list of the values entered by the user.
    """
    while True: 
        value = input(prompt).strip()
        if value: 
            return [item.strip() for item in value.split(delimiter)]
        else: 
            print(err_msg.format(delimiter = delimiter))
            
def inputarrlooping(prompt: str, endsignal: str = 'done', err_msg: str = "Please enter values one by one. Type '{endsignal}' to finish.") -> list: 
    """Input function for lists using a loop.

    Args:
        prompt (str): The prompt to show to the user.
        endsignal (str, optional): The signal to indicate the end of input. Defaults to 'done'.
        err_msg (str, optional): The error message to display if input is invalid (processed with the endsignal above.). Defaults to "Please enter values one by one. Type '{endsignal}' to finish.".

    Returns:
        list: A list of the values entered by the user.
    """
    print(err_msg.format(endsignal = endsignal))
    values  =  []
    while True: 
        value  =  input(prompt).strip()
        if value.lower() == endsignal.lower(): 
            break
        values.append(value)
    return values

def inputdict(prompt: str, separator: str = ':', delimiter: str = ',', err_msg: str = "Please enter key-value pairs in the format 'key{separator}value', separated by '{delimiter}'{}.") -> dict: 
    """Input function for dictionaries.

    Args:
        prompt (str): The prompt to show to the user.
        separator (str, optional): The separator between keys and values. Defaults to ':'.
        delimiter (str, optional): The delimiter between key-value pairs. Defaults to ','.
        err_msg (str, optional): The error message to display if input is invalid. Defaults to "Please enter key-value pairs in the format 'key:value', separated by commas.".

    Returns:
        dict: A dictionary of the key-value pairs entered by the user.
    """
    while True: 
        value = input(prompt).strip()
        if value: 
            try: 
                return {item.split(':')[0].strip(): item.split(':')[1].strip() for item in value.split(',')}
            except IndexError: 
                print(err_msg)
        else: 
            print(err_msg)

def inputchoice(prompt: str, choices: list, err_msg: str = "Please enter one of the following:  {choices}.") -> str: 
    """Input function restricted to a set of values.

    Args:
        prompt (str): The prompt to show to the user.
        choices (list): The list of valid choices.
        err_msg (str, optional): The error message to display if input is invalid. Defaults to "Please enter one of the following: {choices}.".

    Returns:
        str: The valid choice entered by the user.
    """
    choices_str = ', '.join(choices)
    while True: 
        value = input(prompt).strip()
        if value in choices: 
            return value
        else: 
            print(err_msg.format(choices = choices_str))
            
if __name__ == "__main__": 
    # Example usage
    name = inputstr("Enter your name: ")
    age = inputint("Enter your age: ", min_val = 0)
    height = inputfloat("Enter your height in meters: ", min_val = 0)
    likes_python = inputbool("Do you like Python? (yes/no): ")
    hobbies = inputarr("Enter your hobbies separated by commas: ")
    favorite_colors = inputarrlooping("Enter your favorite colors one by one (type 'done' to finish): ")
    choice = inputchoice("Choose a fruit (apple, banana, orange): ", choices = ['apple', 'banana', 'orange'])
    
    print(f"Name: {name}, Age: {age}, Height: {height}, Likes Python: {likes_python}, Hobbies: {hobbies}, Favorite Colors: {favorite_colors}, Chosen Fruit: {choice}")