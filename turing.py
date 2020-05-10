#!/usr/bin/python
from customErrors import NotValidTokenException, UnreacheableTransitionException

class TuringMachine():
    def __init__(self, program):
        self.program = program
    
    def run(self, tape):
        self.tape = tape
        self.tape.bound(self.program.endOfTapeToken())
        return self.evaluate()

    def evaluate(self):
        if self.program.mustStop():
            return self.program.haltResult()
        else: 
           newToken = self.program.makeTransition(self.tape.currentToken())
           self.tape.write(newToken)
           self.tape.shift(self.program.newDirection())
           return self.evaluate()


class Tape():
    def __init__(self, message):
        self.message = message
        self.currentPosition = 0
    
    def currentToken(self):
        return self.message[self.currentPosition]

    def write(self,token):
        buffer = list(self.message)
        buffer[self.currentPosition] = token
        self.message = ''.join(buffer)

    def shift(self, direction):
        self.currentPosition = self.currentPosition + direction

    def bound(self, endOfTapeToken):
        self.message = endOfTapeToken + self.message + endOfTapeToken
        self.currentPosition = 1


class Program():
    def __init__(self, rules):
        self.rules = rules
        self.currentState = rules["START_STATE"]
        self.currentMovement = ''
        self.stopSignal = False

    def endOfTapeToken(self):
        return self.rules["END_OF_TAPE_TOKEN"]

    def makeTransition(self, token):
        if token not in self.rules["TOKENS"]:
            raise NotValidTokenException("read token is not valid. ", token)
        
        key = self.currentState + '*' + token
        value = self.rules["TRANSITION"][key]

        self.currentState = value.split("*")[0]
        if self.currentState == 'NA':
            previousState = key.split("*")[0]
            raise UnreacheableTransitionException(previousState, token)

        token = value.split("*")[1]
        if token not in self.rules["TOKENS"]:
            raise NotFoundTokenException("new token according to transition is not valid", token)

        self.currentMovement = value.split("*")[2]
        if self.currentMovement == 'S':
            self.stopSignal = True
        
        return token

    def newDirection(self):
        magnitude = {
            'L': -1,
            'R':  1,
            'S':  0
        }
        return magnitude[self.currentMovement]

    def mustStop(self):
        return self.stopSignal
    
    def haltResult(self):
        return self.currentState in self.rules["ACCEPT_STATES"]