#! /bin/bash

cd '/home/vlad/Programs/My_projects/humanity'
hg status
hg commit
hg bookmark -r default master
gedit
