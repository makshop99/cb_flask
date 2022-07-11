from flask import Flask
from pages import home as home_content
from pages import subpage as subpahge_content
app = Flask (__name__)

@app.route("/")
@app.route("/index")
@app.route("/index")
def home():
  page_content = home_content.get_content() 
  return page_content

@app.route("/subpage")
def subpage():  
  page_content = subpahge_content.get_content()
  return page_content

if __name__  == '__main__':
  app.run(debug=True)