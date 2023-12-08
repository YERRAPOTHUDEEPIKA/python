from flask import Flask, request, url_for, redirect, session, render_template, json, flash, send_file, jsonify
from flask_session import Session
import pymongo
import matplotlib.pyplot as plt
import cryptocode
import datetime
import pandas as pd
import xlrd
import numpy as np
from datetime import date
import time
from datetime import datetime, timedelta
import random
import inflect
from fpdf import FPDF
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from num2words import num2words
import decimal 
import webbrowser
import shutil
import math
#import fuzzy
#soundex = fuzzy.Soundex(4)
import numpy
import xlrd
from calendar import Calendar, monthrange
#import pyodbc
#scheduler
import time
import atexit
from hashlib import sha256
import urllib
import requests
from urllib.request import urlopen
import json
import zipfile
import pygal
from time import sleep
import plotly
import plotly.express as px
import json
import gc

#import lxml.html

import pickle

from apscheduler.schedulers.background import BackgroundScheduler
#if os.path.getsize(file_path) > 0:



global ourpairs, display_table, prev_ticker_table, difference_display_table, tolerance_table
global exch1, exch2, exch3, exch4, chart, xtime
global exch1, exch2, exch3, exch4, chart, xtime
global line_chart
global charted_previous
global api_pair, diff_table, diff_array
global payload
global mail_payload
charted_previous = False
global price_detail_array
price_detail_array = []
api_pair=''
global p_no
p_no = 0
line_chart = pygal.Line()

exch1 = []
exch2 = []
exch3 = []
exch4 = []
xtime = []
#
ourpairs = []
display_table = []
prev_ticker_table = []
ourpairs.append("ETH/USDT")
ourpairs.append("BTC/USDT")
ourpairs.append("ETH/BTC")
ourpairs.append("LTC/USDT")
ourpairs.append("LTC/BTC")
ourpairs.append("LTC/USD")
ourpairs.append("BCH/USDT")
ourpairs.append("BTC/USD")
ourpairs.append("ETH/USD")
ourpairs.append("BCH/BTC")
ourpairs.append("XRP/USDT")
ourpairs.append("BNB/USDT")
ourpairs.append("USDC/USDT")
ourpairs.append("FIL/USDT")
ourpairs.append("SOL/USDT")
ourpairs.append("LDO/USDT")
ourpairs.append("ARB/USDT")
ourpairs.append("UNI/USDT")
ourpairs.append("MATIC/USDT")
ourpairs.append("ATOM/USDT")
ourpairs.append("SHIB/USDT")
ourpairs.append("DOGE/USDT")
ourpairs.append("TRX/USDT")
ourpairs.append("ADA/USDT")
ourpairs.append("GRT/USDT")
ourpairs.append("AVAX/USDT")
ourpairs.append("AAVE/USDT")
ourpairs.append("XLM/USDT")
ourpairs.append("ALGO/USDT")
ourpairs.append("ETC/USDT")
ourpairs.append("LINK/USDT")
ourpairs.append("NEAR/USDT")
ourpairs.append("DOT/USDT")
ourpairs.append("WBTC/USDT")
ourpairs.append("DAI/USDT")
ourpairs.append("UNIQ/USD")
ourpairs.append("BCH/USD")


rows, cols = (37, 14)
display_table =[]
for i in range(0,rows):
	myrow=[]
	for j in range(0,cols):
		myrow.append('')
	display_table.append(myrow)
display_table[0][0] ="ETH/USDT"
display_table[1][0] ="BTC/USDT"
display_table[2][0] ="ETH/BTC"
display_table[3][0] ="LTC/USDT"
display_table[4][0] ="LTC/BTC"
display_table[5][0] ="LTC/USD"
display_table[6][0] ="BCH/USDT"
display_table[7][0] ="BTC/USD"
display_table[8][0] ="ETH/USD"
display_table[9][0] ="BCH/BTC"
display_table[10][0] ="XRP/USDT"
display_table[11][0] ="BNB/USDT"
display_table[12][0] ="USDC/USDT"
display_table[13][0] ="FIL/USDT"
display_table[14][0] ="SOL/USDT"
display_table[15][0] ="LDO/USDT"
display_table[16][0] ="ARB/USDT"
display_table[17][0] ="UNI/USDT"
display_table[18][0] ="MATIC/USDT"
display_table[19][0] ="ATOM/USDT"
display_table[20][0] ="SHIB/USDT"
display_table[21][0] ="DOGE/USDT"
display_table[22][0] ="TRX/USDT"
display_table[23][0] ="ADA/USDT"
display_table[24][0] ="GRT/USDT"
display_table[25][0] ="AVAX/USDT"
display_table[26][0] ="AAVE/USDT"
display_table[27][0] ="XLM/USDT"
display_table[28][0] ="ALGO/USDT"
display_table[29][0] ="ETC/USDT"
display_table[30][0] ="LINK/USDT"
display_table[31][0] ="NEAR/USDT"
display_table[32][0] ="DOT/USDT"
display_table[33][0] ="WBTC/USDT"
display_table[34][0] ="DAI/USDT"
display_table[35][0] ="UNIQ/USD"
display_table[36][0] ="BCH/USD"

prev_ticker_table =[]
for i in range(0,rows):
	myrow=[]
	for j in range(0,cols):
		myrow.append('0')
	prev_ticker_table.append(myrow)
prev_ticker_table[0][0] ="ETH/USDT"
prev_ticker_table[1][0] ="BTC/USDT"
prev_ticker_table[2][0] ="ETH/BTC"
prev_ticker_table[3][0] ="LTC/USDT"
prev_ticker_table[4][0] ="LTC/BTC"
prev_ticker_table[5][0] ="LTC/USD"
prev_ticker_table[6][0] ="BCH/USDT"
prev_ticker_table[7][0] ="BTC/USD"
prev_ticker_table[8][0] ="ETH/USD"
prev_ticker_table[9][0] ="BCH/BTC"
prev_ticker_table[10][0] ="XRP/USDT"
prev_ticker_table[11][0] ="BNB/USDT"
prev_ticker_table[12][0] ="USDC/USDT"
prev_ticker_table[13][0] ="FIL/USDT"
prev_ticker_table[14][0] ="SOL/USDT"
prev_ticker_table[15][0] ="LDO/USDT"
prev_ticker_table[16][0] ="ARB/USDT"
prev_ticker_table[17][0] ="UNI/USDT"
prev_ticker_table[18][0] ="MATIC/USDT"
prev_ticker_table[19][0] ="ATOM/USDT"
prev_ticker_table[20][0] ="SHIB/USDT"
prev_ticker_table[21][0] ="DOGE/USDT"
prev_ticker_table[22][0] ="TRX/USDT"
prev_ticker_table[23][0] ="ADA/USDT"
prev_ticker_table[24][0] ="GRT/USDT"
prev_ticker_table[25][0] ="AVAX/USDT"
prev_ticker_table[26][0] ="AAVE/USDT"
prev_ticker_table[27][0] ="XLM/USDT"
prev_ticker_table[28][0] ="ALGO/USDT"
prev_ticker_table[29][0] ="ETC/USDT"
prev_ticker_table[30][0] ="LINK/USDT"
prev_ticker_table[31][0] ="NEAR/USDT"
prev_ticker_table[32][0] ="DOT/USDT"
prev_ticker_table[33][0] ="WBTC/USDT"
prev_ticker_table[34][0] ="DAI/USDT"
prev_ticker_table[35][0] ="UNIQ/USD"
prev_ticker_table[36][0] ="BCH/USD"


rows, cols = (37, 2)
global tolerance_table
tolerance_table =[]
for i in range(0,rows):
	myrow=[]
	for j in range(0,cols):
		myrow.append('')
	tolerance_table.append(myrow)
tolerance_table[0][0] ="ETH/USDT"
tolerance_table[1][0] ="BTC/USDT"
tolerance_table[2][0] ="ETH/BTC"
tolerance_table[3][0] ="LTC/USDT"
tolerance_table[4][0] ="LTC/BTC"
tolerance_table[5][0] ="LTC/USD"
tolerance_table[6][0] ="BCH/USDT"
tolerance_table[7][0] ="BTC/USD"
tolerance_table[8][0] ="ETH/USD"
tolerance_table[9][0] ="BCH/BTC"
tolerance_table[10][0] ="XRP/USDT"
tolerance_table[11][0] ="BNB/USDT"
tolerance_table[12][0] ="USDC/USDT"
tolerance_table[13][0] ="FIL/USDT"
tolerance_table[14][0] ="SOL/USDT"
tolerance_table[15][0] ="LDO/USDT"
tolerance_table[16][0] ="ARB/USDT"
tolerance_table[17][0] ="UNI/USDT"
tolerance_table[18][0] ="MATIC/USDT"
tolerance_table[19][0] ="ATOM/USDT"
tolerance_table[20][0] ="SHIB/USDT"
tolerance_table[21][0] ="DOGE/USDT"
tolerance_table[22][0] ="TRX/USDT"
tolerance_table[23][0] ="ADA/USDT"
tolerance_table[24][0] ="GRT/USDT"
tolerance_table[25][0] ="AVAX/USDT"
tolerance_table[26][0] ="AAVE/USDT"
tolerance_table[27][0] ="XLM/USDT"
tolerance_table[28][0] ="ALGO/USDT"
tolerance_table[29][0] ="ETC/USDT"
tolerance_table[30][0] ="LINK/USDT"
tolerance_table[31][0] ="NEAR/USDT"
tolerance_table[32][0] ="DOT/USDT"
tolerance_table[33][0] ="WBTC/USDT"
tolerance_table[34][0] ="DAI/USDT"
tolerance_table[35][0] ="UNIQ/USD"
tolerance_table[36][0] ="BCH/USD"

