import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

BASE_URL = os.getenv("BASE_URL")

prompt = f"""
You are a QA engineer. Generate 3 API test cases in JSON format for {BASE_URL}/posts.

Each test should include:
- name
- method (GET or POST)
- endpoint
- body (if POST)
- expected_status_code

Return ONLY valid JSON array.
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.5
)

# Extract response text
ai_output = response.choices[0].message.content

print("AI Generated Test Cases:")
print(ai_output)

# Save to file
with open("ai-testing/ai_test_cases.json", "w") as f:
    f.write(ai_output)