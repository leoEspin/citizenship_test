import re
import copy
import json

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

def make_json(rawtext: list):
    qbank = []
    q_template = {"question": None, "answers": []}
    current_q = copy.deepcopy(q_template) # need deep copy of template

    while len(rawtext) > 0:
        line = rawtext.pop(0)
        check_question = re.match(pattern, line)
        if check_question:
            if len(current_q['answers']) > 0:
                qbank.append(current_q)
                current_q = copy.deepcopy(q_template) 
            current_q["question"] = check_question.groups()[1].strip()
        elif '▪' in line:
            current_q["answers"].append(re.sub('^[\s▪]+', '', line).strip())

    return  {"Questions": qbank}

with open('question_bank.txt') as raw:
    rawtext = raw.readlines()
rawtext = [line.replace('\t', '').strip() for line in rawtext]
rawtext = [line for line in rawtext if len(line) > 0]

cleaner = []
pattern = '^(\d+\.)(.+)$' # captures whatever comes after the question number dot pattern

while len(rawtext) >0 :
    line = rawtext.pop(0)
    if line[0].isdigit() and not re.match(pattern, line):
        cleaner.append(line + rawtext.pop(0))
    else:
        cleaner.append(line)

processed = make_json(cleaner)

with open('question_bank.json','w') as output:
    json.dump(processed, output, indent = 2)