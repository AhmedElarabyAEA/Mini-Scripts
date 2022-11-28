import math
input_string =(crt.Dialog.Prompt("Enter power readings in mw seperating with space: "))
userList = input_string.split()
x=float(userList[0]) + float(userList[1]) + float(userList[2]) + float(userList[3])
p=float(10*(math.log10(x)))
crt.Dialog.MessageBox(str(p))






