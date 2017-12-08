'''
Created on 2017. 12. 3.

@author: choejunhyeog
'''

import tensorflow as tf
import numpy as np

x_data = np.array(
    [[0,0],[1,0],[1,1],[0,0],[0,0],[0,1]]
    )

y_data = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [1,0,0],
    [1,0,0],
    [0,0,1]
    ])

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)


#w = 