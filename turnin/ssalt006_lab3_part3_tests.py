tests = [ {'description': 'PINA: 0x38 => PORTC: 0xBC',
    'steps': [ {'inputs': [('PINA',0x38)], 'iterations': 2 } ],
    'expected': [('PORTC',0xBC)],
    },

 {'description': 'PINA: 0x28 => PORTC: 0x3C',
    'steps': [ {'inputs': [('PINA',0x28)], 'iterations': 2 } ],
    'expected': [('PORTC',0x3C)],
    },

 {'description': 'PINA: 0x30 => PORTC: 0xC0',
    'steps': [ {'inputs': [('PINA',0x30)], 'iterations': 2 } ],
    'expected': [('PORTC',0xC0)],
    },

    ]
#watch = ['count'k]

