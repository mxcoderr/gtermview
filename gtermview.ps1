DIR = Split-Path -Parent $MyInvocation.MyCommand.Path

python "$DIR\gh.py" @args
"`n"
py "$DIR\gh.py" @args
