from pathlib import Path
import json
import os
from shutil import *

def file_exist(filepath):
    return Path(filepath).exists()

class File:
    def __init__(self,file_path) -> None:
        self.filepath = Path(file_path)
        
    def read(self):
        with open(self.filepath,"r") as f:
            content = f.read()
            f.close()
            return content
        
    def write(self,content):
        with open(self.filepath,"w") as f:
            f.write(content)
            f.close()
    
    def getNewlines(self):
        with open(self.filepath,"r") as f:
            content = f.newlines
            f.close()
            return content
    
    # def __new__(cls,*args,**kwargs):
    #     if file_exist(args[0]) is False:
    #         with open(args[0],"x") as f:
    #             f.close()
    #             return f  

class DataPack:
    def __init__(self, pack_name, pack_version, pack_description, pack_destination):
        self.pack_name = pack_name
        self.pack_version = pack_version
        self.pack_description = pack_description
        self.pack_destination = pack_destination
        self.example_pack_location = Path(r"utils\example")
        self.pack = copytree(self.example_pack_location, Path(f"{self.pack_destination}/{self.pack_name}"))
        self.mcmeta = File(str(Path(f"{self.pack}/pack.mcmeta")))
        self.tick_json = File(str(Path(f"{self.pack}/data/minecraft/tags/functions/tick.json")))
        self.load_json = File(Path(f"{self.pack}/data/minecraft/tags/functions/load.json"))
        self.function_folder = File(Path(f"{self.pack}/data/example/functions"))
        os.rename(Path(f"{self.pack}/data/example"), Path(f"{self.pack}/data/{self.pack_name}"))

    def edit_jsons(self):
        # for mcmeta file
        listed = json.loads(self.mcmeta.read())
        listed["pack"]["description"] = self.pack_description
        listed["pack"]["pack_format"] = self.pack_version
        content = json.dumps(listed)
        self.mcmeta.write(content)

        # for tick file
        listed = json.loads(self.tick_json.read())
        listed["values"] = f"{self.pack_name}:tick"
        content = json.dumps(listed)
        self.tick_json.write(content)

        # for load json
        listed = json.loads(self.load_json.read())
        listed["values"] = f"{self.pack_name}:load"
        content = json.dumps(listed)
        self.load_json.write(content)

    def edit_mc_functions(self, filename, content):
        file = File(f"{self.function_folder}/{filename}.mcfunction")
        file.write(content)

    def create_mc_function(filename):
        File(filename)