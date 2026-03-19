#!/usr/bin/env python3
"""
Azure ML Income Prediction API Test

Calls a deployed Azure ML endpoint to test predictions on sample profiles.
Credentials are loaded from .env file for security.
"""

import json
import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

SAMPLES = [
    {
        "name": "Young entry-level worker",
        "data": {
            "age": 25, "workclass": "Private", "fnlwgt": 178000,
            "education": "HS-grad", "education-num": 9,
            "marital-status": "Never-married", "occupation": "Craft-repair",
            "relationship": "Own-child", "race": "White", "sex": "Male",
            "capital-gain": 0, "capital-loss": 0, "hours-per-week": 40,
            "native-country": "United-States"
        }
    },
    {
        "name": "Experienced professional",
        "data": {
            "age": 45, "workclass": "Private", "fnlwgt": 234000,
            "education": "Masters", "education-num": 14,
            "marital-status": "Married-civ-spouse", "occupation": "Exec-managerial",
            "relationship": "Husband", "race": "White", "sex": "Male",
            "capital-gain": 15000, "capital-loss": 0, "hours-per-week": 50,
            "native-country": "United-States"
        }
    },
    {
        "name": "Mid-career specialist",
        "data": {
            "age": 35, "workclass": "Self-emp-not-inc", "fnlwgt": 180000,
            "education": "Bachelors", "education-num": 13,
            "marital-status": "Married-civ-spouse", "occupation": "Prof-specialty",
            "relationship": "Husband", "race": "Asian-Pac-Islander", "sex": "Male",
            "capital-gain": 5000, "capital-loss": 0, "hours-per-week": 45,
            "native-country": "India"
        }
    },
    {
        "name": "Senior highly educated",
        "data": {
            "age": 60, "workclass": "Private", "fnlwgt": 265000,
            "education": "Doctorate", "education-num": 16,
            "marital-status": "Married-civ-spouse", "occupation": "Prof-specialty",
            "relationship": "Husband", "race": "White", "sex": "Male",
            "capital-gain": 20000, "capital-loss": 2000, "hours-per-week": 55,
            "native-country": "United-States"
        }
    },
    {
        "name": "Part-time service worker",
        "data": {
            "age": 30, "workclass": "Private", "fnlwgt": 150000,
            "education": "Some-college", "education-num": 10,
            "marital-status": "Never-married", "occupation": "Other-service",
            "relationship": "Not-in-family", "race": "Black", "sex": "Female",
            "capital-gain": 0, "capital-loss": 0, "hours-per-week": 30,
            "native-country": "United-States"
        }
    }
]


def validate_config():
    """Verify API credentials are configured."""
    if not API_URL or not API_KEY:
        print("Error: Missing API credentials")
        print("Please set API_ENDPOINT and API_KEY in your .env file")
        print("See SETUP_GUIDE.md for instructions")
        return False
    return True


def predict(profile, name):
    """Call the API and return prediction result."""
    print(f"\n{name}")
    print("-" * 60)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "Inputs": {"input1": [profile]},
        "GlobalParameters": {}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)

        if response.status_code == 200:
            result = response.json()
            if "Results" in result:
                pred = result["Results"]["output1"][0]
                income = pred.get("Predictions", "N/A")
                confidence = pred.get("Scored Probabilities", "N/A")

                print(f"Prediction: {income}")
                if isinstance(confidence, (int, float)):
                    print(f"Confidence: {confidence*100:.1f}%")

                return {"status": "success", "prediction": income, "confidence": confidence}
            else:
                print("Unexpected response format")
                return {"status": "error", "error": "Bad response"}
        else:
            print(f"API Error: HTTP {response.status_code}")
            return {"status": "error", "error": f"HTTP {response.status_code}"}

    except requests.exceptions.Timeout:
        print("Request timeout")
        return {"status": "error", "error": "timeout"}
    except requests.exceptions.ConnectionError:
        print("Connection error - check API endpoint")
        return {"status": "error", "error": "connection"}
    except Exception as e:
        print(f"Error: {e}")
        return {"status": "error", "error": str(e)}


def main():
    """Run predictions on test samples."""
    print("\n" + "="*60)
    print("Azure ML Income Prediction - API Test")
    print("="*60)

    if not validate_config():
        sys.exit(1)

    results = []
    for sample in SAMPLES:
        result = predict(sample["data"], sample["name"])
        results.append(result)

    # Summary
    success_count = sum(1 for r in results if r["status"] == "success")
    print(f"\n" + "="*60)
    print(f"Results: {success_count}/{len(results)} successful")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
