#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def main():
    d = os.path.dirname(__file__)
    DOC_NAME = "cvpr2015papers.txt"
    text = open(os.path.join(d, DOC_NAME)).read()

    # adding computer vision specific stopwords
    stopwords = STOPWORDS.copy()
    stopwords.add("image")

    wc = WordCloud(max_words=300, stopwords=stopwords, width=800, height=400)
    wc.generate(text)
    wc.to_file(os.path.join(d, "cvpr2015wordcloud.png"))

    plt.imshow(wc)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
