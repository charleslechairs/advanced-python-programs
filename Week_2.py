# Sequence and Signal Generation in Python - EXP 12
# Generate unit step, ramp impulse and exponential signals in the range -10 to 10 and visualise the plot using python

import numpy as np
import matplotlib.pyplot as plt

def unit_step():
    """
    Unit Step Signal: u(n) = 1 for n >= 0, 0 for n < 0
    """
    n = np.arange(-10, 11)
    u = np.where(n >= 0, 1, 0)
    
    plt.figure(figsize=(10, 6))
    plt.stem(n, u, basefmt='blue', linefmt='blue', markerfmt='bo')
    plt.xlabel('n', fontsize=12)
    plt.ylabel('u(n)', fontsize=12)
    plt.title('Unit Step Signal', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.show()

def ramp():
    """
    Ramp Signal: r(n) = n for n >= 0, 0 for n < 0
    """
    n = np.arange(-10, 11)
    r = np.where(n >= 0, n, 0)
    
    plt.figure(figsize=(10, 6))
    plt.stem(n, r, basefmt='blue', linefmt='blue', markerfmt='bo')
    plt.xlabel('n', fontsize=12)
    plt.ylabel('r(n)', fontsize=12)
    plt.title('Ramp Signal', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.show()

def impulse():
    """
    Impulse Signal: δ(n) = 1 for n = 0, 0 otherwise
    """
    n = np.arange(-10, 11)
    delta = np.where(n == 0, 1, 0)
    
    plt.figure(figsize=(10, 6))
    plt.stem(n, delta, basefmt='blue', linefmt='blue', markerfmt='blue')
    plt.xlabel('n', fontsize=12)
    plt.ylabel('δ(n)', fontsize=12)
    plt.title('Impulse Signal', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.show()

def exponential():
    """
    Exponential Signal: x(n) = e^(a*n) for all n
    Using a = -0.2 for decaying exponential (e^(-0.2n))
    """
    n = np.arange(-10, 11)
    a = -0.2  # Negative for decay, positive for growth
    x = np.exp(a * n)
    plt.figure(figsize=(10, 6))
    plt.stem(n, x, basefmt='blue', linefmt='blue', markerfmt='blue')
    plt.xlabel('n', fontsize=12)
    plt.ylabel('x(n)', fontsize=12)
    plt.title('Exponential Signal', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axvline(x=0, color='black', linewidth=0.5)
    plt.show()

# Test the functions
unit_step()
ramp()
impulse()
exponential()

