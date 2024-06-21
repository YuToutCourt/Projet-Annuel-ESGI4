#!/bin/sh
python3 server_mail.py &
python3 -m http.server 8080
