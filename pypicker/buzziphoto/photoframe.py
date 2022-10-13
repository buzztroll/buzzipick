import logging

import docopt
import buzziphoto.buzzipick as buzzipick
import buzziphoto.buzzimage as buzzimage

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
    cnt = 0
    done = False
    while not done and cnt < 1_000:
        cnt += 1
        delay = std_delay
        logging.info("Find a photo to select...")
        photo = p.select_photo()
        logging.info("Show photo %s", photo)
        try:
            i.show_picture(photo)
        except Exception as ex:
            delay = 0  # if there is a problem get the next photo right away
            logging.error("Failed to show the photo %s", photo, ex)
        done = i.is_done(timeout=delay)
    i.done()


if __name__ == "__main__":
    main()
