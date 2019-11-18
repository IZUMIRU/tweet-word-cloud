# coding:utf-8
import csv
from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
from collections import Counter, defaultdict
import numpy as np
from PIL import Image

def counter(texts):
    t = Tokenizer()
    words_count = defaultdict(int)
    words = []
    for text in texts:
        tokens = t.tokenize(text)
        for token in tokens:
            pos = token.part_of_speech.split(',')[0]
            if pos in ['名詞']:
                words_count[token.base_form] += 1
                words.append(token.base_form)
    return words_count, words

with open('./tweets/tweet_data', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    texts = []
    for row in reader:
        if(len(row) > 0):
            text = row[0].split('http')
            texts.append(text[0])

words_count, words = counter(texts)
text = ' '.join(words)

fpath = "~/Library/Fonts/RictyDiminished-Bold.ttf"
twitter_logo = np.array(Image.open("./twitter.png"))

# 除外指定
stop_words = [
    u'https', u'co', u'LINE', u'アカウント', u'YahooNewsTopics'
    ,u'news', u'linenews', u'Yahoo', u'ニュース', u'いる', u'する'
    ,u'ある', u'なる', u'れる', u'できる', u'ない', u'これ', u'こと'
    ,u'さん', u'られる', u'やる', u'てる', u'よう', u'そう', u'それ'
]

wordcloud = WordCloud(
    background_color="white",
    font_path = fpath,
    width=800,
    height=500,
    mask=twitter_logo,
    stopwords=set(stop_words),
).generate(text)

wordcloud.to_file("./word_clouds/word_cloud.png")
