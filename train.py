import csv
from gensim.models import Word2Vec
from evaluate import get_score


def main():
    # old_score = 0
    # new_score = 0
    window_size = 20
    with open('joshi_ari.csv', 'r') as f:
        re = csv.reader(f)
        corpus = list(re)
    
    with open("tuning_results.csv", "w") as f:
        wr = csv.writer(f)
        while window_size < 50:
            # nashi_model = Word2Vec(corpus_file='joshi_nashi.csv', window=window_size)
            ari_model = Word2Vec(corpus, window=window_size)
            # nashi_model.save('joshi_nashi.model')
            ari_model.save('joshi_ari.model')
            # old_score = new_score
            # new_score = get_score()
            score = get_score()
            print(window_size, score)
            wr.writerow([window_size, score]) 
            window_size += 10

if __name__ == "__main__":
    main()