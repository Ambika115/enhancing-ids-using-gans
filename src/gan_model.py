import tensorflow as tf
from tensorflow.keras import layers


def build_generator():

    model = tf.keras.Sequential([
        layers.Dense(128, activation="relu"),
        layers.Dense(256, activation="relu"),
        layers.Dense(41, activation="tanh")
    ])

    return model


def build_discriminator():

    model = tf.keras.Sequential([
        layers.Dense(256, activation="relu"),
        layers.Dense(128, activation="relu"),
        layers.Dense(1, activation="sigmoid")
    ])

    return model


generator = build_generator()
discriminator = build_discriminator()

print(generator.summary())
print(discriminator.summary())