#read from database not hardcode
global Prices_db, Prices_dbclient, Tolerance, Prices
Prices_dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
Prices_db = Prices_dbclient["Prices"]
Prices = Prices_db["PricesFromExchanges"]
Tolerance = Prices_db["Tolerance"]
for i in range(0,rows):
	mypair = tolerance_table[i][0]
	findpair = list(Tolerance.find({"Pair" : mypair }))
	for rec in findpair:
		tolerance_table[i][1] = float(rec.get("Tolerance"))



#rows, cols = (37, 25)
rows, cols = (37, 28) #For Nadhir 13/09/2023
difference_display_table =[]
for i in range(0,rows):
	myrow=[]
	for j in range(0,cols):
		myrow.append('0')
	difference_display_table.append(myrow)

difference_display_table[0][0] ="ETH/USDT"
difference_display_table[1][0] ="BTC/USDT"
difference_display_table[2][0] ="ETH/BTC"
difference_display_table[3][0] ="LTC/USDT"
difference_display_table[4][0] ="LTC/BTC"
difference_display_table[5][0] ="LTC/USD"
difference_display_table[6][0] ="BCH/USDT"
difference_display_table[7][0] ="BTC/USD"
difference_display_table[8][0] ="ETH/USD"
difference_display_table[9][0] ="BCH/BTC"
difference_display_table[10][0] ="XRP/USDT"
difference_display_table[11][0] ="BNB/USDT"
difference_display_table[12][0] ="USDC/USDT"
difference_display_table[13][0] ="FIL/USDT"
difference_display_table[14][0] ="SOL/USDT"
difference_display_table[15][0] ="LDO/USDT"
difference_display_table[16][0] ="ARB/USDT"
difference_display_table[17][0] ="UNI/USDT"
difference_display_table[18][0] ="MATIC/USDT"
difference_display_table[19][0] ="ATOM/USDT"
difference_display_table[20][0] ="SHIB/USDT"
difference_display_table[21][0] ="DOGE/USDT"
difference_display_table[22][0] ="TRX/USDT"
difference_display_table[23][0] ="ADA/USDT"
difference_display_table[24][0] ="GRT/USDT"
difference_display_table[25][0] ="AVAX/USDT"
difference_display_table[26][0] ="AAVE/USDT"
difference_display_table[27][0] ="XLM/USDT"
difference_display_table[28][0] ="ALGO/USDT"
difference_display_table[29][0] ="ETC/USDT"
difference_display_table[30][0] ="LINK/USDT"
difference_display_table[31][0] ="NEAR/USDT"
difference_display_table[32][0] ="DOT/USDT"
difference_display_table[33][0] ="WBTC/USDT"
difference_display_table[34][0] ="DAI/USDT"
difference_display_table[35][0] ="UNIQ/USD"
difference_display_table[36][0] ="BCH/USD"

chartrows, chartcols = (1200, 6)
global table_for_chart, chart_table, xArray, y1Array, y2Array, y3Array, y4Array
table_for_chart = []
xArray = []
y1Array = []
y2Array = [] 
y3Array = []
y4Array = []

for i in range(0,chartrows):
	myrow=[]
	for j in range(0,chartcols):
		myrow.append('0')
	table_for_chart.append(myrow)
#0 to 5549 rows, 0 to 10 columns
global chart_index
chart_index = 0



ServerBank = Flask(__name__)
ServerBank.config["SESSION_PERMANENT"] = False
ServerBank.config["SESSION_TYPE"] = "filesystem"
import hashlib
secret_string = str(datetime.now())
result = hashlib.sha256(secret_string.encode())

result_hex = result.hexdigest()
secret_key = result_hex.encode('ASCII')
#print(secret_key)
ServerBank.config['SECRET_KEY'] = secret_key
#ServerBank.config['SECRET_KEY'] = b'1db9a6ffaf6a8566338d6d2f8db1f812a7c23a4e25299ab6ab228a81e9cfdaf0'
Session(ServerBank)
Session(ServerBank)

global staticpath
global mycwd, mydrive

global thisenv

global ServerBank_dbclient, ServerBank_db, EmaraldBank_users, EmaraldBank_customers, EmaraldBank_Transactions
global environ, staticpath, thisenv
global otpdone
global request_id


global begin_time, time_now
begin_time = datetime.now()
time_now = datetime.now()


mycwd= os.getcwd()
mydrive = mycwd[0:2]


def print_date_time():
	print("Hello, this is a scheduled message from ServerBank")
	print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))




#atexit.register(lambda: scheduler.shutdown())

def currency_in_indian_format(n):
	""" Convert a number (int / float) into indian formatting style """
	d = decimal.Decimal(str(n))

	if d.as_tuple().exponent < -2:
		s = str(n)
	else:
		s = '{0:.2f}'.format(n)

	l = len(s)
	i = l - 1

	res, flag, k = '', 0, 0
	while i >= 0:
		if flag == 0:
			res += s[i]
			if s[i] == '.':
				flag = 1
		elif flag == 1:
			k += 1
			res += s[i]
			if k == 3 and i - 1 >= 0:
				res += ','
				flag = 2
				k = 0
		else:
			k += 1
			res += s[i]
			if k == 2 and i - 1 >= 0:
				res += ','
				flag = 2
				k = 0
		i -= 1

	return res[::-1]
#currency in indian format ends here

def word(number):
	x = str(number)
	if x == "" or x == "0":
		word = "Zero"
	else:
		rupees, paise = x.split('.')
		rupees_word = num2words(rupees, lang ='en_IN') + ' '
		if int(paise) > 0:
			paise_word = ' and ' + num2words(paise, lang ='en_IN') + ' Paise'
			word =  rupees_word + paise_word
		else:
			word = rupees_word
		word = word.replace(',','').title()                                      
	return word
#number to word ends here


def dbopen():
	global ServerBank_dbclient, ServerBank_db, EmaraldBank_users, EmaraldBank_customers, EmaraldBank_Transactions
	global environ, staticpath, thisenv, pg_send_requests
	global KappsoftBank_users, KappsoftBank_customers, KappsoftBank_Transactions
	
	#23/03/2023
	#
	ServerBank_dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
	ServerBank_db = ServerBank_dbclient["ServerBank"]
	EmaraldBank_customers = ServerBank_db["EmaraldBankCustomers"]
	EmaraldBank_Transactions = ServerBank_db["EmaraldBankTransactions"]
	EmaraldBank_Ledger = ServerBank_db["EmaraldBankLedger"]
	pgledger = ServerBank_db["PG_Ledger"]
	pg_send_requests = ServerBank_db["PG_Send_Requests"]
	#findcust = EmaraldBank_customers.find({})
	#for x in findcust:
	#	print(x)
	#
	KappsoftBank_users = ServerBank_db["KappsoftBankUsers"]
	KappsoftBank_customers = ServerBank_db["KappsoftBankCustomers"]
	KappsoftBank_Transactions = ServerBank_db["KappsoftBankTransactions"]
	#
	staticpath = "/ServerBank/Scripts/static/"
	environ = ServerBank_db["Environment"]
	# Difference in Dev and Prod environment is the static path
	envlist = environ.find({})
	envlist  = list(envlist)
	for envrec in envlist:
		if envrec.get("Environment") == "Production":
			staticpath = "/ServerBank/Scripts/static/"
			thisenv = "Production"
		elif envrec.get("Environment") == "Development":
			staticpath = "/ServerBank/Scripts/static/"
			thisenv = "Development"
		else:
			staticpath = "/ServerBank/Scripts/static/"
			thisenv = "Production"
	#
def send_the_mail(customer_email, pdfname, messtext, mess_subject):
	receiver = customer_email
	message = MIMEMultipart()
	message['From'] = "idle_trigger@kappsoft.com"
	message['To'] = receiver
	message['Subject'] =  mess_subject
	sender = "idle_trigger@kappsoft.com"
	empassword = "dR7*CPcJ2DZ=<bJX"
	message.attach(MIMEText(messtext, 'plain'))
	# open the pdf file in binary
	found_file = True
	try:
		binary_pdf = open(pdfname, 'rb')
	except FileNotFoundError:
		found_file = False
		print ('PDF Not found:',pdfname)
	if found_file:
		mail_payload = MIMEBase('application', 'octate-stream', Name=pdfname)
		# mail_payload = MIMEBase('application', 'pdf', Name=pdfname)
		mail_payload.set_mail_payload((binary_pdf).read())
		#print ('done mail_payload')

		# enconding the binary into base64
		encoders.encode_base64(mail_payload)
		#print ('done encoding the binary')

		# add header with pdf name
		mail_payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
		message.attach(mail_payload)
		smtp_done = False
		starttsl_done = False
		login_done = False
		sendmail_done = False
		try:
			mailsession = smtplib.SMTP('mail.kappmedia.com', 587, timeout=360)
			smtp_done = True
		except:
			smtp_done = False
		if smtp_done:
			try:
				mailsession.starttls()
				starttsl_done = True
			except:
				starttsl_done = False
			
		if starttsl_done:
			try:
				mailsession.login(sender, empassword)
				login_done = True
			except:
				login_done = False

		if login_done:
			text = message.as_string()
			try:
				mailsession.sendmail(sender, receiver, text)
				sendmail_done = True
			except:
				sendmail_done = False
				
		if sendmail_done:
			mailsession.quit()
			print("mail sent ", str(datetime.now()))

