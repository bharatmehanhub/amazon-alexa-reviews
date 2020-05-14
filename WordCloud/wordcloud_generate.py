#! usr/bin/python

import numpy as np
import pandas as pd
import data_prep
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def generate_wc():
    dataset = pd.read_csv('amazon_alexa.tsv', delimiter='\t', quoting=3)
    dataset = data_prep.data_set_process(dataset)

    ds1 = ' '.join(list(dataset[(dataset['rating'] == 1) & (dataset['feedback'] == 0)]['verified_reviews']))
    ds2 = ' '.join(list(dataset[(dataset['rating'] == 2) & (dataset['feedback'] == 0)]['verified_reviews']))
    ds3 = ' '.join(list(dataset[(dataset['rating'] == 2) & (dataset['feedback'] == 1)]['verified_reviews']))
    ds4 = ' '.join(list(dataset[(dataset['rating'] == 3) & (dataset['feedback'] == 1)]['verified_reviews']))
    ds5 = ' '.join(list(dataset[(dataset['rating'] == 4) & (dataset['feedback'] == 1)]['verified_reviews']))
    ds6 = ' '.join(list(dataset[(dataset['rating'] == 5) & (dataset['feedback'] == 1)]['verified_reviews']))

    if len(ds1) > 0:
        wordCloud = WordCloud(background_color="white", width=1600, height=800).generate(str(ds1))
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(16, 8), dpi=600)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Negative reviews with 1 rating Words')
        plt.savefig('Negative_reviews_with_1_rating_Words.png')

    if len(ds2) > 0:
        wordCloud = WordCloud(background_color="white", width=1600, height=800).generate(str(ds2))
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(16, 8), dpi=600)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Negative reviews with 2 rating Words')
        plt.savefig('Negative_reviews_with_2_rating_Words.png')

    if len(ds3) > 0:
        wordCloud = WordCloud(background_color="white", width=1600, height=800).generate(str(ds3))
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(16, 8), dpi=600)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Positive reviews with 2 rating Words')
        plt.savefig('Positive_reviews_with_2_rating_Words.png')

    if len(ds4) > 0:
        wordCloud = WordCloud(background_color="white", width=1600, height=800).generate(str(ds4))
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(16, 8), dpi=600)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Positive reviews with 3 rating Words')
        plt.savefig('Positive_reviews_with_3_rating_Words.png')

    if len(ds5) > 0:
        wordCloud = WordCloud(background_color="white", width=1600, height=800).generate(str(ds5))
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(16, 8), dpi=600)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Positive reviews with 4 rating Words')
        plt.savefig('Positive_reviews_with_4_rating_Words.png')

    if len(ds6) > 0:
        wordCloud = WordCloud(background_color="white", width=1600, height=800).generate(str(ds6))
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(16, 8), dpi=600)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Positive reviews with 5 rating Words')
        plt.savefig('Positive_reviews_with_5_rating_Words.png')


if __name__ == '__main__':
    generate_wc()
