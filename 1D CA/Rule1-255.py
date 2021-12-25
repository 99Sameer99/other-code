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


# to print the generation
def print_gen(lst):
    print(''.join([ '|' if i == '1' else ' ' for i in lst ]))


def zero_gen(length, rev_idxs = [], def_val = '0'):
    og_gen = [def_val] * length
    rev_val = '1' if def_val == '0' else '0'
    for i in rev_idxs:
        og_gen[i] = rev_val
    return og_gen

while True:
    if input('If you want to continue enter 1 or just press enter: ') != '1':
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

    width = int(input('Enter the numbers of cells to be included: '))

    k = int(input('Enter the number of cells in initial state you ' + 
    'want to have opposite value: '))
    j = []
    for i in range(k):
        j.append(int(input('Enter index {}: '.format(i+1))))

    initial_state = zero_gen(width, j)

    iters = int(input('Enter the number of iterations you want: '))

    print_gen(initial_state)
    for _ in range(iters):
        nex_gen = []
        for i in range(1, width-1):
            nex_gen.append(rules[''.join([initial_state[i-1],
                                         initial_state[i],
                                         initial_state[i+1]])])
        initial_state = ['0'] + nex_gen + ['0']
        print_gen(initial_state)



