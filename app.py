from flask import Flask
from flask import redirect

app = Flask(__name__)


@app.route('/')
def whohasatiny():
    return redirect('https://www.facebook.com/DonaldTrump/')

if __name__ == '__main__':
    app.run()
