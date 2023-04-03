# dataGen - Generate data from LLMs with ease

## Steps
1) Clone this repo
2) install conda
3) Run the following command
```bash
cd dataGen
conda create -n 'dataGen' python=3.8
pip3 install -r requirements.txt
```
4) Create a .env file with the following
```bash
OPENAI_API_KEY=replace_your_api_key
```
5) python3 run.py

## run.py arguments
```python
--task general #general vs code tasks generation
--num-example #number of examples to generate
```
After running, the data will be stored in `generated_data.txt`. If the file is already existed, the data will be concatenated