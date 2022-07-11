from datetime import datetime

def get_content():
  date_time = datetime.now()
  time_stamp = datetime.utcnow()
  page_header = '<h1>Sub Page @%s</1>' % time_stamp  
  page_header += '<br><a href="index">back</a>'
  return page_header