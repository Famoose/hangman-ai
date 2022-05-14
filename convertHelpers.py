keys = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

def convertFeatures(dKey, uKey):
    res_dct = {}
    for key in range(0, len(keys)):
        res_dct[keys[key] + '_disp'] = dKey.count(keys[key])
        res_dct[keys[key] + '_used'] = uKey.count(keys[key])

    res_dct['empty'] = int(dKey.count('_'))
    res_dct['amount'] = int(len(dKey))
    return list(res_dct.values())


def keyToIndex(unKey):
    return int(keys.index(unKey))
