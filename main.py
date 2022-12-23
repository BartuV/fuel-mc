from colorama import *
from pathlib import *
import sys
from utils.lexer_parser import *
from utils.file_sytem_stuff import *
from utils.enums import *
from utils.logger import *

args = sys.argv

a = EnumList(
    {"func":"FUNCTION"},
    {"while":"WHILE"},
    {"loop":"LOOP"},
    {"break":"LOOP_BREAKER"},
    {r"\n":"NEWLINE"},
    {"if":"IF"},
    {"=":"EQUALS_OPERATOR"},
    {"*":"MULTI_OPERATOR"},
    {"-":"MINUS_OPERATOR"},
    {"+":"PLUS_OPERATOR"},
    {"for":"FOR_LOOP"},
    {"end":"END"},
    {"and":"IF_AND"},
    {"do":"LOOP_STARTER"},
    {"then":"IF_STARTER"},
    {"const":"CONSTANT_VARIABLE"},
    {"var":"VARIABLE_STARTER"}
)

def compile(file_path):
    file = File(file_path)
    content = file.read()
    lexer = Lexer(content)
    lexer.lex()
    
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
        elif args[1] == "compile":
            compile(args[2])
        
    if filepath.exists():
        datapack = DataPack(pack_name, version, pack_description, filepath)
        globals()["datapack"] = datapack
        datapack.edit_jsons()

if __name__ == "__main__":
    main()