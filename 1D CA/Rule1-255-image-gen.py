from PIL import Image, ImageDraw
from datetime import datetime
import random

    
# to turn index of the rule to binary
def to_binary(number, length = 8):
    return format(number, '#0{}b'.format(length + 2))[2:]


# to figure out rules from rule index
# and return it as a dictionary of input and corressponding
# outputs
def rule(idx):
    ipt = ['111', '110', '101', '100', '011', '010', '001', '000']
    opt = list(to_binary(idx))
    rule_dict = dict(zip(ipt, opt))
    return rule_dict


def zero_gen(length, rev_idxs = [], def_val = '0'):
    og_gen = [def_val] * length
    rev_val = '1' if def_val == '0' else '0'
    for i in rev_idxs:
        og_gen[i] = rev_val
    return og_gen


##r = lambda: random.randint(0,215)
##rc = lambda: (r(), r(), r())
width = 3686
height = 2048

while True:
    if input('If you want to continue enter 1 or just press enter to stop: ') != '1':
        print('End')
        break
    
    idx = int(input('Enter the rule index: '))
    if idx > 255:
        print('Enter a number less than or equal to 255')
        continue
    
    rules = rule(idx)
    print('These are the rules based on the index you entered({})'.format(idx))
    for k, v in rules.items():
        print(k + ' => ' + v)

    cell_size = int(input('Enter the size of a cell: '))
    popltn = width // cell_size
    
    rev_pos_list = []
    for j in range(random.randint(1, 10)):
        rev_pos_list.append(random.randint(1, popltn-1))
    
    initial_state = zero_gen(popltn, rev_pos_list)

    iters = height // cell_size

    orig_img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(orig_img)
    
    for _ in range(iters):
        nex_gen = []
        for i in range(1, popltn-1):
            nex_gen.append(rules[''.join([initial_state[i-1],
                                         initial_state[i],
                                         initial_state[i+1]])])
        initial_state = ['0'] + nex_gen + ['0']
        for n, cell in enumerate(initial_state):
            color = 'black' if cell == '1' else 'white'
            draw.rectangle((n*cell_size, _*cell_size, (n+1)*cell_size, (_+1)*cell_size)
                 , color, cell_size)
    
    if input('if you want to save the image enter 1 or just press enter to only show: ') != '1':
        print('Displaying Image')
        orig_img.show()
    else:
        orig_img.show()
        now = datetime.now()
        orig_img.save('Rule{}-{}x{}-{}.jpg'.format(idx, width, height, now.strftime('%d-%m-%y %H-%M-%S')))



