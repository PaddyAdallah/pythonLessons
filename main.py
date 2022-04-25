"""
MIGRATING TO SCRIPTING
def get_commands(vlan, name):
    commands = ['vlan' + vlan, 'name' + name]
    return commands


def push_commands(device, commands):
    print('Connecting to device' + device)
    for cmd in commands:
        print('Sending command' + cmd)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    devices = ['switch1', 'switch2', 'switch3']

    vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
             {'id': '30', 'name': 'WLAN'}]
    for vlan in vlans:
        vid = vlan.get('id')
        name = vlan.get('name')
        print('\n')
        commands = get_commands(vid, name)
        print('CONFIGURING VLAN' + vid)

        for device in devices:
            push_commands(device, commands)
            print('\n')
"""

if __name__ == '__main__':
    txt = input('Enter your sentence: ')
    word = txt.split()

    print(word)
    dictman = {i: len(i) for i in word}
    maxman = max(dictman[i] for i in word)

    for i in dictman:
        if dictman[i] == maxman:
            print(i)

