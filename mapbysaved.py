import pickle
from pydraw import draw_timeline_with_map


def load_obj(name):
    with open('saved/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


keywords = input('keywords:')
info_dict = load_obj(keywords)
tl = draw_timeline_with_map(info_dict, keywords)
tl.render('output\\%s搜索指数.html' % keywords)
