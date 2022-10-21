'''
Module to read .yaml file and return dictionary out of it
'''
#!/usr/bin/env python

import os
import yaml
#from readingConfFile import reading_conf_file

import configparser
config = configparser.ConfigParser()

def reading_yaml_file(filename):
    with open(filename, "r") as stream:
        try:
            data = yaml.safe_load(stream)
            #print(data)
            return data
        except yaml.YAMLError as exc:
            print(exc)

#reading_yaml_file("example.yaml")
