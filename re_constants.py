import re

mandarin_vowel_tones = [['ā', 'ō', 'ē', 'ī', 'ū', 'ǖ'],
                        ['á', 'ó', 'é', 'í', 'ú', 'ǘ'],
                        ['ǎ', 'ǒ', 'ě', 'ǐ', 'ǔ', 'ǚ'],
                        ['à', 'ò', 'è', 'ì', 'ù', 'ǜ']]
mandarin_single_vowels = ['a', 'o', 'e', 'i', 'u', 'ü']

mandarin_initials = ['', 'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'z', 'c', 's', 'j', 'q', 'x', 'zh',
                     'ch', 'sh', 'r', 'y', 'w']
mandarin_vowels = ['a', 'o', 'e', 'i', 'u', 'ü', 'ai', 'ei', 'ui', 'ao', 'ou', 'iu', 'ie', 'üe', 'er', 'an', 'en',
                   'in', 'un', 'ün', 'ang', 'eng', 'ing', 'ong', 'ia', 'ian', 'iang', 'iao', 'iong', 'ua', 'uan',
                   'uang', 'uai', 'uo']
mandarin_tones = ['0', '1', '2', '3', '4']  # 0 代表轻声

cantonese_initials = ['', 'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'z', 'c', 's', 'gw', 'kw', 'j', 'w',
                      'ng']

# cantonese_front_vowels = ['i', 'yu', 'u', 'e', 'eo', 'oe', 'o', 'a', 'aa']
# cantonese_back_vowels = ['', 'i', 'u', 'm', 'n', 'ng', 'p', 't', 'k']
# print([i+j for i in cantonese_front_vowels for j in cantonese_back_vowels])
cantonese_vowels = ['', 'i', 'iu', 'im', 'in', 'ing', 'ip', 'it', 'ik', 'yu', 'yun', 'yut', 'u', 'ui', 'um', 'un',
                    'ung', 'up', 'ut', 'uk', 'e', 'ei', 'eu', 'em', 'en', 'eng', 'ep', 'et', 'ek', 'eoi', 'eon', 'eot',
                    'oe', 'oeng', 'oet', 'oek', 'o', 'oi', 'ou', 'om', 'on', 'ong', 'ot', 'ok', 'a', 'ai', 'au', 'am',
                    'an', 'ang', 'ap', 'at', 'ak', 'aa', 'aai', 'aau', 'aam', 'aan', 'aang', 'aap', 'aat', 'aak']
# 粤语元音61个没错，因为2018年新加了2个元音：a 和 oet，资料来源：https://jyutping.org/jyutping/
cantonese_tones = ['1', '2', '3', '4', '5', '6']

# !: 注意 | 周围不能有空格，因为会被正则表达式识别
jyutping_initials_re = '|'.join(i for i in ['(' + j + ')' for j in cantonese_initials])  # join 连接列表元素成字符串
jyutping_vowels_re = '|'.join(i for i in ['(' + j + ')' for j in cantonese_vowels])
jyutping_tones_re = '|'.join(i for i in ['(' + j + ')' for j in cantonese_tones])
pinyin_initials_re = '|'.join(i for i in ['(' + j + ')' for j in mandarin_initials])
pinyin_vowels_re = '|'.join(i for i in ['(' + j + ')' for j in mandarin_vowels])
pinyin_tones_re = '|'.join(i for i in ['(' + j + ')' for j in mandarin_tones])
# print(pinyin_tones_re)  # !: a new idea: what if print the name of the object which the mouse is pointed to?

jyutping_pattern = re.compile('(?P<init>' + jyutping_initials_re + ')' + '(?P<vowel>' + jyutping_vowels_re + ')' +
                              '(?P<tone>' + jyutping_tones_re + ')')
pinyin_pattern = re.compile('(?P<init>' + pinyin_initials_re + ')' + '(?P<vowel>' + pinyin_vowels_re + ')' +
                            '(?P<tone>' + pinyin_tones_re + ')')
# print(pinyin_pattern)  # 输出有长度限制，但是其正则表达式的长度是没有限制的

# 1: 普通话、粤语声母可以为空！粤语有韵母为空的情况：ng4。
# 2: 普通话中的韵母还要算上两个韵母组合的情况，如 iang。
# 3: 在普通话中，为严谨将 j、q、x、y 后的 u 全改为 ü，如此，ün 只在 j、q、x、y 后出现，而 üe 和 ü 除了在他们外还在 l、n 后出现
#    （且 ue 这个韵母代表的读音在普通话中不存在）。之所以这么改动是为了让韵母和读音间一一对应。这一点在 format 文件中的第29行实现。
