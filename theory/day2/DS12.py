#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:22:45 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
released
= iphone " : 2007, iphone 3G" : 2008, " iphone 3GS" : 2009,
iphone 4" : 2010, " iphone 4S" : 2011, " iphone 5" : 2012, "iPhone 5S" :
2013, " iphone 6" : 2014, " iphone 6S" : 2015, " iphone 7" : 2016, " iphone
8" : 2017, " iphone X" : 2017}
- Add the iphone XS for the year 2018
- Remove the first iphone
- Which is the year of the iphone 3G
- Print all the smartphone names
- Obtain this output on the screen
iphone 3G => 2008
iphone 4S => 2011
iphone 3GS => 2009
iphone => 2007
iphone 5 => 2012
iphone 4 => 2010
"""

released = {"iphone" : 2007, "iphone 3G" : 2008, "iphone 3GS" : 2009, 
"iphone 4" : 2010, "iphone 4S" : 2011, "iphone 5" : 2012,
"iPhone 5S" : 2013, "iphone 6" : 2014, "iphone 6S" : 2015, 
"iphone 7" : 2016, "iphone 8" : 2017, "iphone X" : 2017}

# - Add the iphone XS for the year 2018

released["iphone XS"] = 2018

# - Remove the first iphone

del released["iphone"]

# - Which is the year of the iphone 3G

print(released["iphone 3G"])

# - Print all the smartphone names

print(released.keys())

# - Obtain this output on the screen

for k in released.keys():
    print(k,"=>",released[k])


