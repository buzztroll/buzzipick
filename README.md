# Buzz iPick

## tldr;

The point of this distribution is to serve photos from an Apple Photos database via a non apple system.  I backup
my Photos library over my network to a hard drive connected to a raspberry pi.  I want to be able to use that
backup to browse photos as well.  This repository is a set of projects that do something with those photos.

In addition, I am hoping to use these project ideas to learn Rust.  I started with Python because it is *right there*
and I wanted to see something working quickly.

## Explanation 

I created this repository because I really like the features that Apple Photos provides, but I hate how
proprietary it is.  I hate that it only works well on an internal hard drive on a single Apple machine.  I tried
keeping my album on an external drive, but it is an awful experience.  The AI software that finds faces and otherwise
organizes the pictures (scary right?... but so convenient!) does not work well if the file system is not always
there.

Further I hate that my pictures are organized in an incomprehensible way on the file system.  There is no
obvious way to make sense of them from just the filesystem, so you pretty much have to only use Apple Photos
and you will be stuck with it in perpetuity (the Apple way).

However, the good news is that Apple Photos uses sqlite as its database!  Sqlite is amazing and easy and well
standardized, thus to make sense of the photo layout all we have to do is reverse engineer the Apple Photos
database layout.

This repo has (will have) a few different programs in a couple of languages which do various things with the Apple
Photo database.  A couple of early examples are:

1. Select a photo at random and serve it as a web page
2. Select a photo at random and show it on the scren like a photo frame

Look in the subdirectories for more information.
