#! /usr/bin/python3


import os, os.path

os.chdir ( os.path.dirname(__file__) )
print ("Current directory: ", os.getcwd())


os.system('hg addremove')
os.system('hg commit')
os.system('hg bookmark -r default master')
os.system('hg push git+ssh://git@github.com:vlad1777d/humanity.git')
print("Script finished.")
