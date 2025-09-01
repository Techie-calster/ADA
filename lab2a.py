import matplotlib.pyplot as plt
n_values = [100, 500, 1000, 5000, 10000, 50000,100000]
time_values=[0.000024, 0.000077 , 0.000168, 0.000885, 0.001830, 0.009555,0.019635] # in seconds
plt.plot(n_values, time_values, marker='o')
plt.title("Merge Sort: Time vs Number of Elements")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.grid(True)
plt.show()