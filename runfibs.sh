#!/bin/bash 

# Name: Chelsea Parlett & Chris Watkins
# Student ID: 2298930 & 1450263
# Email: parlette@chapman.edu & watki115@mail.chapman.edu
# Course: CS520 Fall 2017
# Assignment: Classwork 3
###
if [ -f ./fibs.csv ]
then 
    if [ -f ./fibs.csv.bak ]
    then
        echo "Backup Exists"
        exit 0
    else
        mv fibs.csv fibs.csv.bak
        rm fibs.csv
        echo "Backup Occured"
    fi   
    touch fibs.csv
else
    touch fibs.csv
fi
for i in {1..10000..1}
do
n=$(python3 fib.py $i)
if [[ $i -lt 10000 ]]
then
printf "$n""," >> fibs.csv
else
printf "$n" >> fibs.csv
fi
done