import random

label_names = []

def add_label():
    label = input('Enter label name: ')
    label_names.append(label)

def view_labels():
    for i, label in enumerate(label_names):
        print(f'{i+1}: {label}')

def generate_label_code():
    label_indices = input('Enter label numbers separated by commas: ')
    label_indices = [int(i) for i in label_indices.split(',')]
    label_code = '<View>\n  <Text name="text" value="$text" maxLength="5000"/>\n  <Labels name="labels" toName="text">\n'
    for i in label_indices:
        label = label_names[i-1]
        color = f'#{random.randint(0, 0xFFFFFF):06x}'
        shortcut = chr(i+64)
        label_code += f'    <Label value="{label}" style="background: {color};" shortcut="{shortcut}"/>\n'
    label_code += '  </Labels>\n</View>\n'
    print(label_code)
    with open('labels.txt', 'w') as f:
        f.write('Labels:\n')
        for label in label_names:
            f.write(f'{label}\n')
        f.write('\nCode:\n')
        f.write(label_code)

def import_labels():
    with open('labels.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('Labels:'):
                continue
            elif line.startswith('\n'):
                break
            else:
                label_names.append(line.strip())

while True:
    action = input('Enter action (1: add label, 2: view labels, 3: generate code, 4: import labels): ')
    if action == '1':
        add_label()
    elif action == '2':
        view_labels()
    elif action == '3':
        generate_label_code()
    elif action == '4':
        import_labels()
