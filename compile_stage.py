#!/usr/bin/python
import os
import requests
import sys

import yaml
from jinja2 import Environment, FileSystemLoader
import json
import pprint

def compile():

    """ Compile the yaml template """
    
    # open the config file 
    stages = yaml.load(open('./group_vars/'+sys.argv[1]+'/vars.yml'))["Stages"]
    
    # get root path
    file_path = os.path.dirname(os.path.realpath(__file__))

    # refrence templates directory 
    env = Environment(loader = FileSystemLoader(file_path+'/templates'), trim_blocks=True, lstrip_blocks=True)

    # load the template file
    template = env.get_template('./template.yml.j2')

    # compile and save the stack template
    config_file = open(file_path+"/templates/stack.yml.j2", "w+")
    config_file.write(template.render(list = stages))

if __name__ == "__main__":
    compile()