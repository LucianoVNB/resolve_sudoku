from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Pasta para armazenar imagens enviadas
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    image_file = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file and file.filename.endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            image_file = file.filename
    return render_template('index.html', image_file=image_file)

if __name__ == '__main__':
    app.run(debug=True)
