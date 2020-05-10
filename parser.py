#!/usr/bin/python
import re

myFile = open("rules1.txt", "r").readlines()

rules = {
    "DESCRIPTION" : '',
    "STATES": '',
    "ALPHABET_TOKENS": '',
    "TAPE_TOKENS": '',
    "END_OF_TAPE_TOKEN": '',
    "START_STATE": '',
    "ACCEPT_STATES" : '',
    "TRANSITION" : ''
}

# record in dictionary each line(s) where each turing machine attribute appears 
for line in myFile:
    for attribute in rules:    
        if line.startswith(attribute):
            rules[attribute] = line
            lastParsedAttribute = attribute #for later use in case of multiline attribute definition
            break

    # ignore newlines and comments
    if line.startswith("\n") or line.startswith("//"):
        pass
    elif not line.startswith(lastParsedAttribute):
        # line is a continuation of last parsed attribute, so append it
        rules[lastParsedAttribute] += line

# now we can parse corresponding line(s) for each attribute using regular expressions

states                     = re.findall(r'\[([^\[]*)\]',rules["STATES"])[0]
rules["STATES"]            = [x.strip() for x in states.split(",")] 

alphabetTokens             = re.findall(r'\[([^\[]*)\]',rules["ALPHABET_TOKENS"])[0]
rules["ALPHABET_TOKENS"]   = [x.strip() for x in alphabetTokens.split(",")]   

tapeTokens                 = re.findall(r'\[([^\[]*)\]',rules["TAPE_TOKENS"])[0]
rules["TAPE_TOKENS"]       = [x.strip() for x in tapeTokens.split(",")] 

rules["TOKENS"]            = rules["ALPHABET_TOKENS"] + rules["TAPE_TOKENS"]

rules["START_STATE"]       = rules["START_STATE"].split("=",1)[1].replace(" ","").replace("\n","")

acceptStates               = re.findall(r'\[([^\[]*)\]',rules["ACCEPT_STATES"])[0]
rules["ACCEPT_STATES"]     = [x.strip() for x in acceptStates.split(",")] 

rules["END_OF_TAPE_TOKEN"] = rules["END_OF_TAPE_TOKEN"].split("=",1)[1].replace(" ","").replace("\n","")


rules["TRANSITION"] = rules["TRANSITION"].replace(" ","").split("=",1)[1]
# put an entry in dictionary for every transition
dictionary = {}
for transition in re.findall(r'.+-->.+',rules["TRANSITION"]):
  key               = re.findall(r'(.+)-->',transition)[0]
  value             = re.findall(r'-->(.+)',transition)[0]
  dictionary[key] = value

rules["TRANSITION"] = dictionary