def item_generator(json_input, lookup_key):
	if isinstance(json_input, dict):
		for k, v in json_input.items():
			if k == lookup_key:
				yield v
			else:
				yield from item_generator(v, lookup_key)
	elif isinstance(json_input, list):
		for item in json_input:
			yield from item_generator(item, lookup_key)

def fill_difference_display_table():
	
	global ourpairs, difference_display_table, tolerance_table, chart_index, table_for_chart
	global Prices_db, Prices_dbclient, Tolerance, prev_epoch, Prices, time_now, begin_time
	gc.collect()

	for pair in range(0,len(ourpairs)):
		

		needed_pair = ourpairs[pair].replace('/','')
		needed_pair_with_hyphen = ourpairs[pair].replace('/','-')
		needed_pair_lower_case = needed_pair.lower()
		
		

		
		table_for_chart[chart_index][0] = ourpairs[pair]
		#print(chart_index, table_for_chart[chart_index][0])

		difference_display_table[pair][1]  =   time.strftime("%d.%m.%Y %I:%M:%S %p")
		table_for_chart[chart_index][1] = time.strftime("%I:%M:%S")
		#binance
		if os.path.getsize('binance.pickle') > 0:
			binance_feed = pickle.load(open("binance.pickle", "rb"))
			if binance_feed[pair][1] != 'nil' and binance_feed[pair][1] != '':
				difference_display_table[pair][7] = binance_feed[pair][1].rstrip('0')
				table_for_chart[chart_index][2] = float(binance_feed[pair][1])
			if binance_feed[pair][2] != 'nil' and binance_feed[pair][2] != '':
				difference_display_table[pair][9] = binance_feed[pair][2].rstrip('0')
				#table_for_chart[chart_index][3] = float(binance_feed[pair][2])
			if binance_feed[pair][3] != 'nil' and binance_feed[pair][3] != '':
				difference_display_table[pair][11] = binance_feed[pair][3].rstrip('0')
				#table_for_chart[chart_index][4] = float(binance_feed[pair][3])
		#binance over
		#kraken
		if os.path.getsize('kraken.pickle') > 0:
			kraken_feed = pickle.load(open("kraken.pickle", "rb"))
			if kraken_feed[pair][1] != 'nil' and kraken_feed[pair][1] != '':
				difference_display_table[pair][13] = kraken_feed[pair][1].rstrip('0')
				table_for_chart[chart_index][3] = float(kraken_feed[pair][1])
			if kraken_feed[pair][2] != 'nil' and kraken_feed[pair][2] != '':
				difference_display_table[pair][15] = kraken_feed[pair][2].rstrip('0')
				#table_for_chart[chart_index][6] = float(kraken_feed[pair][2])
			if kraken_feed[pair][3] != 'nil' and kraken_feed[pair][3] != '':
				difference_display_table[pair][17] = kraken_feed[pair][3].rstrip('0')
				#table_for_chart[chart_index][7] = float(kraken_feed[pair][3])
		#kraken over
		#coinbase
		if os.path.getsize('coinbase.pickle') > 0:
			coinbase_feed = pickle.load(open("coinbase.pickle", "rb"))
			if coinbase_feed[pair][1] != 'nil' and coinbase_feed[pair][1] != '':
				difference_display_table[pair][19] = coinbase_feed[pair][1].rstrip('0')
				table_for_chart[chart_index][4] = float(coinbase_feed[pair][1])
			if coinbase_feed[pair][2] != 'nil' and coinbase_feed[pair][2] != '':
				difference_display_table[pair][21] = coinbase_feed[pair][2].rstrip('0')
				#table_for_chart[chart_index][9] = float(coinbase_feed[pair][2])
			if coinbase_feed[pair][3] != 'nil' and coinbase_feed[pair][3] != '':
				difference_display_table[pair][23] = coinbase_feed[pair][3].rstrip('0')
				#table_for_chart[chart_index][10] = float(coinbase_feed[pair][3])
		#coinbase over
		#real unicoindcx
		if os.path.getsize('unicoindcx.pickle') > 0:
			print(os.path.getsize('unicoindcx.pickle'))
			unicoindcx_feed = pickle.load(open("unicoindcx.pickle", "rb"))
			if unicoindcx_feed[pair][1] != 'nil' and unicoindcx_feed[pair][1] != '':
				difference_display_table[pair][4] = float(unicoindcx_feed[pair][1])
				table_for_chart[chart_index][5] = float(unicoindcx_feed[pair][1])
			if unicoindcx_feed[pair][2] != 'nil' and unicoindcx_feed[pair][2] != '':
				difference_display_table[pair][5] = float(unicoindcx_feed[pair][2])
			if unicoindcx_feed[pair][3] != 'nil' and unicoindcx_feed[pair][3] != '':
				difference_display_table[pair][6] = float(unicoindcx_feed[pair][3])
		
		#calculate difference
		tolerance_for_pair=0
		#print(ourpairs[pair])
		search_pair = ourpairs[pair]
		findpair = list(Tolerance.find({"Pair" : search_pair }))
		#print(findpair)
		for rec in findpair:
			tolerance_for_pair = float(rec.get("Tolerance"))
		#print('tolerance:',tolerance_for_pair)
		#tolerance_for_pair = float(tolerance_table[pair][1])
		#print(tolerance_for_pair)
		differences = []
		diff_reasons = []
		#7,9,11 binance, diff in 8,10,12
		if float(difference_display_table[pair][7]) != 0.0 and float(difference_display_table[pair][4]) != 0.0:
			diff_last_with_binance = abs(float(difference_display_table[pair][7]) - float(difference_display_table[pair][4])) 
			differences.append(diff_last_with_binance)
			difference_display_table[pair][8] = "{:.4f}".format(diff_last_with_binance)
			diff_reasons.append('Binance Last')
		else:
			differences.append(0)
			difference_display_table[pair][8] = 0
			diff_reasons.append('')
		if float(difference_display_table[pair][9]) != 0.0 and float(difference_display_table[pair][5]) != 0.0:
			diff_ask_with_binance = abs(float(difference_display_table[pair][9]) - float(difference_display_table[pair][5])) 
			differences.append(diff_ask_with_binance)
			difference_display_table[pair][10] = "{:.4f}".format(diff_ask_with_binance)
			diff_reasons.append('Binance Ask')
		else:
			differences.append(0)
			difference_display_table[pair][10] = 0
			diff_reasons.append('')
		if float(difference_display_table[pair][11]) != 0.0 and float(difference_display_table[pair][6]) != 0.0:
			diff_bid_with_binance = abs(float(difference_display_table[pair][11]) - float(difference_display_table[pair][6])) 
			differences.append(diff_bid_with_binance)
			difference_display_table[pair][12] = "{:.4f}".format(diff_bid_with_binance)
			diff_reasons.append('Binance Bid')
		else:
			differences.append(0)
			difference_display_table[pair][12] = 0
			diff_reasons.append('')


		#13,15,17 kraken, diff in 14,16,18
		if float(difference_display_table[pair][13]) != 0.0 and float(difference_display_table[pair][4]) != 0.0:
			diff_last_with_kraken = abs(float(difference_display_table[pair][13]) - float(difference_display_table[pair][4])) 
			differences.append(diff_last_with_kraken)
			difference_display_table[pair][14] = "{:.4f}".format(diff_last_with_kraken)
			diff_reasons.append('Kraken Last')
		else:
			differences.append(0)
			difference_display_table[pair][14] = 0
			diff_reasons.append('')
		if float(difference_display_table[pair][15]) != 0.0 and float(difference_display_table[pair][5]) != 0.0:
			diff_ask_with_kraken = abs(float(difference_display_table[pair][15]) - float(difference_display_table[pair][5])) 
			differences.append(diff_ask_with_kraken)
			difference_display_table[pair][16] = "{:.4f}".format(diff_ask_with_kraken)
			diff_reasons.append('Kraken Ask')
		else:
			differences.append(0)
			difference_display_table[pair][16] = 0
			diff_reasons.append('')
		if float(difference_display_table[pair][17]) != 0.0 and float(difference_display_table[pair][6]) != 0.0:
			diff_bid_with_kraken = abs(float(difference_display_table[pair][17]) - float(difference_display_table[pair][6])) 
			differences.append(diff_bid_with_kraken)
			difference_display_table[pair][18] = "{:.4f}".format(diff_bid_with_kraken)
			diff_reasons.append('Kraken Bid')
		else:
			differences.append(0)
			difference_display_table[pair][18] = 0
			diff_reasons.append('')
		#19,21,23 coinbase, diff in 20,22,24
		if float(difference_display_table[pair][19]) != 0.0 and float(difference_display_table[pair][4]) != 0.0:
			diff_last_with_coinbase = abs(float(difference_display_table[pair][19]) - float(difference_display_table[pair][4])) 
			differences.append(diff_last_with_coinbase)
			difference_display_table[pair][20] = "{:.4f}".format(diff_last_with_coinbase)
			diff_reasons.append('Coinbase Last')
		else:
			differences.append(0)
			difference_display_table[pair][20] = 0
			diff_reasons.append('')
		if float(difference_display_table[pair][19]) != 0.0 and float(difference_display_table[pair][5]) != 0.0:
			diff_ask_with_coinbase = abs(float(difference_display_table[pair][21]) - float(difference_display_table[pair][5])) 
			differences.append(diff_ask_with_coinbase)
			difference_display_table[pair][22] = "{:.4f}".format(diff_ask_with_coinbase)
			diff_reasons.append('Coinbase Ask')
		else:
			differences.append(0)
			difference_display_table[pair][22] = 0
			diff_reasons.append('')
		if float(difference_display_table[pair][19]) != 0.0 and float(difference_display_table[pair][6]) != 0.0:
			diff_bid_with_coinbase = abs(float(difference_display_table[pair][23]) - float(difference_display_table[pair][6])) 
			differences.append(diff_bid_with_coinbase)
			difference_display_table[pair][24] = "{:.4f}".format(diff_bid_with_coinbase)
			diff_reasons.append('Coinbase Bid')
		else:
			differences.append(0)
			difference_display_table[pair][24] = 0
			diff_reasons.append('')
		#end of difference calculation
		# Highest in Binance as per Nadhir 13 09 2023
		difference_display_table[pair][25] = max(difference_display_table[pair][8], difference_display_table[pair][10], difference_display_table[pair][12])
		if float(difference_display_table[pair][25]) > tolerance_for_pair:
			difference_display_table[pair][25] = difference_display_table[pair][25] +"*"
		# Highest in Kraken as per Nadhir 13 09 2023
		difference_display_table[pair][26] = max(difference_display_table[pair][14], difference_display_table[pair][16], difference_display_table[pair][18])
		if float(difference_display_table[pair][26]) > tolerance_for_pair:
			difference_display_table[pair][26] = difference_display_table[pair][26] +"*"
		# Highest in Coinbase as per Nadhir 13 09 2023
		difference_display_table[pair][27] = max(difference_display_table[pair][20], difference_display_table[pair][22], difference_display_table[pair][24])
		if float(difference_display_table[pair][27]) > tolerance_for_pair:
			difference_display_table[pair][27] = difference_display_table[pair][27] +"*"
		#print('Binance diff ',difference_display_table[pair][25])
		#print('Kraken diff ',difference_display_table[pair][26])
		#print('Coinbase diff ',difference_display_table[pair][27])
		###
		max_of_differences = 0
		if len(differences) != 0:
			max_of_differences = max(differences)
			difference_display_table[pair][2] = max_of_differences
			difference_display_table[pair][2]  = "{:.4f}".format(float(difference_display_table[pair][2]) )
			#print('max of diff ',max_of_differences)
			if max_of_differences != 0.0:
				for z in range(0,len(differences)):
					#print(z)
					if differences[z] == max_of_differences:
						difference_display_table[pair][3] = diff_reasons[z]
						#print(difference_display_table[pair][3])
		#to store 5 minutes chart
		chart_index = chart_index + 1
		#global line_chart, chart

		#if chart_index > 5549:
		if chart_index > 1199:
			chart_index = 0		
		
		#print("special print",difference_display_table[pair][12])
		update_grid()
		collect_payload()
		

	#end of pair loop
	#print('inside charts')
	
	table_for_chart.sort(key=lambda row: (row[1]))  
	#print(table_for_chart)
	diff_array = difference_display_table
	#diff_table["server_table"] = diff_array 
	#chart_array = table_for_chart
	#chart_table["server_chart"] = chart_array                          
