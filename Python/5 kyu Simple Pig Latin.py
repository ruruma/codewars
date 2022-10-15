import string


def pig_it(text):
    x = text.split()
    res = []
    punc = string.punctuation

    for count, item in enumerate(x):
        if item not in punc:
            item = (item + item[0] + 'ay')[1::]
            res.append(item)
        else:
            res.append(item)
    return " ".join(res)
