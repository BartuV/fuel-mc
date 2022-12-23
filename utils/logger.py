import colorama

class Error:
    def __new__(cls,*args, **kwargs):
        for i in args:
            if i is not None and i is not "":  
                print(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}Error: {str(i)}{colorama.Style.RESET_ALL}")
            
class Warn:
    def __new__(cls,*args, **kwargs):
        for i in args:
            if i is not None and i is not "":  
                print(f"{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}Warn: {str(i)}{colorama.Style.RESET_ALL}")
            
class Info:
    def __new__(cls,*args, **kwargs):
        for i in args:
            if i is not None and i is not "":  
                print(f"{colorama.Fore.GREEN}{colorama.Style.BRIGHT}Info: {str(i)}{colorama.Style.RESET_ALL}")