import time
import pandas as pd

from gensim.models import Word2Vec


def split_sentences(corpus):
    size = len(corpus) 
    idx_list = [i + 1 for i, val in
                enumerate(corpus) if val == '。'] 
  
    sentences = [
        corpus[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))
    ] 
    return sentences


def remove_joshi(df):
    joshi = df[df['品詞'].str.contains('助詞')]
    return df.drop(joshi.index)


def main():
    start = time.time()
    df = pd.read_csv('extracted.csv').dropna()
    joshi_nashi = split_sentences(remove_joshi(df)['原文文字列'].to_list())
    joshi_ari = split_sentences(df['原文文字列'].to_list())
    nashi_model = Word2Vec(joshi_nashi, window_size=10)
    ari_model = Word2Vec(joshi_ari, window_size=10)
    nashi_model.save('joshi_nashi.model')
    ari_model.save('joshi_ari.model')
    print(f"vectors created          time elapsed: {(time.time() - start):.2f}")


if __name__ == "__main__":
    main()