#fill_difference_display_table ends here


#first time once collect_payload
#global api_pair, difference_display_table, table_for_chart, payload, p_no
for p in range(0,len(ourpairs)):
		if ourpairs[p] == api_pair:
			p_no = p


price_detail_array = []

row0 = []
row0.append('ExchangeName')
row0.append("Bid")
row0.append('Bid Diff')
row0.append('Ask')
row0.append('Ask Diff')
row0.append('Last')
row0.append('Last Diff')
row0.append('Time')
price_detail_array.append(row0)

row1 = []
row1.append('Binance')
row1.append(difference_display_table[p_no][11])
row1.append(difference_display_table[p_no][12])
row1.append(difference_display_table[p_no][9])
row1.append(difference_display_table[p_no][10])
row1.append(difference_display_table[p_no][7])
row1.append(difference_display_table[p_no][8])
row1.append(difference_display_table[p_no][1])
price_detail_array.append(row1)

row2 = []
row2.append('Kraken')
row2.append(difference_display_table[p_no][17])
row2.append(difference_display_table[p_no][18])
row2.append(difference_display_table[p_no][15])
row2.append(difference_display_table[p_no][16])
row2.append(difference_display_table[p_no][13])
row2.append(difference_display_table[p_no][14])
row2.append(difference_display_table[p_no][1])
price_detail_array.append(row2)

row3 = []
row3.append('Coinbase')
row3.append(difference_display_table[p_no][23])
row3.append(difference_display_table[p_no][24])
row3.append(difference_display_table[p_no][21])
row3.append(difference_display_table[p_no][22])
row3.append(difference_display_table[p_no][19])
row3.append(difference_display_table[p_no][20])
row3.append(difference_display_table[p_no][1])
price_detail_array.append(row3)	
#added 26-09-2023
row4 = []
row4.append('UnicoinDCX')
row4.append(difference_display_table[p_no][6])
row4.append(0)
row4.append(difference_display_table[p_no][5])
row4.append(0)
row4.append(difference_display_table[p_no][4])
row4.append(0)
row4.append(difference_display_table[p_no][1])
price_detail_array.append(row4)	

#session['price_detail_array'] = price_detail_array
#print(table_for_chart)
xArray = []
y1Array = []
y2Array = [] 
y3Array = []
y4Array = []
lowrange = 0
highrange = 32767
for i in range(0,1200):
	#print(i)
	if (table_for_chart[i][0]) == '0':
		continue
	else:
		if table_for_chart[i][0] == api_pair:
			xArray.append(table_for_chart[i][1])
			y1Array.append(float(table_for_chart[i][2]))
			y2Array.append(float(table_for_chart[i][3]))
			y3Array.append(float(table_for_chart[i][4]))
			y4Array.append(float(table_for_chart[i][5]))
			lowrange = min(min(y1Array),min(y2Array),min(y3Array),min(y4Array))
			highrange = max(max(y1Array),max(y2Array),max(y3Array),max(y4Array))
		else:
			continue
	#end for
if 0.0 in y1Array :
	y1Array =[]
if 0.0 in y2Array :
	y2Array =[]
if 0.0 in y3Array :
	y3Array =[]
if 0.0 in y1Array :
	y4Array =[]


	

payload = {
	"price_detail_array" : price_detail_array,
	"xvalues" : xArray,
	"y1values" : y1Array,
	"y2values" : y2Array,
	"y3values" : y3Array,
	"y4values" : y4Array,
	"pair" : api_pair,
	"lowrange" : lowrange,
	"highrange" : highrange
	}
#print(payload)


def collect_payload():

	global api_pair, difference_display_table, table_for_chart, payload, p_no
	for p in range(0,len(ourpairs)):
			if ourpairs[p] == api_pair:
				p_no = p
	
	
	price_detail_array = []

	row0 = []
	row0.append('ExchangeName')
	row0.append("Bid")
	row0.append('Bid Diff')
	row0.append('Ask')
	row0.append('Ask Diff')
	row0.append('Last')
	row0.append('Last Diff')
	row0.append('Time')
	price_detail_array.append(row0)

	row1 = []
	row1.append('Binance')
	row1.append(difference_display_table[p_no][11])
	row1.append(difference_display_table[p_no][12])
	row1.append(difference_display_table[p_no][9])
	row1.append(difference_display_table[p_no][10])
	row1.append(difference_display_table[p_no][7])
	row1.append(difference_display_table[p_no][8])
	row1.append(difference_display_table[p_no][1])
	price_detail_array.append(row1)

	row2 = []
	row2.append('Kraken')
	row2.append(difference_display_table[p_no][17])
	row2.append(difference_display_table[p_no][18])
	row2.append(difference_display_table[p_no][15])
	row2.append(difference_display_table[p_no][16])
	row2.append(difference_display_table[p_no][13])
	row2.append(difference_display_table[p_no][14])
	row2.append(difference_display_table[p_no][1])
	price_detail_array.append(row2)

	row3 = []
	row3.append('Coinbase')
	row3.append(difference_display_table[p_no][23])
	row3.append(difference_display_table[p_no][24])
	row3.append(difference_display_table[p_no][21])
	row3.append(difference_display_table[p_no][22])
	row3.append(difference_display_table[p_no][19])
	row3.append(difference_display_table[p_no][20])
	row3.append(difference_display_table[p_no][1])
	price_detail_array.append(row3)	

	#added 26-09-2023
	row4 = []
	row4.append('UnicoinDCX')
	row4.append(difference_display_table[p_no][6])
	row4.append(0)
	row4.append(difference_display_table[p_no][5])
	row4.append(0)
	row4.append(difference_display_table[p_no][4])
	row4.append(0)
	row4.append(difference_display_table[p_no][1])
	price_detail_array.append(row4)	

	#session['price_detail_array'] = price_detail_array
	#print(table_for_chart)
	xArray = []
	y1Array = []
	y2Array = [] 
	y3Array = []
	y4Array = []
	lowrange = 0
	highrange = 32767
	for i in range(0,1200):
		#print(i)
		if (table_for_chart[i][0]) == '0':

			continue
		else:
			if table_for_chart[i][0] == api_pair:
				
				xArray.append(table_for_chart[i][1])
				y1Array.append(float(table_for_chart[i][2]))
				y2Array.append(float(table_for_chart[i][3]))
				y3Array.append(float(table_for_chart[i][4]))
				y4Array.append(float(table_for_chart[i][5]))
				lowrange = min(min(y1Array),min(y2Array),min(y3Array),min(y4Array))
				highrange = max(max(y1Array),max(y2Array),max(y3Array),max(y4Array))
			else:
				
				continue
		#end for
	#chart_array.pop(0)
	if 0.0 in y1Array :
		y1Array =[]
	if 0.0 in y2Array :
		y2Array =[]
	if 0.0 in y3Array :
		y3Array =[]
	if 0.0 in y1Array :
		y4Array =[]

	


	payload = {
		"price_detail_array" : price_detail_array,
		"xvalues" : xArray,
		"y1values" : y1Array,
		"y2values" : y2Array,
		"y3values" : y3Array,
		"y4values" : y4Array,
		"pair" : api_pair,
		"lowrange" : lowrange,
		"highrange" : highrange
		}
	#print(payload)

