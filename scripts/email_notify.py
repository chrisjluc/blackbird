import time
import subprocess
import select
import sys
import os

from consts import *

ENTRY_FOUND = 'ENTRY FOUND'
ENTRY_LINES = 15

EXIT_FOUND = 'EXIT FOUND'
EXIT_LINES = 19

status = None
lines = []

def send_email():
    subject = status
    message = ''.join(lines)
    command = 'sendEmail -o tls=yes -f {} -t {} -s {} -xu {} -xp {} -u "{}" -m "{}"'.format(
            SENDER_EMAIL, RECEIVER_EMAIL, SMTP_SERVER, SENDER_EMAIL, SENDER_PASSWORD, subject, message)
    os.system(command)

def check_and_set_status(code, line):
    global status
    if not status and code in line:
       status = code

def check_and_append_line(code, num_lines, line):
    global status
    global lines
    if status == code:
        lines.append(line)
        if len(lines) >= num_lines:
            send_email()
            lines = []
            status = None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ' + sys.argv[0] + '[log_file]')
        sys.exit(1)

    log_file = sys.argv[1]

    f = subprocess.Popen(['tail', '-F', log_file],\
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = select.poll()
    p.register(f.stdout)

    while True:
        if p.poll():
            line = f.stdout.readline().decode('utf-8')

            check_and_set_status(ENTRY_FOUND, line)
            check_and_append_line(ENTRY_FOUND, ENTRY_LINES, line)

            check_and_set_status(EXIT_FOUND, line)
            check_and_append_line(EXIT_FOUND, EXIT_LINES, line)

