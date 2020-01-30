{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from __future__ import absolute_import, division, print_function, unicode_literals\n",
    "\n",
    "# Install TensorFlow\n",
    "\n",
    "import tensorflow as tf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "mnist = tf.keras.datasets.mnist\n",
    "\n",
    "(x_train, y_train), (x_test, y_test) = mnist.load_data()\n",
    "x_train, x_test = x_train / 255.0, x_test / 255.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = tf.keras.models.Sequential([\n",
    "  tf.keras.layers.Flatten(input_shape=(28, 28)),\n",
    "  tf.keras.layers.Dense(128, activation='relu'),\n",
    "  tf.keras.layers.Dropout(0.2),\n",
    "  tf.keras.layers.Dense(10, activation='softmax')\n",
    "])\n",
    "\n",
    "model.compile(optimizer='adam',\n",
    "              loss='sparse_categorical_crossentropy',\n",
    "              metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train on 60000 samples\n",
      "Epoch 1/5\n",
      "60000/60000 [==============================] - 13s 218us/sample - loss: 0.2996 - accuracy: 0.9130\n",
      "Epoch 2/5\n",
      "60000/60000 [==============================] - 7s 117us/sample - loss: 0.1447 - accuracy: 0.9570\n",
      "Epoch 3/5\n",
      "60000/60000 [==============================] - 7s 113us/sample - loss: 0.1086 - accuracy: 0.9671\n",
      "Epoch 4/5\n",
      "60000/60000 [==============================] - 7s 113us/sample - loss: 0.0876 - accuracy: 0.9728\n",
      "Epoch 5/5\n",
      "60000/60000 [==============================] - 6s 108us/sample - loss: 0.0738 - accuracy: 0.9765\n",
      "10000/1 - 1s - loss: 0.0423 - accuracy: 0.9742\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0.08121528563369065, 0.9742]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(x_train, y_train, epochs=5)\n",
    "\n",
    "model.evaluate(x_test,  y_test, verbose=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'x_train' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-39e86978938a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmodel\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx_train\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_train\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mepochs\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mmodel\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mevaluate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx_test\u001b[0m\u001b[1;33m,\u001b[0m  \u001b[0my_test\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mverbose\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'x_train' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "TensorFlow-rd-2.0.0",
   "language": "python",
   "name": "tf-rd"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
