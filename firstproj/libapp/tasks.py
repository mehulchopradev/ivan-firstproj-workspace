from celery import shared_task
import time

@shared_task
def send_verification_email(email):
  print('About to send email to {0}'.format(email))

  # simulate the long running task
  time.sleep(15)

  print('Email sent to {0}'.format(email))