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
if info.is_cookies_valid(info.cookie):
    pass
else:
    print('invalid cookie,program will exit')
    exit(1)
# 预检查cookie是否可以使用

print('Welcome to BaiduIndexMap.Input the keywords you want to search and program will output the result.')
keywords = input('keywords:')
timeset = input('do you want to set time?(y/n):')
if timeset == 'y':
    startt = input('start time:')
else:
    startt = None
for key in info_dict.keys():
    info_dict[key] = index.get_index_data(keywords, start=startt, location=key)

save_obj(info_dict, keywords)
print(f'{keywords} has been saved')
info_dict = load_obj(keywords)
tl = draw_timeline_with_map(info_dict, keywords)
tl.render('output\\%s搜索指数.html' % keywords)
