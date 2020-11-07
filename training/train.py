import csv
import sys

from gensim.models import Word2Vec
from evaluate import get_score


def main(sg, window, size):
    with open('joshi_ari.csv', 'r') as f:
        re = csv.reader(f)
        ari_corpus = list(re)
    with open('joshi_nashi.csv', 'r') as f:
        re = csv.reader(f)
        nashi_corpus = list(re)
    
    with open("tuning_results.csv", "a", newline="") as f:
        wr = csv.writer(f)
        nashi_model = Word2Vec(nashi_corpus, window=window, size=size, sg=sg)
        ari_model = Word2Vec(ari_corpus, window=window, size=size, sg=sg)
        ari_score, nashi_score = get_score(ari_model.wv, nashi_model.wv)
        print(sg, window, size, ari_score, nashi_score)
        wr.writerow([sg, window, size, ari_score, nashi_score])

if __name__ == "__main__":
    sg = sys.argv[1]
    window = sys.argv[2]
    size = sys.argv[3]
    main(sg, window, size)
