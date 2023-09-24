import os
import sys
import db
import json
from concurrent import futures
import word2vec
import google.protobuf.empty_pb2 as empty_pb2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../protos")))
import post_pb2
import post_pb2_grpc


class Post(post_pb2_grpc.PostServiceServicer):
    def GeneratePosts(self, request, context):
        print("GeneratePosts request received")

        # unpack request
        uid = request.uid
        prompt = request.prompt

        # get average word2vec embedding of prompt
        # if prompt cannot be embedded, return grpc empty
        embedded_prompt = word2vec.embed_words(prompt.split(" "))
        if not embedded_prompt:
            return empty_pb2.Empty()

        # query db for photos that match the given uid
        db.connect()
        photos = db.select_photos(uid)
        db.close()

        # for each photo, calculate its word2vec similarity
        def process_photo(photo):
            photo["similarity"] = word2vec.similarity(
                embedded_prompt, json.loads(photo["word2vec"])
            )
            return photo

        with futures.ThreadPoolExecutor() as executor:
            photos = executor.map(process_photo, photos)
        
        # sort photos based on its word2vec similarity
        photos = sorted(photos, key=lambda photo: photo["similarity"], reverse=True)

        # send stream of responses, with each response containing a post
        for photo in photos:
            response = post_pb2.GeneratePostResponse(post={"photo_src": photo["src"]})
            yield response
