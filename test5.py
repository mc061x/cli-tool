from system.runFile import FileRunner
from config.generalCfg import GeneralConfig

testname = 'hashtable-comp'
folder = 'performance-test-testcases'

import random, sys

def rand():
    return random.randrange(0, int(1e20))

def e(base: int, power: int):
    return base * int(10**power)

def generate_testcases(count: int):
    for testcase in range(count):
        current_name = f'{testname}-{testcase}.in'
        f = open(current_name, 'w')

        sys.stdout = f

        N = rand() % e(4, 6) 
        X = rand() % e(4, 14)
        print(N, X)
        for i in range(N):
            print(rand() % e(1, 9), end=' ')
        
        sys.stdout = sys.__stdout__    

generate_testcases(2)

import os
os.system('g++ test.cpp -o test.cpp.out')

