# -*- coding: utf-8 -*-
"""Img classifying using Max pooling .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u5BtoXgleinMg-p4Q5BuBylGp8uZMSuB

## Mood classfication using CNN in GPU (HAPPY / SAD)
"""

from google.colab import drive
drive.mount('/content/drive')

"""Steps
 * Create 3 folder.
 * Traing, testing and validation.
 * Please collect 20 pics (collect Happy & sad images)
 * Inside training creat 2 folder as happy and not happy
 * paste all the images in testing part
"""

from tensorflow.keras.preprocessing.image import ImageDataGenerator  #for data augmentation in image processing tasks
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import cv2
import os
#image data generator is the package to lable the images & it will automatically lable all the images

img = image.load_img('/content/drive/MyDrive/Img Class/1. Training/Happy/snsns.jpg')

plt.imshow(img)

i1 = cv2.imread(r'/content/drive/MyDrive/Img Class/1. Training/Happy/snsns.jpg')
i1
# 3 dimension metrics are created for the image
# the value ranges from 0-255

i1.shape
# shape of your image height, weight, rgb

train = ImageDataGenerator(rescale = 1/255)
validataion = ImageDataGenerator(rescale = 1/255)
# to scale all the images i need to divide with 255
# we need to resize the image using 200, 200 pixel

train_dataset = train.flow_from_directory(r'/content/drive/MyDrive/Img Class/1. Training',
                                         target_size = (200,200),
                                         batch_size = 3,
                                         class_mode = 'binary')
validataion_dataset = validataion.flow_from_directory(r'/content/drive/MyDrive/Img Class/3. Validations',
                                          target_size = (200,200),
                                          batch_size = 3,
                                          class_mode = 'binary')

train_dataset.class_indices

train_dataset.classes

# now we are applying maxpooling

model = tf.keras.models.Sequential([ tf.keras.layers.Conv2D(16,(3,3),activation = 'relu',input_shape = (200,200,3)),
                                    tf.keras.layers.MaxPool2D(2,2), #3 filtr we applied hear
                                    #
                                    tf.keras.layers.Conv2D(32,(3,3),activation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    #
                                    tf.keras.layers.Conv2D(64,(3,3),activation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    ##
                                    tf.keras.layers.Flatten(),
                                    ##
                                    tf.keras.layers.Dense(512, activation = 'relu'),
                                    #
                                    tf.keras.layers.Dense(1,activation= 'sigmoid')
                                    ]
                                    )

model.compile(loss='binary_crossentropy',
              optimizer = tf.keras.optimizers.RMSprop(lr = 0.001),
              metrics = ['accuracy']
              )

model_fit = model.fit(train_dataset,
                     epochs = 10,
                     validation_data = validataion_dataset)

dir_path = r'/content/drive/MyDrive/Img Class/2. Testing'
for i in os.listdir(dir_path ):
    print(i)
    #img = image.load_img(dir_path+ '//'+i, target_size = (200,200))
   # plt.imshow(img)
   # plt.show()

dir_path = r'/content/drive/MyDrive/Img Class/2. Testing'
for i in os.listdir(dir_path ):
    img = image.load_img(dir_path+ '//'+i, target_size = (200,200))
    plt.imshow(img)
    plt.show()

dir_path = r'/content/drive/MyDrive/Img Class/2. Testing'
for i in os.listdir(dir_path ):
    img = image.load_img(dir_path+ '//'+i, target_size = (200,200))
    plt.imshow(img)
    plt.show()

    x= image.img_to_array(img)
    x=np.expand_dims(x,axis = 0)
    images = np.vstack([x])

    val = model.predict(images)
    if val == 0:
        print( ' i am happy')
    else:
        print('i am not happy')