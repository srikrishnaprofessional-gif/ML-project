import requests

API_URL = "http://127.0.0.1:8000/predict"

def chatbot_response(age, salary, purchases):
    try:
        res = requests.post(
            "http://127.0.0.1:8000/predict",
            json={
                "age": int(age),
                "salary": int(salary),
                "purchases": int(purchases)
            }
        )

        result = res.json()
        print("FULL API RESPONSE:", result)

        if "churn" not in result:
            return f"❌ API error: {result}"

        confidence = result.get("confidence", 0.5)

        if result["churn"] == 1:
            return f"⚠️ High churn risk ({confidence:.2f}) → Offer discount"
        else:
            return f"✅ Low churn risk ({confidence:.2f}) → Upsell"

    except Exception as e:
        print("ERROR:", e)
        return "❌ API connection failed"