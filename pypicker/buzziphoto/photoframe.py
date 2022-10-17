import logging

import docopt
import buzziphoto.buzzipick as buzzipick
import buzziphoto.buzzimage as buzzimage
from buzziphoto import picmgr

logging.basicConfig(level="INFO")
g_logger = logging.getLogger(__file__)

g_usage = '''
Usage: 
  buzzimage.py [options] <photoalbum>

Options:
  -h --help         Show this screen.
  --interval=<int>  Delay time in seconds between pictures [default: 5]
  --version         Show version.
  --debug           Run in debug mode
'''


def main():
    args = docopt.docopt(g_usage)
    debug = args['--debug']
    std_delay = int(args['--interval']) * 1000
    album_dir = args['<photoalbum>']
    g_logger.info("Initialize the photo database")
    p = buzzipick.PhotoPicker(album_dir)
    g_logger.info("Initialize the display")
    i = buzzimage.BuzzScreenImage()
    mgr = picmgr.PictureManager(p)
    done = False
    while not done:
        delay = std_delay
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
        except Exception as ex:
            delay = 0  # if there is a problem get the next photo right away
            logging.error("Failed to show the photo %s", photo, ex)
        if event == buzzimage.QUIT:
            done = True
    i.done()


if __name__ == "__main__":
    main()
