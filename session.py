# $language = "Python3"
# $interface = "1.0"

import os
from readmail import SiteName



def Main():

	#strValue = crt.Session.Config.GetOption("Is Session")
	#crt.Dialog.MessageBox(str(strValue))
	#crt.Session.Connect("/SSH2 /PORT 9090 /PASSWORD @AhmedAEa102 ahmed.hasanein@213.158.187.244")
	config = crt.OpenSessionConfiguration("213.158.187.244")
	#crt.Dialog.MessageBox(config.GetOption("Password"))
	crt.Session.Connect("/SSH2 -p 9090 /ENCRYPTEDPASSWORD " + config.GetOption("Password") + " "+config.GetOption("Username")+"@"+config.GetOption("Hostname")+":9090")

	#objTab = object.ConnectInTab()
	#crt.Session.ConnectInTab("/SSH2 213.158.187.244 9090")
	#tab = crt.Session.GetTab()
	#crt.Dialog.MessageBox(tab)
	crt.Screen.WaitForString("~]$")
	crt.Screen.Send(SiteName)


Main()
