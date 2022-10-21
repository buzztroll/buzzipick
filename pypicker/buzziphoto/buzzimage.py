import datetime
import logging

import pygame


g_logger = logging.getLogger(__file__)


QUIT = "QUIT"
PAUSE = "PAUSE"
BACK = "BACK"
FORWARD = "FORWARD"
NEXT = "NEXT"


class BuzzScreenImage(object):
    def __init__(self, fullscreen=False):
        pygame.init()
        if fullscreen:
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.window = pygame.display.set_mode((0, 0))

        self.dims = self.window.get_rect()

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

    def get_event(self, timeout=5_000):
        now = datetime.datetime.now()
        end_time = now + datetime.timedelta(milliseconds=timeout)
        while end_time > now:
            diff = end_time - now
            to = int(diff.total_seconds() * 1_000)
            g_logger.info("wait for events for %dms", to)
            events = [pygame.event.wait(timeout=to)]
            for event in events:
                g_logger.info("Found event %s", event)
                if event.type == pygame.QUIT:
                    g_logger.info("Received a quit event")
                    return QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                        g_logger.info("Received a keyboard quit event")
                        return QUIT
                    if event.unicode == ' ':
                        return PAUSE
                    if event.key == pygame.K_RETURN:
                        return NEXT
                    if event.key == pygame.K_LEFT:
                        return BACK
                    if event.key == pygame.K_RIGHT:
                        return FORWARD
            now = datetime.datetime.now()

        return NEXT

    def done(self):
        g_logger.info("Shutting down the display")
        pygame.quit()
