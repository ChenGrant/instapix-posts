import os
import sys
import db
import json
from max_heap_pq import MaxHeapPriorityQueue
import word2vec
import google.protobuf.empty_pb2 as empty_pb2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../proto")))
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
        prompt_embedding = word2vec.embed_words(prompt.split(" "))
        if not prompt_embedding:
            return empty_pb2.Empty()
        avg_prompt_embedding = word2vec.avg_embedding(prompt_embedding)

        # query db for photos that match the given uid
        db.connect()
        photos = db.select_photos(uid)
        db.close()

        # for each photo, push into priority queue where the priority
        # is its cosine similarity with 'avg_prompt_embedding'
        photo_pq = MaxHeapPriorityQueue()
        for photo in photos:
            priority = word2vec.cosine_similarity(
                avg_prompt_embedding,
                word2vec.avg_embedding(json.loads(photo["word2vec"])),
            )
            del photo["word2vec"]
            del photo["labels"]
            photo_pq.push(priority, photo)

        # send stream of responses, with each response containing a post
        while not photo_pq.is_empty():
            photo = photo_pq.pop()
            response = post_pb2.GeneratePostResponse(post={"photo_src": photo["src"]})
            yield response
