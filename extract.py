import json
import html

i = 1

wFile = open(r'writingFile.txt', 'w')

with open('data.json') as file:
    data = json.load(file)

    for p in data['results']:
        que = html.unescape(p['question'])
        answ = html.unescape(p['correct_answer'])    
    
        wFile.write('Question ' + str(i) + ': ' + que + '\n')
        wFile.write('Answer ' + str(i) + ': ' + answ + '\n')

        i += 1

wFile.close()