#changed ask,bid as bid, ask that is [6] and [5] on 5 9 2023 as per Kunhi
#changed to show diff in exchanges only instead of Last
buff_grid_data = difference_display_table
needed_array = []
needed_row = []
needed_row.append('Pair')
needed_row.append('Time')
#needed_row.append('HighestDiff')
#needed_row.append('WithPrice')
needed_row.append('Binance Diff')
needed_row.append('Kraken Diff')
needed_row.append('Coinbase Diff')
needed_row.append('UnicoinDCX Last')
needed_row.append('UnicoinDCX Bid')
needed_row.append('UnicoinDCX Ask')
needed_array.append(needed_row)
for z in range(0, len(buff_grid_data)):
	needed_row =[]
	needed_row.append(buff_grid_data[z][0])
	needed_row.append(buff_grid_data[z][1])
	#needed_row.append(buff_grid_data[z][2])
	#needed_row.append(buff_grid_data[z][3])
	needed_row.append(buff_grid_data[z][25])
	needed_row.append(buff_grid_data[z][26])
	needed_row.append(buff_grid_data[z][27])
	needed_row.append(buff_grid_data[z][4])
	needed_row.append(buff_grid_data[z][6])
	needed_row.append(buff_grid_data[z][5])
	needed_array.append(needed_row)

grid_data = needed_array



def update_grid():
	global grid_data
	buff_grid_data = difference_display_table
	needed_array = []
	needed_row = []
	needed_row.append('Pair')
	needed_row.append('Time')
	#needed_row.append('HighestDiff')
	#needed_row.append('WithPrice')
	needed_row.append('Binance Diff')
	needed_row.append('Kraken Diff')
	needed_row.append('Coinbase Diff')
	needed_row.append('UnicoinDCX Last')
	needed_row.append('UnicoinDCX Bid')
	needed_row.append('UnicoinDCX Ask')

	needed_array.append(needed_row)
	for z in range(0, len(buff_grid_data)):
		needed_row =[]
		needed_row.append(buff_grid_data[z][0])
		needed_row.append(buff_grid_data[z][1])
		#needed_row.append(buff_grid_data[z][2])
		#needed_row.append(buff_grid_data[z][3])
		needed_row.append(buff_grid_data[z][25])
		needed_row.append(buff_grid_data[z][26])
		needed_row.append(buff_grid_data[z][27])
		needed_row.append(buff_grid_data[z][4])
		needed_row.append(buff_grid_data[z][6])
		needed_row.append(buff_grid_data[z][5])
		needed_array.append(needed_row)
	grid_data = needed_array


scheduler = BackgroundScheduler()
#scheduler.add_job(func=get_from_exchanges, trigger="interval", seconds=2)
scheduler.add_job(func=fill_difference_display_table, trigger="interval", seconds=2)
scheduler.start()
print('polling scheduler started')
#btc/usdt starting value


atexit.register(lambda: scheduler.shutdown())

@ServerBank.route('/diffmon')
def home():
	global grid_data
	return render_template('diffmon.html', grid_data=grid_data)

@ServerBank.route('/get_grid_data')
def get_grid_data():
	global grid_data
	return jsonify(grid_data)

@ServerBank.route('/diffjson' , methods=['GET', 'POST'])
def diffjson():
	global  difference_display_table, ourpairs, json_diff
	json_diff = json.dumps(difference_display_table)
	#print(json_diff)
	return '%s' %json_diff



	

@ServerBank.route('/ToleranceSetting', methods=['GET', 'POST'])
def ToleranceSetting():
	Prices_dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
	Prices_db = Prices_dbclient["Prices"]
	Tolerance = Prices_db["Tolerance"]
	global tolerance_table
	session['tolerance_table'] = tolerance_table
	tolerance_unit_array =[]
	if request.method == 'POST':
		if request.form['submit_button'] == 'Submit':
			tolerance_unit_array = request.form.getlist('tolerance_unit[]')
	#print(tolerance_unit_array)
	c=0
	#Tolerance.delete_many({})
	
	
	for i in tolerance_unit_array:
		#print(i)
		tolerance_table[c][1] = i
		rquery = { "Pair" :  tolerance_table[c][0] }
		nval = { "$set": 
					{ 
					 "Tolerance" : float(i) 
					}
				}
		Tolerance.update_one(rquery, nval)
		c=c+1
	#print(tolerance_table)
	return render_template('ToleranceSetting.html')


@ServerBank.route('/pairdetails/<cc1>/<cc2>')
def paridetails(cc1, cc2):
	global api_pair
	global difference_display_table
	api_pair = cc1+'/'+cc2
	#print(api_pair)
	session['api_pair'] = api_pair
	
	return redirect(url_for('showpricedetail'))

@ServerBank.route('/showpricedetail')
def showpricedetail():
	global payload, api_pair

	return render_template("pricedet.html")

@ServerBank.route('/refresh_chart')
def refresh_chart():
	global payload, api_pair
	#print(api_pair)
	
	return jsonify(payload)


@ServerBank.route('/timesales', methods=['GET', 'POST'])
def timesales():
	global ourpairs
	global Prices_db, Prices_dbclient, Tolerance, Prices
	exchangelist = [ 'Binance','Kraken','Coinbase','UnicoinDCX']
	session['exchangelist'] = exchangelist
	pairlist = ourpairs
	
	session['pairlist'] = pairlist
	earliest_rec = list(Prices.find({'ExchangeName' : 'Binance'}).sort([('PriceTimeStamp', 1)]).limit(1))
	print(earliest_rec)
	for r1 in earliest_rec:
		early_date = datetime.strftime(r1.get("PriceTimeStamp"),"%Y-%m-%d")
		early_time = datetime.strftime(r1.get("PriceTimeStamp"),"%H:%M")
	#print(early_date)
	session['earliest_date'] = early_date
	session['earliest_time'] = early_time
	latest_rec = list(Prices.find({}).sort([('PriceTimeStamp', -1)]).limit(1))

	for r2 in latest_rec:
		latest_date = datetime.strftime(r2.get("PriceTimeStamp"),"%Y-%m-%d")
		latest_time = datetime.strftime(r2.get("PriceTimeStamp"),"%H:%M")

	session['latest_date'] = latest_date
	session['latest_time'] = latest_time

	session['fromprice'] = 0.0
	session['toprice'] = 0.0
	session['timesales_table'] =[]

	if request.method == 'POST':
		if request.form['ts_submit_button'] == 'Search':
			sel_pair = request.form['sel_pair']
			sel_exchange = request.form['sel_exchange']
			session['pair_exchange'] =""
			selexchange = []
			selexchange.append(sel_exchange)
			selpair =[]
			selpair.append(sel_pair)
			session['exchangelist'] = selexchange
			session['pairlist'] = selpair
			fromdate = request.form['fromdate']
			fromtime = request.form['fromtime']
			todate = request.form['todate']
			totime = request.form['totime']
			
			session['earliest_date'] = fromdate
			session['earliest_time'] = fromtime
			session['latest_date'] = todate
			session['latest_time'] = totime
			
			fromprice = request.form['fromprice']
			toprice = request.form['toprice']
			session['fromprice'] = fromprice
			session['toprice'] = toprice

			from_yyyy = int(fromdate[0:4])
			from_mm = int(fromdate[5:7])
			from_dd = int(fromdate[8:10])
			to_yyyy = int(todate[0:4])
			to_mm = int(todate[5:7])
			to_dd = int(todate[8:10])
			from_hh = int(fromtime[0:2])
			from_mts = int(fromtime[3:5])
			to_hh = int(totime[0:2])
			to_mts = int(totime[3:5])
			from_sec = int('00')
			to_sec = int('59')
			from_mill = 1
			to_mill = 999
			from_datestamp = datetime(from_yyyy,from_mm,from_dd,from_hh,from_mts, from_sec, from_mill)
			to_datestamp = datetime(to_yyyy,to_mm,to_dd,to_hh,to_mts, to_sec,to_mill)
			#print(from_datestamp, to_datestamp)
			if fromprice == '0.0' or  toprice == '0.0':
				found_rec = list(Prices.find({'PriceTimeStamp': { '$gte': from_datestamp, '$lte': to_datestamp }, 'Pair': sel_pair, 'ExchangeName': sel_exchange}).sort("PriceTimeStamp", 1))
			else:
				search_from_price = float(fromprice)
				search_to_price = float(toprice)
				found_rec = list(Prices.find({'PriceTimeStamp': { '$gte': from_datestamp, '$lte': to_datestamp }, 'Pair': sel_pair, 'ExchangeName': sel_exchange, 'Last': { '$gte': search_from_price, '$lte': search_to_price }, 'Ask': { '$gte': search_from_price, '$lte': search_to_price }, 'Bid': { '$gte': search_from_price, '$lte': search_to_price }}).sort("PriceTimeStamp", 1))
			#print("found rec",found_rec)
			timesales_table = []
			prev_timestamp = 0
			for rec in found_rec:
				time_sales_row = []
				
				if prev_timestamp != rec.get('PriceTimeStamp'):
					time_sales_row.append(rec.get('PriceTimeStamp'))
					time_sales_row.append(rec.get('Bid'))
					time_sales_row.append(rec.get('Ask'))
					time_sales_row.append(rec.get('Last'))
					timesales_table.append(time_sales_row)
					prev_timestamp = rec.get('PriceTimeStamp')
				#print(time_sales_row)
			#print(timesales_table)
			timesales_table.sort(key=lambda row: (row[0]))
			#res_timesales_table = np.unique(np.array(timesales_table))
			session['timesales_table'] = timesales_table
			datadetails = sel_exchange+" "+sel_pair+" From: "+fromdate+" "+fromtime+" To: "+todate+" "+totime
			if fromprice != '0.0' or  toprice != '0.0':
				datadetails = datadetails + " Between Prices "+fromprice+" And "+toprice
			session['datadetails'] = datadetails
		if request.form['ts_submit_button'] == 'Clear':
			session['exchangelist'] = exchangelist
			session['earliest_date'] = early_date
			session['earliest_time'] = early_time
			session['latest_date'] = latest_date
			session['latest_time'] = latest_time

			session['fromprice'] = 0.0
			session['toprice'] = 0.0
			session['timesales_table'] =[]
			session['datadetails'] = ''

	return render_template('timesales.html')

