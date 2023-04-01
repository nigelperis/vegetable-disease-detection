# vegetable-disease-detection

Demo Website : https://vegetable-disease-detection-production.up.railway.app/

## Project Description

This project aims to classify Tomato and Corn Images to 12 diseases and idenitfy if they are healthy otherwise. We have used CNN architecture and from Machine Learning to develop a model. Our aim was to develop mobile compatable so that if we build an android app, the model can easily be integrated.

### Diseases
1. Corn : Cercospora Gray leaf spot
2. Corn : Common rust
3. Corn : Northern Leaf Blight
4. Corn : Healthy
5. Tomato : Early blight
6. Tomato : Late blight
7. Tomato : Leaf Mold
8. Tomato : Mosaic virus
9. Tomato : Spider mites
10. Tomato : Bacterial spot
11. Tomato : Yellow Leaf Curl Virus
12. Tomato : Target Spot
13. Tomato : Septoria leaf spot
14. Tomato : Healthy

## Project Details

* Dataset Reference : [Kaggle Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
* Model Architecture : Mobile Net V2 [Pretrained]
* Projgraming Language : Python
* Ml Framework : PyTorch
* Backend Framework : Flask
* Website Stack : HTML, CSS
* Deployment Platform : Railway

## Model Details

* Optimizer : Stochastic Gradient Descent ( With momentum = 0.9 )
* Loss Funcation : Corss Entropy
* Learning Rate : 0.9991
* Train Data size : 1600 Images per class
* Validation Data size : 400 Images per class
* Image size preffered : 224x224 pixels
* Model Architecture : Mobile Net V2 [Pretrained]

## Results

* Validation Accuracy : 98.5%
* Validation Loss : 7.775
* Accuracy and Loss graph over 40 epochs [27th epoch model selected]

![graph](https://github.com/nandakishormpai/vegetable-disease-detection/raw/main/images/graph.png)

* Confusion Matrix on 27th epoch

![confusion matrix](https://github.com/nandakishormpai/vegetable-disease-detection/raw/main/images/confusion%20matrix.png)

## Website

Flask web app built using HTML frontend where user can upload images and get the classificaiton results <br>
Demo Website : https://vegetable-disease-detection-production.up.railway.app/
