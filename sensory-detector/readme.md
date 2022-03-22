# Sensory detector

This detector module creates small "sensory" files on the file-system
to periodically check if the file was encrypted. If the file was encrypted,
then the program can conclude that the file was encrypted. By default, the sensor files will have the
file extension `.rcsensor.txt`.

## Usage

To run the program, simply run:

```sh
python3 main.py
```

## Log files

Log files are stored in `logs/` directory

## config.yml

`directories_to_check`: To set directories to have the sensor files placed in
`frequency_to_check`: Frequency of how often to check the sensor files for change

## Furthur improvements

- Detection at an even shorter interval (milliseconds)
- Run check once file IO is detected (if implement in kernel, we can pause file IO during interrupt and run this routine before) returning control flow back to program
- Hidden files completely from file-system
