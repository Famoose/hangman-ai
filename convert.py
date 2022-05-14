# Load the dataset
import json
import numpy as np

import convertHelpers

f = open('./data/playData.json')

# returns JSON object as
# a dictionary
data = list(json.load(f))
f.close()
data = np.array(data, dtype=object)
displayedKeys = data[:, 1]

#normalize data
normUsedKeys = []

#features = all keys empty ones and used keys, word length
x_features = []
usedKeys = data[:, 2]

for index in range(len(displayedKeys)):
    dKey = displayedKeys[index]
    uKey = usedKeys[index]
    values = convertHelpers.convertFeatures(dKey, uKey)
    x_features.append(values)

y_unormalized_keys = data[:, 0]
y_key = []

for unKey in y_unormalized_keys:
    y_key.append(convertHelpers.keyToIndex(unKey))

f = open("./data/x_playData_2.json", "w")
f.write(json.dumps(x_features))
f.close()

f = open("./data/y_playData_2.json", "w")
f.write(json.dumps(y_key))
f.close()

print('finished')