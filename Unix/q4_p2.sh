#!/bin/bash
a=1

while [ $a -lt 11 ]
do
   rem=$(($a % 2))
   if [ $rem -eq 0 ]; then
	mkdir "even$a"
	chmod 764 "even$a"
   else
	mkdir "odd$a"
	chmod 554 "odd$a"
   fi
   a=`expr $a + 1`
done
