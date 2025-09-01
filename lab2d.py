import matplotlib.pyplot as plt
n_values = [100, 500, 1000, 5000, 10000]
time_values=[0.000018,0.000276,0.001080 ,0.032526, 0.154258,] # in seconds
plt.plot(n_values, time_values, marker='o')
plt.title("Selection Sort: Time vs Number of Elements")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.grid(True)
plt.show()