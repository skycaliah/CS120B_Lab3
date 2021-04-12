tests = [ {'description': 'PINA: 0x05 => PORTC: 0x38',
    'steps': [ {'inputs': [('PINA',0x05)], 'iterations': 2 } ],
    'expected': [('PORTC',0x38)],
    },

   {'description': 'PINA: 0x0F => PORTC: 0x3F',
    'steps': [ {'inputs': [('PINA',0x0F)], 'iterations': 5 } ],
    'expected': [('PORTC',0x3F)],
    },

   {'description': 'PINA: 0x01 => PORTC: 0x60',
    'steps': [ {'inputs': [('PINA',0x01)], 'iterations': 5 } ],
    'expected': [('PORTC',0x60)],
    },


   {'description': 'PINA: 0x09 => PORTC: 0x3C',
    'steps': [ {'inputs': [('PINA',0x09)], 'iterations': 5 } ],
    'expected': [('PORTC',0x3C)],
    },
   
   {'description': 'PINA: 0x83 => PORTC: 0x70',
    'steps': [ {'inputs': [('PINA',0x83)], 'iterations': 5 } ],
    'expected': [('PORTC',0x70)],
    },
   
   ]

#watch = ['PORTC']
#watch = ['count'k]

