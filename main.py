import falcon
import redis
import uuid
import json

cache = redis.StrictRedis(host='localhost', port=6379,
                          charset="utf-8", decode_responses=True)


class CacheResource(object):
    def on_get(self, req, resp, id):
        url = cache.get(id)
        resp.status = falcon.HTTP_301
        resp.set_header('Location', url)
        raise falcon.HTTPMovedPermanently(url)

    def on_post(self, req, resp, id):
        doc = json.load(req.stream)
        id = uuid.uuid4()
        cache.set(id, doc["url"])
        resp.status = falcon.HTTP_201
        resp.content_type = "application/json"
        resp.body = (
            '{"shortened_url":"http://localhost:8000/' + str(id) + '"}')


app = falcon.API()
app.add_route('/{id}', CacheResource())
