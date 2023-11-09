#!/bin/bash

usage()
{
	echo "usage: ./create-pico-challenge-writeup.sh -c (be|crypt|foren|gs|re|we) -n \"challenge_name\" -p challenge_points"

}

while getopts "hc:n:p:" option; do
   case $option in
  
      c) #enter a category name
         cn=$OPTARG;;
         
      n) # Enter a name
         challenge_name=$OPTARG;;

      
      p) # Enter a name
         challenge_points=$OPTARG;;
         
  *|?|h) # Invalid option
         usage
         exit;;
   esac
done

if [ "$cn" == "be" ];
then
   category="binary-exploitation"  
   category_name="Binary Exploitation"
   
elif [ "$cn" == "crypt" ];
then
   category="cryptography"
   category_name="Cryptogrphy"
   
elif [ "$cn" == "foren" ];
then
   category="forensics"
   category_name="Forensics"
   
elif [ "$cn" == "gs" ];
then
   category="general-skills"
   category_name="General Skills"
   
elif [ "$cn" == "re" ];
then
   category="reverse-engineering"
   category_name="Reverse Engineering"
   
elif [ "$cn" == "we" ];
then
   category="web-exploitation"
   category_name="Web Exploitation"
   
else
   echo "Wrong category for -c flag"
   usage
   exit
fi


if [ -d "../PicoCTF/$category/" ] && [ ! -d "../PicoCTF/$category/$challenge_name/" ];
then

echo "Creating Challenge \"$challenge_name\" in \"$category\""
mkdir -p "../PicoCTF/$category/$challenge_name/assets"
touch "../PicoCTF/$category/$challenge_name/writeup.md"
cat >> "../PicoCTF/$category/$challenge_name/writeup.md" << EOL
---
tags:
  - $category
points: $challenge_points points
---

[<-- $category_name Write-ups](../writeup-list.md)

# $challenge_name
## Write-up

##### Concept Coverage :
This challenge is 

##### Following are the steps for the challenge: 
1. 
EOL

else
	if [ -d "../PicoCTF/$category/$challenge_name/" ];
	then
		echo "$challenge_name challenge already exists in $category_name"
	else
		echo "$category_name category doesnot exist"
	fi
fi

