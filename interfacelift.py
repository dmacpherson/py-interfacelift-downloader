#!/usr/bin/env python
import os
import urllib2

url       = 'http://interfacelift.com/wallpaper/downloads/date/hdtv/1080p/'
directory = '/datapool/public/wallpaper/1080p'
start     = '<a href="/wallpaper/i8r4q'  #check interfacelift.com to see what the randomly generated part is at the end
end       = '">'
useragent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'

count     = 1
while count < 999999:
        data       = urllib2.urlopen(url + "index" + str(count) + ".html").read()
        currentpos = 0
        urlcount   = 0
        while True:
                index      = data.find(start, currentpos)
                if index == -1:
                        break
                endofindex = data.find(end, index)
                currentpos = index + 1
                urlcount  += 1
                if os.path.exists(directory + data[index+len(start):endofindex]):
                        print 'Directory up to date. Found existing file.'
                        quit()
                os.system('wget -P ' + directory + ' -nc -U "' + useragent + '" ' + 'http://interfacelift.com' + data[index+9:endofindex])
        if urlcount == 0:
                quit()
        count += 1
