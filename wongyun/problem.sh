#!/bin/bash

mkdir $1
touch $1/$1.py
touch $1/$1_input.txt

code $1/$1.py
code $1/$1_input.txt
