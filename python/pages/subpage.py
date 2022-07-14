from datetime import datetime

def get_content():
  time_stamp = datetime.utcnow()
  page_name = 'Subpage'
  next_page = 'Home'
  page_link = 'home'
  
  return_dict = {
    'page_name' : page_name,
    'time_stamp' : time_stamp,
    'next_page' : next_page,
    'page_link' : page_link
  }
  return return_dict