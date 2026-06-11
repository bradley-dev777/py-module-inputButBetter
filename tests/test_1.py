# -*- coding: utf-8 -*-
import pytest
from inputbutbetter import main
def test_inputstr(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'test string')
    assert main.inputstr("Enter a string: ") == 'test string'
    
def test_inputint(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '42')
    assert main.inputint("Enter an integer: ") == 42
    
def test_inputint_with_range(monkeypatch):
    inputs = iter(['-1', '101', '50'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert main.inputint("Enter an integer between 0 and 100: ", min_val=0, max_val=100) == 50

def test_inputfloat(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3.14')
    assert main.inputfloat("Enter a float: ") == 3.14

def test_inputfloat_with_range(monkeypatch):
    inputs = iter(['-1.0', '101.0', '50.0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert main.inputfloat("Enter a float between 0 and 100: ", min_val=0, max_val=100) == 50.0

def test_inputbool(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'yes')
    assert main.inputbool("Do you like Python? (yes/no): ") == True

def test_inputarr(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'apple, banana, orange')
    assert main.inputarr("Enter fruits separated by commas: ") == ['apple', 'banana', 'orange']

def test_inputarrlooping(monkeypatch):
    inputs = iter(['red', 'blue', 'green', 'done'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert main.inputarrlooping("Enter colors one by one (type 'done' to finish): ") == ['red', 'blue', 'green']

def test_inputchoice(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'apple')
    assert main.inputchoice("Choose a fruit (apple, banana, orange): ", choices=['apple', 'banana', 'orange']) == 'apple'