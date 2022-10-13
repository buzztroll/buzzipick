# Buzz iPick

## Why?

### tldr;

The point of this distribution is to serve photos from an Apple Photos database via a non apple system. The first two thoughts are:
1. Server random pictures from the Apple database via a web server
2. Show random pictures on a monitor (likely from a raspberry pi)

See the various language base subdirectories for specific on installing
and running.

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
