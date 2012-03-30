#!/usr/bin/env python
import os
import urllib2
import re

# -- Changable Variables

url             = 'http://interfacelift.com/wallpaper/downloads/date/2_screens/2880x900/' #Browse to the page that has all the wallpaper you want and paste here
directory       = '/home/user/1440x900x2' #Path to download to
useragent       = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)' #Fake useragent since wget is blocked
pattern         = '(?<=<a href=")/wallpaper/.*jpg(?=">)' # The regex pattern used to look up picture url paths
picturepattern  = '[^/]*$' # The regex pattern to pull picture filename to see if file exists
stoponfind      = '1' # Set to 0 to download all files even if the file exists and 1 to stop when it finds where it left off
wallpapercount  = 0

# -- Should not need to edit below here unless something stops working --
count     = 1
while count < 9999999:
        data       = urllib2.urlopen(url + "index" + str(count) + ".html").read()
        pictures   = re.findall(pattern, data)
        urlcount   = len(pictures)
        for picture in pictures:
                wallpapercount += 1
                m = re.search(picturepattern, picture)
                picturefile=m.group()
                if os.path.exists(directory + "/" + picturefile):
                        if stoponfind == "1":
                                print 'Directory up to date.'
                                quit()
                os.system('wget -P ' + directory + ' -nc -U "' + useragent + '" ' + 'http://interfacelift.com' + picture)

        if urlcount == 0:
                print "Downloaded " + str(wallpapercount) + " wallpaper from InterfaceLift." 
                quit()
        count += 1
