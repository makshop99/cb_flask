from flask import Flask
from pages import home as home_content
app = Flask (__name__)

@app.route("/")
@app.route("/index")
def home():
  page_content = home_content.get_content()
  return page_content


if __name__  == '__main__':
  app.run(debug=True)