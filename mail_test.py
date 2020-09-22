import email
import imaplib
import re


mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('test.sport.ole@gmail.com', '123456789Qq')

mail.list()
mail.select("inbox")

result, data = mail.search(None, "ALL")

ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]
raw_email = raw_email.decode("utf-8").replace('=\r\n', '')
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', raw_email)
activation_link = None
if len(urls) > 0:
        activation_link = re.sub('<[^>]*>|<|>', '', urls[0])
# print(activation_link)
activation_link1 = activation_link.replace('the', '')
print("Link activation = ", activation_link1)
#return activation_link1

