# Azure ML Income Prediction - Secure Setup Guide

**This guide explains how to securely use this project WITHOUT exposing your Azure credentials on GitHub.**

---

## 🔒 Security First

**Important:** This project is designed so that:
- ✅ No Azure credentials are stored in GitHub
- ✅ No API keys are in any committed files
- ✅ Your credentials stay private and secure
- ✅ The code is reusable by anyone with their own Azure endpoint

---

## 📋 Prerequisites

1. **Azure subscription** with deployed ML endpoint
2. **Python 3.7+** installed on your computer
3. **Git** installed (to clone/use this project)

---

## 🚀 Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
cd adult-income-prediction
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all required packages including:
- `requests` - for API calls
- `python-dotenv` - for loading environment variables securely
- Other dependencies for data processing

### Step 3: Get Your Azure Credentials

You need two pieces of information from Azure ML:

#### Getting your API Endpoint:
1. Go to [Azure ML Studio](https://ml.azure.com)
2. In the left sidebar, click **Endpoints**
3. Click on your endpoint name (e.g., "Pipeline-Created-on-03-16-2026-real time inference")
4. Look for **REST endpoint** - copy this full URL

#### Getting your API Key:
1. In the same endpoint details page
2. Look for **Keys** or **API Key** section
3. Click **Show** to reveal your primary key
4. Copy the key (it's a long string of characters)

### Step 4: Create Your .env File

1. In the project folder, create a new file named `.env` (note: exactly `.env`, not `.env.example`)

2. Copy the structure from `.env.example`:
```
API_ENDPOINT=<paste-your-endpoint-url-here>
API_KEY=<paste-your-api-key-here>
```

3. Replace the values with your actual credentials:
```
API_ENDPOINT=https://eastus2.api.azureml.ms/pipelines/v1.0/subscriptions/...
API_KEY=abc123def456...
```

4. **Save the file** - it's automatically ignored by git (see `.gitignore`)

### Step 5: Run the Script

```bash
python api_test.py
```

You should see:
- ✅ Connection to your Azure endpoint
- ✅ Predictions on sample profiles
- ✅ Results showing income predictions

---

## 📁 File Descriptions

```
.
├── api_test.py              # Main script - reads credentials from .env
├── requirements.txt         # Python dependencies
├── .env.example            # Template for .env file (EXAMPLE ONLY)
├── .env                    # YOUR credentials (NEVER commit this!)
├── .gitignore              # Prevents .env from being committed
└── README.md               # Project documentation
```

### Important Files:

- **`.env`** (Created by you)
  - ❌ NOT in GitHub
  - Contains YOUR credentials
  - KEEP PRIVATE
  - Added to `.gitignore`

- **`.env.example`**
  - ✅ In GitHub
  - Shows structure only
  - No real credentials
  - Safe to share

---

## 🔐 Security Best Practices

### ✅ DO:
- Keep `.env` file private and secure
- Use `.env.example` as a template
- Rotate your API keys regularly
- Review what files you're committing to git

### ❌ DON'T:
- Commit `.env` files to git
- Hardcode credentials in Python scripts
- Share your API key with others
- Commit `.env` files by mistake

---

## 🆘 Troubleshooting

### Error: "Missing credentials"
- Make sure `.env` file exists in the project folder
- Check that `API_ENDPOINT` and `API_KEY` are set correctly
- Make sure there are no typos in `.env`

### Error: "Connection refused"
- Verify your `API_ENDPOINT` URL is correct
- Check that your Azure endpoint is still deployed and active
- Make sure you have internet connection

### Error: "Unauthorized" (HTTP 401)
- Your `API_KEY` might be wrong or expired
- Go back to Azure ML and get the fresh key
- Paste it into your `.env` file

---

## 💡 Usage Example

Edit the sample profiles in `api_test.py` to test different scenarios:

```python
# In api_test.py, modify the sample data:
SAMPLE_1 = {
    "age": 25,
    "workclass": "Private",
    "education": "HS-grad",
    # ... other fields
}
```

Then run the script to get predictions for your custom profile.

---

## 📚 Additional Resources

- [Azure ML Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/)
- [REST API Best Practices](https://restfulapi.net/http-status-codes/)
- [Environment Variables in Python](https://realpython.com/python-dotenv/)

---

## 📝 License & Attribution

This project demonstrates:
- Secure credential management
- Azure ML endpoint integration
- Python API testing best practices

**Author:** Ajay Ramineni
**Created:** March 2026

---

**Questions?** Check the troubleshooting section or review the `.env.example` file for setup details.
