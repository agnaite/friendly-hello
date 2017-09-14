
from flask import Flask, render_template
from flask_assets import Environment
from redis import Redis, RedisError
import jinja2
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)
app.config['ASSETS_DEBUG'] = True

assets = Environment(app)
assets.url = app.static_url_path

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "cannot connect to Redis, counter disabled"

    return render_template('index.html',
                           name=os.getenv("NAME", "world"),
                           hostname=socket.gethostname(),
                           visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
