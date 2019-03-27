#!/bin/bash
declare -a foo;
foo[0]=0
foo[1]=1
temp=$(bc <<< "$#+1")
echo $temp
for (( i=2; 0<$#; i++ )); do 
foo[i]=$1
shift
done
echo here
for (( i=2;i<${#foo[@]};i++ )) do

j=$((i-1))
k=$((i-2))

m=${foo[j]}
l=${foo[k]}
n=$(bc <<<"$l + $m")
foo[i]=$n
done

echo ${foo[4]}
