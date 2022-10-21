import os
from readingConfFile import reading_conf_file

def set_os_env() :
    line = reading_conf_file("sample.conf")
    def set_env(d):
        for k, v in d.items():
            if isinstance(v, dict):
                set_env(v)
            else:
                os.environ[k] = v
                #print("{0} : {1}".format(k, v))   
    set_env(line)

set_os_env()