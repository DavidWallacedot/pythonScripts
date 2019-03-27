#!/bin/bash
function Backup(){

if [ -e "$1" ]; then
if [ -f "$1" ]; then
FILENAME=$( basename "$1")
DATE=$( date +%F )
BACKUP_FILENAME="${DATE}-$FILENAME.gz"
gzip -c "$1" > "$BACKUP_FILENAME"
fi
if [ -d "$1" ]; then
DIRNAME=$( dirname "$1")
DATE=$( date +%F )
BACKUP_FILENAME="${DATE}-$DIRNAME.gz"
tar -cvf $BACKUP_FILENAME.tar.gz $1 
fi
else
echo "error: "$1" : No such file or directory"
fi
}

if [ $# -eq 0 ];then
echo "Usage: dmwallace42_backup.sh infile..."
fi

for ((i=0; 0<$#;i++ ));do
Backup $1
shift
done

