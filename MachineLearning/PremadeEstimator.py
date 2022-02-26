import tensorflow as tf
import numpy as np
import pandas as pd
import os


def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text

def input_fn(features, labels, training=True, batch_size=256):
    """An input function for training or evaluating"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle and repeat if you are in training mode.
    if training:
        dataset = dataset.shuffle(1000).repeat()
    
    return dataset.batch(batch_size)


def input_fna(features, batch_size=256):
    """An input function for prediction."""
    # Convert the inputs to a Dataset without labels.
    return tf.data.Dataset.from_tensor_slices(dict(features)).batch(batch_size)



def DO(train,train_y,test):

    

    my_feature_columns = []
    for key in train.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 30 and 10 nodes respectively.
        hidden_units=[30, 10],
        # The model must choose between 3 classes.
        n_classes=4)

    classifier.train(
        input_fn=lambda: input_fn(train, train_y, training=True),
        steps=5000)

    

    predictions = classifier.predict(
        input_fn=lambda: input_fna(test))
    
 
    output = []
    probabilitys = []
    
    for pred_dict in predictions:
     class_id = pred_dict['class_ids'][0]
     probability = pred_dict['probabilities'][class_id] * 100
     output.append(class_id)
     probabilitys.append(probability)
     
    
    screen_clear()

    return output,probabilitys
    




