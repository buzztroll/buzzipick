# Buzz iPick

## Why?

### tldr;

The point of this distribution is to serve photos from an Apple Photos database via a web browsers.  In the
first revision it runs a single endpoint webserver.  When a GET is made on that endpoint a random photo is
selected from the Apple database and served to the client.  As the user refreshes the webpage new photos are
served.

### Explanation 

I created this repository because I really like the features that Apple Photos provides, but I hate how
proprietary it is.  I hate that it only works well on an internal hard drive on a single Apple machine.  I tried
keeping my album on an external drive, but it is an awful experience.  The AI software that finds faces and otherwise
organizes the pictures (scary right?... but so convenient!) does not work well if the file system is not always
there.

Further I hate that my pictures are organized in an incomprehensible way on the file system.  There is no way
to make sense of any of them without using Photos.  I get it, but it sucks if I ever want to look at my pictures
outside of the Apple empire.

I rsync my Photo album to a raspberry pi as a backup.  It occured to me that I could serve these picture via a
webserver from that raspberry pi and thus this repo got started.

## Mechanics

Apple Photos uses sqlite as its database of photo metadata.  This is a great choice as sqlite is amazing.
This also allows for easy lookups of pictures.  This program opens that database and selects a photo from it
at random.  It then serves that photo and its metadata as a web page.  Everytime a page request is made the
server pics a new photo and serves it to the client.

It uses python and flask.  I hope to try it in a Rust as well.

## Installing

Open up the source files and look at them.  Then look at the systemd example I have.  Then figure out how to
make it work for you.  What do you want from me?  I already typed this much of a README that no one will ever look
at.


This distribution includes programs for pulling pictures out of the Apple Photos' database and displaying them in
a web browsers.  My hope is to write this in a few (go, java, rust... C?!) of languages but I will likely just make
it in python quickly for my own use and stop pretending that anyone cares about the code I write.
