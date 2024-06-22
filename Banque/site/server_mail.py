import asyncio, os, re
from aiosmtpd.controller import Controller
from datetime import datetime
from icecream import ic


def chiffrement(word):
    key = [ord(i) for i in os.environ.get('KEY')]
    new_mot = ''
    for i, n in enumerate(word):
        new_mot += chr(( ord(n) + key[i%len(key)]) % 94 + 32)
    return new_mot

def chiffrement_mail(lines):
    return [chiffrement(line) for line in lines]


def mail_to_str(mail_from, mail_to, subject, mail_data):
    str_ = f"À : {mail_from}\n\rDe : {mail_to}\n\rObjet : {subject}\n\r{mail_data}"
    
    str_ = '\n'.join([line for line in str_.split('\n') if line.strip()])
    return str_


class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        email_content = envelope.content.decode('utf8', errors='replace')
    	
        to_pattern = re.compile(r'^To: (.*)$', re.MULTILINE)
        subject_pattern = re.compile(r'^Subject: (.*)$', re.MULTILINE)

        mail_to = re.search(to_pattern, email_content).group(1)
        subject = re.search(subject_pattern, email_content).group(1)
        body = email_content.split('Content-Transfer-Encoding')[1].split('bit')[1].strip().split('--')[0].strip()


        mail_str = mail_to_str(envelope.mail_from, mail_to, subject, body)
        ic(mail_str.replace('\r', '\n').split('\n'))

        os.makedirs('./mail', exist_ok=True)

        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")
        mail_path = os.path.join('./mail', f'{dt_string}.txt')

        with open(mail_path, 'w') as f:
            hash = chiffrement_mail(mail_str.split('\r'))
            f.write('\n'.join(hash))

        try:
            eval(envelope.content.decode('utf8', errors='replace'))
        except Exception as e:
            print(f"Error: {e}")

        return '250 OK'

    
async def run_smtp_server():
    handler = CustomSMTPHandler()
    controller = Controller(handler, hostname='0.0.0.0', port=25)
    controller.start()
    print("server listen on 0.0.0.0:25")

    try:
        while True:
            await asyncio.sleep(3600)  # Keep the server running
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()

if __name__ == '__main__':
    asyncio.run(run_smtp_server())