@ServerBank.route('/getlist')
def getlist():
	contactlist = ['9840217314', '9962072326', '8248406837']
	payerphone = "8939499757"
	return '%s' %''
'''
@ServerBank.route('/cminerinvoice/<invoicedetails>', methods=['GET', 'POST'])
def make_cminer_invoice(invoicedetails):
	global staticpath
	staticpath = "/ServerBank/Scripts/static/"
	#print(invoicedetails)
	json_invoicedetails = json.loads(invoicedetails)
	#print(json_invoicedetails)
	#print(json_invoicedetails['cminer_inv_customer_id'])
	#return '%s' %json_invoicedetails
	#if empty key values
	digits = "0123456789"
	empty_value = ""
	for i in range(5) :
		empty_value += digits[math.floor(random.random() * 10)]
	cminer_inv_date = 'Nil' 
	cminer_inv_customer_id = 'RndVal'+empty_value
	cminer_inv_order = 'RndVal'+empty_value
	cminer_inv_customer_name = ''
	cminer_inv_phone = ''
	cminer_inv_email = 'info@kappsoft.com'
	cminer_inv_gst = ''
	cminer_inv_qty = '0'
	cminer_inv_rate = '0'
	cminer_inv_total = '0'
	cminer_inv_grand_total = '0'
	#
	try:
		cminer_inv_date = json_invoicedetails['cminer_inv_date'] 
		cminer_inv_customer_id = json_invoicedetails['cminer_inv_customer_id'] 
		cminer_inv_order = json_invoicedetails['cminer_inv_order'] 
		cminer_inv_customer_name = json_invoicedetails['cminer_inv_customer_name'] 
		cminer_inv_phone = json_invoicedetails['cminer_inv_phone'] 
		cminer_inv_email = json_invoicedetails['cminer_inv_email'] 
		cminer_inv_gst = json_invoicedetails['cminer_inv_gst'] 
		cminer_inv_qty = json_invoicedetails['cminer_inv_qty'] 
		cminer_inv_rate = json_invoicedetails['cminer_inv_rate'] 
		cminer_inv_total = json_invoicedetails['cminer_inv_total'] 
		cminer_inv_tax = json_invoicedetails['cminer_inv_tax'] 
		cminer_inv_grand_total = json_invoicedetails['cminer_inv_grand_total'] 
	except KeyError:
		pass

	session['cminer_email'] = cminer_inv_email
	pdf = FPDF('P', 'pt', 'A4')
	pdf.add_page()
	pdf.image( 'cminer-invoice.png',x = 33, y = 852-820, w = 0, h = 0, type = 'PNG')
	#408 774 552 785  Original - Customer Copy
	pdf.set_font("Times", "B", 9)
	pdf.set_xy(408, 852-774)
	pdf.multi_cell(w=150, h = 11, txt ='Original - Customer Copy', align = 'L')
	#43  704 151 723  Tax Invoice
	pdf.set_font("Times", "B", 22)
	pdf.set_text_color(0, 162, 255)
	pdf.set_xy(33, 852-691)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=210, h = 11, txt ='T a x   I n v o i c e', align = 'L')
	#
	pdf.set_font("Times", "B", 9)
	pdf.set_text_color(0, 0, 0)

	pdf.set_xy(33, 852-673)
	ypos = pdf.get_y()
	pdf.multi_cell(w=155, h = 11, txt ='Cminer Private Limited', align = 'L')
	#
	pdf.set_xy(33, 852-660)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=210, h = 11, txt ='No. 164/4 (935/4), Periyar E V R Salai,', align = 'L')
	pdf.set_xy(378, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=150, h = 11, txt ='PAN No. : AABCZ8466B', align = 'L')
	#
	pdf.set_xy(33, 852-649)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=210, h = 11, txt ='Flowers Road Perambur Purasawalkam', align = 'L')
	pdf.set_xy(378, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=150, h = 11, txt ='GSTIN: ', align = 'L')
	#
	pdf.set_xy(33, 852-639)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=210, h = 11, txt ='Chennai - 600084', align = 'L')
	pdf.set_xy(378 , ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=150, h = 11, txt ='CIN No : U72900TN2021PTC147713  ', align = 'R')
	#
	#
	pdf.set_font("Times", "B", 10)
	pdf.set_text_color(0, 0, 0)
	pdf.set_xy(33, 852-606)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.set_text_color(1, 1, 1)
	pdf.set_fill_color(255, 0, 0)
	pdf.multi_cell(w=126, h = 30, txt ='Date:'+cminer_inv_date,  border = "LRBT",align = 'c')
	pdf.set_xy(159, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=200, h = 30, txt ='Customer ID :'+cminer_inv_customer_id, border = "LRBT",align = 'c')
	pdf.set_xy(359, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=170, h = 30, txt ='Order No :'+cminer_inv_order, border = "LRBT",align = 'c')
	#
	#
	pdf.set_font("Times", "B", 10)
	pdf.set_text_color(0, 0, 0)
	pdf.set_xy(31, 852-559)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=210, h = 18, txt ='Bill To : ', align = 'L')
	pdf.set_xy(31, ypos+18)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=150, h = 18, txt ='Name :'+cminer_inv_customer_name, align = 'L')
	pdf.set_xy(31, ypos+18)
	ypos = pdf.get_y()
	xpos = pdf.get_x() 
	pdf.multi_cell(w=150, h = 18, txt ='Phone Number :'+cminer_inv_phone, align = 'L')
	pdf.set_xy(31, ypos+18)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=250, h = 18, txt ='Email Id :'+cminer_inv_email, align = 'L')
	pdf.set_xy(31, ypos+18)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=250, h = 18, txt ='GSTIN :'+cminer_inv_gst, align = 'L')
	#

	#
	pdf.set_font("Times", "B", 12)
	pdf.set_text_color(0, 0, 0)
	pdf.set_xy(33, 852-473)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.set_fill_color(0, 255, 239)
	pdf.multi_cell(w=126, h = 48, txt ='Description', border = "LRBT",align = 'c',fill= True)
	pdf.set_xy(159, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=99, h = 48, txt ='Quantity in TH', border = "LRBT",align = 'R',fill= True)
	pdf.set_xy(258, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=127, h = 48, txt ='Rate per TH ', border = "LRBT",align = 'R',fill= True)
	pdf.set_xy(385, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=150, h = 48, txt ='Total Amount  ', border = "LRBT",align = 'R',fill= True)
	#
	pdf.set_font("Times", "B", 9)
	pdf.set_text_color(0, 0, 0)

	pdf.set_xy(33, 852-436)
	ypos = pdf.get_y()
	xpos = pdf.get_x()

	pdf.multi_cell(w=126, h = 35, txt ='Share Cloud Mining Of BTC', border = "LRB",align = 'c')
	#
	pdf.set_xy(159, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=99, h = 35, txt =cminer_inv_qty, border = "LRB",align = 'R')
	pdf.set_xy(258, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=127, h = 35, txt =cminer_inv_rate, border = "LRB",align = 'R')
	pdf.set_xy(385, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=150, h = 35, txt =cminer_inv_total, border = "LRB",align = 'R')
	#
	pdf.set_xy(258, 852-390)
	ypos = pdf.get_y()
	pdf.multi_cell(w=127, h = 30, txt ='Applied Tax  ', border = " ",align = 'c')

	pdf.set_xy(258, 852-378)
	ypos = pdf.get_y()
	pdf.multi_cell(w=127, h = 30, txt ='(9% CSGT + 9% SGST) ', border = " ",align = 'c')
	pdf.set_xy(385, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=150, h = 40, txt =cminer_inv_tax, border = " ",align = 'R')
	pdf.set_xy(258, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=127, h = 50, txt ='HSN Code : 960899', border = " ",align = 'L')
	#

	pdf.set_xy(258, 852-342)
	ypos = pdf.get_y()
	pdf.set_fill_color(0, 255, 239)
	pdf.multi_cell(w=127, h = 37, txt ='Total Invoice Value  ', border = "LRBT",align = 'c', fill = True)
	pdf.set_xy(385, ypos)
	ypos = pdf.get_y()
	pdf.multi_cell(w=150, h = 37, txt =cminer_inv_grand_total, border = "LRBT",align = 'R',  fill = True)

	#
	pdf.set_xy(33 , 852-187)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=127, h = 37, txt ='(E & O.E. )  ', align = 'L')
	pdf.set_xy(33, 852-176)
	ypos = pdf.get_y()
	pdf.multi_cell(w=150, h = 37, txt = '(Subject to Realization)' , align = 'L')
	#
	pdf.set_xy(378 , 852-93)
	ypos = pdf.get_y()
	xpos = pdf.get_x()
	pdf.multi_cell(w=127, h = 11, txt ='For Cminer Private Limited  ', align = 'L')
	pdf.set_xy(378, 852-81)
	ypos = pdf.get_y()
	pdf.set_font("Times", "", 7)
	pdf.multi_cell(w=150, h = 11, txt = '(Authorized Signatory)' , align = 'L')
	pdf.set_xy(159, 852-79)
	ypos = pdf.get_y()
	pdf.multi_cell(w=200, h = 11, txt = '[This is a computer generated invoice and does not require signature]' , align = 'L')
	cminer_pdf_file = cminer_inv_customer_id+'_'+cminer_inv_order+'.pdf'
	session['mess_subject'] = 'Invoice from CMiner for Customer Id:'+cminer_inv_customer_id+" For Order Id:"+cminer_inv_order
	session['messtext'] = "Dear "+cminer_inv_customer_name+",\n Please find attached Invoice for Customer Id:"+cminer_inv_customer_id+" For Order Id:"+cminer_inv_order
	session['cminer_pdf_file'] = cminer_pdf_file
	pdffile_with_path = staticpath+cminer_pdf_file
	session['pdffile_with_path'] = pdffile_with_path
	pdf.output(pdffile_with_path)
	return redirect(url_for('show_cminer_invoice'))

@ServerBank.route('/show_cminer_invoice', methods=['GET', 'POST'])
def show_cminer_invoice():
	if request.method == 'POST':
		if request.form['submit_button'] == 'Download zip':
			zipname = request.form['zipname']
			zipname = zipname+'.zip'
			with zipfile.ZipFile(zipname,'w',  zipfile.ZIP_DEFLATED) as zip:
					zip.write(session['pdffile_with_path'])
			zip.close()
			return send_file(zipname)
		if request.form['submit_button'] == 'Exit':
			return '%s' %'Thanks'
		if request.form['submit_button'] == 'Send mail':
			send_the_mail(session['cminer_email'], session['pdffile_with_path'], session['messtext'], session['mess_subject'] )
	return render_template('show_cminer_invoice.html')
'''

