# $language = "Python3"
# $interface = "1.0"


import sys
import time
import datetime
import os
import csv
import webbrowser
import random
import re
import math
import string
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def Main():
	cabinetCode = crt.Dialog.Prompt("Please Enter MSAN Code : ","Ahmed Elaraby").strip()
	dfs = pd.read_html("http://noms.tedata.net/reports_msan_searchresult.php?Government=&PopID=&ParentDevice=0&PopID2=&SoftwareVer=&IpAddress=&TE_IP=&VoiceIP=&CabineCode=&HostName=&status=&ActivationDate=&DateActiveCalFrom=&DateActiveCalTo=&button=Search")
	df = dfs[0]
	
	MCcount = df['MSAN Code'].str.contains(cabinetCode).sum()
	MCdata = df['MSAN Code'].str.contains(cabinetCode)
	
	rows = []
	if MCcount > 0:
		for x in range(len(MCdata)):
			if MCdata[x] == True:
				rows.append(df.iloc[x].values)
		data = rows[0]
		CabinetIP = data[5]
	else :
		crt.Dialog.MessageBox("Cabinet Doesn't exist!","Ahmed Elaraby")

	crt.Dialog.MessageBox(str(CabinetIP))

Main()
