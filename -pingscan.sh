#!/bin/bash

INT=1
SUBNET="192.168.1"
 
while [ $INT -lt 255 ] ; do
  ping -c 1 -t 1 $SUBNET.$INT 
  if [ "$?" -eq "0" ]; then
    echo "$SUBNET.$INT"
  fi
  let INT=$INT+1
done
