# https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.LineSentence

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from gensim.models import Word2Vec
from numpy.polynomial.polynomial import polyfit


def get_cs_rating_df(vector, word_pairs):
    df = pd.DataFrame(columns=['Target', 'Neighbor', 'Cosine_Similarity', 'Rating'])
    zipped = zip(word_pairs['Target'], word_pairs['Neighbor'], word_pairs['Rating'])
    for target, neighbor, rating in zipped:
        if not (target in vector.vocab and neighbor in vector.vocab):
            continue
        cosine_similarity = vector.similarity(w1=target, w2=neighbor)
        row = dict(
            Target=target,
            Neighbor=neighbor,
            Cosine_Similarity=cosine_similarity,
            Rating=rating
        )
        df = df.append(row, ignore_index=True)
    return df


def plot(df, title, cc):
    x = df['Cosine_Similarity']
    y = df['Rating']

    #create basic scatterplot
    plt.plot(x, y, '.')
    plt.xlabel('コサイン類似度')
    plt.ylabel('評定平均値')

    #obtain m (slope) and b(intercept) of linear regression line
    m, b = np.polyfit(x, y, 1)

    #add linear regression line to scatterplot 
    plt.plot(x, m*x+b, label=f'相関係数：{cc}')
    plt.title(title)
    plt.savefig(f"{title}.png")
    plt.clf()


def main():
    start = time.time()
    ari_vector = Word2Vec.load('joshi_ari.model').wv
    nashi_vector = Word2Vec.load('joshi_nashi.model').wv
    word_pairs = pd.read_excel(
        'O-S.xlsx',
        sheet_name='All',
        use_cols=['Target', 'Neighbor', 'Rating']
    )
    ari_res = get_cs_rating_df(ari_vector, word_pairs)
    nashi_res = get_cs_rating_df(nashi_vector, word_pairs)
    ari_cc = ari_res['Cosine_Similarity'].corr(ari_res['Rating'])
    nashi_cc = nashi_res['Cosine_Similarity'].corr(nashi_res['Rating'])
    print(ari_res.head())
    print(nashi_res.head())
    plot(ari_res, '助詞あり', ari_cc)
    plot(nashi_res, '助詞なし', nashi_cc)
    print(time.time()-start)


if __name__ == "__main__":
    main()