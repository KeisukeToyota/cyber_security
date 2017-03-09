import sys
import socket
import getopt
import threading
import subprocess

# グローバル変数の定義
listen = False
command = False
upload = False
excute = ''
tearget = ''
upload_destination = ''
port = 0

def usage():
    print('BHP Net Tool\n\n'
          'Usage: bhnet.py -t target_host -p port\n'
          '-l --listen ')

