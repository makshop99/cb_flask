from datetime import datetime
import re

def get_content():  
  time_stamp = datetime.utcnow()
  page_name = 'Home'
  next_page = 'Subpage'
  page_link = 'subpage'
  
  return_dict = {
    'page_name' : page_name,
    'time_stamp' : time_stamp,
    'next_page' : next_page,
    'page_link' : page_link
  }
  print('content ---------------------')
  return return_dict