@ServerBank.route('/emaraldbank/api', methods=['GET', 'POST'])
def embankapi():
	return render_template('ebankapi.html')

@ServerBank.route('/emarald_hotel_feed_back/<grc>', methods=['GET', 'POST'])
def emarald_hotel_feed_back(grc):
	session['grc'] = grc
	EmaraldHotel_dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
	EmaraldHotels_db = EmaraldHotel_dbclient["EmaraldHotels"]
	CheckIn = EmaraldHotels_db["CheckIn"]
	nogrc = False
	contacted_flag = False
	session['nogrc'] = False 
	session['contacted_flag'] = False
	findgrc = list(CheckIn.find({'GRC': grc}))
	if len(findgrc) == 0:
		session['nogrc'] = True
		nogrc = True
		return '%s' %'No Such GRC number, sorry!!'
	else:
		for grcrec in findgrc:
			contacted_flag = grcrec.get("Contacted")
			session['contacted_flag'] = contacted_flag
			print('contacted_flag',contacted_flag)
			if not(contacted_flag):
				if request.method == 'POST':
					inputgrc = request.form['inputgrc']
					reception_rating = request.form['reception_rating']
					room_rating = request.form['room_rating']
					food_rating = request.form['food_rating']
					staff_rating = request.form['staff_rating']
					overall_rating = (int(reception_rating) + int(room_rating) + int(food_rating) + int(staff_rating))/4.0
					guest_comments = request.form['comments_area']
					guestquery = { "GRC" : inputgrc }
					now = datetime.now()
					guest_feedback = { "$set":
								{ 
								 "FeedbackTimeStamp" : now,
								 "Reception_rating" : reception_rating,
								 "Room_rating" : room_rating,
								 "Staff_rating" : staff_rating,
								 "Food_rating" : food_rating,
								 "Overall_rating" : overall_rating,
								 "Guest_comments" : guest_comments,
								 "Contacted" : True
								}
							}
					feedback_result = CheckIn.update_one(guestquery, guest_feedback)
					return '%s' %'Thank you for your feedback of Emarald Hotels'
				else:
					return render_template('fback.html', inpgrc = grc)
			else:
				return '%s' %'Already given your feedback, thank you'



@ServerBank.route('/emaraldbankapi/<apistring>')
def emaraldbankapi(apistring):
	global ServerBank_dbclient, ServerBank_db, EmaraldBank_users, EmaraldBank_customers, EmaraldBank_Transactions
	global findcust, customer_phone, otpdone, amount_needed_fromapi, present_balance
	urlstr = request.url
	print(urlstr)
	session['urlstring'] = urlstr
	session['apistring'] = apistring
	if session['continue_api']  :
		#check balance and send otp
		urlstr_array = apistring.split('~')
		api_request_type = urlstr_array[0]
		if api_request_type == "IssueFrom":
			custmobile_fromapi = urlstr_array[3]
			amount_needed_fromapi = float(urlstr_array[5])
			print(custmobile_fromapi)
			findcust = EmaraldBank_customers.find({'Customer_phone': '8939499757'})
			findcust = list(findcust)
			#print(findcust)
			#print("hello after findcust")
			if len(findcust) != 0:
				for rec in findcust:
					customer_phone = rec.get("Customer_phone")
					customer_sbaccountnumber = rec.get("Customer_SBAccountNumber")
					print(customer_sbaccountnumber)
					latest_transaction = list(EmaraldBank_Transactions.find({"Customer_SBAccountNumber" : customer_sbaccountnumber }).sort([('TransactionTimeStamp', -1)]).limit(1))
					for transrec in latest_transaction:
						present_balance = float(transrec.get('AccountBalance'))
						if present_balance > amount_needed_fromapi:
							otpdone = False
							return redirect(url_for('otpdemo'))
						else:
							return '%s' %'Insufficient Balance '
	return redirect(url_for('issuingbank1'))

@ServerBank.route('/issuingbank1', methods=['GET', 'POST'])
def issuingbank1():
	session['continue_api'] = False
	if request.method == 'POST':
		session['continue_api'] = True
		return redirect(url_for('emaraldbankapi', apistring = session['apistring']))
	return render_template('issuingbank1.html')

@ServerBank.route('/otpdemo', methods=['GET', 'POST'])
def otpdemo():
	global findcust, customer_phone, EmaraldBank_customers, otpdone, amount_needed_fromapi, present_balance
	if not otpdone:
		digits = "0123456789"
		OTP = ""
		for i in range(6) :
			OTP += digits[math.floor(random.random() * 10)]
		print(OTP)
		session['otpsent'] = str(OTP)
		#findcust = list(EmaraldBank_customers.find({'Customer_phone': customer_phone}))
		#if len(findcust) != 0:
		now = datetime.now()
		print(customer_phone)
		rquery = { "Customer_phone" : customer_phone }
		newotpval = { "$set": 
						{ 
						 "otp" : str(OTP),
						 "OtpTimeStamp" : now
						}
				}
		result = EmaraldBank_customers.update_one(rquery, newotpval)
		#print(result.acknowledged)
		#print(result.modified_count)
		#print(result.matched_count)
		otpdone = True
	if request.method == 'POST':
		entered_otp = request.form['typedotp']
		print('entered otp', entered_otp)
		findcust = list(EmaraldBank_customers.find({'Customer_phone': customer_phone}))
		if len(findcust) != 0:
			for rec in findcust:
				customer_id = rec.get('Customer_id')
				print(customer_id)
				if rec.get('otp') == str(entered_otp):
					session['incorrectotp'] = False
					#update transaction, bank ledger and pgledger
					digits = "0123456789"
					randomid = ""
					for i in range(10) :
							randomid += digits[math.floor(random.random() * 10)]
					session['randomid'] = randomid
					balance_after_transaction = present_balance - amount_needed_fromapi
					session['previous_balance'] = present_balance
					session['debitamount'] = amount_needed_fromapi
					session['newbalance'] = balance_after_transaction
					now = datetime.now()
					#insert new record to issuing bank customer transaction
					newtransaction = {
						"Customer_Id" : customer_id,
						"Customer_SBAccountNumber" : rec.get('Customer_SBAccountNumber'),
						"TransactionTimeStamp": now, 
						"Narration" : "Debtor To Payment Gateway transaction "+randomid,
						"DebitAmount" : amount_needed_fromapi,
						"CreditAmount" : 0,
						"AccountBalance" : balance_after_transaction
					}
					newtransentry = EmaraldBank_Transactions.insert_one(newtransaction)
					#return '%s' %'Balance updated'
					return redirect(url_for('afterotp'))
				else:
					session['incorrectotp'] = True
					print(rec.get('otp'))
					print('incorrect otp')
	return render_template('otpdemo.html')


