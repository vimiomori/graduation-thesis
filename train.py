import csv
from gensim.models import Word2Vec
from evaluate import get_score


def main():
    window_size = 5
    with open('joshi_ari.csv', 'r') as f:
        re = csv.reader(f)
        ari_corpus = list(re)
    with open('joshi_nashi.csv', 'r') as f:
        re = csv.reader(f)
        nashi_corpus = list(re)
    
    with open("tuning_results.csv", "w") as f:
        wr = csv.writer(f)
        # while window_size < 50:
        nashi_model = Word2Vec(nashi_corpus, window=window_size)
        ari_model = Word2Vec(ari_corpus, window=window_size)
        # nashi_model.save('joshi_nashi.model')
        # ari_model.save('joshi_ari.model')
        ari_score, nashi_score = get_score(ari_model.wv, nashi_model.wv)
        print(window_size, ari_score, nashi_score)
        wr.writerow([window_size, ari_score, nashi_score])
            # window_size += 5

if __name__ == "__main__":
    main()
