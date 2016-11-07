#!/bin/bash

CURR=1
SUBNET="192.168.1"
 
while [ $CURR -lt 255 ] ; do
  ping -c 1 -t 1 $SUBNET.$CURR
  if [ "$?" -eq "0" ]; then
    echo "$SUBNET.$CURR"
  fi
  let CURR=$CURR+1
done
