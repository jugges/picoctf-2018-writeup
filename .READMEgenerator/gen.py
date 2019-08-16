import json
import html2markdown
import os

with open('data.json', 'r') as f:
    problems = json.load(f)

os.chdir('..')

for problem in problems:
    print(problem['name'])
    directory = problem['category']+"/"+problem['name'].replace('?', '')
    if not os.path.exists(directory):
        os.makedirs(directory)
        with open(directory+"/"+'README.md', 'w', encoding="utf-8") as r:
            r.write("## Question\n")
            r.write('>'+html2markdown.convert(problem['description'])+"\n\n")
            r.write("### Hint\n")
            for hint in problem['hints']:
                r.write('>'+html2markdown.convert(hint)+"\n")
