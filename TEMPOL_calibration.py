import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np



filename = 'data/05.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) 
    
    fields, dA_dFs = [], []
    for row in reader:
        field = float(row[0])
        dA_dF = int(row[1])
        fields.append(field)
        dA_dFs.append(dA_dF)
    
y_range_first_peak_05 = dA_dFs[1000:1500]
max_05y_first_peak = max(y_range_first_peak_05)
min_05y_first_peak = min(y_range_first_peak_05)
y_intensity_first_peak_05 = max_05y_first_peak - min_05y_first_peak


y_range_second_peak_05 = dA_dFs[1750:2500]
max_05y_second_peak = max(y_range_second_peak_05)
min_05y_second_peak = min(y_range_second_peak_05)
y_intensity_second_peak_05 = max_05y_second_peak - min_05y_second_peak


y_range_third_peak_05 = dA_dFs[2750:3250]
max_05y_third_peak = max(y_range_third_peak_05)
min_05y_thrid_peak = min(y_range_third_peak_05)
y_intensity_third_peak_05 = max_05y_third_peak - min_05y_thrid_peak


y_05_total_intensities = (y_intensity_first_peak_05 +
                          y_intensity_second_peak_05 +
                          y_intensity_third_peak_05)

average_05 = y_05_total_intensities / 3
print(average_05)

       
filename = 'data/10.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  
    
    fields_1, dA_dFs_1 = [], []
    for row in reader:
        field_1 = float(row[0])
        dA_dF_1 = int(row[1])
        dA_dFs_1.append(dA_dF_1)
        fields_1.append(field_1)
        
y_range_first_peak_10 = dA_dFs_1[1000:1500]
max_10y_first_peak = max(y_range_first_peak_10)
min_10y_first_peak = min(y_range_first_peak_10)
y_intensity_first_peak_10 = max_10y_first_peak - min_10y_first_peak


y_range_second_peak_10 = dA_dFs_1[1750:2500]
max_10y_second_peak = max(y_range_second_peak_10)
min_10y_second_peak = min(y_range_second_peak_10)
y_intensity_second_peak_10 = max_10y_second_peak - min_10y_second_peak


y_range_third_peak_10 = dA_dFs_1[2750:3250]
max_10y_third_peak = max(y_range_third_peak_10)
min_10y_thrid_peak = min(y_range_third_peak_10)
y_intensity_third_peak_10 = max_10y_third_peak - min_10y_thrid_peak


y_10_total_intensities = (y_intensity_first_peak_10 +
                          y_intensity_second_peak_10 +
                          y_intensity_third_peak_10)

average_10 = y_10_total_intensities / 3
print(average_10)
        
filename = 'data/20.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  
    
    fields_2, dA_dFs_2 = [], []
    for row in reader:
        field_2 = float(row[0])
        dA_dF_2 = int(row[1])
        dA_dFs_2.append(dA_dF_2)
        fields_2.append(field_2)
        
y_range_first_peak_20 = dA_dFs_2[1000:1500]
max_20y_first_peak = max(y_range_first_peak_20)
min_20y_first_peak = min(y_range_first_peak_20)
y_intensity_first_peak_20 = max_20y_first_peak - min_20y_first_peak


y_range_second_peak_20 = dA_dFs_2[1750:2500]
max_20y_second_peak = max(y_range_second_peak_20)
min_20y_second_peak = min(y_range_second_peak_20)
y_intensity_second_peak_20 = max_10y_second_peak - min_20y_second_peak


y_range_third_peak_20 = dA_dFs_2[2750:3250]
max_20y_third_peak = max(y_range_third_peak_20)
min_20y_third_peak = min(y_range_third_peak_20)
y_intensity_third_peak_20 = max_20y_third_peak - min_20y_third_peak


y_20_total_intensities = (y_intensity_first_peak_20 +
                          y_intensity_second_peak_20 +
                          y_intensity_third_peak_20)

average_20 = y_20_total_intensities / 3
print(average_20)
        
filename = 'data/30.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  
    
    fields_3, dA_dFs_3 = [], []
    for row in reader:
        field_3 = float(row[0])
        dA_dF_3 = int(row[1])
        dA_dFs_3.append(dA_dF_3)
        fields_3.append(field_3)
        
y_range_first_peak_30 = dA_dFs_3[1000:1500]
max_30y_first_peak = max(y_range_first_peak_30)
min_30y_first_peak = min(y_range_first_peak_30)
y_intensity_first_peak_30 = max_30y_first_peak - min_30y_first_peak


y_range_second_peak_30 = dA_dFs_3[1750:2500]
max_30y_second_peak = max(y_range_second_peak_30)
min_30y_second_peak = min(y_range_second_peak_30)
y_intensity_second_peak_30 = max_30y_second_peak - min_30y_second_peak


y_range_third_peak_30 = dA_dFs_3[2750:3250]
max_30y_third_peak = max(y_range_third_peak_30)
min_30y_third_peak = min(y_range_third_peak_30)
y_intensity_third_peak_30 = max_30y_third_peak - min_30y_third_peak


y_30_total_intensities = (y_intensity_first_peak_30 +
                          y_intensity_second_peak_30 +
                          y_intensity_third_peak_30)

average_30 = y_30_total_intensities / 3
print(average_30)

#Make the calibration curve
tempol_concentrations = [0.5, 1.0, 2.0, 3.0]
y_averages = [average_05, average_10, average_20, average_30]

x = np.array([0.5, 1.0, 2.0, 3.0])
y = np.array([average_05, average_10, average_20, average_30])
linreg = LinearRegression()
x = x.reshape(-1, 1)
linreg.fit(x, y)
y_pred = linreg.predict(x)

#Find equation
m = linreg.coef_
b = linreg.intercept_
print(f"m = {m}")
print(f"b = {b}")
print(f"Equation: y = {m}x + {b}")

#r^2 value
regressor = LinearRegression(fit_intercept= False)
regressor.fit(x, y)
print(f"r^2 value = {regressor.score(x, y)}")

plt.style.use('seaborn-white')
fig, ax = plt.subplots()
ax.scatter(tempol_concentrations, y_averages, s = 50)
ax.plot(x, y_pred, c = 'red', label = f"y = {m}x + {b}")
ax.plot([], [], '', label = f"r^2 = {regressor.score(x, y)}", c = 'white')

ax.set_title("TEMPOL Calibration", fontsize = 24)
ax.set_xlabel("Concentration (\u03BCM)", fontsize = 18)
ax.set_ylabel("dA/dF", fontsize = 18)
ax.tick_params(axis = 'both', length = 10, width = 2, direction = 'out',
               labelsize = 18)

ax.plot(label = f"y = {m}x + b")
leg = ax.legend();
ax.legend("Text")
ax.legend(frameon = True, loc = 'lower right', fontsize = 18)

plt.show()


    




        
