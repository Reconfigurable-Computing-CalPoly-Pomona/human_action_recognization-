from keras.models import load_model
#import tensorflow as tf

model = load_model('scripts/inception.017-0.91.hdf5')
print(model.outputs)
# [<tf.Tensor 'dense_2/Softmax:0' shape=(?, 10) dtype=float32>]
print(model.inputs)
# [<tf.Tensor 'conv2d_1_input:0' shape=(?, 28, 28, 1) dtype=float32>]

#tf.saved_model.save(model, 'model2/')