import pickle


def dumpPickle(filename, post_dict):
    with open('data/' + filename, 'wb') as handle:
        pickle.dump(post_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def readPickle(filename):
    with open('data/' + filename, 'rb') as handle:
        return pickle.load(handle)


def dumpSubreddit(filename, sub_list):
    with open('data/' + filename, 'w') as f:
        for x in sub_list:
            f.write(x + '\n')


def readSubreddits(filename):
    tmp = []
    with open('data/' + filename, 'r') as f:
        for x in f.readlines():
            tmp.append(x.strip())
    return tmp
