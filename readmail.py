# $language = "Python3"
# $interface = "1.0"

#pip install pywin32

import win32com.client

import os
from datetime import datetime, timedelta



def Main():

	outlook = win32com.client.Dispatch('outlook.application')
	mapi = outlook.GetNamespace("MAPI")
	"""
	for account in mapi.Accounts:
		print(account.DeliveryStore.DisplayName)
	"""
	inbox = mapi.GetDefaultFolder(6).Folders["Sites"]
	messages = inbox.Items
	for message in messages:
		if message.Unread == True:
			subject = message.Subject
			#reply = message.ReplyAll()
			#reply.Body = "test"
			#reply.Send()
			message.Display()
			message.Display == False
			#message.Unread == False
			
			

	#message = messages.GetLast()
	#subject = message.Subject
	
	site = subject.split(" ")
	for i in range (0, len(site)):
		sitename0 = site[i].strip()
		if sitename0.startswith("L") == True:
			SiteName = sitename0
	
	print(SiteName)
	#crt.Dialog.MessageBox(str(SiteName))

	#os.system('cmd /c "SecureCRT.exe /Script C:\\Users\\ahmed.hasanein\\Desktop\\session.py"')

	


Main()