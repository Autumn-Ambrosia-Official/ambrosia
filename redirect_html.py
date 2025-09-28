from flask import Flask, redirect
import random

app = Flask(__name__)

@app.route('/')
def home():
  try:
    html_link = ["https://index-autumn.onrender.com", "https://autumn-ambrosia.pages.dev"]
    return redirect(random.choice(html_link))
  except:
    return "<h2>Failed to redirect. Please try again</h2>"

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
