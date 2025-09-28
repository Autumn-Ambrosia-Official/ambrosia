from flask import Flask, redirect

app = Flask(__name__)

i = 0

@app.route('/')
def home():
  global i
  try:
    html_link = ["https://index-autumn.onrender.com", "https://autumn-ambrosia.pages.dev"]
    index = len(html_link)
    i += 1
    if i == index:
      i = 0

    return redirect(html_link[i])
  except:
    return "<h2>Failed to redirect. Please try again</h2>"

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
