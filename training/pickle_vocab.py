import pickle
import csv


def main():
    with open('joshi_ari.csv', 'r') as f:
        re = csv.reader(f)
        ari_corpus = list(re)
    with open('joshi_nashi.csv', 'r') as f:
        re = csv.reader(f)
        nashi_corpus = list(re)
    with open('joshi_ari.pkl', 'wb') as f:
        pickle.dump(ari_corpus, f)
    with open('joshi_nashi.pkl', 'wb') as f:
        pickle.dump(nashi_corpus, f)


if __name__ == "__main__":
    main()