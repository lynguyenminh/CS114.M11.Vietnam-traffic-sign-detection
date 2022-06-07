from flask import Flask, render_template, request
import os
import subprocess
import shutil

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/image', methods=['POST'])
def predict():
    if request.method=='POST':
        file = request.files['image_name']
        if os.path.isdir(os.path.join(os.getcwd(), 'static')) is False:
            os.mkdir(os.path.join(os.getcwd(), 'static'))
        file.save(os.path.join(os.getcwd(), 'static', 'upload_image.jpg'))

        try: 
            shutil.rmtree("./runs/detect")
        except:
            pass

        subprocess.run(["sh", "./run.sh"])

        try: 
            shutil.move("./runs/detect/exp/upload_image.jpg", "./static/result.jpg")
            shutil.move("./runs/detect/exp/labels/upload_image.txt", "./static/result.txt")
        except: 
            pass

        return render_template('output.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)