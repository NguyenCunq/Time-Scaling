import wave
import struct
import numpy as np

# Set the audio parameters
sample_rate = 44100
duration = 5 # seconds
amplitude = 32767 # maximum amplitude for 16-bit signed integer

# Generate a sine wave signal
frequency = 440 # Hz
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Open a new wave file
with wave.open('integer_audio.wav', 'wb') as wavefile:
    # Set the audio parameters
    wavefile.setnchannels(1) # mono
    wavefile.setsampwidth(2) # 16-bit signed integer
    wavefile.setframerate(sample_rate)

    # Convert the signal to a byte string
    signal_bytes = b''
    for s in signal:
        signal_bytes += struct.pack('h', int(s))

    # Write the signal to the wave file
    wavefile.writeframes(signal_bytes)