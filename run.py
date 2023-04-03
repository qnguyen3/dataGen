import openai
import argparse
from dotenv import load_dotenv
import os


data_gen = openai.ChatCompletion()
load_dotenv()
parser = argparse.ArgumentParser(description='dataGen')

openai.api_key = os.getenv("OPENAI_API_KEY")

parser.add_argument('--task', type=str, help='general vs code', default='general', choices=['general', 'code'])
parser.add_argument('--num-example', type=int, default=10, help='Number of example you want to generate')
args = parser.parse_args()
task = args.task
num_example = args.num_example

file_name = ''

if task == 'general':
    num_example = int(num_example/5)
    file_name = 'prompt.txt'
else:
    file_name = 'code_prompt.txt'

with open(file_name, 'r') as file:
    file_contents = file.read()

messages=[
        {"role": "system", "content": file_contents},
    ]
for i in range(num_example):
    response = data_gen.create(model='gpt-3.5-turbo',
                    messages=messages,
                    temperature=0.7,
                    )
    text =  response.choices[0].message.content + '\n'
    if os.path.exists("generated_data.txt"):
    # If the file exists, append the text to the end of the file
        with open("generated_data.txt", "a") as file:
            file.write(text)
    else:
    # If the file doesn't exist, create a new file and write the text to it
        with open("generated_data.txt", "w") as file:
            file.write(text)
