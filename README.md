# overwatch_assistant

<h3 align="center">OVERWATCH ASSISTANT</h3>

  <p align="center">
    Use your real voice to trigger overwatch voice commands!<br>
    <br/>
  </p>
  
### Video Demonstration
[![Watch the video](https://i9.ytimg.com/vi_webp/XRAZusHod-M/mqdefault.webp?time=1611098400000&sqp=CKDSnYAG&rs=AOn4CLB70DnR7FEl37Ojb72XDObH5hwm3A)](https://www.youtube.com/watch?v=XRAZusHod-M)

### Prerequisites

* Python3.6 (later versions cause install errors with speech_recognition packages - if you can get around this, go for it!)<br>
https://www.python.org/downloads/release/python-368/

### Installation

1. Clone the repo and cd in
```
git clone https://github.com/PeterGSWhite/overwatch_assistant.git
cd overwatch_assistant
```

2. Create venv and install python modules
```
virtualenv --python=python3.6 venv
venv/Scripts/activate
pip install -r requirements.txt
```

3. (optional) Update the phonetic dictionary <br>
```
I updated the pronounciation dictionary to suit my particular British accent.
To use this dictionary, move the .dict file in Dict/ to venv/Lib/site-packages/speech_recognition/pocketsphinx-data/en-US/
You also can choose to leave the original US pronounciations as they are, or change pronounciations to suit yourself
```

### Setting up keybinds
The keybinds can be found in Brain.py<br>
The buttons listed should match your Overwatch settings. Here you can also change what phrases trigger the keypresses.
