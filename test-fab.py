import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(count):
    """Generate the first 'count' prime numbers."""
    primes = []
    candidate = 2
    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def plot_prime_spiral(primes):
    """Plot a Fibonacci spiral using the prime numbers."""
    angles = np.linspace(0, 2 * np.pi, len(primes), endpoint=False)
    radius = np.cumsum(primes)  # Cumulative sum to spread the spiral
    theta = np.linspace(0, 4 * np.pi, len(primes))  # Increase the angle for the spiral

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, marker='o', label='Prime Spiral')
    for i, prime in enumerate(primes):
        plt.text(x[i], y[i], str(prime), fontsize=8, ha='center')

    plt.title("Fibonacci Spiral with Prime Numbers")
    plt.axis('equal')
    plt.legend()
    plt.show()

# Parameters
num_primes = 50  # Number of prime numbers to use

# Generate and plot
prime_numbers = generate_primes(num_primes)
plot_prime_spiral(prime_numbers)
