# Turing machine

A command line linear bounded turing machine written in python

## How to use?

You are supposed to write a file with rules for your machine following the syntax used in the example document.
I hope the syntax is intuitive and self explanatory.

Before you run main.py, remember to edit the parser.py file to select the name of the file you just created. Or you could just rewrite the example file to suit your needs.

# Example
```
DESCRIPTION = machine that matches strings with pattern x^n y^n                 
where n is a positive integer and x and y are characters representing alphabet tokens
                                                                                
STATES = [ q0, q1, q2, q3]                                                      
                                                                                                                                                                
ALPHABET_TOKENS = [a,b]                                                         
                                                                                
TAPE_TOKENS = [ _ , # ]                                                         
                                                                                
END_OF_TAPE_TOKEN = #                                                           
                                                                                
START_STATE = q0                                                                
                                                                                
ACCEPT_STATES = [q2]                                                            
                                                                                
// write transitions in the format: from --> to                                 
// use an asterik (*) to separate values like this:                             
// currentState * currentToken --> nextState * newToken * shiftDirection        
// if transition not reachable, write NA after -->                              
                                                                                
TRANSITION =                                                                    
                                                                                
q0 * a --> q0 * a * R                                                           
q0 * b --> q1 * _ * L                                                           
q0 * _ --> q0 * _ * R                                                           
q0 * # --> q2 * # * L                                                           
                                                                                
q1 * a --> q0 * _ * R                                                           
q1 * b --> NA
```
