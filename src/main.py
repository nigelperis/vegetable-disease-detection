from flask import Flask, render_template, request, redirect, url_for, flash
import os
import torch
import torchvision.transforms as transforms
from model.load_model import mobilenetV2
import json
from PIL import Image
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)
app.secret_key = "your_secret_key"

model = mobilenetV2() # initialize your PyTorch model here
model.eval()
print("Model Downloaded")
device = 'cpu'

with open('./model/num_to_labels.json') as json_file:
    num_to_labels = json.load(json_file)

@torch.no_grad()
def predict(img_path):
    image = Image.open(img_path).convert('RGB')
    resize = transforms.Compose(
             [ transforms.Resize(224),
              transforms.ToTensor(),
              transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])              
    image = resize(image)
    image = image.to(device)

    with torch.no_grad():
        y_result = torch.softmax(model(image.unsqueeze(0)),dim=1)
        result_idx = int(y_result.argmax(dim=1)[0])
    if(float(y_result.max(dim=1)[0]) < 0.90):
        return "unclear"
    return num_to_labels[str(result_idx)]



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # check if the post request has the file part
        if "image" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["image"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # save uploaded image to uploads directory
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            # pass image to your PyTorch model for prediction
            prediction = predict(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            if prediction == "unclear":
                plant = "unclear"
                disease = "unclear"
            elif 'Corn' in prediction:
                plant = 'Corn'
                disease = (" ".join(prediction.split("__")[1].split("_"))).strip()
            elif 'Tomato':
                plant = 'Tomato'
                disease = (" ".join(prediction.split("__")[1].split("_"))).strip()
            return render_template("index.html", plant=plant, disease=disease, filename=filename)
    return render_template("index.html")

# define allowed file types
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# configure upload folder and maximum file size
app.config["UPLOAD_FOLDER"] = os.path.join("static","uploads")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024 # 10MB

if __name__ == "__main__":
    app.run(debug=True)
