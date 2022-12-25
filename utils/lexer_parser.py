import re
from utils.enums import *

class Token:
    def __init__(self, value, token_id, token_index):
        self.id = token_id
        self.token_index = token_index
        self.value = value
        
class Compiler:
    def __init__(self,regex_enums,input):
        for key in regex_enums:
            # print(key)
            result = re.search(key,input)
            if result:
                if result.string == r"\n":
                    continue
                
        
class Lexer:
    def __init__(self, input_string,enums):
        self.input = input_string.split()
        self.tokens = []
        self.enums = enums
        for i in range(len(self.input)):
            cur = self.input[i]
            if cur in self.enums:
                # print(f"{self.enums[cur].getValue()}: {cur}")
                self.tokens.append(Token(cur,self.enums[cur].getValue() ,i))
            else:
                self.tokens.append(Token(cur, "IDENTIFIER",i))
                
        for i in range(len(self.tokens)):
            cur = self.tokens[i]