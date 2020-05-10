#!/usr/bin/python

class NotValidTokenException(Exception):
    def __init__(self, message,token):
        self.message = "Error: " + message + "token: " + token

class UnreacheableTransitionException(Exception):
    def __init__(self, state, token):
        self.message = "Error: There is not a valid transition from state " + state + "given token " + token