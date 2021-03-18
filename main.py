import re
from itertools import combinations

class wff:
    def __init__(self, value):
        self.value = value
    def __not__(self): # ~A
        return wff(not self.value)
    def __and__(self, oth): # A and B
        return wff(self.value and oth.value)
    def __xor__(self, oth): # A or B
        return wff(self.value or oth.value)
    def __or__(self, oth): # A -> B
        return wff((not self.value) or oth.value)
    def __eq__(self, oth): # A <-> B
        return wff(self.value == oth.value)

expression = re.compile('(->|and|or|~|<->| |\\(|\\))').split(input())
variables = {}
replace_table = {'T': 'wff(True)', 'F': 'wff(False)', '~': '~', 'and': '&', 'or':'^', '->':'|','<->': '==', ' ':'', '':'', '(':'(', ')': ')'}
has_false = False

for key, identifier in enumerate(expression):
    if identifier not in replace_table:
        variables[identifier] = False
        replace_table[identifier] = 'wff(variables['+identifier.__repr__()+'])'
    expression[key] = replace_table[identifier]

expression = ' '.join(expression)

for i in range(len(variables)+1):
    for combination in combinations(variables.keys(),i):
        for key in variables:
            variables[key] = False
        
        for key in combination:
            variables[key] = True
        
        if not eval(expression).value:
            has_false = True
            print('=====모순 발생=====')
            for key in variables:
                print(key + ': ' + str(variables[key]))
            print('')

if not has_false:
    print('항진입니다.')
