# Davy Chen's first ChatGPT experiment
# April 27th, 2023

import os
import openai

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# Customized input data forged myself randomly
input1 = f"""
name, age, gender, location, weight \
Desmond, 35, male,   Richmond,  195 \
Henry,   31, male,   Blaine,    182 \
Jasmine, 36, female, crossroad, 163
"""

prompt1 = f"""
Convert the text delimited by triple backticks \
into a list of five made-up friend's names along \ 
with their ages, genders, locations and weight. 
Provide them in JSON format with the following keys: 
friend_id, name, age, gender, location, weight.
```{input1}```
"""

response = get_completion(prompt1)

f = open("output1.txt", "w")
f.write(response)
f.close()

print(response)