from flask import Flask
from flask import render_template
from pages import home as home_content
from pages import subpage as subpage_content
app = Flask (__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
  page_data = home_content.get_content()   
  #page_content 
  
  return render_template('main_template.html', page_name=page_data['page_name'], time_stamp=page_data['time_stamp'], page_link=page_data['page_link'], next_page=page_data['next_page'])

@app.route("/subpage")
def subpage():  
  page_data = subpage_content.get_content()
  return render_template('main_template.html', page_name=page_data['page_name'], time_stamp=page_data['time_stamp'], page_link=page_data['page_link'], next_page=page_data['next_page'])

if __name__  == '__main__':
  app.run(debug=True)
  
  
  # run with "flask run --host=0.0.0.0 --port=5001" to make the page reachable from outside