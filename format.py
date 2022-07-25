import pandas as pd
import numpy as np
import re
from re_constants import mandarin_vowel_tones as tones, mandarin_single_vowels as vowels

data_frame = pd.read_csv('mandarin.csv')
pinyin = data_frame.values.tolist()
data_frame = pd.read_csv('cantonese.csv')
jyutping = data_frame.values.tolist()

for i in range(len(pinyin)):
    for j in range(1, 3):
        if isinstance(pinyin[i][j], float) and np.isnan(pinyin[i][j]):  # be aware numpy.isnan can only be used for
            # float instances
            pinyin[i] = pinyin[i][:j]
            break
        else:
            for k in range(len(tones)):
                for u in range(len(tones[0])):
                    if re.search(tones[k][u], pinyin[i][j]):
                        pinyin[i][j] = re.sub(tones[k][u], vowels[u], pinyin[i][j].strip()) + str(k+1)
                        break
                else:
                    continue
                # 利用 for...else 语法完成跳出两层循环，妙啊
            # pinyin[i][j] = re.sub('ɑ', 'a', pinyin[i][j])  # !: 不能替换 ɑ，因为无法得知原本的读音，只能放弃统计该字
            if re.search(r'\d', pinyin[i][j]) is None:  # !: [-2:-1] to represent the last char isn't correct!
                pinyin[i][j] = pinyin[i][j] + '0'
        pinyin[i][j] = re.sub('((j)|(q)|(x)|(y))u', r'\1ü', pinyin[i][j])  # \数字 用以获得之前捕获的字符串。?: 那嵌套的括号呢？

for i in range(len(jyutping)):
    for j in range(1, 10):
        if isinstance(jyutping[i][j], float) and np.isnan(jyutping[i][j]):
            jyutping[i] = jyutping[i][:j]
            break
        else:
            jyutping[i][j] = re.sub('"', "", jyutping[i][j].strip())
# print('ā'.encode('utf-8'))  # ?: convert char to int in Python like in C
