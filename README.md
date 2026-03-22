# gtermview - tiny tui github viewer written on python

## installation
Linux/MacOS(windows not supported):
1. clone this repo:
```bash
git clone https://github.com/mxcoderr/gtermview
pip3 install rich requests
cd gtermview
```
2.add to Your PATH file with bash code(gtermview.sh):
```bash
# on zsh
chmod +x gtermview.sh && \
DIR="$PWD" && \
grep -qxF "export PATH=\"$DIR:\$PATH\"" ~/.zshrc || \
echo "export PATH=\"$DIR:\$PATH\"" >> ~/.zshrc && \
source ~/.zshrc
# on bash
chmod +x gtermview.sh && \
DIR="$PWD" && \
grep -qxF "export PATH=\"$DIR:\$PATH\"" ~/.bashrc || \
echo "export PATH=\"$DIR:\$PATH\"" >> ~/.bashrc && \
source ~/.bashrc
```
## commands

1.View Profile
'''
gtermview.sh <username> # example: gtermview.sh mxcoderr
'''

2.View Profile and save in json file

'''
gtermview.sh <username> --json # example gtermview.sh mxcoderr --json
'''
