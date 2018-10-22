import imaplib
import email
from email.header import Header, decode_header, make_header

user = 'PlexingPython@gmail.com'
password = '<insert password>'
imap_url = 'imap.gmail.com'


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


mail = imaplib.IMAP4_SSL(imap_url)
mail.login(user,password)
mail.select('INBOX')

# result, data = con.fetch(b'3', '(RFC822)')
# raw = email.message_from_bytes(data[0][1])
# print(get_body(raw))

type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    print(num)


# msg = email.message_from_string(raw_email.decode('utf-8'))
# email_subject = msg['subject']
# email_from = msg['from']
# print ('From : ' + email_from + '\n')
# print ('Subject : ' + email_subject + '\n')
# print(msg.get_payload(decode=True))



    for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode('utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                print ('From : ' + email_from + '\n')
                print ('Subject : ' + email_subject + '\n')
                print(msg.get_payload(decode=True))
