'''
Module to read .conf file and return dictionary out of it
'''

import configparser
config = configparser.ConfigParser()


# Program to convert .conf file to dict
def reading_conf_file(filename):
    config.read(filename)

    dict1 = {}
    for section in config.sections():
        dict1[section] = {}
        for option in config.options(section):
            dict1[section][option] = config.get(section, option)
    #print(dict1)
    return dict1

#reading_conf_file("sample.conf")
