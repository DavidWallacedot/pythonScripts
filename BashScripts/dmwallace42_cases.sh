#!/bin/bash
#while-menu2: a menu drive system information program
while true;
do

	clear
	echo "
		Please Select :
		
		A. Display System Information
		B. Display Disk Space
		C. Display Home Space Utilization 
		D. Quit
	
		"
	read -p "Enter selection [A, B, C, D] > "
	case "$REPLY" in 
	d|D)	echo "Program terminated."
		break 
		;;
	a|A) 	echo "Hostname: $HOSTNAME"
		uptime
		echo "Press enter to continue"
		read junk
		;;
	b|B)	df -h 
		echo "Press enter to continue"
		read junk		
		;;
	c|C)	if [[ "$(id -u)" -eq 0 ]]; then 
			echo "Home Space Utilization (All Users)"
			du -sh /home/*
		else
			echo "Home Space Utilization ($USER)"
			du -sh "$HOME"
		fi
		echo "Press enter to continue"
		read junk		
		;;
	*)	echo "Invalid entry " >&2
		echo "Please enter [A, B, C, D]"
		echo "Press enter to return to menu"
		read junk
		;;
esac	
done
