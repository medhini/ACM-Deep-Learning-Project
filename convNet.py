import numpy
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.utils import np_utils
from keras import backend as K

r,c=28,28
(trainX, trainY),(testX, testY) = mnist.load_data()
if K.image_dim_ordering() == 'th':
    trainX = trainX.reshape(trainX.shape[0], 1, r, c)
    testX = testX.reshape(testX.shape[0], 1, r, c)
    input_shape = (1, r, c)
else:
    trainX = trainX.reshape(trainX.shape[0], r, c, 1)
    testX = testX.reshape(testX.shape[0], r, c, 1)
    input_shape = (r, c, 1)
trainX = trainX.astype('float32')
testX = testX.astype('float32')
trainX /= 255
testX /= 255
print('trainX shape:', trainX.shape)
print(trainX.shape[0], 'train samples')
print(testX.shape[0], 'test samples')
trainY = np_utils.to_categorical(trainY, 10)
testY = np_utils.to_categorical(testY, 10)
model = Sequential()
model.add(Convolution2D(32, 3, 3, border_mode='valid', input_shape=input_shape))
model.add(Activation('relu'))
model.add(Convolution2D(32, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))
model.summary()
model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])

model.fit(trainX, trainY, batch_size=100, nb_epoch=12,
          verbose=1, validation_data=(testX, testY))
score = model.evaluate(X_test, Y_test, verbose=1)
print('Test score:', score[0])
print('Test accuracy:', score[1])