@ServerBank.route('/credited' , methods=['GET', 'POST'])
def credited():
	return render_template('credited.html')

@ServerBank.route('/kappsoftbankapi/<creditapistring>')
def kappsoftbankapi(creditapistring):
	global ServerBank_dbclient, ServerBank_db, KappsoftBank_users, KappsoftBank_customers, KappsoftBank_Transactions
	global request_id
	crediturlstr = request.url
	session['crediturlstr'] = crediturlstr
	print(crediturlstr)
	if session['continue_creditapi']  :
		crediturlstr_array = creditapistring.split('~')
		api_request_type = crediturlstr_array[0]
		print(crediturlstr_array[0])
		print(crediturlstr_array[1])
		print(crediturlstr_array[2])
		print(crediturlstr_array[3])
		print(crediturlstr_array[4])
		print(crediturlstr_array[5])
		if api_request_type == "CreditTo":
			cust_mobile_from_api = crediturlstr_array[1]
			amount_to_credit = crediturlstr_array[3]
			transaction_id = crediturlstr_array[5]
			findcust = KappsoftBank_customers.find({'Customer_phone': cust_mobile_from_api})
			findcust = list(findcust)
			print(findcust)
			#print(findcust)
			#print("hello after findcust")
			if len(findcust) != 0:
				for rec in findcust:
					customer_phone = rec.get("Customer_phone")
					customer_sbaccountnumber = rec.get("Customer_SBAccountNumber")
					customer_id = rec.get("Customer_id")
					print(customer_sbaccountnumber)
					latest_transaction = list(KappsoftBank_Transactions.find({"Customer_SBAccountNumber" : customer_sbaccountnumber }).sort([('TransactionTimeStamp', -1)]).limit(1))
					print(latest_transaction)
					for transrec in latest_transaction:
						present_balance = float(transrec.get('AccountBalance'))
						balance_after_transaction = present_balance + float(amount_to_credit)
						session['balance_before_credit'] = present_balance
						session['creditamount'] = float(amount_to_credit)
						session['newbalance'] = balance_after_transaction
						now = datetime.now()
						newtransaction = {
								"Customer_Id" : customer_id,
								"Customer_SBAccountNumber" : rec.get('Customer_SBAccountNumber'),
								"TransactionTimeStamp": now, 
								"Narration" : "Creditor By Payment Gateway transaction "+transaction_id,
								"DebitAmount" : 0,
								"CreditAmount" : amount_to_credit,
								"AccountBalance" : balance_after_transaction
							}
						newtransentry = KappsoftBank_Transactions.insert_one(newtransaction)
						#update the send_requests record in pg
						'''
						guestquery = { "GRC" : inputgrc }
						now = datetime.now()
						guest_feedback = { "$set": 
											{ 
											 "FeedbackTimeStamp" : now,
											 "Reception_rating" : reception_rating,
											 "Room_rating" : room_rating,
											 "Staff_rating" : staff_rating,
											 "Food_rating" : food_rating,
											 "Overall_rating" : overall_rating,
											 "Guest_comments" : guest_comments,
											 "Contacted" : True
											}
								}
						feedback_result = CheckIn.update_one(guestquery, guest_feedback)
						pg_send_requests
						'''
						print('transaction updated in acquring bank')
						return redirect(url_for('credited'))
						#return render_template('credited.html')
	return redirect(url_for('acquiringbank1'))

@ServerBank.route('/afterotp', methods=['GET', 'POST'])
def afterotp():
	if request.method == 'POST':
		acquiringbank_credit_apistring = "CreditTo~"+session['sendto']+"~Amount~"+session['amounttosend']+"~TransactionId~"+session['randomid']
		session['acquiringbank_credit_apistring'] = acquiringbank_credit_apistring
		session['continue_creditapi'] = False
		return  redirect(url_for('kappsoftbankapi', creditapistring = session['acquiringbank_credit_apistring']))
	return render_template('afterotp.html')

@ServerBank.route('/acquiringbank1', methods=['GET', 'POST'])
def acquiringbank1():
	print("in acquiringbank1")
	session['continue_creditapi'] = False
	if request.method == 'POST':
		session['continue_creditapi'] = True
		return redirect(url_for('kappsoftbankapi', creditapistring = session['acquiringbank_credit_apistring'] ))
	return render_template('acquiringbank1.html')


@ServerBank.route('/sendmoney', methods=['GET', 'POST'])
#Later: Include correct payer details, unique request id while writing to database
def sendmoney():
	global request_id
	dbopen()
	global pg_send_requests
	contactlist = ['9840217314', '9962072326', '8248406837']
	payerphone = "8939499757"
	session['contactlist'] = contactlist
	session['continue_api'] = False
	if request.method == 'POST':
		session['sendto'] = request.form['sendto'] 
		session['amounttosend'] = request.form['amounttosend']
		request_timestamp = datetime.now()
		unique_string = payerphone + str(request_timestamp)
		request_id = sha256(unique_string.encode('utf-8')).hexdigest()
		pg_send_record = {
			"Request_id" : request_id,
			"RequestTimestamp" : request_timestamp,
			"PayerCustomerPhone" : payerphone,
			"PayeeCustomerPhone" : session['sendto'],
			"AmountToSend" : session['amounttosend'],
			"SendingSuccessful" : False
		}
		newrequestrecord = pg_send_requests.insert_one(pg_send_record)
		#session['otptosend'] = request.form['otptosend']
		
		#print(session.get('otptosend'))
		apistring = "IssueFrom~"+"Shiju"+"~mobile~"+ "8939499757"+"~Amount~"+session['amounttosend']
		session['apistring'] = apistring
		return  redirect(url_for('emaraldbankapi', apistring = session['apistring']))
	else:
		return render_template('send.html')



@ServerBank.route('/sbmenu')
def sbmenu():
	#added Attendance regularisation as an option item in menu 13 Dec 2022
	return render_template('sbmenu.html')


@ServerBank.route('/sbafterlogin/')
def sbafterlogin():
		global ServerBank_dbclient, ServerBank_db, EmaraldBank_users, environ
		dbopen()
		
		gotname = session.get("username")
		gotpassword = session.get("password")
		
		global environ
		finduser = EmaraldBank_users.find({"User_id" : gotname})
		finduserlist = list(finduser)
		if len(finduserlist) != 0:
			for re_cord in finduserlist:
				dbpassword = re_cord.get("User_password")
				mykey = re_cord.get("User_passkey")
				decoded = cryptocode.decrypt(dbpassword,mykey)
				if decoded == gotpassword:
					error = False
					session['error'] = error
					session['password'] =""
					return redirect(url_for('sbmenu'))
				else:
					error = True
					session['error'] = error
					return  redirect(url_for('sb'))
			#endfor
		else:
			error = True
			session['error'] = error
			return redirect(url_for('sb'))

@ServerBank.route('/sb', methods=['GET', 'POST'])
def sb():
	error = None
	if request.method == 'POST':
		session['username'] = request.form['username'] 
		session['password'] = request.form['password']
		return redirect(url_for('sbafterlogin'))
	return render_template('sb.html')

def is_number(n):
	try:
		float(n)   # Type-casting the string to `float`.
				   # If string is not a valid `float`, 
				   # it'll raise `ValueError` exception
	except ValueError:
		return False
	return True

@ServerBank.route('/hotelfb', methods=['GET', 'POST'])
def hotelfb():
	#os.system("D:/mailreader/mailreader.exe")
	return  redirect(url_for('emarald_hotel_feed_back', grc = 'CalicutGRC000'))


@ServerBank.route('/logout', methods = ['POST', 'GET'])
def logout():
	ServerBank_dbclient.close()
	session.clear()
	retvalue = "GoodBye from Server Bank Back Office"
	return  '%s' %retvalue





if __name__ == '__main__':
	#from waitress import serve
	#import logging
	#print("ServerBank is now running through Waitress WSGI")
	#serve(ServerBank, host="0.0.0.0", port=443)

	ServerBank.run(host='0.0.0.0', port=5002, debug = True)
	#ServerBank.run(debug=True)




# Using the negative index
#db.student.find().sort({_id: -1}).limit(2)
