{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "mnist = tf.keras.datasets.mnist\n",
    "\n",
    "(train_images, train_labels), (test_images, test_labels) = mnist.load_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# reshape and rescale data for the CNN\n",
    "\n",
    "train_images = train_images.reshape(60000, 28, 28, 1)\n",
    "\n",
    "test_images = test_images.reshape(10000, 28, 28, 1)\n",
    "\n",
    "train_images, test_images = train_images/255, test_images/255"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
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
   "source": [
    "model.fit(x_train, y_train, epochs=5)\n",
    "\n",
    "model.evaluate(x_test,  y_test, verbose=2)"
   ]
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
