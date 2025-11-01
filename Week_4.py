# Spectral Analysis of Signals - EXP 14
# Generate a signal that is the sum of 2 sinusoids x(t) = sin(2*pi*20t) + cos(2*pi*30t) compute its FT and magnitude spectrum plot all the signals

import numpy as np
import matplotlib.pyplot as plt

duration = 1 
fs = 200  
N = int(fs * duration)
t = np.linspace(0, duration, N, endpoint=False)
x = np.sin(2 * np.pi * 20 * t) + np.cos(2 * np.pi * 30 * t)
X = np.fft.fft(x)
freqs = np.fft.fftfreq(N, 1/fs)
magnitude = np.abs(X)
x_reconstructed = np.fft.ifft(X).real

fig, axs = plt.subplots(1, 3, figsize=(16, 5))

axs[0].plot(t, x, 'b-', linewidth=2)
axs[0].set_xlabel('Time (seconds)', fontsize=11)
axs[0].set_ylabel('Amplitude', fontsize=11)
axs[0].set_title('Original Signal: x(t) = sin(2π·20t) + cos(2π·30t)', 
                    fontsize=12, fontweight='bold')
axs[0].grid(True, alpha=0.3)
axs[0].axhline(y=0, color='k', linewidth=0.5)

axs[1].stem(freqs[:N//2], magnitude[:N//2], linefmt='r-', markerfmt='ro', basefmt='r-')
axs[1].set_xlabel('Frequency (Hz)', fontsize=11)
axs[1].set_ylabel('Magnitude', fontsize=11)
axs[1].set_title('Magnitude Spectrum', fontsize=12, fontweight='bold')
axs[1].grid(True, alpha=0.3)
axs[1].set_xlim(0, 50)

axs[2].plot(t, x, 'b-', linewidth=2, label='Original', alpha=0.7)
axs[2].plot(t, x_reconstructed, 'm--', linewidth=2, label='Reconstructed (IFFT)', alpha=0.9)
axs[2].set_xlabel('Time (seconds)', fontsize=11)
axs[2].set_ylabel('Amplitude', fontsize=11)
axs[2].set_title('Original vs Reconstructed Signal', fontsize=12, fontweight='bold')
axs[2].legend(fontsize=10)
axs[2].grid(True, alpha=0.3)
axs[2].axhline(y=0, color='k', linewidth=0.5)

plt.show()
