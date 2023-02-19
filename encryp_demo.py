import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from virtru_tdf3_python import Client, Policy, EncryptFileParam, LogLevel, Protocol


# SMTP Variables
smtp_from_address = "sender@gmail.com"
smtp_to_address = "receiver@gmail.com"

fromaddr="sender@gmail.com"
toaddr="receiver@gmail.com"
password="password"
# Virtru Variables
virtru_appid = "4f3aa9c5-1eb3-4c6e-962c-ffb720091f19"
virtru_owner = "mehendibutwal@gmail.com"
# File Variables
file_name_tdf = "cron_text.txt"
file_path_plain="cron_text.txt"
file_path_tdf="cron_text.txt"



client = Client(owner=virtru_owner, app_id=virtru_appid)
policy = Policy()
policy.share_with_users([smtp_to_address,smtp_cc_address])
param = EncryptFileParam(in_file_path=file_name_plain,
                         out_file_path=file_name_tdf)
param.set_policy(policy)
client.encrypt_file(encrypt_file_param=param)



msg = MIMEMultipart()
msg['From'] = smtp_from_address
msg['To'] = smtp_to_address
msg['CC'] = smtp_cc_address
msg['Subject'] = "Test Email"
body = "Message Body"
msg.attach(MIMEText(body, 'plain'))
attachment = open(file_name_tdf, "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
attachment_disposition = "attachment; filename= {}".format(filename)
p.add_header('Content-Disposition', attachment_disposition)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 465)
s.starttls()
server.login(fromaddr,password)
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()
