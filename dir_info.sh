#!/bin/bash

list_files=$(du -ah --max-depth=1 2>/dev/null | sort -hr) 

# Помогите, пожалуйста, завернуть  list_files в функцию, что бы работала в цикле
#correct_display(){        
#	echo "$list_files"
#}

for i in "$list_files";
do
	echo -e "$i\n"
done | more -10


