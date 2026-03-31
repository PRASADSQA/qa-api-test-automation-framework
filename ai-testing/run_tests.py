import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

with open("ai-testing/ai_test_cases.json") as f:
    tests = json.load(f)

results = []

for test in tests:
    name = test.get("name")
    method = test.get("method").upper()
    endpoint = test.get("endpoint")
    body = test.get("body", None)
    expected_status = test.get("expected_status_code", 200)

    url = f"{BASE_URL}{endpoint}"

    if method == "GET":
        resp = requests.get(url)
    elif method == "POST":
        resp = requests.post(url, json=body)
    else:
        continue

    results.append({
        "test_name": name,
        "status_code": resp.status_code,
        "expected": expected_status,
        "passed": resp.status_code == expected_status
    })

# Save results
os.makedirs("ai-testing/reports", exist_ok=True)
with open("ai-testing/reports/ai_test_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("AI test execution completed. Results saved in ai-testing/reports/ai_test_results.json")