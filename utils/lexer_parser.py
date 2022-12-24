class Token:
    def __init__(self, value, token_id, token_index):
        self.id = token_id
        self.token_index = token_index
        self.value = value


class Lexer:
    def __init__(self, input_string,enums):
        self.input = input_string.split()
        self.tokens = []
        self.enums = enums
        
    def lex(self):
        for i in range(len(self.input)):
            cur = self.input[i]
            
            if cur in self.enums:
                print(f"{self.enums[cur].getValue()}: {cur}")
                self.tokens.append(Token(cur,self.enums[cur].getValue() ,i))
            else:
                self.tokens.append(Token(cur, "IDENTIFIER",i))
                    
    def add_token(self,token):
        self.tokens.append(token)


class Parser:
    def __init__(self, input_tokens):
        self.tokens = input_tokens
        
    def parse(self):
        for i in range(len(self.tokens)):
            cur = self.tokens[i]
