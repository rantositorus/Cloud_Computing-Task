import time
import redis
from flask import Flask

app = Flask(__name__)
# Koneksi ke container bernama 'redis'
cache = redis.Redis(host='redis', port=6379)

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
    return '<h1>Hello from Docker!</h1><p>Halaman ini telah dilihat <strong>{}</strong> kali.</p>'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)