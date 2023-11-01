![brain mri](https://github.com/dennerbocardi/brain_tumor_detection/blob/main/images/mri_image.png)
# Brain Tumor Detection with TensorFlow 

## Overview
Magnetic resonance imaging (MRI) is a medical imaging technique that uses a magnetic field and computer-generated radio waves to create detailed images of the organs and tissues in your body.

Most MRI machines are large, tube-shaped magnets. When you lie inside an MRI machine, the magnetic field inside works with radio waves and hydrogen atoms in your body to create cross-sectional images — like slices in a loaf of bread.

The MRI machine also can produce 3D images that can be viewed from different angles.

### Why it is done?
MRI is a noninvasive way for a medical professional to examine your organs, tissues and skeletal system. It produces high-resolution images of the inside of the body that help diagnose a variety of conditions.

## The Problem
We want to build a Convolutional Neural Network using TensorFlow to identify if a brain MRI image indicates if there is a tumor or not. We have a sample with 253 MRI brain images, 91 of them with no tumor visible and 154 with at least one visible tumor. The challenge is to build, train, and test a CNN to, given a brain MRI image it can identify a tumor on that image. This is only the first step because when we get the CNN trained and tested, we need to evaluate it not only by accuracy score, we have to take a really special look at the recall score for, in our case, we need to minimize the false-negatives, i.e., when there is a tumor in the image and the CNN can't identify it. We will do it by looking at the Confusion Matrix, of the SKLearn lib. 

## Dataset
The sample of images were found on Kagle: [here](https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection).

>[!NOTE]
>I do not own any image of this dataset.


## Approach
The approach here is quite simple: 
- We load the images using the os lib;
- Create and name two classes of images: Tumor and No Tumor;
- Split the images into the train and test sets;
- Do the data augmentation;
- Build the convolutional neural network;
- Train and test the CNN;
- Test for the best threshold to get the best recall score with no damage to the  accuracy score (we need to balance these two metrics);
- Build and look at the confusion matrix;
- Do the prediction on the validation set.<p>

At the end of this roadmap, we would be able to, given an MRI of a brain, we can identify whether there is a tumor or not with an acceptable error rate.

## Lenguages and Tools
<p align="left">  <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a><a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a><a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/> </a> <a href="https://jupyter.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" alt="jupyter" width="40" height="40"/> </a>

![model output](https://github.com/dennerbocardi/brain_tumor_detection/blob/main/images/output.png)