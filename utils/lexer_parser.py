class Token:
    def __init__(self, value, token_id, token_index):
        self.id = token_id
        self.token_index = token_index
        self.value = value


class Lexer:
    def __init__(self, input_string):
        self.input = input_string.split()
        self.tokens = []
        
    def lex(self):
        for i in range(len(self.input)):
            cur = self.input[i]
            print(cur)
            # if cur == "func":
            #     self.tokens.append(Token(cur, "FUNCTION",i))

            # else:
            #     self.tokens.append(Token(cur, "IDENTIFIER", i))
            # for key in self.token_list.keys():
            #     if cur == key:
            #         self.add_token(Token(i, self.token_list[i], 1))
            #     else:
            #         self.add_token(Token(i, "IDENTIFIER", 1))
                    
    def add_token(self,token):
        self.tokens.append(token)


class Parser:
    def __init__(self, input_tokens):
        self.tokens = input_tokens
        
    def parse(self):
        for i in range(len(self.tokens)):
            cur = self.tokens[i]
