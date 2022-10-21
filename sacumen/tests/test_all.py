'''
Test case to teest the file convert from .cfg, .conf or .yaml to  dictionary
'''
import sys
import os
from sys import stderr
import pytest
import subprocess
from src.sacumen_assignment.readingCfgFile import reading_cfg_file
from src.sacumen_assignment.readingConfFile import reading_conf_file
from src.sacumen_assignment.readingYamlFile import reading_yaml_file
from main import readingFile


def test_conf_file_read() :
    expected = {'DBConfigfile': {"'db_url'": "'http//localhost/'",
                  "'db_user'": "'user1'",
                  "'db_password'": "'testpass'",
                  "'db_host'": "'localhost'",
                  "'db_port'": '8080',
                  "'db_name'": "'testdb'"}}
    assert reading_conf_file('resource/sample.conf') == expected


def test_cfg_file_read() :
    expected = {'Section': {'language': 'en-US',
             'order': '4',
             'start': 'tex',
             'heading': 'headingheading',
             'program': 'CHART',
             '07.07.04 00': '00:00'}}
    assert reading_cfg_file('resource/example.cfg') == expected

def test_yaml_file_read() :
    expected = {'European': ['Boston Red Sox', 'Detroit Tigers', 'New York Yankees'],
                'national': ['New York Mets', 'Chicago Cubs', 'Atlanta Braves']}
    assert reading_yaml_file('resource/example.yaml') == expected


# def test_reading_file_from_main(capsys) :
#     out_file_name = 0
#     file_name, file_type = os.path.splitext("example.cfg")
#     file_name = "example.cfg"
#     if len(sys.argv) > 2 :
#         out_file_name, out_file_type = os.path.splitext(sys.argv[2])

#     readingFile(file_name, file_type, out_file_name)
#     expected = {'Section': {'language': 'en-US',
#              'order': '4',
#              'start': 'tex',
#              'heading': 'headingheading',
#              'program': 'CHART',
#              '07.07.04 00': '00:00'}}
#     out, err = capsys.readouterr()
#     assert  isinstance(expected, dict)    
