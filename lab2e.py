import matplotlib.pyplot as plt
n_values = [100, 500, 1000, 5000, 10000]
time_values=[0.000014,0.000264,0.001033, 0.025568, 0.103294] # in seconds
plt.plot(n_values, time_values, marker='o')
plt.title("Insertion Sort: Time vs Number of Elements")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.grid(True)
plt.show()