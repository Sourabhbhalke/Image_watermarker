import os
import uuid
from flask import request, render_template
from app import app
import numpy as np
import cv2
from PIL import Image
from skimage.metrics import structural_similarity

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        option = request.form['options']
        image_upload = request.files['image_upload']
        imagename = image_upload.filename
        image = Image.open(image_upload)
        image_array = np.array(image.convert('RGB'))
        
        # Generate a unique filename
        unique_filename = str(uuid.uuid4()) + '.png'

        if option == 'logo_watermark':
            logo_upload = request.files['logo_upload']
            logoname = logo_upload.filename
            logo = Image.open(logo_upload)
            logo_array = np.array(logo.convert('RGB'))
            
            h_image, w_image, _ = image_array.shape
            h_logo, w_logo, _ = logo_array.shape
            center_y = int(h_image / 2)
            center_x = int(w_image / 2)
            top_y = center_y - int(h_logo / 2)
            left_x = center_x - int(w_logo / 2)
            bottom_y = top_y + h_logo
            right_x = left_x + w_logo

            roi = image_array[top_y: bottom_y, left_x: right_x]
            result = cv2.addWeighted(roi, 1, logo_array, 1, 0)
            cv2.line(image_array, (0, center_y), (left_x, center_y), (0, 0, 255), 1)
            cv2.line(image_array, (right_x, center_y), (w_image, center_y), (0, 0, 255), 1)
            image_array[top_y: bottom_y, left_x: right_x] = result

        else:  # text_watermark
            text_mark = request.form['text_mark']
            cv2.putText(image_array, text=text_mark, org=(w_image - 95, h_image - 10), 
                        fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, 
                        color=(0, 0, 255), thickness=2, lineType=cv2.LINE_4)
        
        # Save the processed image with a unique filename
        img = Image.fromarray(image_array, 'RGB')
        img.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], unique_filename))
        
        full_filename = f'static/uploads/{unique_filename}'
        return render_template('index.html', full_filename=full_filename)


