# 简介
很早之前就想做的一个东西拖到现在。因为原来听说现代大多数方言都是中古汉语的后代，所以想应该可以统计普通话拼音到粤拼的转化数据，并从中找到一些规律。 
代码就不讲了，随便写的，很丑也没啥运行效率可言。 

爬取数据的网站有：
- 粤语发音词典：http://m.yueyv.com/
- 汉典：https://www.zdic.net/zd/zb/cc1/ （《现代汉语常用字表》常用字(2500字)）
- https://www.zdic.net/zd/zb/cc2/ （《现代汉语常用字表》次常用字(1000字)）

另外粤拼方案参考的网站：https://jyutping.org/ （这个网站真不错）

# 食用方法
有用的文件只有三个：inits.csv、vowels.csv 和 tones.csv。 
三个文件分别统计的声母、韵母和声调的转换。

以 vowels.csv 为例，行标签（index）是普通话的各韵母，列标签（column）是普通话的各声母（其中 total 代表不考虑韵母只考虑声母的统计数据，no init 表示无声母）。 
以其中一个数据项举例，d 和 ai 确定的那一格的内容是“oi: 2/4, aai: 2/4”，就代表统计的2000多个汉字中，所有普通话拼音是 dai 的字有4个，其中2个在粤语中的韵母是 oi，2个是aai。

不过需注意的是，我原本以为会有很强的规律性，但好像规律不是特别明显，也许是我统计的数据不够多，常用3500个汉字剔掉多音字就只有2000多个了，所以仅作参考。 还挺失望的。
听说声调分阴阳是因为声母的清浊，所以声调的规律还挺明显，有参考价值。
