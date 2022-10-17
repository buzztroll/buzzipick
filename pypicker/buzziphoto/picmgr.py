
class PictureManager(object):
    def __init__(self, picdb, max_pix=32):
        self.max_pix = max_pix
        self.pic_list = []
        self.current_ndx = -1
        self._paused = False
        self._picdb = picdb

    def _add_pic(self, filename):
        self.pic_list.append(filename)
        if len(self.pic_list) > self.max_pix:
            self.pic_list.pop(0)
        self.current_ndx = len(self.pic_list) - 1

    def get_current(self):
        try:
            return self.pic_list[self.current_ndx]
        except IndexError:
            return None

    def next(self):
        if self._paused:
            return
        p = self._picdb.select_photo()
        self._add_pic(p)

    def back(self):
        self.current_ndx -= 1
        if self.current_ndx < 0:
            self.current_ndx = 0

    def forward(self):
        self.current_ndx += 1
        if self.current_ndx >= len(self.pic_list):
            self.current_ndx = len(self.pic_list) - 1

    def pause(self):
        self._paused = not self._paused
        self.next()  # if not paused get the next picture right away
