#!/bin/bash
function Fib(){
if [[ "$1" -le 1 ]]; then
	echo $1

else
	a=${Fib[$1-1]}
	b=${Fib[$1-2]}
	
	c=$( Fib a )
	
	d=$( Fib b)
	echo $d
	echo $((c + d))
	
	fi
}

Fib $1
