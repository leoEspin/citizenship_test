import numpy as np
import json
import time

# class found here: https://stackoverflow.com/a/287944/10946181
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
with open('question_bank.json', 'r') as q:
    qbank = json.load(q)
#assert len(qbank['Questions']) == 100, 'There\'s missing questions'

questions = qbank['Questions']

def start_attempt(qlist: list):
    start = time.time()
    attempt = np.random.choice(len(qlist), size=10, replace=False)
    print(f'{bcolors.WARNING}If multiple answers are required, separate them with commas (,):{bcolors.ENDC}')
    for x in attempt:
        print(f'{bcolors.OKCYAN}{qlist[x]["question"]}{bcolors.ENDC}')
        resp = input('Answer(s):').split(',')
        resp = {x.strip() for x in resp}
        if resp.issubset(qlist[x]['answers']):
            print(f'{bcolors.OKGREEN}correct{bcolors.ENDC}')
        else:
            print(f'{bcolors.FAIL}incorrect{bcolors.ENDC}. The valid answer(s) are')
            for t in qlist[x]['answers']:
                print(t)
                
    elapsed = time.time() - start         
    print(f'Elapsed time: {elapsed/60} minutes')
    return elapsed


