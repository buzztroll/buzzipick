import logging
import os.path
import sqlite3
import PIL.Image as Image
import PIL.ExifTags as ExifTags

g_logger = logging.getLogger(__file__)


class PhotoPicker(object):
    def __init__(self, photos_base_path):
        self.originals_path = os.path.join(photos_base_path, "originals")
        self.db_path = os.path.join(photos_base_path, "database", "Photos.sqlite")
        self.select_statement = "select ZDIRECTORY, ZFILENAME from ZASSET order by random() limit 1"
        self.con = sqlite3.connect(self.db_path)
        self.template_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          "../templates/index.template.html")

    def select_photo(self):
        cur = self.con.cursor()
        res = cur.execute(self.select_statement)
        row = res.fetchone()
        cur.close()
        return os.path.join(self.originals_path, row[0], row[1])

    def get_metadata(self, photo_file):
        md_table = {}
        image = Image.open(photo_file)
        exif = image.getexif()
        for tag_id in exif:
            # get the tag name, instead of human unreadable tag id
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            data = exif.get(tag_id)
            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            md_table[tag] = data
        md_table['File'] = os.path.basename(photo_file)
        return md_table
