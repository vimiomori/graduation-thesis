# https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.LineSentence

import time
import pandas as pd
import numpy as np
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import matplotlib.pyplot as plt
    # import japanize_matplotlib

from gensim.models import Word2Vec
from numpy.polynomial.polynomial import polyfit


def get_cs_rating_df(ari_vector, nashi_vector, word_pairs):
    df = pd.DataFrame(columns=['Target', 'Neighbor', 'Ari_Cosine_Similarity', 'Nashi_Cosine_Similarity', 'Rating'])
    zipped = zip(word_pairs['Target'], word_pairs['Neighbor'], word_pairs['Rating'])
    for target, neighbor, rating in zipped:
        if not (target in ari_vector.vocab
                and neighbor in ari_vector.vocab
                and target in nashi_vector.vocab
                and neighbor in nashi_vector.vocab):
            continue
        ari_cosine_similarity = ari_vector.similarity(w1=target, w2=neighbor)
        nashi_cosine_similarity = nashi_vector.similarity(w1=target, w2=neighbor)
        row = dict(
            Target=target,
            Neighbor=neighbor,
            Ari_Cosine_Similarity=ari_cosine_similarity,
            Nashi_Cosine_Similarity=nashi_cosine_similarity,
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


def get_score(ari_vector, nashi_vector):
    # ari_vector = Word2Vec.load('joshi_ari.model').wv
    # nashi_vector = Word2Vec.load('joshi_nashi.model').wv
    word_pairs = pd.read_excel(
        'O-S.xlsx',
        sheet_name='All',
        use_cols=['Target', 'Neighbor', 'Rating']
    )
    res_df = get_cs_rating_df(ari_vector, nashi_vector, word_pairs)

    ari_cc = res_df['Ari_Cosine_Similarity'].corr(res_df['Rating'])
    nashi_cc = res_df['Nashi_Cosine_Similarity'].corr(res_df['Rating'])
    res_df.to_excel('output.xlsx')
    return ari_cc, nashi_cc


def main():
    start = time.time()
    get_score()
    
    plot(ari_res, '助詞あり', ari_cc)
    plot(nashi_res, '助詞なし', nashi_cc)
    print(time.time()-start)


if __name__ == "__main__":
    main()