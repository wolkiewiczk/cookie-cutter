from cookie_cutter.cookie_cutter.helpers import CookieMold
from cookie_cutter.settings import settings

from flask import Flask, request, render_template, send_file

from zipfile import ZipFile
from io import BytesIO


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/oven', methods=['POST'])
    def oven():
        zipfile = BytesIO()
        with ZipFile(zipfile, mode='w') as cookie_jar:
            for img in request.files.getlist('images'):
                filename, ext = img.filename.split(".")
                if ext not in ['jpg', 'png']:
                    continue
                mold = CookieMold(img, rows=int(request.form['rows']), columns=int(request.form['columns']))
                cookie_wrapping = BytesIO()
                cookie, x, y = mold.cut(int(request.form['ray']))
                cookie.save(cookie_wrapping, format='png')
                cookie_jar.writestr(f'{filename}_cookie_{x}_{y}.png', cookie_wrapping.getvalue())
        zipfile.seek(0)
        return send_file(
            zipfile, mimetype='application/zip', as_attachment=True, attachment_filename='image_cookies.zip'
        )

    return app


application = create_app()
