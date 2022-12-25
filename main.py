from colorama import *
from pathlib import *
import sys
import re as regex
from utils.lexer_parser import *
from utils.file_sytem_stuff import *
from utils.enums import *
from utils.logger import *

args = sys.argv

regex_enums = EnumList(
    {r'\n+':"NEWLINE"},                                         # group 0: newline
    {r'^($\n)':"WHITE_SPACE"},                                  # group 0: white_space
    {r'("(.*?)")':"STRING"},                                    # group 0: strings
    {r'^\b((func.*? ).*?(\(.*\)))(.*?\n)*?\b(end)':"FUNCTION"}, # group 0: function, group 1: function header, group 2: func, group 3: function arguments, group 4: function insides, group 5: end
    {r'if (.*?) then(.*?\n)*?\bend':"IF"},                      # group 0: if, group 1: condition, group 2: if insides
    {r'while (.*?) do(.*?\n)*?\bend':"WHILE"},                  # group 0: while, group 1: condition, group 2: while insides
    {r'for (.*?) do(.*?\n)*?\bend':"FOR"},                      # group 0: for, group 1: condition, group 2: for insides
    {r'var (.*?)=(.*|\n)':"VARIABLE"},                          # group 0: var, group 1: name, group 2: value
    {r'^(.*?[0-9]+)\+([0-9]+).*?':"PLUS_OPERATOR"},             # group 0: expresion, group 1: first number, group 2: second number
    {r'^(.*?[0-9]+)\/([0-9]+).*?':"DIVIDE_OPERATOR"},           # group 0: expresion, group 1: first number, group 2: second number
    {r'^(.*?[0-9]+)\*([0-9]+).*?':"MULTI_OPERATOR"},            # group 0: expresion, group 1: first number, group 2: second number
    {r'^(.*?[0-9]+)\-([0-9]+).*?':"MINUS_OPERATOR"},            # group 0: expresion, group 1: first number, group 2: second number
    {r"[0-9]+":"NUMBER"},                                       # group 0: numbers
    {r'(\band)':"AND"},                                         # group 0: and
    {r'(\bbreak)':"BREAK"}                                      # group 0: break
)

def compile(file_path):
    file = File(file_path)
    content = file.read()
    Compiler(regex_enums,content)
    
def main():
    filepath = Path()
    version = 9
    pack_name = ""
    pack_description = ""
    
    if args[1] is not None:
        if args[1] == "create":
            if len(args) == 2:
                filepath = Path(input(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Enter the pack location> {Style.RESET_ALL}"))
                version = input(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Enter the pack version> {Style.RESET_ALL}")
                pack_description = input(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Enter the pack description> {Style.RESET_ALL}")
                pack_name = input(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Enter the pack name> {Style.RESET_ALL}")
            elif len(args) == 6:
                pack_name = args[1].replace(r'"', "")
                version = args[2]
                pack_description = args[3].replace(r'"', "")
                filepath = args[4].replace(r'"', "")
            
                if filepath.exists():
                    datapack = DataPack(pack_name, version, pack_description, filepath)
                    globals()["datapack"] = datapack
                    datapack.edit_jsons()
        elif args[1] == "compile":
            if args[2] is not None:
                compile(Path(args[2]))
            else:
                compile(Path(input(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Enter the pack name> {Style.RESET_ALL}")))

if __name__ == "__main__":
    main()