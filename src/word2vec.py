from gensim.models import KeyedVectors
import sklearn.metrics.pairwise as pairwise
import numpy as np

print("loading model")
# load model
model_path = "../model/GoogleNews-vectors-negative300.bin.gz"
model = KeyedVectors.load_word2vec_format(model_path, binary=True, limit=None)


# get average embedding from word2vec embedding
def avg_embedding(embedding):
    return np.mean(embedding, axis=0)


# get word2vec embedding from a list of words
def embed_words(words):
    return [
        model.get_vector(word).tolist() for word in words if word in model.key_to_index
    ]


# calculates the cosine similarity of two 'numpy.ndarry's
def cosine_similarity(a, b):
    return pairwise.cosine_similarity([a], [b])[0][0]
