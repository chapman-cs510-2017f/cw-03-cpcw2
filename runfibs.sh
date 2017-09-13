#!/bin/bash 
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
for i in {1..5..1}
do
n=$(python3 fib.py $i)
if [[ $i -lt 5 ]]
then
printf "$n""," >> fibs.csv
else
printf "$n" >> fibs.csv
fi
done