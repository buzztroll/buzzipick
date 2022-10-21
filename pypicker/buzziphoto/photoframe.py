import logging
import sys

import docopt
import buzziphoto.buzzipick as buzzipick
import buzziphoto.buzzimage as buzzimage
from buzziphoto import picmgr

g_logger = logging.getLogger(__file__)

_LOG_LEVELS = {"ERROR": logging.ERROR,
               "WARN": logging.WARN,
               "INFO": logging.INFO,
               "DEBUG": logging.DEBUG}

g_usage = f'''
Usage: 
  buzzimage.py [options] <photoalbum>

Options:
  -h --help           Show this screen.
  --interval=<int>    Delay time in seconds between pictures [default: 5]
  --version           Show version.
  --log-level=<str>   The type of information to log, one of {",".join(_LOG_LEVELS.keys())} [default: INFO]
  --log-file=<path>   The file where information will be logged.
  --fullscreen        Enable fullscreen instead of in a smaller window
'''


def main():
    args = docopt.docopt(g_usage)
    std_delay = int(args['--interval']) * 1000
    log_level = args['--log-level'].upper()
    if log_level not in _LOG_LEVELS.keys():
        raise Exception(f'{log_level} is not a valid choice.  It must be one of {",".join(_LOG_LEVELS.keys())}')
    if '--log-file' in args:
        logging.basicConfig(level=_LOG_LEVELS[log_level], filename=args['--log-file'])
    else:
        logging.basicConfig(level=_LOG_LEVELS[log_level], stream=sys.stderr)

    album_dir = args['<photoalbum>']
    g_logger.info("Initialize the photo database")
    p = buzzipick.PhotoPicker(album_dir)
    g_logger.info("Initialize the display")
    i = buzzimage.BuzzScreenImage(args['--fullscreen'])
    try:
        mgr = picmgr.PictureManager(p)
        done = False
        delay = 0
        while not done:
            event = i.get_event(timeout=delay)
            if event == buzzimage.NEXT:
                mgr.next()
            elif event == buzzimage.BACK:
                mgr.back()
            elif event == buzzimage.FORWARD:
                mgr.forward()
            elif event == buzzimage.PAUSE:
                mgr.pause()
            photo = mgr.get_current()

            logging.info("Show photo %s", photo)
            try:
                i.show_picture(photo)
                delay = std_delay
            except Exception as ex:
                delay = 0  # if there is a problem get the next photo right away
                logging.error("Failed to show the photo %s", photo, ex)
            if event == buzzimage.QUIT:
                done = True
    except Exception as ex:
        g_logger.error("A top level error occurred", ex)
    finally:
        i.done()


if __name__ == "__main__":
    main()
