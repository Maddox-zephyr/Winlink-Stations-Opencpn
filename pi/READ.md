Automatic download and conversion of winlink-pactor stations to a gpx file to be used by OpenCPN on a raspberry pi.

Install python tools and libraries:

	sudo apt-get install python-dev
	sudo pip install pyhamtools
	sudo pip install gpxpy

Make a directory
	mkdir makegpx		(this will be /home/pi/makegpx)

Download the python conversion program

	wget https://github.com/Maddox-zephyr/Winlink-Stations-Opencpn/blob/master/pi/winlink-station-opencpn.py

Copy bash script to download the stations-frequencies and convert to gpx. 

	wget https://github.com/Maddox-zephyr/Winlink-Stations-Opencpn/blob/master/pi/winlink-pactor.sh

Run the script
	sh /home/pi/makegpx/winlink-pactor.sh

The latest frequency list gets downloaded, and then converted to the gpx file (/home/pi/makegpx/winlink-pactor-stations.gpx)

To automatically (once a day) have the gpx generated, add the following to the crontab

$ sudo crontab -e

	0 0 * * *  /home/pi/winlink-pactor.sh		# every night at midnight, run the script to update
