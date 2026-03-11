from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY= Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_pandas_query(question, columns):

    prompt = f"""
You are a data analyst.

A pandas dataframe named df already exists.

Columns in the dataframe:
{columns}

Convert the user's question into pandas python code.

Rules:
- Return ONLY python code
- Store the output in variable called result
- df is already loaded
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt + "\nQuestion: " + question}
        ],
        temperature=0
    )

    code = response.choices[0].message.content

    # Remove markdown formatting if present
    code = code.replace("```python", "").replace("```", "")

    return code