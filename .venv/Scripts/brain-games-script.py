#!c:\users\sony\oxana-sh_brain_games\.venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'oxana-sh-brain-games','console_scripts','brain-games'
__requires__ = 'oxana-sh-brain-games'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('oxana-sh-brain-games', 'console_scripts', 'brain-games')()
    )
