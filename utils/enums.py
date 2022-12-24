class Enum:
    def __init__(self,name,**value) -> None:
        self.name = name
        self.value = value
    
    def __str__(self) -> str:
        key = self.value.get("value")
        return f"{self.name}:{key}"

    def getValue(self):
        key = self.value.get("value")
        return key
    
    def getName(self):
        return self.name
                
class EnumList: 
    def __new__(cls, *args, **kwargs):
        cls.tokens = {}
        
        for i in args:
            if type(i) == set:
                en = Enum(list(i)[0],0)
                key = list(i)[0]
                cls.tokens.update({key:en})
            elif type(i) == dict:
                key = str(list(i.keys())[0])
                value = str(i[list(i.keys())[0]])
                en = Enum(name=key,value=value)
                cls.tokens.update({key:en})
    
        return cls.tokens