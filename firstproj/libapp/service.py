from datetime import datetime

def getgreeting():
  now = datetime.now()
  hour = now.hour
  if hour >= 0 and hour < 12:
    message = 'Good Morning'
  elif hour >= 12 and hour < 16:
    message = 'Good Afternoon'
  else:
    message = 'Good Evening'
  
  return message

def getcountries():
  # imagine u have got the countries from the database
  return [
    ('IN', 'India'),
    ('NE', 'Netherlands'),
    ('US', 'United states of america'),
    ('FR', 'France')
  ]