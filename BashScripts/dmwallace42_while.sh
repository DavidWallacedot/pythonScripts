#!/bin/bash
#while-menu2: a menu drive system information program
DELAY=3 # Number of seconds to display results
while true;
do 
	clear
	cat<<- _EOF_
		Please Select :
		
		1. Display System Information
		2. Display Disk Space
		3. Display Hom eSpace Utilization 
		0. Quit
	
		_EOF_
	read -p "Enter selection [0-3] > "
	if [[ "$REPLY" =~ ^[0-3]$ ]]; then
		if [[ "$REPLY" == 1 ]]; then
			echo "Hostname: $HOSTNAME"
			uptime
			echo "Press enter to continue"
			read junk
			continue
		fi
		if [[ "$REPLY" == 2 ]]; then
			df -h
			echo "Press enter to continue"
			read junk			
			continue
		fi
		if [[ "$REPLY" == 3 ]]; then
			if [[ "$(id -u)" -eq 0 ]]; then 
			echo "Home Space Utilization (All Users)"
			du -sh /home/*
			else
				echo "Home Space Utilization ($USER)"
				du -sh "$HOME"
			fi
			echo "Press enter to continue"
			read junk			
			continue
		fi
		if [[ "$REPLY"==0 ]]; then
			break
		fi
	else
		echo "Invalid entry."
		echo "Press enter to continue"
		read junk
	fi
done
echo "Program terminated."

