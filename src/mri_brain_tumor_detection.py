import cv2           
import numpy as np
import tensorflow as tf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow import keras
from PIL import Image, ImageDraw, ImageFont

model = tf.keras.saving.load_model("model_building/model.keras") 


def show_image(image_path):
    try:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        width, height = image.size
        return image
    except Exception as e:
        print(f"Error on image processing", {e})
        return None



def cnn_brain_tumor_identifier(image_path):
    print("Loading Image")
    image = cv2.imread(image_path)
    img = cv2.resize(image, (128, 128))
    img = np.expand_dims(img, axis=0)


    pred = fitted_model.predict(img)
    pred = float(pred[0,0])

    if pred > 0.9:
        print("Tumor")
        return show_image(image_path)
    else:
        print("No Tumor")
        return show_image(image_path)
    
image_path = input("Enter the brain MRI Image path:")

cnn_brain_tumor_identifier(image_path)