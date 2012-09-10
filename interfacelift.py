#!/usr/bin/env python
import os, urllib2, re, sys, commands, random

# -- Changable Variables
url             = 'http://interfacelift.com/wallpaper/downloads/date/2_screens/2880x900/' #Browse to the page that has all the wallpaper you want and paste here
directory       = '/home/user/wallpaper/2880x900' #Path to download to
stoponfind      = '1' # Set to 0 to download all files even if the file exists and 1 to stop when it finds where it left off
wgetpath        = '/usr/bin/wget' #Default on linux systems /usr/local/bin/wget on freebsd

# -- Should not need to edit below here unless something stops working --
useragent       = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)' #Fake useragent since wget is blocked
pattern         = '(?<=<a href=")/wallpaper/.*jpg(?=">)' # The regex pattern used to look up picture url paths
picturepattern  = '[^/]*$' # The regex pattern to pull picture filename to see if file exists
wallpapercount  = 0
count           = 1

while count < 9999999:
        headers    = { 'User-Agent' : useragent }
        request    = urllib2.Request(url + "index" + str(count) + ".html", None, headers)
        data       = urllib2.urlopen(request).read()
        pictures   = re.findall(pattern, data)
        urlcount   = len(pictures)
        for picture in pictures:
                m = re.search(picturepattern, picture)
                picturefile=m.group()
                if os.path.exists(directory + "/" + picturefile):
                        if stoponfind == "1":
                                print 'Directory up to date. Downloaded ' + str(wallpapercount) + ' new wallpaper.'
                                quit()
                status, output = commands.getstatusoutput(wgetpath + ' -P ' + directory + ' -nc -U "' + useragent + '" ' + 'http://interfacelift.com' + picture)
                if status == 0:
                        print str(wallpapercount) + '. Downloaded http://interfacelift.com' + picture + ' ...'
                else:
                        print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                        print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WGET OUTPUT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                        print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                        print '----------------------------------------------------------------------------------'
                        print output
                        print '----------------------------------------------------------------------------------'
                        print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                        print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                        print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                        print str(wallpapercount) + '. DOWNLOAD FAILED check wget output above for reason.'
                        print 'Exiting script ... wget returned non 0 exit status code: ' + str(status)
                        quit()
                wallpapercount += 1
        if urlcount == 0:
                print "Downloaded " + str(wallpapercount) + " wallpaper from InterfaceLift."
                quit()
        count += 1
        randomnum  = random.randint(0,30)
        print 'Sleeping for :' + str(randomnum)
        time.sleep(randomnum)

