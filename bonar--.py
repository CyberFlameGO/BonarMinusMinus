# -*- coding: utf-8 -*-
# Esolang compiler based on Boner++
# Bonar--

# read the input file (extension is '.bonar')

import sys

filename = sys.argv[1]

f = open(filename + '.bonar', 'r')

code = f.read()

# dictionary of words to be swapped

swap = {
            'gamming' : 'for',
            'sonic' : 'while',
            'shitpost' : 'in',
            'hmm' : 'if',
            'wtf' : 'else',
            'wtmm' : 'elif',
            'doitwork' : 'try',
            'nah' : 'except',
            'kaolo' : 'break',
            'clobbong' : 'continue',
            'gibin' : 'input',
            'gebneralk' : 'class',
            'chumbender' : 'def',
            'jeff' : 'return',
            'away' : '-',
            'yang' : '+', 
            'perc' : '%',
            'deliberately_equals' : '==',
            ' bonar ' : ' = ',
            ' unfunwaa ' : ' < ',
            ' funwaa ' : ' > ',
            'yote' : '<=',
            'yeet' : '>=',
            'xon' : 'and',
            'detecotb' : 'or',
            'itdobe' : 'is',
            'zenzi' : 'not',
            'hpock' : 'import',
            'tysob' : 'from',
            'blorgia' : 'as',
            'dick' : 'with',
            'anime' : 'True',
            'no_anime' : 'False',
            'soulLESS' : 'None',
            'ban' : 'del',
            'shit' : 'print',
            'zoom' : 'yield',
            'troll' : 'lambda',
            'ADL' : 'raise',
            'oil' : 'pass',
            'zoomer' : 'nonlocal', 
            'boomer' : 'global',
            'doge' : 'finally',
            'sus' : 'await',
            'amongus' : 'assert',
            'chungus' : 'async',
            'blacksheets' : 'dict',
            'thumbnail' : 'str',
            'xomc' : 'int',
            'dicde' : 'double',
            'boatin' : 'float',
            'touhou' : 'chr',
            'osu' : 'map',
            'reimu' : 'set',
            'based' : 'max',
            'cringe' : 'min',
            'BrUH' : 'range',
            'mips' : 'round',
            'vig' : 'sum',
            'pringle' : 'super',
            'dino' : 'tuple',
            'rshig' : 'zip',
            'racoon' : 'type',
            'dong' : 'len',
            'balls' : 'list',
            'jeb' : 'open',
            'pipeline' : 'join',
            'epyc' : 'file',
            'skeet' : 'split',
            'goof' : 'append',
            'cock' : 'run',
            'chumburger' : '[]',
            'eburger' : '\'\'',
            'howdy' : 'message',
            'sprite' : 'event',
            '!!' : ':',
            'tree' : '3'
}

new = code

if '=' in code:
    print('fuck outa here with that python')
    sys.exit()
elif ':' in code:
    print('fuck outa here with that python')
    sys.exit()
elif '3' in code:
    print('fuck outa here with that python')
    sys.exit()

for item in swap: new = new.replace(item, swap[item])

# now we just have regular python code

print("Bonar-- shits fixed")
# confirm message

exec('# -*- coding: utf-8 -*-\n' + new)




            
            
  
