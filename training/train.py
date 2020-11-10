import time
import csv
import pickle
import sys

from gensim.models import Word2Vec
from evaluate import get_score


def main(sg, window, size):
    start = time.time()
    print(">"*10, "Preparing corpuses", "<"*10)
    print("Loading 助詞あり corpus")
    with open('joshi_ari.pkl', 'rb') as f:
        ari_corpus = pickle.load(f)
    print("Loading 助詞なし corpus")
    with open('joshi_nashi.pkl', 'rb') as f:
        nashi_corpus = pickle.load(f)
    print(">"*10, f"Corpuses loaded, time elapsed: {((time.time() - start)/60):.2f} mins", "<"*10)
    
    with open("tuning_results.csv", "a", newline="") as f:
        wr = csv.writer(f)
        print("-" * 10, f"Beginning to train with params: window: {window}, size: {size}, sg: {sg}", "-" * 10) 
        print("Training 助詞なし model")
        nashi_model = Word2Vec(nashi_corpus, window=window, size=size, sg=sg)
        print("Training 助詞あり model")
        ari_model = Word2Vec(ari_corpus, window=window, size=size, sg=sg)
        print("Calculating scores")
        ari_score, nashi_score = get_score(ari_model.wv, nashi_model.wv)
        print("*" * 30)
        print(f"Results: 助詞あり score: {ari_score}, 助詞なし score: {nashi_score}")
        print(f"Total elapsed time for this iteration: {((time.time() - start)/60):.2f} mins")
        print("*" * 30)
        wr.writerow([sg, window, size, ari_score, nashi_score])

if __name__ == "__main__":
    sg = int(sys.argv[1])
    window = int(sys.argv[2])
    size = int(sys.argv[3])
    main(sg, window, size)
