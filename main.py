import falcon
import redis
import uuid
import json

cache = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True)

class CacheResource(object):
    def on_get(self, req, resp, id):
        resp.status = falcon.HTTP_301
        url = cache.get(id)
        raise falcon.HTTPMovedPermanently(url)

    def on_post(self, req, resp, id):
        resp.status = falcon.HTTP_201
        doc = json.load(req.stream)
        id = uuid.uuid4()
        cache.set(id, doc["url"])
        resp.content_type = "application/json"
        resp.body = ('{"shortened_url":"http://localhost:8000/' + str(id) + '"}')


app = falcon.API()
app.add_route('/{id}', CacheResource())
