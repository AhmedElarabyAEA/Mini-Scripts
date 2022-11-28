# $language = "Python3"
# $interface = "1.0"

#pip install netmiko
from netmiko import ConnectHandler, redispatch
import time


def Main():

	connect_info = {
		"device_type":'linux',
		"host": "213.158.187.244",
		"port": "9090",
		"username":"ahmed.hasanein",
		"password":"@AhmedAEa102"
	}

	try:
		with ConnectHandler(**connect_info) as conn:
			print("Connection is Successful")
			conn.write_channel("telnet 10.45.23.151\n")
			time.sleep(1)
			output = conn.read_channel()
			if "Username:" in output:
				conn.write_channel("ahmed.hasanein\n")
			#time.sleep(1)
			output2 = conn.read_channel()
			if "Password:" in output2:
				conn.write_channel("Goto@home3030\n")
			#conn.send_command("ahmed.hasanein",expect_string="Password:")
			#conn.send_command("Goto@home3030",expect_string="#")
			redispatch(conn,device_type='cisco_ios')
			out = conn.send_command("show version")
			print(out)
	except Exception:
		print("Connection is Failed!")


Main()