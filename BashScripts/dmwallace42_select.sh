#!/bin/bash
#while-menu2: a menu drive system information program

while true;
do
	PS3="Enter Selection [1-4] > "
	clear
	var1="Display System Information"
	var2="Display Disk Space"	
	var3="Display Home Space Utilization"
	
	 select REPLY in "$var1" "$var2" "$var3"   exit
do
	case "$REPLY" in 
exit)	echo "Program terminated."
		break 2 
		;;
	$var1) 	echo "Hostname: $HOSTNAME"
		uptime
		echo "Press enter to continue"
		read junk
		break
		;;
	$var2)	df -h 
		echo "Press enter to continue"
		read junk
		break		
		;;
	$var3)	if [[ "$(id -u)" -eq 0 ]]; then 
			echo "Home Space Utilization (All Users)"
			du -sh /home/*
		else
			echo "Home Space Utilization ($USER)"
			du -sh "$HOME"
		fi
		echo "Press enter to continue"
		read junk		
		break		
		;;
	*)	echo "Invalid entry " >&2
		echo "Please enter [A, B, C, D]"
		echo "Press enter to return to menu"
		read junk
		break
		;;
esac
done

done
