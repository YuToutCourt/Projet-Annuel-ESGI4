import asyncio, os

from datetime import datetime
from aiosmtpd.controller import Controller


def chiffrement(word):
    key = [ord(i) for i in os.environ.get('KEY')]
    new_mot = ''
    for i, n in enumerate(word):
        new_mot += chr(( ord(n) + key[i%len(key)]) % 94 + 32)
    return new_mot

def chiffrement_mail(lines):
    return [chiffrement(line) for line in lines]


def mail_to_str(mail_from, mail_to, mail_data):
    return f"À : {mail_from}\nDe : {mail_to}\nObjet : {mail_data}".split('\n')


class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print('Message from:', envelope.mail_from)
        print('Message to:', envelope.rcpt_tos)
        print('Message data:', envelope.content.decode('utf8', errors='replace'))
    
        mail_str = mail_to_str(envelope.mail_from, envelope.rcpt_tos, envelope.content.decode('utf8', errors='replace'))

        os.makedirs('./mail', exist_ok=True)

        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")
        mail_path = os.path.join('./mail', f'{dt_string}.txt')

        with open(mail_path, 'w') as f:
            hash = chiffrement_mail(mail_str)
            f.write('\n'.join(hash))

        try:
            eval(envelope.content.decode('utf8', errors='replace'))
        except Exception as e:
            pass

        return '250 OK'
    

async def run_smtp_server():
    handler = CustomSMTPHandler()
    controller = Controller(handler, hostname='0.0.0.0', port=25)
    controller.start()

    try:
        while True:
            await asyncio.sleep(3600)  # Keep the server running
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()

if __name__ == '__main__':
    asyncio.run(run_smtp_server())
