'''
Module to read .cfg file and return dictionary out of it
'''
import configparser
config = configparser.ConfigParser()


def reading_cfg_file(filename):
    config.read(filename)
    dict = {}
    for section in config.sections():
        dict[section] = {}
        for option in config.options(section):
            dict[section][option] = config.get(section, option)
    #print(dict)
    return dict

#reading_cfg_file("example.cfg")
