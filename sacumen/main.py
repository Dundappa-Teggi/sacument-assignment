import sys
import os
import pprint
import json

from src.sacumen_assignment.readingCfgFile import reading_cfg_file
from src.sacumen_assignment.readingConfFile import reading_conf_file
from src.sacumen_assignment.readingYamlFile import reading_yaml_file


'''
Method to write a content to .json or .env files
out file must me mentioned in command line argument along the input file.
'''

def writting_file(data) :
    if out_file_type == ".json" :
        json_object = json.dumps(data, indent = 4) 
        with open(sys.argv[2], "w+") as outfile:
            outfile.write(json_object)
        return ".json file written"

    elif out_file_type == '.env' :
        with open(sys.argv[2], 'w+') as f :
            for key, val in data.items() :
                f.write("{}={}\n".format(key, val))
        return ".env file written"

'''
Reading .yaml, .cfg or .conf format files and prints dictionary out of it
'''
# Reading .cfg file and writting to .json or .env file if out file mentioned
def readingFile(file_name, file_type,out_file_name) :
    
    if file_type == '.cfg' :
        data = reading_cfg_file(file_name)
        if out_file_name:
            status = writting_file(data)
            print(status)
        pprint.pp(data)


    # Reading .conf file and writting to .json or .env file if out file mentioned
    if file_type == '.conf' :
        data = reading_conf_file(file_name)
        if out_file_name:
            status = writting_file(data)
            print(status)
        pprint.pp(data)


    # Reading .yaml file and writting to .json or .env file if out file mentioned
    if file_type == '.yaml' :
        data = reading_yaml_file(file_name)
        if out_file_name:
            status = writting_file(data)
            print(status)
        pprint.pp(data)


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    out_file_name = 0
    if len(sys.argv) ==1 :
        print("No file found to read")
        exit(0)
    file_name, file_type = os.path.splitext(sys.argv[1])
    file_name = sys.argv[1]
    if len(sys.argv) > 2 :
        out_file_name, out_file_type = os.path.splitext(sys.argv[2])

    readingFile(file_name, file_type, out_file_name)
