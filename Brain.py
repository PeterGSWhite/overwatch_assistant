from sphinxbase import sphinxbase
import win32com.client as comclt
wsh= comclt.Dispatch("WScript.Shell")

# Keys are phrases actively listened for. The tuples are (overwatch_keybind, phrase_sensitivity)
command_bindings = {
    'attack with me': ['m', 1],
    "let's defend": ['b', 1],
    'after my count': ['{BACKSPACE}', 1],
    'fall back': ['l', 1],
    'go go go': ['[', 1],
    "i'm going in": [']', 1],
    'goodbye': ["'", 1],
    'incoming': ['#', 1],
    'help me': [',', 1],
    'negative': ['.', 1],
    "on my way": ['/', 1],
    'attack now': ['=', 1],
    'push forward': ['j', 1],
    "i'm ready": ['-', 1],
    'sorry': ['0', 1],
    "i'm with you": ['9', 0.9],
    'affirmative': ['8', 1],
    "you're welcome": ['7', 1],
    'hello there': ['3', 1],
    'need healing': ['4', 0.9],
    'group up': ['5', 1],
    'have ultimate': ['z', 1],
    'understood': ['g', 1],
    'thanks': ['6', 1]
}
# keys match keys in command_bindings. Values are new phrase: sensitivities which will match the same keybind
command_extensions = {
    'after my count': {"on my count": 1},
    'go go go': {"let's go": 1},
    "i'm going in": {"going in": 1},
    'incoming': {"they're pushing": 1},
    'help me': {'save me': 1},
    'negative': {'no no no': 0.9, 'no way': 1},
    'push forward': {'keep pushing': 0.9, 'push push push':0.9},
    "i'm with you": {"i with you": 0.9},
    'affirmative': {'yeah ok': 1, 'yeah sure': 0.9, 'sure thing': 0.9},
    "you're welcome": {'no problem': 1},
    'hello there': {"what's up": 1},
    'need healing': {'heal me please': 1, 'healing please': 1, 'i need healing': 0.9},
    'group up': {'regroup': 1, "don't feed": 1},
    'have ultimate': {'my ultimate s ready': 0.9, 'my ultimate ready': 0.9, 'have my ultimate': 1, 'my ultimate s charging': 0.9, 'my ultimate charging': 0.9},
    'thanks': {'thank you': 1, 'cheers mate': 1}
}
update_dict = {}
for base_phrase in command_bindings:
    key_bind = command_bindings[base_phrase][0]
    for sub_phrase, sensitivity in command_extensions.get(base_phrase, {}).items():
        update_dict[sub_phrase] = [key_bind, sensitivity]
command_bindings.update(update_dict)

def think(heard):
    print("Athena thinks you said '", heard, "'")
    heard = heard.strip()
    multiple = heard.split('  ')
    if multiple:
        print('multiple matches:', multiple)
        binds = set()
        for h in multiple:
            binds.add(command_bindings[h.strip()][0])
        if len(binds) == 1:
            wsh.SendKeys(binds.pop()) # send the keybind
    elif heard in command_bindings:
        print(heard)
        wsh.SendKeys(command_bindings[heard][0]) # send the keybind