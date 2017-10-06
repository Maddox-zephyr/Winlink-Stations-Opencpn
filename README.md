# Winlink-Stations-Opencpn
Convert Winlink Station List to a gpx file to use with OpenCPN

This is probably most interesting to fellow mariners.  
I use OpenCPN as one of my onboard chartplotting solutions and I have an Icom IC-M802 SSB radio with
a Pactor modem to communicate and download weather and other information underway.  I use Airmail 2000
as my mail interface with the radio.  I use both Sailmail and Winlink.

It is useful to understand where winlink pactor stations are and by using layers on OpenCPN, we can overlay
Winlink stations on the chart.

The python program in this repo takes a list of winlink stations that I download via Airmail, and converts
it into a gpx file to be used by OpenCPN.  I have included a copy of the Winlink stations file in this repo 
as well as the generated gpx file.

There are likely more elegant ways to have writen this, but it works!  If Winlink decides to change the file format, 
then all bets are off on this program.

There are two file paths that need to be edited in the program:

winlinkgpx = path to file (example:  c:\users\maddox\opencpn\winlink.gpx)  This is the file that is written.
y = path to input file    (example:  c:\users\maddox\opecpn\winlink-station-list)  This is the file downloaded via airmail.

To use with OpenCPN, click on the Tools tab, select the Route & Mark Manager option, and then the Layers tab.  Select the 
Temporary Layers button, and then point it to the file just created (the gpx file).  Return to the chart display and if a 
station is within the display window (zoom in/out if necessary), a circle will be at the spot that was converted from the 
Maidenhead Grid Square of the station (example: station WI6M has a maidenhead locator code of DM12JR, which converts to 
32.729 degrees north, and -117.208 degrees (minus sign means east))

Installation:

Download python version 2.7 and install on your machine.

The program uses several add in libraries, 

- Pyhamtools (https://github.com/dh1tw/pyhamtools)
- gpxpy      (https://github.com/tkrajina/gpxpy)

so do the following at a command promp (with a path to pip):

  $ pip install pyhamtools
  
  $ pip install pygpx



