# IO detector

This detector uses the Linux command line tool `iotop` to perform periodic checks on the processes using the highest IO

## Usage

Simply run it from the detector in the root directory:

```sh
python3 main.py -d IODetector
```

## Furthur improvements

- Logging
- Able to kill the process with the highest IO
- Cross-checking with sensory detectors and signature detectors for collaborated method of ransomware detection
