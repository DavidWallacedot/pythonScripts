#!/bin/bash
num1=$1
num2=$2

if [ "$num1" -eq "$num2" ]; then
	echo "$num1 is equal to $num2"
elif [ "$num1" -gt "$num2" ]; then
	echo "$num1 is greater  $num2"
elif [ "$num1" -lt "$num2" ]; then
	echo "$num1 is less than  $num2"
else
	echo "there was an error"
fi
