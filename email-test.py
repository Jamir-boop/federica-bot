import os
import csv
from imapclient import IMAPClient
from dotenv import load_dotenv
from email import message_from_string

class EmailLogger:
    def __init__(self, server, email, email_password):
        self.server = server
        self.email = email
        self.email_password = email_password
        self.registry_file = 'email_registry.txt'
        self.fetched_ids = self.load_registry()

    def load_registry(self):
        if os.path.exists(self.registry_file):
            with open(self.registry_file, 'r', encoding='utf-8') as file:
                return set(file.read().splitlines())
        return set()

    def update_registry(self, msgid):
        with open(self.registry_file, 'a', encoding='utf-8') as file:
            file.write(f'{msgid}\n')

    def login(self):
        self.server.login(self.email, self.email_password)

    def logout(self):
        self.server.logout()

    def fetch_emails(self, criteria):
        self.server.select_folder('INBOX')
        messages = self.server.search(criteria)
        return self.server.fetch(messages, ['ENVELOPE', 'BODY[]'])

    def decode_content(self, part):
        try:
            return part.get_payload(decode=True).decode('utf-8')
        except UnicodeDecodeError:
            return part.get_payload(decode=True).decode('latin-1')

    def log_emails(self, email_data):
        for msgid, data in email_data.items():
            if str(msgid) in self.fetched_ids:
                continue  # Skip emails that have been fetched already
            filename = f'mail_{msgid}.csv'
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Subject", "Received Date", "Content"])
                envelope = data[b'ENVELOPE']
                raw_email = data[b'BODY[]']
                msg = message_from_string(raw_email.decode())
                content = ''
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            content = self.decode_content(part)
                            break
                else:
                    content = self.decode_content(msg)
                writer.writerow([msgid, envelope.subject.decode(), envelope.date, content])
            self.update_registry(msgid)  # Update the registry with the new email ID

def main():
    load_dotenv()
    email = os.getenv('EMAIL')
    email_password = os.getenv('EMAIL_PASSWORD')
    server = IMAPClient('imap.gmail.com', use_uid=True)

    email_logger = EmailLogger(server, email, email_password)
    email_logger.login()
    email_data = email_logger.fetch_emails(['FROM', 'notificaciones@notificacionesbcp.com.pe'])
    email_logger.log_emails(email_data)
    email_logger.logout()

if __name__ == "__main__":
    main()
