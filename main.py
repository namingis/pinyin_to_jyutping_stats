import pandas as pd

from re_constants import pinyin_pattern, jyutping_pattern
from format import pinyin, jyutping
import re

# print(pinyin)
# print(jyutping)

selected_pinyin = []
selected_jyutping = []
for i in range(len(pinyin)):
    if len(pinyin[i]) == 2 and len(jyutping[i]) == 2:
        pinyin_match = pinyin_pattern.match(pinyin[i][1])
        jyutping_match = jyutping_pattern.match(jyutping[i][1])
        if pinyin_match is not None and jyutping_match is not None:
            selected_pinyin.append(pinyin_match)
            selected_jyutping.append(jyutping_match)
init_dict = {}
vowel_dict = {}
tone_dict = {}

for i in range(len(selected_pinyin)):
    if selected_pinyin[i].group('init') not in init_dict:
        init_dict[selected_pinyin[i].group('init')] = {}
    if selected_pinyin[i].group('vowel') not in init_dict[selected_pinyin[i].group('init')]:
        init_dict[selected_pinyin[i].group('init')][selected_pinyin[i].group('vowel')] = {}
    if selected_jyutping[i].group('init') not in init_dict[selected_pinyin[i].group('init')][selected_pinyin[i].group('vowel')]:
        init_dict[selected_pinyin[i].group('init')][selected_pinyin[i].group('vowel')][
            selected_jyutping[i].group('init')] = 0
    init_dict[selected_pinyin[i].group('init')][selected_pinyin[i].group('vowel')][
        selected_jyutping[i].group('init')] += 1
    if 'total' not in init_dict[selected_pinyin[i].group('init')]:
        init_dict[selected_pinyin[i].group('init')]['total'] = {}
    if selected_jyutping[i].group('init') not in init_dict[selected_pinyin[i].group('init')]['total']:
        init_dict[selected_pinyin[i].group('init')]['total'][selected_jyutping[i].group('init')] = 0
    init_dict[selected_pinyin[i].group('init')]['total'][selected_jyutping[i].group('init')] += 1

# print(init_dict)
for i in init_dict:
    for j in init_dict[i]:
        init_dict[i][j] = [[k, init_dict[i][j][k]] for k in init_dict[i][j]]
        init_dict[i][j].sort(key=lambda elem: elem[1], reverse=True)
        total = 0
        for k in range(len(init_dict[i][j])):
            total += init_dict[i][j][k][1]
        for k in range(len(init_dict[i][j])):
            init_dict[i][j][k][1] = str(init_dict[i][j][k][1]) + '/' + str(total)
        init_dict[i][j] = ', '.join(item[0] + ': ' + str(item[1]) for item in init_dict[i][j])

init_df = pd.DataFrame(init_dict)  # !: Pandas 支持将嵌套字典转换成 DataFrame
init_df.to_csv("inits.csv")

for i in range(len(selected_pinyin)):
    if selected_pinyin[i].group('init') not in vowel_dict:
        vowel_dict[selected_pinyin[i].group('init')] = {}
    if selected_pinyin[i].group('vowel') not in vowel_dict[selected_pinyin[i].group('init')]:
        vowel_dict[selected_pinyin[i].group('init')][selected_pinyin[i].group('vowel')] = {}
    if selected_jyutping[i].group('vowel') not in vowel_dict[selected_pinyin[i].group('init')][selected_pinyin[i].group('vowel')]:
        vowel_dict[selected_pinyin[i].group('init')][selected_pinyin[i].group('vowel')][
            selected_jyutping[i].group('vowel')] = 0
    vowel_dict[selected_pinyin[i].group('init')][selected_pinyin[i].group('vowel')][
        selected_jyutping[i].group('vowel')] += 1
    if 'total' not in vowel_dict:
        vowel_dict['total'] = {}
    if selected_pinyin[i].group('vowel') not in vowel_dict['total']:
        vowel_dict['total'][selected_pinyin[i].group('vowel')] = {}
    if selected_jyutping[i].group('vowel') not in vowel_dict['total'][selected_pinyin[i].group('vowel')]:
        vowel_dict['total'][selected_pinyin[i].group('vowel')][selected_jyutping[i].group('vowel')] = 0
    vowel_dict['total'][selected_pinyin[i].group('vowel')][selected_jyutping[i].group('vowel')] += 1

for i in vowel_dict:
    for j in vowel_dict[i]:
        vowel_dict[i][j] = [[k, vowel_dict[i][j][k]] for k in vowel_dict[i][j]]
        vowel_dict[i][j].sort(key=lambda elem: elem[1], reverse=True)
        total = 0
        for k in range(len(vowel_dict[i][j])):
            total += vowel_dict[i][j][k][1]
        for k in range(len(vowel_dict[i][j])):
            vowel_dict[i][j][k][1] = str(vowel_dict[i][j][k][1]) + '/' + str(total)
        vowel_dict[i][j] = ', '.join(item[0] + ': ' + str(item[1]) for item in vowel_dict[i][j])
# print(vowel_dict)
vowel_df = pd.DataFrame(vowel_dict)
vowel_df.to_csv("vowels.csv")

for i in range(len(selected_pinyin)):
    if selected_pinyin[i].group('tone') not in tone_dict:
        tone_dict[selected_pinyin[i].group('tone')] = {}
    if selected_pinyin[i].group('init') not in tone_dict[selected_pinyin[i].group('tone')]:
        tone_dict[selected_pinyin[i].group('tone')][selected_pinyin[i].group('init')] = {}
    if selected_jyutping[i].group('tone') not in tone_dict[selected_pinyin[i].group('tone')][selected_pinyin[i].group('init')]:
        tone_dict[selected_pinyin[i].group('tone')][selected_pinyin[i].group('init')][
            selected_jyutping[i].group('tone')] = 0
    tone_dict[selected_pinyin[i].group('tone')][selected_pinyin[i].group('init')][
        selected_jyutping[i].group('tone')] += 1
# print(tone_dict)
for i in tone_dict:
    for j in tone_dict[i]:
        tone_dict[i][j] = [[k, tone_dict[i][j][k]] for k in tone_dict[i][j]]
        tone_dict[i][j].sort(key=lambda elem: elem[1], reverse=True)
        total = 0
        for k in range(len(tone_dict[i][j])):
            total += tone_dict[i][j][k][1]
        for k in range(len(tone_dict[i][j])):
            tone_dict[i][j][k][1] = str(tone_dict[i][j][k][1]) + '/' + str(total)
        tone_dict[i][j] = ', '.join(item[0] + ': ' + str(item[1]) for item in tone_dict[i][j])
tone_dict = dict(sorted(tone_dict.items(), key=lambda item: item[0]))
tone_df = pd.DataFrame(tone_dict)
tone_df.to_csv("tones.csv")
