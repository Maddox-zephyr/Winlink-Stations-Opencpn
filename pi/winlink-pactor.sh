#!/bin/bash

wget http://services.wlw.winlink.org/listings/RmsPactorListing.aspx?serviceCodes=PUBLIC -O /home/pi/makegpx/pactor-freq-list.txt

sudo python /home/pi/makegpx/winlink-station-opencpn.py