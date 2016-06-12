from flask import Flask
from flask import redirect

################################## CONFIG ######################################
app = Flask(__name__)


################################## ROUTES ######################################

@app.route('/')
def whohasatiny():
    return redirect('https://www.facebook.com/DonaldTrump/')

@app.route('/github')
def github():
    return redirect('https://github.com/jainshubhi/redirect-to-douchebag')

if __name__ == '__main__':
    app.run()
