#!c:\users\tckel\desktop\myproject\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'crypto==1.4.1','console_scripts','decrypto'
__requires__ = 'crypto==1.4.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('crypto==1.4.1', 'console_scripts', 'decrypto')()
    )
