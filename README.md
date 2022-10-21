# sacumen-assignment
Write an installable module in python with the following functionality.

# Description 
The module should be able to read .yaml, .cfg, .conf configuration file formats, read the configurations and generate a flat dictionary out of it.
Depending on the requirement, the module should be able to write the configurations in .env file, .json file or it should also be able to set the configurations in the os environment.”

# Required packages 
python3
pyyaml
pytest

# Package Installtion 
pip install python3
pip install pyyaml
pip install pytest

# Excuting the file 
python main.py <reading file path> [optional]<writting file path>

Where reading file path is the path of .conf/.cfg/.yaml file and it prints dictionalry out of it in terminal. 
Where writting file path is optional of type .json or .env and prints the dictionalry out of reading file and writes it to specified file format.

# Files information 
main.py - main module to excute the code.
readingCfgFile.py - reading the .cfg file and return the dict out of it.
readingConfFile.py - reading the .conf file and return the dict out of it.
readingYamlFile.py - reading the .yaml file and return the dict out of it.
setEnvVar.py - set the os environment variables

