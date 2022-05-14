import json
import os

import numpy as np
import tensorflow as tf


def get_dataset_partitions_tf(ds, ds_size, train_split=0.8, val_split=0.1, test_split=0.1, shuffle=True,
                              shuffle_size=10000):
    assert (train_split + test_split + val_split) == 1

    if shuffle:
        # Specify seed to always have the same split distribution between runs
        ds = ds.shuffle(shuffle_size, seed=12)

    train_size = int(train_split * ds_size)
    val_size = int(val_split * ds_size)

    train_ds = ds.take(train_size)
    val_ds = ds.skip(train_size).take(val_size)
    test_ds = ds.skip(train_size).skip(val_size)

    return train_ds, val_ds, test_ds

f = open('../data/x_playData_2.json')
x_features = np.array(list(json.load(f)))
f.close()

f = open('../data/y_playData_2.json')
y_key = np.array(list(json.load(f)))
f.close()

checkpoint_path = "training_tf/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

#model = tf.keras.Sequential([
#    tf.keras.layers.Dense(54),
#    tf.keras.layers.Dense(108, activation='relu'),
#    tf.keras.layers.Dense(26)
#])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(52),
    tf.keras.layers.Dense(104, activation='relu'),
    tf.keras.layers.Dense(26)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(x_features, y_key, epochs=10)

model.save_weights('./training_tf/final_2')

#predict
#probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
#predictions = probability_model.predict(test_images)
