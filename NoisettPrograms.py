# Noisett programs for Python interpreter

# Decimal counter
counter = NewNut("Counter",
    [
     ['Start Count from *', '>', 'Print $1'],
     ['Start Count from *', '>', 'Increment $1'],
     ['Print *', '>', 'Increment $1'],
       
    ],
    ['Start Count from 1'],
    [
     ['=', '', 'Incrementer', '='],
     ['=', '', 'Printer', '='],
    ]
)

incrementer = NewNut("Incrementer",
    [
     ['Increment *0', '>', 'Print $11'],
     ['Increment *1', '>', 'Print $12'],
     ['Increment *2', '>', 'Print $13'],
     ['Increment *3', '>', 'Print $14'],
     ['Increment *4', '>', 'Print $15'],
     ['Increment *5', '>', 'Print $16'],
     ['Increment *6', '>', 'Print $17'],
     ['Increment *7', '>', 'Print $18'],
     ['Increment *8', '>', 'Print $19'],
     ['Increment *9', '>', 'DoCarry $1c0'],
    ],
    [],
    [
     ['=', '', 'Counter', '='],
     ['=', '', 'Carrier', '='],
     ['=', '', 'Printer', '='],
    ]
)

carrier = NewNut("Carrier",
    [
     ['DoCarry c*', '>', 'Print 1$1'],
     ['DoCarry *0c*', '>', 'Print $11$2'],
     ['DoCarry *1c*', '>', 'Print $12$2'],
     ['DoCarry *2c*', '>', 'Print $13$2'],
     ['DoCarry *3c*', '>', 'Print $14$2'],
     ['DoCarry *4c*', '>', 'Print $15$2'],
     ['DoCarry *5c*', '>', 'Print $16$2'],
     ['DoCarry *6c*', '>', 'Print $17$2'],
     ['DoCarry *7c*', '>', 'Print $18$2'],
     ['DoCarry *8c*', '>', 'Print $19$2'],
     ['DoCarry *9c*', '<', 'DoCarry $1c0$2']
    ],
    [],
    [
     ['=', '', 'Counter', '='],
     ['=', '', 'Printer', '='],
    ]
)

printer = NewNut("Printer",
    [
     ['Print *', '>', '$1'],  
    ],
    [],
    [['=', '', 'stdout', '=']]
)

AddNut(counter, NUTS)
AddNut(incrementer, NUTS)
AddNut(carrier, NUTS)
AddNut(printer, NUTS)


# Decimal counter (simplified)
counter = NewNut("Counter",
    [
     ['Start Count from *', '<', 'Next $1'],
     ['Next *', '>', '$1'],
     ['Next *', '<', 'Increment $1'],

     ['Increment *0', '<', 'Next $11'],
     ['Increment *1', '<', 'Next $12'],
     ['Increment *2', '<', 'Next $13'],
     ['Increment *3', '<', 'Next $14'],
     ['Increment *4', '<', 'Next $15'],
     ['Increment *5', '<', 'Next $16'],
     ['Increment *6', '<', 'Next $17'],
     ['Increment *7', '<', 'Next $18'],
     ['Increment *8', '<', 'Next $19'],
     ['Increment *9', '<', 'DoCarry $1c0'],
       
     ['DoCarry c*', '<', 'Next 1$1'],
     ['DoCarry *0c*', '<', 'Next $11$2'],
     ['DoCarry *1c*', '<', 'Next $12$2'],
     ['DoCarry *2c*', '<', 'Next $13$2'],
     ['DoCarry *3c*', '<', 'Next $14$2'],
     ['DoCarry *4c*', '<', 'Next $15$2'],
     ['DoCarry *5c*', '<', 'Next $16$2'],
     ['DoCarry *6c*', '<', 'Next $17$2'],
     ['DoCarry *7c*', '<', 'Next $18$2'],
     ['DoCarry *8c*', '<', 'Next $19$2'],
     ['DoCarry *9c*', '<', 'DoCarry $1c0$2']
    ],
    ['Start Count from 1'],
    [
     ['=', '', 'stdout', '='],
    ]
)

AddNut(counter, NUTS)


