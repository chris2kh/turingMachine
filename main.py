#!/usr/bin/python

from parser import rules
from turing import TuringMachine, Tape, Program
from customErrors import NotValidTokenException, UnreacheableTransitionException

print("Welcome to this Turing machine little project\n")
print(rules["DESCRIPTION"])
string = raw_input("please enter the string:  ")
tape = Tape(string)
program = Program(rules)
machine = TuringMachine(program)

try:
    success = machine.run(tape)
    if success:
        print("The string is valid for this program!")
    else:
        print("The string is not valid for this program")
except NotValidTokenException as e: 
    print(e.message)
except UnreacheableTransitionException as e:
    print(e.message)
