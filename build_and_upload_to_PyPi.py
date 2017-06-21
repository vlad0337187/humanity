#! /usr/bin/python3


import os, os.path

os.chdir ( os.path.dirname(__file__) )
print ("Current directory: ", os.getcwd())


os.system('python3 setup.py sdist upload')
os.system('python3 setup.py bdist_wheel upload')
