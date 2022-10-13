import docopt
import buzziphoto.buzzipick as buzzipick
import buzziphoto.buzzimage as buzzimage

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
    delay = int(args['--interval']) * 1000
    album_dir = args['<photoalbum>']
    p = buzzipick.PhotoPicker(album_dir)
    i = buzzimage.BuzzScreenImage()
    cnt = 0
    done = False
    while not done and cnt < 100:
        cnt += 1
        photo = p.select_photo()
        try:
            i.show_picture(photo)
        except Exception as ex:
            print(ex)
        done = i.is_done(timeout=delay)
    i.done()


if __name__ == "__main__":
    main()
