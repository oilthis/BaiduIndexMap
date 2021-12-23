import index
import info
import pickle
from pydraw import draw_timeline_with_map


def save_obj(obj, name):
    with open('saved/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('saved/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


info_dict = info.location_code.copy()

keywords = input('keywords:')
timeset = input('do you want to set time?(y/n):')
if timeset == 'y':
    startt = input('start time:')
else:
    startt = None
for key in info_dict.keys():
    info_dict[key] = index.get_index_data(keywords, start=startt, location=key)

save_obj(info_dict, keywords)
info_dict = load_obj(keywords)
tl = draw_timeline_with_map(info_dict, keywords)
tl.render('output\\%s搜索指数.html' % keywords)
