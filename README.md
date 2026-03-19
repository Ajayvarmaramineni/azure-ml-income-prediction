# Adult Income Prediction - Azure ML Project

A secure, production-ready Python project for testing predictions from a deployed Azure Machine Learning endpoint.

## 🎯 Project Overview

This project demonstrates:
- Secure API credential management (no secrets in code)
- Python REST API client implementation
- Best practices for ML model deployment testing
- Industry-standard project structure

## 🔒 Security Features

✅ **Zero Credentials in Code**
- All sensitive data loaded from environment variables
- `.env` file is in `.gitignore` and never committed
- Safe to use with public GitHub repositories

✅ **Production-Ready Structure**
- Proper error handling and logging
- Configuration management
- Reusable API client code
- Comprehensive documentation

## 📦 What's Included

```
├── api_test.py              # API testing script
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
├── SETUP_GUIDE.md          # Complete setup instructions
└── GITHUB_README.md        # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Deployed Azure ML endpoint
- API credentials from Azure ML Studio

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure credentials:**
   - Copy `.env.example` to `.env`
   - Fill in your API endpoint and key
   - Never commit the `.env` file

4. **Run the test:**
   ```bash
   python api_test.py
   ```

## 📖 Detailed Setup

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for:
- Step-by-step credential retrieval from Azure
- Troubleshooting guide
- Configuration details
- Security best practices

## 🔑 Environment Variables

The project requires two environment variables (loaded from `.env` file):

```
API_ENDPOINT   # Your Azure ML endpoint URL
API_KEY        # Your Azure ML API key
```

**Note:** These are kept secure using a `.env` file that is NOT committed to git.

## 📊 Sample Usage

The script tests predictions on 5 sample profiles:
1. Young entry-level worker
2. Experienced professional
3. Mid-career specialist
4. Senior highly educated worker
5. Part-time service worker

Results show predicted income level and confidence scores.

## 🛠️ Technologies Used

- **Python 3.8+** - Programming language
- **requests** - HTTP client library
- **python-dotenv** - Environment variable management
- **Azure Machine Learning** - ML platform

## 📝 Project Structure

This project follows Python best practices:
- Clear separation of configuration from code
- Reusable, testable functions
- Comprehensive error handling
- Detailed comments and documentation
- Security-first approach

## 🔐 Security Notes

⚠️ **Important:**
- Never commit `.env` files containing credentials
- Always use `.env.example` as a template
- Rotate API keys periodically
- Keep Azure credentials private

## 💡 Use Cases

This project can be used to:
- Test Azure ML endpoints locally
- Integrate predictions into applications
- Demo ML models to stakeholders
- Learn about ML deployment workflows
- Template for production ML projects

## 🤝 Contributing

This is an educational project. Feel free to fork and adapt for your use case!

## 📚 Learning Resources

- [Azure ML Documentation](https://learn.microsoft.com/azure/machine-learning/)
- [Python Requests Library](https://docs.python-requests.org/)
- [Environment Variables Best Practices](https://12factor.net/config)

## 📄 License

This project is provided as-is for educational purposes.

## ✨ Features

- ✅ Secure credential management
- ✅ Comprehensive error handling
- ✅ Multiple test profiles
- ✅ Detailed result formatting
- ✅ Easy to extend and customize
- ✅ Production-ready code
- ✅ Extensive documentation

## 🎓 What You'll Learn

By reviewing this project, you'll learn:
1. How to securely manage credentials in Python projects
2. How to call REST APIs from Python
3. How to structure Python projects professionally
4. Azure ML endpoint integration
5. Security best practices for GitHub projects

---

**Status:** Ready for use | **Last Updated:** March 2026

For detailed setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md)
