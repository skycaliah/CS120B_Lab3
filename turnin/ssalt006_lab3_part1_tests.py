tests = [ {'description': 'PINA: 0x00, PINB: 0x00  => PORTC: 0x00',
    'steps': [ {'inputs': [('PINA',0x00), ('PINB', 0x00)], 'iterations': 2 } ],
    'expected': [('PORTC',0x00)],
    },

   {'description': 'PINA: 0x0A, PINB: 0x0A  => PORTC: 0x04',
    'steps': [ {'inputs': [('PINA',0x0A), ('PINB', 0x0A)], 'iterations': 5 } ],
    'expected': [('PORTC',0x04)],
    },

   ]

#watch = ['PORTC']
#watch = ['count']

