subs = { #excludes case changes
    #deliberate
    'O':['0'], #Capital O
    '0':['0','o'], #Zero
    'o':['0'], #small o
    '!':['i','I','1','L','l'],
    'i':['!','L','l','1'],
    'L':['!','1','i','I'],
    '1':['I','i','l','L'],
    '@':['A','a'],
    'A':['@'],
    'a':['@'],
    #nearby
    'q':['1','2','w','s','a'],
    #german keyboard
    'z':['y'],
    'y':['z']
}

ends = [
    "",
    "1",
    "01",
    "123",
    "@#",
    "12",
    "99",
]

