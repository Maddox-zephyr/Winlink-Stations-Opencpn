#!/usr/bin/python
#----------------------------------------------------
# Parse a WInlink Pactor Station list file in order to store the stations
# in a gpx file that can be used in OpenCPN to geo position the staions on the map
#
# Bruce Toal N5VQP
# October 5, 2017
#
# States:
#   0 - Get the date the list was generated
#   0 - Search each line to find the one with dashes
#   1 - Skip Blank lines, then store station Callsign and Locator code
#   2 - Find line that has a dash in position 3, then ctore the frquencies
#       as a comment in the gpx record.
#
# This program is completely dependent on the file layout
# -------------------------

from pyhamtools.locator import locator_to_latlong
import gpxpy
import gpxpy.gpx
import datetime as mod_datetime

winlinkgpx = r'/home/pi/makegpx/winlink-pactor-stations.gpx'
y= r'/home/pi/makegpx/pactor-freq-list.txt'

dashes = "------------------"
dbldash = "====="
date = "WINLINK"
state = 0

f = open(y, "r")

lines = f.readlines()                       # Read all lines in the file into a list

f.close()

i = len(lines)                              # number of lines in the file

#print i, lines[i-1]

gpx = gpxpy.gpx.GPX()                       # Create GPX structure
gpx.time = mod_datetime.datetime.today()


for x in range (0,i):
    
    if state == 0:                          # Search for Date
        if lines[x].startswith(date):
            #print x, lines[x]
            open_paren = lines[x].find("(")
            close_paren = lines[x].find(")")
            datelast = lines[x][open_paren+1 : close_paren-4]
            print datelast
            gpx.time = mod_datetime.datetime.strptime(datelast, "%A, %B %d, %Y %H:%M")
            print gpx.time
            state = 1

        
    if state == 1:                          # Search for line with dashes
        if lines[x].startswith(dashes):
            #print x, lines[x]
            state = 2

    elif state == 2:                        # Skip blank lines, process callsign & emloc
        #print x, lines[x]
        isblank = lines[x].isspace()
        #print isblank
        if isblank:
            nop = 0
        else:
            if lines[x].startswith(dbldash):    # "====" marks the end of the stations
                state = 0                   # Harmless to search for date to end of lines
            else:
                #print x, "not blank"
                #print lines[x]
                state = 3
                index = lines[x].find(".")
                callsign = lines[x][0 : index]
                print callsign
                index = lines[x].find("[")
                endex = lines[x].find(":")
                emloc = lines[x][index+1 : endex]
                print emloc
                try:
                    latitude, longitude = locator_to_latlong(emloc)
                except:
                    print x, lines[x]
                print latitude, longitude

                gpx_waypoint = gpxpy.gpx.GPXWaypoint()  # Create Waypoint
                gpx_waypoint.latitude = latitude
                gpx_waypoint.longitude = longitude
                gpx_waypoint.time = gpx.time
                gpx_waypoint.name = callsign
            

    elif state == 3:                        # Find Frequencies line
        index = lines[x].find("-")
        if (index == 3):
            frequencies = lines[x][5 : ]    # include as comment
            print frequencies
            gpx_waypoint.description = frequencies
            gpx_waypoint.symbol = 'circle'
            gpx.waypoints.append(gpx_waypoint)
            state = 2

else:
    win = open(winlinkgpx,"w+")
    win.write(gpx.to_xml())
    win.close()
    print "done", x


