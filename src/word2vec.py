import sys
import os
import grpc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../protos")))
import word2vec_pb2_grpc
import word2vec_pb2


# get word2vec embedding from a list of words
def embed_words(words):
    with grpc.insecure_channel(os.environ["WORD2VEC_SERVER_ADDRESS"]) as channel:
        stub = word2vec_pb2_grpc.Word2VecServiceStub(channel)
        response = stub.EmbedWords(word2vec_pb2.EmbedWordsRequest(words=words))
        embeddings = [embedding.embedding for embedding in response.embeddings]
        return embeddings


# calculates the similarity of two word2vec embeddings
def similarity(embeddings1, embeddings2):
    with grpc.insecure_channel(os.environ["WORD2VEC_SERVER_ADDRESS"]) as channel:
        stub = word2vec_pb2_grpc.Word2VecServiceStub(channel)
        embeddings1 = [word2vec_pb2.Embedding(embedding=embedding) for embedding in embeddings1]
        embeddings2 = [word2vec_pb2.Embedding(embedding=embedding) for embedding in embeddings2]
        response = stub.Similarity(
            word2vec_pb2.SimilarityRequest(embeddings1=embeddings1, embeddings2=embeddings2)
        )
        return response.similarity
