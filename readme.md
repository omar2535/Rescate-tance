# Rescate Tance

[![Maintainability](https://api.codeclimate.com/v1/badges/6de634a20ef1f5e51810/maintainability)](https://codeclimate.com/github/omar2535/Rescate-tance/maintainability)

A POC ransomware detector for CMPT733 project

## ⚒ Setup

**Setting up the environment:**

```sh
# Creating the virtual environment
python3 -m venv .env

# Activating the virtual environment
source .env/bin/activate
```

**Installing dependencies:**

```sh
(.env) pip install -r requirements.txt
```

**Setting up pre-commit hooks:**

```sh
(.env) pre-commit install
```

## 📁 Folder structure
- **io-detector**: Detects ranosmware by looking at high file I/O
- **sensory-detector:** Detects ransomware by creating sensor files
