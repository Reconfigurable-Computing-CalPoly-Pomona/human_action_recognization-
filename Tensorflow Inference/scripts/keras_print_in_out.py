from keras import backend as K
import tensorflow as tf

from keras.models import load_model
model = load_model('models_hdf5/inception.104-0.74.hdf5')
print(model.outputs)
# [<tf.Tensor 'dense_2/Softmax:0' shape=(?, 10) dtype=float32>]
print(model.inputs)
# [<tf.Tensor 'conv2d_1_input:0' shape=(?, 28, 28, 1) dtype=float32>]					  