# Text to Binary Tone Converter
This Python script converts an input text message into its binary representation and plays corresponding tones for each bit using pyaudio and numpy. Each bit of the binary representation is mapped to a specific frequency: one frequency for '1' and another for '0'.

## Features
- Converts input text to binary representation.
- Generates sine wave tones for each bit in the binary representation.
- Plays the generated tones through the system's audio output.

## Requirements
- Python 3.x
- numpy
- pyaudio

## Installation

1. Clone the repository:

```
https://github.com/William2716057/toBinarySound.git
```
2. Install the required libraries:
```
pip install numpy pyaudio
```

## Usage
1. Run the script:
```
python toBinarySound
```
2. Input your message when prompted:
```
Input message: Hello World
```
3. Listen to the generated tones.

## How It Works
- Input Message: The user inputs a message.
- Binary Conversion: Each character of the message is converted to its binary representation.
- Tone Generation: A sine wave tone is generated for each bit. The frequency for '1' is set to 440 Hz and for '0' is set to 500 Hz.
- Play Sound: The generated tones are played sequentially through the system's audio output.
