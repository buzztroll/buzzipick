import datetime

import docopt
import pygame

import buzzipick


g_usage = '''
Usage: 
  photoframe.py [options] <photoalbum>

Options:
  -h --help         Show this screen.
  --interval=<int>  Delay time in seconds between pictures [default: 5]
  --version         Show version.
  --debug           Run in debug mode
'''


class ImageShower(object):
    def __init__(self, width=640, height=480):
        pygame.init()
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.dims = self.window.get_rect()
        # pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def show_picture(self, pic_file):
        img = pygame.image.load(pic_file)
        img_dims = img.get_rect()
        new_width = img_dims[2]
        new_height = img_dims[3]
        screen_dims = self.window.get_rect()
        scale_x = screen_dims[2] / new_width
        scale_y = screen_dims[3] / new_height
        # pick the smaller
        scaller = min(scale_x, scale_y)
        # only scale if too big
        if scaller < 1.0:
            new_width = new_width * scaller
            new_height = new_height * scaller
            img = pygame.transform.scale(img, (new_width, new_height))
        # now center it
        start_x = (screen_dims[2] - new_width) / 2
        start_y = (screen_dims[3] - new_height) / 2
        self.window.fill((0, 0, 0))
        self.window.blit(img, (start_x, start_y, new_width, new_height))
        pygame.display.flip()

    def is_done(self, timeout=5_000):
        end_time = datetime.datetime.now() + datetime.timedelta(milliseconds=timeout)
        while end_time > datetime.datetime.now():
            events = [pygame.event.wait(timeout=timeout)]
            for event in events:
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                        return True
                    if event.unicode == ' ':
                        return False
        return False


def main():
    args = docopt.docopt(g_usage)
    debug = args['--debug']
    delay = int(args['--interval']) * 1000
    album_dir = args['<photoalbum>']
    p = buzzipick.PhotoPicker(album_dir)
    i = ImageShower()
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
    pygame.quit()


if __name__ == "__main__":
    main()