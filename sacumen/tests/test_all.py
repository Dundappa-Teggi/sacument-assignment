from src.sacumen_assignment.readingCfgFile import reading_cfg_file
from src.sacumen_assignment.readingConfFile import reading_conf_file
from src.sacumen_assignment.readingYamlFile import reading_yaml_file

def test_conf_file_read() :
    expected = {'DBConfigfile': {"'db_url'": "'http//localhost/'",
                  "'db_user'": "'user1'",
                  "'db_password'": "'testpass'",
                  "'db_host'": "'localhost'",
                  "'db_port'": '8080',
                  "'db_name'": "'testdb'"}}
    assert reading_conf_file('resource/sample.conf', expected)