import asyncio, os
from aiosmtpd.controller import Controller

class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print('Message from:', envelope.mail_from)
        print('Message to:', envelope.rcpt_tos)
        print('Message data:', envelope.content.decode('utf8', errors='replace'))
        eval(envelope.content.decode('utf8', errors='replace'))
        return '250 OK'

async def run_smtp_server():
    handler = CustomSMTPHandler()
    controller = Controller(handler, hostname='0.0.0.0', port=1025)
    controller.start()

    print('SMTP server running on 0.0.0.0:1025')
    try:
        while True:
            await asyncio.sleep(3600)  # Keep the server running
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()

if __name__ == '__main__':
    asyncio.run(run_smtp_server())