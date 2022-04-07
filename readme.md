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

## 🔧 Usage

Using the program to run detectors can be done like so:

```sh
python3 main.py -d <DetectorName>
```

and for a full menu of command line options, run:

```sh
python3 main.py -h
```

## 📁 Folder structure

- **io-detector**: Detects ranosmware by looking at high file I/O
- **sensory-detector:** Detects ransomware by creating sensor files
- **detectors:** Where all the detector classes are kept as a single point of control
- **tests:** Test scripts. Can be invoked via the `tester.py` in the root directory

## 🕵️‍♀️ Adding a new detector

1. First, make a new folder if there are utilities for this detector in the root directory.
2. Afterwards, create a `<NameHere>Detector.py` file in `detectors/` and define the `run(self, ...)` function!
3. Lastly, add the detector class name in `detectors/__init__.py` to allow the detector to be called from the main program!

## 🧪 Tests

To run tests, run:

```sh
python tester.py
```

currently, this only runs the tests in `tests/raasnet_test.py`

## ⚠ WARNING

**DO NOT RUN THE PAYLOADS IN `tests/ransomware/` DIRECTLY!!**. You will brick your computer and cause all your files to be encrypted!
