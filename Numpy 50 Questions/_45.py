# 45. Compute the Fast Fourier Transform (FFT) of a given array
import numpy as np
import matplotlib.pyplot as plt

# Create a sample array (time-domain signal)
# Let's create a signal with 2 frequencies: 50 Hz and 120 Hz
t = np.linspace(0, 1, 500)  # Time array from 0 to 1 second with 500 points
signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)  # Signal with 50Hz and 120Hz frequencies

# Compute the FFT of the signal
fft_signal = np.fft.fft(signal)

# Compute the corresponding frequency values
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])

# Plot the original signal and its FFT
plt.figure(figsize=(12, 6))

# Plot time-domain signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Time-Domain Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the frequency-domain (FFT)
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_signal))
plt.title('Frequency-Domain (FFT)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
