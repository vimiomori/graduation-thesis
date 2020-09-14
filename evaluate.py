# https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.LineSentence

import pandas as pd
from gensim.models import Word2Vec


def eval_ari():
    ari_model = Word2Vec.load('joshi_ari.model')


def eval_nashi():
    nashi_model = Word2Vec.load('joshi_nashi.model')


def main():
    ratings = pd.read_excel('O-S.xlsx', sheet_name='All')


if __name__ == "__main__":
    main()
    