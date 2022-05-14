import numpy as np
import tensorflow as tf

import convertHelpers
from gameController import GameController

model = tf.keras.Sequential([
    tf.keras.layers.Dense(54),
    tf.keras.layers.Dense(108, activation='relu'),
    tf.keras.layers.Dense(26)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.load_weights('./training_tf/final')
#predict
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
#predictions = probability_model.predict(test_images)

correct = 0
wrong = 0
wordGuessed = 0
notGuessed = 0
for i in range(10000):
    if i%1000 == 0:
        print(i)
    gc = GameController()
    while not (gc.wordGuessed or gc.gameover):
        usableKeys = gc.getUsableKeys()
        wordBefore = gc.showWord()
        features = np.array(convertHelpers.convertFeatures(wordBefore, usableKeys))
        prediction = probability_model(np.array([features])).numpy()[0]
        predictedKey = convertHelpers.keys[np.argmax(prediction)]
        indexTried = -2
        sortedPrediction = np.argsort(prediction, axis=0)
        while predictedKey not in usableKeys:
            #print('key picked which is not in used key')
            predictedKey = convertHelpers.keys[sortedPrediction[indexTried]]
            indexTried -= 1

        success = gc.guesKey(predictedKey)
        if success:
            correct += 1
        else:
            wrong += 1
            #print('wrong')
    if(gc.wordGuessed):
        wordGuessed += 1
        #print('word guessed')
    else:
        notGuessed += 1
        #print('not guessed')

print(wordGuessed)
print(notGuessed)