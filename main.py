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
    {r'\n+':"NEWLINE"},
    {r"[\()]":"BRAKETS"},
    {r'^\s*$(^(\r\n|\n|\r)$)|(^(\r\n|\n|\r))|^\s*$/gm':"WHITE_SPACE"},
    {r'("(.*?)")':"STRING"},
    {r'(\((.*?)\))':"VARIABLE"},
    {r'func(.*?\n)*?\bend':"FUNCTION"},
    {r'if (.*?) then(.*?\n)*?\bend':"IF"},
    {r'while (.*?) do(.*?\n)*?\bend':"WHILE"},
    {r'for (.*?) do(.*?\n)*?\bend':"WHILE"},
    {r'var (.*?)=(.*|\n)':"VARIABLE"},
    {r'^(.*?[0-9]+)\+([0-9]+).*?':"PLUS_OPERATOR"},
    {r'^(.*?[0-9]+)\/([0-9]+).*?':"DIVIDE_OPERATOR"},
    {r'^(.*?[0-9]+)\*([0-9]+).*?':"MULTI_OPERATOR"},
    {r'^(.*?[0-9]+)\-([0-9]+).*?':"MINUS_OPERATOR"},
    {r"[0-9]+":"NUMBER"},
    {r'(\band)':"AND"},
    {r'(\bbreak)':"BREAK"}
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