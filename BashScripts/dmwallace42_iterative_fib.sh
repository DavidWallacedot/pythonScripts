#!/bin/bash
function Fib(){
declare -a foo;
foo[0]=0
foo[1]=1
length=$(bc <<< "$1-1")
for (( i=2;i<$1;i++ )); do

j=$((i-1))
k=$((i-2))

m=${foo[j]}
l=${foo[k]}
n=$(bc <<<"$l + $m")
foo[i]=$n

done
#echo -n F($1)
echo -n "F($1):"
echo ${foo[length]}
}

for (( i=1; 0<$#; i++ )); do 
Fib $1
shift
done
