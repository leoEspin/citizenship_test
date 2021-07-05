import re
import copy
import json

with open('question_bank.txt') as raw:
    rawtext = raw.readlines()
rawtext = [line.replace('\t', '').strip() for line in rawtext]
rawtext = [line for line in rawtext if len(line) > 0]

cleaner = []
pattern = '^(\d+\.)(.+)$' # captures whatever comes after the question number dot pattern
for i in range(len(rawtext)):
    if rawtext[i][0].isdigit() and not re.match(pattern, rawtext[i]):
        cleaner.append(rawtext[i] + rawtext[i+1])
    else:
        cleaner.append(rawtext[i])

qbank = []
q_template = {"question": None, "answers": []}
N = len(rawtext)
current_q = copy.deepcopy(q_template) # need deep copy of template

for i in range(N):
    line = rawtext.pop(0)
    check_question = re.match(pattern, line)
    if check_question:
        if len(current_q['answers']) > 0:
            qbank.append(current_q)
            current_q = copy.deepcopy(q_template) 
        current_q["question"] = check_question.groups()[1].strip()
    elif '▪' in line:
        current_q["answers"].append(re.sub('^[\s▪]+', '', line).strip())

with open('question_bank.json','w') as output:
    json.dump({"Questions": qbank}, output, indent = 2)