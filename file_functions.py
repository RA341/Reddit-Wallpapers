import os
import pickle


def dumpDictionary(filename, post_dict):
    with open('data/'+filename, 'wb') as handle:
        pickle.dump(post_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def readDictionary(filename):
    with open('data/'+filename, 'rb') as handle:
        return pickle.load(handle)


def dumpList(filename, sub_list):
    with open('data/'+filename, 'w') as f:
        for x in sub_list:
            f.write(x + '\n')


def readList(filename):
    tmp = []
    with open('data/'+filename, 'r') as f:
        for x in f.readlines():
            tmp.append(x.strip())
    return tmp


if __name__ == '__main__':
    os.mkdir('data')
    post_dict = {'y1aifi': 'https://i.redd.it/vzastf54s6t91.jpg', 'xxgbtz': 'https://i.redd.it/8hekpbqv29s91.jpg',
                 'x9un1w': 'https://i.redd.it/pvp6s2oywtm91.png', 'wqogt9': ['https://i.redd.it/lwgz9e1uu9i91.png',
                                                                             'https://i.redd.it/3rtlr21uu9i91.png',
                                                                             'https://i.redd.it/0ff29b1uu9i91.png',
                                                                             'https://i.redd.it/rz1q0a1uu9i91.png',
                                                                             'https://i.redd.it/xvzpjw0uu9i91.png',
                                                                             'https://i.redd.it/ovsn801uu9i91.png',
                                                                             'https://i.redd.it/jx5ztw0uu9i91.png',
                                                                             'https://i.redd.it/g1vzx31uu9i91.png',
                                                                             'https://i.redd.it/6g89h6obwwf91.jpg',
                                                                             'https://i.redd.it/dy1mlxpbwwf91.jpg',
                                                                             'https://i.redd.it/pxjqv5obwwf91.jpg',
                                                                             'https://i.redd.it/gyoi15xbwwf91.png',
                                                                             'https://i.redd.it/tmtattrbwwf91.jpg',
                                                                             'https://i.redd.it/vjbx74bsxwf91.jpg',
                                                                             'https://i.redd.it/tlpmca7ixwf91.jpg',
                                                                             'https://i.redd.it/6t9476obwwf91.jpg',
                                                                             'https://i.redd.it/jiy4j5xbwwf91.png',
                                                                             'https://i.redd.it/sjd74qnbwwf91.jpg',
                                                                             'https://i.redd.it/roj8lwnbwwf91.jpg',
                                                                             'https://i.redd.it/j4dsuvrbwwf91.png',
                                                                             'https://i.redd.it/o1i0utnbwwf91.png',
                                                                             'https://i.redd.it/h0s7fopbwwf91.jpg',
                                                                             'https://i.redd.it/sbiddwubwwf91.png',
                                                                             'https://i.redd.it/ocu3glrbwwf91.png',
                                                                             'https://i.redd.it/07x86ypbwwf91.jpg',
                                                                             'https://i.redd.it/hra7jrnbwwf91.jpg',
                                                                             'https://i.redd.it/7filuosbwwf91.png',
                                                                             'https://i.redd.it/bcqj1kvbwwf91.jpg',
                                                                             'https://i.redd.it/yndw671xs4r81.png',
                                                                             'https://i.redd.it/d6hxtqwws4r81.jpg',
                                                                             'https://i.redd.it/mqbbwtuws4r81.jpg',
                                                                             'https://i.redd.it/j4ki1kwws4r81.jpg',
                                                                             'https://i.redd.it/1ma5jywws4r81.png',
                                                                             'https://i.redd.it/6eus5r2xs4r81.jpg',
                                                                             'https://i.redd.it/9jkjavuws4r81.jpg',
                                                                             'https://i.redd.it/iprespwws4r81.jpg',
                                                                             'https://i.redd.it/yo9xyxwws4r81.jpg',
                                                                             'https://i.redd.it/z2pzf9vws4r81.jpg',
                                                                             'https://i.redd.it/t7s2ztuws4r81.jpg',
                                                                             'https://i.redd.it/2906q61xs4r81.jpg',
                                                                             'https://i.redd.it/l5655c6xs4r81.jpg',
                                                                             'https://i.redd.it/mfimk1vws4r81.png',
                                                                             'https://i.redd.it/kf8ijwuws4r81.jpg',
                                                                             'https://i.redd.it/pricd1xws4r81.jpg',
                                                                             'https://i.redd.it/0e2qttuws4r81.jpg',
                                                                             'https://i.redd.it/z6xsxvwws4r81.jpg',
                                                                             'https://i.redd.it/qa06ddzws4r81.jpg',
                                                                             'https://i.redd.it/mitqf8vws4r81.jpg'],
                 'wgvr91': 'https://i.redd.it/tickqtntewf91.jpg', 'wgybif': [
            'https://i.redd.it/lwgz9e1uu9i91.png', 'https://i.redd.it/3rtlr21uu9i91.png',
            'https://i.redd.it/0ff29b1uu9i91.png', 'https://i.redd.it/rz1q0a1uu9i91.png',
            'https://i.redd.it/xvzpjw0uu9i91.png', 'https://i.redd.it/ovsn801uu9i91.png',
            'https://i.redd.it/jx5ztw0uu9i91.png', 'https://i.redd.it/g1vzx31uu9i91.png',
            'https://i.redd.it/6g89h6obwwf91.jpg', 'https://i.redd.it/dy1mlxpbwwf91.jpg',
            'https://i.redd.it/pxjqv5obwwf91.jpg', 'https://i.redd.it/gyoi15xbwwf91.png',
            'https://i.redd.it/tmtattrbwwf91.jpg', 'https://i.redd.it/vjbx74bsxwf91.jpg',
            'https://i.redd.it/tlpmca7ixwf91.jpg', 'https://i.redd.it/6t9476obwwf91.jpg',
            'https://i.redd.it/jiy4j5xbwwf91.png', 'https://i.redd.it/sjd74qnbwwf91.jpg',
            'https://i.redd.it/roj8lwnbwwf91.jpg', 'https://i.redd.it/j4dsuvrbwwf91.png',
            'https://i.redd.it/o1i0utnbwwf91.png', 'https://i.redd.it/h0s7fopbwwf91.jpg',
            'https://i.redd.it/sbiddwubwwf91.png', 'https://i.redd.it/ocu3glrbwwf91.png',
            'https://i.redd.it/07x86ypbwwf91.jpg', 'https://i.redd.it/hra7jrnbwwf91.jpg',
            'https://i.redd.it/7filuosbwwf91.png', 'https://i.redd.it/bcqj1kvbwwf91.jpg',
            'https://i.redd.it/yndw671xs4r81.png', 'https://i.redd.it/d6hxtqwws4r81.jpg',
            'https://i.redd.it/mqbbwtuws4r81.jpg', 'https://i.redd.it/j4ki1kwws4r81.jpg',
            'https://i.redd.it/1ma5jywws4r81.png', 'https://i.redd.it/6eus5r2xs4r81.jpg',
            'https://i.redd.it/9jkjavuws4r81.jpg', 'https://i.redd.it/iprespwws4r81.jpg',
            'https://i.redd.it/yo9xyxwws4r81.jpg', 'https://i.redd.it/z2pzf9vws4r81.jpg',
            'https://i.redd.it/t7s2ztuws4r81.jpg', 'https://i.redd.it/2906q61xs4r81.jpg',
            'https://i.redd.it/l5655c6xs4r81.jpg', 'https://i.redd.it/mfimk1vws4r81.png',
            'https://i.redd.it/kf8ijwuws4r81.jpg', 'https://i.redd.it/pricd1xws4r81.jpg',
            'https://i.redd.it/0e2qttuws4r81.jpg', 'https://i.redd.it/z6xsxvwws4r81.jpg',
            'https://i.redd.it/qa06ddzws4r81.jpg', 'https://i.redd.it/mitqf8vws4r81.jpg'], 'tyxxt9':
                     'https://i.redd.it/okpsguyla9s81.jpg', 'tul5p1': ['https://i.redd.it/lwgz9e1uu9i91.png',
                                                                       'https://i.redd.it/3rtlr21uu9i91.png',
                                                                       'https://i.redd.it/0ff29b1uu9i91.png',
                                                                       'https://i.redd.it/rz1q0a1uu9i91.png',
                                                                       'https://i.redd.it/xvzpjw0uu9i91.png',
                                                                       'https://i.redd.it/ovsn801uu9i91.png',
                                                                       'https://i.redd.it/jx5ztw0uu9i91.png',
                                                                       'https://i.redd.it/g1vzx31uu9i91.png',
                                                                       'https://i.redd.it/6g89h6obwwf91.jpg',
                                                                       'https://i.redd.it/dy1mlxpbwwf91.jpg',
                                                                       'https://i.redd.it/pxjqv5obwwf91.jpg',
                                                                       'https://i.redd.it/gyoi15xbwwf91.png',
                                                                       'https://i.redd.it/tmtattrbwwf91.jpg',
                                                                       'https://i.redd.it/vjbx74bsxwf91.jpg',
                                                                       'https://i.redd.it/tlpmca7ixwf91.jpg',
                                                                       'https://i.redd.it/6t9476obwwf91.jpg',
                                                                       'https://i.redd.it/jiy4j5xbwwf91.png',
                                                                       'https://i.redd.it/sjd74qnbwwf91.jpg',
                                                                       'https://i.redd.it/roj8lwnbwwf91.jpg',
                                                                       'https://i.redd.it/j4dsuvrbwwf91.png',
                                                                       'https://i.redd.it/o1i0utnbwwf91.png',
                                                                       'https://i.redd.it/h0s7fopbwwf91.jpg',
                                                                       'https://i.redd.it/sbiddwubwwf91.png',
                                                                       'https://i.redd.it/ocu3glrbwwf91.png',
                                                                       'https://i.redd.it/07x86ypbwwf91.jpg',
                                                                       'https://i.redd.it/hra7jrnbwwf91.jpg',
                                                                       'https://i.redd.it/7filuosbwwf91.png',
                                                                       'https://i.redd.it/bcqj1kvbwwf91.jpg',
                                                                       'https://i.redd.it/yndw671xs4r81.png',
                                                                       'https://i.redd.it/d6hxtqwws4r81.jpg',
                                                                       'https://i.redd.it/mqbbwtuws4r81.jpg',
                                                                       'https://i.redd.it/j4ki1kwws4r81.jpg',
                                                                       'https://i.redd.it/1ma5jywws4r81.png',
                                                                       'https://i.redd.it/6eus5r2xs4r81.jpg',
                                                                       'https://i.redd.it/9jkjavuws4r81.jpg',
                                                                       'https://i.redd.it/iprespwws4r81.jpg',
                                                                       'https://i.redd.it/yo9xyxwws4r81.jpg',
                                                                       'https://i.redd.it/z2pzf9vws4r81.jpg',
                                                                       'https://i.redd.it/t7s2ztuws4r81.jpg',
                                                                       'https://i.redd.it/2906q61xs4r81.jpg',
                                                                       'https://i.redd.it/l5655c6xs4r81.jpg',
                                                                       'https://i.redd.it/mfimk1vws4r81.png',
                                                                       'https://i.redd.it/kf8ijwuws4r81.jpg',
                                                                       'https://i.redd.it/pricd1xws4r81.jpg',
                                                                       'https://i.redd.it/0e2qttuws4r81.jpg',
                                                                       'https://i.redd.it/z6xsxvwws4r81.jpg',
                                                                       'https://i.redd.it/qa06ddzws4r81.jpg',
                                                                       'https://i.redd.it/mitqf8vws4r81.jpg'],
                 'r9j1fp': 'https://i.redd.it/2haowd4e1r381.png', 'ra24su':
                     'https://i.redd.it/74yxxacdqv381.jpg', 'r9efid': 'https://i.redd.it/itlvqsl8tp381.jpg', 'l2z8xv':
                     'https://i.redd.it/97mb1ke5ryc61.jpg'}
    subreddits = ['wallpapers', 'wallpaper']
    dumpList("subreddits.txt", subreddits)
    print(readList("subreddits.txt"))
