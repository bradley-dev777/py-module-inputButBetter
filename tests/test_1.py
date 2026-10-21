# -*- coding: utf-8 -*-
from inputbutbetter import main


def test_inputstr(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'test string')
    assert main.inputstr("Enter a string: ") == 'test string'


def test_inputstr_rejects_blank_when_requested(monkeypatch, capsys):
    inputs = iter(['   ', 'test string'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert main.inputstr("Enter a string: ", accept_blank=False) == 'test string'
    assert 'Input cannot be blank' in capsys.readouterr().out


def test_inputint(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '42')
    assert main.inputint("Enter an integer: ") == 42


def test_inputint_retries_invalid_input(monkeypatch, capsys):
    inputs = iter(['not an integer', '42'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert main.inputint("Enter an integer: ") == 42
    assert 'Please enter a valid integer.' in capsys.readouterr().out


def test_inputint_with_range(monkeypatch, capsys):
    inputs = iter(['-1', '101', '50'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert main.inputint(
        "Enter an integer between 0 and 100: ", min_val=0, max_val=100
    ) == 50
    assert capsys.readouterr().out.count('Please enter a value between 0 and 100.') == 2


def test_inputfloat(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3.14')
    assert main.inputfloat("Enter a float: ") == 3.14


def test_inputfloat_with_range(monkeypatch, capsys):
    inputs = iter(['-1.0', '101.0', '50.0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert main.inputfloat(
        "Enter a float between 0 and 100: ", min_val=0, max_val=100
    ) == 50.0
    assert capsys.readouterr().out.count('Please enter a value between 0 and 100.') == 2


def test_inputbool_accepts_case_and_whitespace(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: ' YES ')
    assert main.inputbool("Do you like Python? (yes/no): ") is True


def test_inputbool_accepts_custom_values(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'enabled')
    assert main.inputbool(
        "Enable? ", true_values=['enabled'], false_values=['disabled']
    ) is True


def test_inputbool_retries_invalid_value(monkeypatch, capsys):
    inputs = iter(['maybe', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert main.inputbool("Do you like Python? (yes/no): ") is False
    assert 'Please enter a value' in capsys.readouterr().out


def test_inputarr(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'apple, banana, orange')
    assert main.inputarr("Enter fruits separated by commas: ") == [
        'apple', 'banana', 'orange'
    ]


def test_inputarr_with_custom_delimiter(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'red; blue; green')
    assert main.inputarr("Enter colors: ", delimiter=';') == [
        'red', 'blue', 'green'
    ]


def test_inputarr_retries_blank_input(monkeypatch, capsys):
    inputs = iter(['   ', 'apple, banana'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert main.inputarr("Enter fruits: ") == ['apple', 'banana']
    assert 'Please enter values separated by ,' in capsys.readouterr().out


def test_inputarrlooping(monkeypatch):
    inputs = iter(['red', 'blue', 'green', 'done'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert main.inputarrlooping(
        "Enter colors one by one (type 'done' to finish): "
    ) == ['red', 'blue', 'green']


def test_inputarrlooping_with_custom_endsignal(monkeypatch):
    inputs = iter(['red', 'stop'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert main.inputarrlooping("Enter colors: ", endsignal='stop') == ['red']


def test_inputchoice(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'apple')
    assert main.inputchoice(
        "Choose a fruit (apple, banana, orange): ",
        choices=['apple', 'banana', 'orange'],
    ) == 'apple'


def test_inputchoice_strips_whitespace_and_retries_invalid_choice(monkeypatch, capsys):
    inputs = iter(['pear', ' banana '])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert main.inputchoice("Choose a fruit: ", choices=['apple', 'banana']) == 'banana'
    assert 'Please enter one of the following: apple, banana.' in capsys.readouterr().out