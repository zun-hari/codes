#!/usr/bin/env python
# coding: utf-8

# ## Installing Packages

# In[4]:




import numpy as np
import pandas_gbq
import pandas as pd
import pyarrow
import pandasql as ps
from google.cloud import bigquery
import time
from datetime import datetime
import pytz
import gc
from datetime import datetime
from dateutil import rrule
from dateutil.relativedelta import relativedelta
from pandas.io import gbq
from collections import Counter
from operator import attrgetter
from urllib.parse import urlparse
from dateutil.relativedelta import relativedelta
from urllib.parse import parse_qs
import mysql.connector as sql
from mysql.connector.constants import ClientFlag
pd.set_option('display.max_rows',7000)
from google.oauth2 import service_account

import os
# biguery_config_file_path = os.environ['biguery_config_file_path']
# sheet_config_file_path = os.environ['sheet_config_file_path']


# credentials = service_account.Credentials.from_service_account_file(biguery_config_file_path)
# credentials = service_account.Credentials.from_service_account_file('C:/Users/Admin/Downloads/zunpulse4development-374ba97aecf0+(1).json')
# project_id = 'zunpulse4development'
# client = bigquery.Client(credentials= credentials,project=project_id)


# In[5]:


#Email trigger for fail safe
# error_list=[platform_error,order_status_error,category_error,sub_category_error,product_error,state_error]
# error_dict={platform_error:failsafe_message_platform,order_status_error:failsafe_message_order_status,
#             category_error:failsafe_message_category,sub-category_error:failsafe_message_sub-category,
#             product_error:failsafe_message_product,state_error:failsafe_message_state}
    
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "hari.kumar@zunpulse.com"
                # toaddr = "EMAIL address of the receiver"

                # instance of MIMEMultipart
msg = MIMEMultipart()
                # storing the senders email address  
msg['From'] = fromaddr
                # storing the receivers email address 
                # msg['To'] = "hari.kumar@zunpulse.com,kunal.shekhar@zunpulse.com"
# msg['To'] = "hari.kumar@zunpulse.com,ashank.garg@zunpulse.com,kunal.shekhar@zunpulse.com,product@zunroof.com"
msg['To'] = "hari.kumar@zunpulse.com"

                # storing the subject 
msg['Subject'] = "Automation TEST"
                # string to store the body of the mail
body = "ERROR!!!"
line='\n'
                # attach the body with the msg instance
msg.attach(MIMEText(body))
msg.attach(MIMEText(line))



                # open the file to be sent 
                # filename = "bquxjob_1c050a90_18340a7d279.csv"
                # attachment = open(r"C:\Users\USER\Downloads\bquxjob_1c050a90_18340a7d279.csv","rb")
                # instance of MIMEBase and named as p
                # p = MIMEBase('application', 'octet-stream')
                # To change the payload into encoded form
                # p.set_payload((attachment).read())
                # encode into base64
                # encoders.encode_base64(p)

                # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                # attach the instance 'p' to instance 'msg'
                # msg.attach(p)
                # creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
                # start TLS for security
s.starttls()

                # Authentication
s.login("hari.kumar@zunpulse.com", "vihzjpywqccydedn")

                # Converts the Multipart msg into a string
text = msg.as_string()
                # text=df

                # list of email_id to send the mail
                # li = ["hari.kumar@zunpulse.com","kunal.shekhar@zunpulse.com"]
# li=["hari.kumar@zunpulse.com","ashank.garg@zunpulse.com","kunal.shekhar@zunpulse.com","product@zunroof.com"]
li=["hari.kumar@zunpulse.com"]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("hari.kumar@zunpulse.com", "vihzjpywqccydedn")
    message = "Test email"
    s.sendmail("fromaddr", dest, text)
    s.quit()
    break


                # # sending the mail
                # s.sendmail(fromaddr, toaddr, text)

                # # terminating the session
                # s.quit()


# In[ ]:




