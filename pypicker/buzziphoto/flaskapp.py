import os.path
import shutil

import flask
import docopt

import buzziphoto.buzzipick as buzzipick


app = flask.Flask(
 __name__,
 template_folder="./templates",
 static_folder="./static",
)


@app.route("/")
def getpix():
    d = app.config['PIX_DB']
    p = buzzipick.PhotoPicker(d)
    picked = False
    error_count = 0
    while not picked:
        try:
            photo_file = p.select_photo()
            md = p.get_metadata(photo_file)
            dst_file = os.path.join(app.static_folder, "pic.jpeg")
            shutil.copy(photo_file, dst_file)
            picked = True
        except Exception as ex:
            #  some pictures cannot load properly, skip a few
            error_count += 1
            if error_count > 10:
                raise
            app.logger.warn(f"Bad picture selected {str(ex)}")

    return flask.render_template("index.template.html", metadata=md, pic_file=os.path.basename(dst_file))


g_usage = '''
Usage: 
  buzzipick.py [options] <photoalbum>

Options:
  -h --help      Show this screen.
  --version      Show version.
  --port=<port>  Port to listen on [default: 8000].
  --host=<host>  Host to listen on [default: 0.0.0.0].
  --debug        Run in debug mode
'''


def main():
    args = docopt.docopt(g_usage)
    port = int(args['--port'])
    debug = int(args['--debug'])
    app.config['PIX_DB'] = args['<photoalbum>']
    app.run(port=port, debug=debug, host=args['--host'])


if __name__ == "__main__":
    main()
