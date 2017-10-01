#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fich = open(sys.argv[1], 'r')
linelist = fich.readlines()
fich.close()
calc = calcoohija.CalculadoraHija()
for line in linelist:
    operat = line[:line.find(',')]
    nums = line[line.find(',') + 1:]
    numlist = []
    while (',' in nums) == 1:
        numlist.append(nums[:nums.find(',')])
        nums = nums[nums.find(',') + 1:]
    
    if ('\n' in nums) == 1:
        numlist.append(nums[:nums.find('\n')])
    
    if operat == 'suma':
        i = 0
        result = 0
        for num in numlist:
            result = calc.suma(result, int(numlist[i]))
            i = i + 1
            
    elif operat == 'resta':
        i = 0
        result = int(numlist[i])
        for num in numlist:
            try: 
                result = calc.resta(result, int(numlist[i + 1]))
                i = i + 1
            except IndexError:
                result = result
                
    elif operat == 'multiplica':
        i = 0
        result = 1
        for num in numlist:
            result = calc.multiplica(result, int(numlist[i]))
            i = i + 1
            
    elif operat == 'divide':
        i = 0
        result = int(numlist[i])
        for num in numlist:
            try: 
                result = calc.divide(result, int(numlist[i + 1]))
                i = i + 1
            except IndexError:
                result = result
            except ZeroDivisionError:
                sys.exit('División por cero')

    print('Resultado:', result)

