my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    },
    'set': {1, 2, 3, 4, 5}
}

print(my_dict['tuple'][-1])
my_dict['list'].append('hi!')
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = False
my_dict['dict'].pop('c')
my_dict['set'].add(5.5)
my_dict['set'].discard(5)

print(my_dict)
