FlickrTools
===========

A collection of scripts I've built for working with Flickr and my site.
There's not going to be much documentation here, but most of the stuff should
be fairly simple. I'll try to comment code as well and list dependencies.

Sets2Table
----------

This is a simple script which creates a HTML table of all your Flickr sets.
The resulting table (with jQuery setup) is [here.](http://michaelballphoto.com/photography)
Note that is pretty terribly written at the moment, but it might give you an
idea if you're looking to do something.

It currently requires the Python FlickrAPI, and is using 1.4.2, which is
included in the repo. 

The HTML is simply output to _stdout_, so the easiest way to run it is:
    python Sets2Table.py > file.html
    
SOME UPLOADER THING
------------------

I'm currently working on an uploader so just check out my files. It's a work
in progress, and as long as this is here, don't expect it to work! ;)

LICENSE
=======

All work in this repo is licensed under the BSD License (3-clause).
See the license file for details. 