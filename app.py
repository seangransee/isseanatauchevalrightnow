import os
import urlparse
from flask import Flask, redirect, render_template
import redis

REDIS_URL = os.environ.get('REDISCLOUD_URL')
PARSED_REDIS_URL = urlparse.urlparse(REDIS_URL)
r = redis.StrictRedis.from_url(REDIS_URL)

app = Flask(__name__)


@app.route('/')
def main():
  answer = r.get('answer') or 'No'
  return render_template('app.html', answer=answer)


@app.route(os.environ.get('yes'))
def yes():
  r.set('answer', 'Yes')
  return redirect('/')


@app.route(os.environ.get('no'))
def no():
  r.set('answer', 'No')
  return redirect('/')


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
