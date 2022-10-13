import logging
import os.path
import pathlib
import sqlite3
import PIL.Image as Image
import PIL.ExifTags as ExifTags

g_logger = logging.getLogger(__file__)


class PhotoPicker(object):
    def __init__(self, photos_base_path, only_favorites=True):
        self.originals_path = os.path.join(photos_base_path, "originals")
        self.db_path = os.path.join(photos_base_path, "database", "Photos.sqlite")
        if only_favorites:
            self.select_statement = "select ZDIRECTORY, ZFILENAME from ZASSET where ZFAVORITE = 1 and ZUNIFORMTYPEIDENTIFIER = \"public.jpeg\" order by random() limit 1"
        else:
            self.select_statement = "select ZDIRECTORY, ZFILENAME from ZASSET order by random() limit 1"
        self.con = sqlite3.connect(self.db_path)
        self.template_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          "templates/index.template.html")
        self.allowed_extension = ['.jpg', '.jpeg', '.png']
        self.max_find_tries = 8

    def select_photo(self):
        done = False
        try_count = 0
        while not done:
            cur = self.con.cursor()
            res = cur.execute(self.select_statement)
            row = res.fetchone()
            filename = row[1]
            dir_path = row[0]
            file_extension = pathlib.Path(filename).suffix.lower()
            g_logger.info("Found the file %s with type %s", filename, file_extension)
            cur.close()
            if file_extension in self.allowed_extension:
                return os.path.join(self.originals_path, dir_path, filename)
            g_logger.warning("The file %s does not have a supported extension", filename)
            try_count += 1
            if try_count > self.max_find_tries:
                raise Exception("Unable to find a supported picture")

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
