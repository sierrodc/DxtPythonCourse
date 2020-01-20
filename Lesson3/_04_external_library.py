# Import the necessary packages and modules
# req
# pip install numpy
# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

# vantaggi di numpy per memorizzare array
# - operazioni efficienti -> c, 
# - località spaziale -> numeri salvati (di un certo tipo) in luogo contiguo (cache cpu)
# - operazioni vettorizzate (SIMD, SSE, AVX...)
# - ottimizzazione da altre librerie BLAS/LAPACK/MKL/Multithread...

# Prepare the data
x = np.linspace(0, 15, 100)
print(f"la somma degli elementi di x è: {x.sum()}")
y = x ** 2

# Plot the data
plt.plot(x, y, label='x^2')
plt.plot([0, 5, 8, 13], [10, 20, 25, 80], color='lightblue', linewidth=3)
plt.scatter([1, 3, 7, 12], [11, 25, 9, 26], color='darkgreen', marker='^')

# Add legend
plt.legend()
plt.title("This is the title")
plt.xlabel("X label")

# Show the plot
plt.show(block=True)