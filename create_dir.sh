#! /bin/bash
 
if [ $(find ~ -type d -name $1) ] 

then
	echo "the directory does exist"
else
	mkdir ~/devnet/$1 && echo "I made a new directory at " && echo $(find ~ -type d -name $1)
fi

