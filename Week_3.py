# Sampling of Signals using python - EXP 13

# Write a python program to generate and plot continous time sinusoidal signals x(t)=sin(2 pi f t) for a frequency of 5Hz over 1 second. sample the signal at 10Hz to obtain a discrete time signal and plot both continous and discrete time signal on the same graph
# Generate two discrete time signals. x1[n]=sin(2 pi 3 n) x2[n]=cos(2 pi 5 n). Write a python program to compute and plot the sum and product of the two signals fot a time period of 1 second.
# Generate a 15Hz sinusoidal signal and sample it at 20Hz and 50Hz. Plot both time domain and frequnecy domain representations
# Generate a continous time sinusoidal signal x(t)= sin(2 pi 5 t) and sample it at different rates. (10Hz, 20Hz and 50Hz) over one second. Plot the conitnous and sampled signals.

import numpy as np
import matplotlib.pyplot as plt

def one():
    """
    Generate continuous-time sinusoidal signal x(t)=sin(2πft) for f=5Hz over 1 second.
    Sample at 10Hz and plot both continuous and discrete signals on same graph.
    """
    # Signal parameters
    f = 5  # Frequency in Hz
    duration = 1  # 1 second
    fs = 10  # Sampling frequency in Hz
    
    # Continuous time signal (dense sampling for smooth curve)
    t_cont = np.linspace(0, duration, 1000)
    x_cont = np.sin(2 * np.pi * f * t_cont)
    
    # Discrete time signal (sampled at 10Hz)
    t_disc = np.arange(0, duration, 1/fs)
    x_disc = np.sin(2 * np.pi * f * t_disc)
    
    # Plot both on same graph
    plt.figure(figsize=(12, 6))
    plt.plot(t_cont, x_cont, 'purple', linewidth=2, label='Continuous Signal')
    plt.stem(t_disc, x_disc, linefmt='r-', markerfmt='ro', basefmt='r-', 
             label=f'Discrete Signal (sampled at {fs}Hz)')
    
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.title(f'Continuous vs Discrete Sinusoidal Signal (f={f}Hz)', 
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(loc ='upper right')
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.show()

def two():
    """
    Generate two discrete signals: x1[n]=sin(2π*3*n), x2[n]=cos(2π*5*n).
    Compute and plot their sum and product over 1 second.
    """
    # Time parameters
    duration = 1  # 1 second
    fs = 50  # Sampling frequency (high enough for smooth discrete plot)
    n = np.arange(0, duration, 1/fs)
    
    # Generate two discrete signals
    x1 = np.sin(2 * np.pi * 3 * n)
    x2 = np.cos(2 * np.pi * 5 * n)
    
    # Compute sum and product
    x_sum = x1 + x2
    x_prod = x1 * x2
    
    # Create 3 subplots (3 rows, 1 column)
    plt.figure(figsize=(12, 10))
    
    # Plot x1[n] and x2[n] on the same subplot
    plt.subplot(3, 1, 1)
    plt.stem(n, x1, linefmt='b-', markerfmt='bo', basefmt='b-', label='x1[n]')
    plt.stem(n, x2, linefmt='g-', markerfmt='go', basefmt='g-', label='x2[n]')
    plt.xlabel('n (seconds)', fontsize=10)
    plt.ylabel('Amplitude', fontsize=10)
    plt.title('Original Signals', fontsize=12, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    
    # Plot sum
    plt.subplot(3, 1, 2)
    plt.stem(n, x_sum, linefmt='r-', markerfmt='ro', basefmt='r-')
    plt.xlabel('n (seconds)', fontsize=10)
    plt.ylabel('x1[n] + x2[n]', fontsize=10)
    plt.title('Sum: x1[n] + x2[n]', fontsize=12, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    
    # Plot product
    plt.subplot(3, 1, 3)
    plt.stem(n, x_prod, linefmt='m-', markerfmt='mo', basefmt='m-')
    plt.xlabel('n (seconds)', fontsize=10)
    plt.ylabel('x1[n] * x2[n]', fontsize=10)
    plt.title('Product: x1[n] * x2[n]', fontsize=12, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    
   
    plt.show()

def three():
    """
    Generate 15Hz sinusoidal signal and sample at 20Hz and 50Hz.
    Plot both time domain and frequency domain representations.
    """
    # Signal parameters
    f = 15  # Signal frequency in Hz
    duration = 1  # 1 second
    
    # Continuous signal for reference
    t_cont = np.linspace(0, duration, 1000)
    x_cont = np.sin(2 * np.pi * f * t_cont)
    
    # Sample at 20Hz
    fs1 = 20
    t_sample1 = np.arange(0, duration, 1/fs1)
    x_sample1 = np.sin(2 * np.pi * f * t_sample1)
    
    # Sample at 50Hz
    fs2 = 50
    t_sample2 = np.arange(0, duration, 1/fs2)
    x_sample2 = np.sin(2 * np.pi * f * t_sample2)
    
    # Compute FFT for frequency domain
    X_sample1 = np.fft.fft(x_sample1)
    freqs1 = np.fft.fftfreq(len(x_sample1), 1/fs1)
    
    X_sample2 = np.fft.fft(x_sample2)
    freqs2 = np.fft.fftfreq(len(x_sample2), 1/fs2)
    
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    
    # Time domain - 20Hz sampling
    axs[0, 0].plot(t_cont, x_cont, 'b-', linewidth=1, alpha=0.5, label='Continuous')
    axs[0, 0].stem(t_sample1, x_sample1, linefmt='r-', markerfmt='ro', basefmt='r-', 
                   label=f'Sampled at {fs1}Hz')
    axs[0, 0].set_xlabel('Time (s)', fontsize=10)
    axs[0, 0].set_ylabel('Amplitude', fontsize=10)
    axs[0, 0].set_title(f'Time Domain: {f}Hz Signal Sampled at {fs1}Hz', fontsize=12, fontweight='bold')
    axs[0, 0].legend()
    axs[0, 0].grid(True, alpha=0.3)
    axs[0, 0].axhline(y=0, color='k', linewidth=0.5)
    
    # Frequency domain - 20Hz sampling
    axs[0, 1].stem(freqs1[:len(freqs1)//2], np.abs(X_sample1)[:len(X_sample1)//2], 
                   linefmt='r-', markerfmt='ro', basefmt='r-')
    axs[0, 1].set_xlabel('Frequency (Hz)', fontsize=10)
    axs[0, 1].set_ylabel('Magnitude', fontsize=10)
    axs[0, 1].set_title(f'Frequency Domain: Sampled at {fs1}Hz', fontsize=12, fontweight='bold')
    axs[0, 1].grid(True, alpha=0.3)
    axs[0, 1].set_xlim(0, fs1/2)
    
    # Time domain - 50Hz sampling
    axs[1, 0].plot(t_cont, x_cont, 'b-', linewidth=1, alpha=0.5, label='Continuous')
    axs[1, 0].stem(t_sample2, x_sample2, linefmt='g-', markerfmt='go', basefmt='g-', 
                   label=f'Sampled at {fs2}Hz')
    axs[1, 0].set_xlabel('Time (s)', fontsize=10)
    axs[1, 0].set_ylabel('Amplitude', fontsize=10)
    axs[1, 0].set_title(f'Time Domain: {f}Hz Signal Sampled at {fs2}Hz', fontsize=12, fontweight='bold')
    axs[1, 0].legend()
    axs[1, 0].grid(True, alpha=0.3)
    axs[1, 0].axhline(y=0, color='k', linewidth=0.5)
    
    # Frequency domain - 50Hz sampling
    axs[1, 1].stem(freqs2[:len(freqs2)//2], np.abs(X_sample2)[:len(X_sample2)//2], 
                   linefmt='g-', markerfmt='go', basefmt='g-')
    axs[1, 1].set_xlabel('Frequency (Hz)', fontsize=10)
    axs[1, 1].set_ylabel('Magnitude', fontsize=10)
    axs[1, 1].set_title(f'Frequency Domain: Sampled at {fs2}Hz', fontsize=12, fontweight='bold')
    axs[1, 1].grid(True, alpha=0.3)
    axs[1, 1].set_xlim(0, fs2/2)
    plt.show()

def four():
    """
    Generate continuous sinusoidal x(t)=sin(2π*5*t) and sample at 
    10Hz, 20Hz, and 50Hz over 1 second. Plot continuous and sampled signals.
    """
    # Signal parameters
    f = 5  # Signal frequency in Hz
    duration = 1  # 1 second
    
    # Continuous signal
    t_cont = np.linspace(0, duration, 1000)
    x_cont = np.sin(2 * np.pi * f * t_cont)
    
    # Sample at different rates
    fs_rates = [10, 20, 50]  # Sampling frequencies
    
    # Create subplots
    fig, axs = plt.subplots(3, 1, figsize=(12, 10))
    
    for i, fs in enumerate(fs_rates):
        # Discrete sampling
        t_disc = np.arange(0, duration, 1/fs)
        x_disc = np.sin(2 * np.pi * f * t_disc)
        
        # Plot
        axs[i].plot(t_cont, x_cont, 'b-', linewidth=2, 
                    label='Continuous Signal', alpha=0.7)
        axs[i].stem(t_disc, x_disc, linefmt='r-', markerfmt='ro', 
                    basefmt='r-', label=f'Sampled at {fs}Hz')
        axs[i].set_xlabel('Time (seconds)', fontsize=10)
        axs[i].set_ylabel('Amplitude', fontsize=10)
        axs[i].set_title(f'Sampling at {fs}Hz (Nyquist Rate: {2*f}Hz)', 
                        fontsize=12, fontweight='bold')
        axs[i].legend()
        axs[i].grid(True, alpha=0.3)
        axs[i].axhline(y=0, color='k', linewidth=0.5)
    plt.show()

# Test the functions
# one()
# two()
# three()
# four()