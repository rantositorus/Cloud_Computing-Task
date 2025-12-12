import time
import redis
from flask import Flask
import os

app = Flask(__name__)

cache = redis.Redis(host='redis-db', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return '<h1>Case 5 Berhasil!</h1><p>Aplikasi Python connect ke Redis. Dilihat <strong>{}</strong> kali.</p>'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)