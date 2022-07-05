import numpy as np
import tensorflow as tf
from data.make_numpy import parse_txt_file
from sklearn.model_selection import train_test_split


def get_nn():
    inp = tf.keras.layers.Input(shape=(4, 26,))
    prep = tf.keras.layers.Reshape((4 * 26,))(inp)
    h1 = tf.keras.layers.Dense(100, activation='relu')(prep)
    h2 = tf.keras.layers.Dense(50, activation='relu')(h1)
    h3 = tf.keras.layers.Dense(50, activation='relu')(h2)
    out = tf.keras.layers.Dense(25, activation='softmax')(h3)

    model = tf.keras.models.Model(inputs=inp, outputs=out)
    model.compile(
        loss='sparse_categorical_crossentropy',
        optimizer=tf.keras.optimizers.Adam(0.001),
        metrics=['accuracy'],
    )
    return model


def main():
    model = get_nn()
    X, y = parse_txt_file()
    X_new = {}
    y_new = {}
    X_new['train'], X_new['test'], y_new['train'], y_new['test'] = train_test_split(X, y, test_size=0.5)
    model.fit(
        X_new['train'], y_new['train'],
        epochs=20,
        validation_data=(X_new['test'], y_new['test']),
    )


if __name__ == '__main__':
    main()


# output:
# Epoch 1/20
# 1091/1091 [==============================] - 2s 1ms/step - loss: 2.2385 - accuracy: 0.1769 - val_loss: 1.7860 - val_accuracy: 0.2596
# Epoch 2/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.6828 - accuracy: 0.2987 - val_loss: 1.6647 - val_accuracy: 0.3042
# Epoch 3/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.5747 - accuracy: 0.3334 - val_loss: 1.6231 - val_accuracy: 0.3214
# Epoch 4/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.5049 - accuracy: 0.3626 - val_loss: 1.6255 - val_accuracy: 0.3167
# Epoch 5/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.4721 - accuracy: 0.3669 - val_loss: 1.6057 - val_accuracy: 0.3260
# Epoch 6/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.4412 - accuracy: 0.3889 - val_loss: 1.5877 - val_accuracy: 0.3367
# Epoch 7/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.4064 - accuracy: 0.3980 - val_loss: 1.6235 - val_accuracy: 0.3287
# Epoch 8/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.3791 - accuracy: 0.4078 - val_loss: 1.5937 - val_accuracy: 0.3385
# Epoch 9/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.3619 - accuracy: 0.4098 - val_loss: 1.5893 - val_accuracy: 0.3370
# Epoch 10/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.3426 - accuracy: 0.4217 - val_loss: 1.5819 - val_accuracy: 0.3421
# Epoch 11/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.3195 - accuracy: 0.4320 - val_loss: 1.5848 - val_accuracy: 0.3413
# Epoch 12/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.3081 - accuracy: 0.4433 - val_loss: 1.5928 - val_accuracy: 0.3432
# Epoch 13/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.2821 - accuracy: 0.4508 - val_loss: 1.5896 - val_accuracy: 0.3464
# Epoch 14/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.2686 - accuracy: 0.4560 - val_loss: 1.6062 - val_accuracy: 0.3467
# Epoch 15/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.2661 - accuracy: 0.4531 - val_loss: 1.6193 - val_accuracy: 0.3494
# Epoch 16/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.2504 - accuracy: 0.4588 - val_loss: 1.6206 - val_accuracy: 0.3462
# Epoch 17/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.2289 - accuracy: 0.4721 - val_loss: 1.6167 - val_accuracy: 0.3500
# Epoch 18/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.2130 - accuracy: 0.4772 - val_loss: 1.6467 - val_accuracy: 0.3480
# Epoch 19/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.1963 - accuracy: 0.4884 - val_loss: 1.6493 - val_accuracy: 0.3492
# Epoch 20/20
# 1091/1091 [==============================] - 1s 1ms/step - loss: 1.1878 - accuracy: 0.4887 - val_loss: 1.6420 - val_accuracy: 0.3525