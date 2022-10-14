import pickle


def dumpPickle(filepath, post_dict):
    with open(filepath, 'wb') as handle:
        pickle.dump(post_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def readPickle(filepath):
    with open(filepath, 'rb') as handle:
        return pickle.load(handle)


def dumpSubreddit(filepath, sub_list):
    with open(filepath, 'w') as f:
        for x in sub_list:
            f.write(x + '\n')


def readSubreddits(filepath):
    tmp = []
    with open(filepath, 'r') as f:
        for x in f.readlines():
            tmp.append(x.strip())
    return tmp
