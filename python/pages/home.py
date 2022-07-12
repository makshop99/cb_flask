from datetime import datetime

def get_content():
  date_time = datetime.now()
  time_stamp = datetime.utcnow()
  page_header = '<h1>Home Page @%s</1>' % time_stamp  
  page_header += '<br><a href="subpage">Sub Page</a>'
  return page_header

