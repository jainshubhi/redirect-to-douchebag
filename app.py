from flask import Flask
from flask import redirect

################################## CONFIG ######################################
app = Flask(__name__)


################################## ROUTES ######################################

@app.route('/')
def whohasatiny():
    return redirect('https://www.facebook.com/DonaldTrump/')

if __name__ == '__main__':
    app.run()
