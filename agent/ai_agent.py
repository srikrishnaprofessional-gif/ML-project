import requests

def churn_agent(age, salary, purchases):

    url = "http://127.0.0.1:8000/predict"

    params = {
        "age": age,
        "salary": salary,
        "purchases": purchases
    }

    res = requests.post(url, params=params)
    result = res.json()

    print("RAW API RESPONSE:", result)

    if "churn" not in result:
        return "❌ API error: check input or server"

    if result["churn"] == 1:
        return "⚠️ High risk → give discount"
    else:
        return "✅ Low risk → upsell"

# Call agent with correct values
print(churn_agent(30, 50000, 2))
