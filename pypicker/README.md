# Python iPhoto Picker

This is the python implementation of a project to present the Apple Photo album on a raspberry pi.

There are two programs in it.  Both use a base class that opens up the Apple Photo sqlite database
to select photos at random.

## Photo Frame

The program `buzz-photoframe` uses [pygame](https://www.pygame.org/news) to show a photo in full screen.  It
will randomly pick a photo from the database every N seconds and display it.  This is basically just a standard
photo frame application only it gets it source pictures from Apple Photos.

I have a [Piper](https://www.playpiper.com/) that I got my daughter for Christmas a few years ago, and it is
perfect for this kind of application.

## Photo Web Server

The program `buzz-photoweb` is a flask app that is effectively a web server with a single anonymous endpoint.
When a client does a GET on that endpoint a photo is randomly selected from the Apple Photo database and is
served as an HTML webpage.

## Installation

The easiest way to get going with this repo is to used [virtualenv](https://pythonbasics.org/virtualenv/) with
Python.  Simply create a virtualenv and install this repository into it in the following way:

```bash
virtualenv -p $(which python3) venv
. venv/bin/activate
python setup.py install
```

Now you can run `--help` on each of the programs that are found in `venv/bin`:

buzz-photoframe:
```bash
% ./venv/bin/buzz-photoframe --help
pygame 2.1.2 (SDL 2.0.18, Python 3.9.13)
Hello from the pygame community. https://www.pygame.org/contribute.html
Usage:
  buzzimage.py [options] <photoalbum>

Options:
  -h --help         Show this screen.
  --interval=<int>  Delay time in seconds between pictures [default: 5]
  --version         Show version.
  --debug           Run in debug mode
```

buzz-photoweb
```bash
% ./venv/bin/buzz-photoweb --help
Usage:
  buzzipick.py [options] <photoalbum>

Options:
  -h --help      Show this screen.
  --version      Show version.
  --port=<port>  Port to listen on [default: 8000].
  --host=<host>  Host to listen on [default: 0.0.0.0].
  --debug        Run in debug mode```