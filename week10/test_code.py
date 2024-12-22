# test code imported from https://www.tensorflow.org/
import tensorflow as tf
from tensorflow import keras

# Keras is the high-level API of the TensorFlow platform - https://www.tensorflow.org/guide/keras.
mnist = tf.keras.datasets.mnist

# Load and prepare the MNIST dataset. The pixel values of the images range from 0 through 255.
(x_train, y_train),(x_test, y_test) = mnist.load_data()

# Scale these values to a range of 0 to 1 by dividing the values by 255.0. This also converts the
# sample data from integers to floating-point numbers.
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
  loss='sparse_categorical_crossentropy',
  metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
print("evaluation:\n",model.evaluate(x_test, y_test, verbose=2))
