import numpy as np
import pyaudio

plaintext = input("Input message: ")
binary_representation = ' '.join([bin(ord(char))[2:].zfill(8) for char in plaintext])
print(binary_representation)


def generate_tone(frequency, duration, sample_rate, amplitude=0.5):
    #generate sine wave
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return signal

def play_sound(signal, sample_rate):
    #play the audio
    p = pyaudio.PyAudio()
    
    #open stream
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)
    
    #convert signal to bytes and play
    stream.write(signal.astype(np.float32).tobytes())
    
    #close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

def main():
    #parameters
    sample_rate = 44100  #sample rate
    duration = 0.5  #duration in seconds for each bit

    #iterate over each bit in the binary representation
    for bit in binary_representation.replace(' ', ''):
        if bit == "1":
            frequency = 440  #frequency in Hz for '1'
        else:
            frequency = 500  #frequency in Hz for '0'
        
        #generate tone
        signal = generate_tone(frequency, duration, sample_rate)
        
        #play tone
        play_sound(signal, sample_rate)
    
    print("Playing tones...")

if __name__ == "__main__":
    main()