import matplotlib.pyplot as plt
import csv
import os
import numpy as np
from sklearn.linear_model import LinearRegression

def get_da_dFs(filename):
    """Gets concentration data from your files"""
    
    #Opens file
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        fields = []
        dA_dFs = []
        
        #Appends data to lists
        for row in reader:
            fields.append(float(row[0]))
            dA_dFs.append(int(row[1]))
            
        
        
        
      
    
    return fields, dA_dFs


def get_concentrations(path,plot=True):
    """Reads  concentrations from files and plots them if you 
    so choose, outputs a data dictionary containing the Fields and dA_dFs
    parameters for each concentration file"""
    
    #Data dictionary
    data = {}
    
    #Gets all the files in the concentrations folder
    files = os.listdir(path)
    
    #Populates the data dictionary with entries corresponding to each
    #File in the concentrations folder
    for file in files:
        file_path = '/'.join([path,file])
        fields, dA_dFs = get_da_dFs(file_path)
        name = file.split('.',2)[0]
        data[name] = {'Field':fields,'dA_dFs':dA_dFs}
    
    #Plots a graph with the collected data if you want it
    if plot:
        plt.style.use('seaborn-white')
        fig, ax = plt.subplots()
        
        #plots a new axis for each entry in the dictionary
        for key, value in data.items():
            x = value['Field']
            y = value['dA_dFs']
            try:
                label = int(key) / 10
            except ValueError:
                label = key
            ax.plot(x, y, label = label)
        
        #Sets the tick marks 
        lower_bound = int(min(x)) + 1
        upper_bound = int(max(x)) 
        print(lower_bound,upper_bound)
        ticks = [(lower_bound + i) for i in range(upper_bound-lower_bound+1)]
        
        
        #Graph properties
        ax.tick_params(axis = 'both', length = 10, width = 2, direction = 'out',
                        labelsize = 18)
        
        leg = ax.legend();
        ax.legend(frameon = True, loc = 'lower right', fontsize = 18)
        
        
        plt.title("TEMPOL EPR Graphs- 062620", fontsize = 24)
        plt.xlabel("Field (mT)", fontsize = 18)
        plt.ylabel("dA/dF", fontsize = 18)
        plt.axis([lower_bound,upper_bound,8000,24000])
        
        ax.set_xticks(ticks)
        
        
        plt.show()
    
    
    return data

def get_peak_parameters(path,peaks,conce_plot=False):
    """Calls get_concentrations() and uses the gathered concentration data
    to generate a peak parameters dictionary containing the following:
        (1) Peak parameters Data
        (2) Total intensity of all peaks
        (3) Average peak intensity
        (4) Concentration spectrum data
        """
    
    data = get_concentrations(path,plot=conce_plot)
    

    
    peak_parameters = {}
    for key, val in data.items():
        conce_params = {}
        x = val['Field']
        y = val['dA_dFs']
        
        total_intensity = 0
        for k,v in peaks.items():
            
            y_range = y[v[0]:v[1]]
            y_intensity = max(y_range) - min(y_range)
            conce_params[k] = {'Range':[v[0],v[1]],
                                  'Intensity':y_intensity
                                  }
            total_intensity += y_intensity
        
        avg_int = total_intensity / len(peaks)
        
        peak_parameters[key] = {'Peak_Params':conce_params,
                              'Total_Intensity':total_intensity,
                              'Avg_Int':avg_int,
                              'Field':x,
                              'dA_dFs':y
                              }
        
    return peak_parameters


def tmp_cal(path,peaks,cal_plot=False,std_plot=False):
    """Performs a concentration spectrum calibration based on
    input standards, use the parameters of the best fit linear
    function to calculate unknown concentrations of targeted samples.
    """
    
    cal_params = {}
    
    
    #Get peak parameters
    pk_pm = get_peak_parameters(path,peaks,std_plot)
    
    #Get the calibration curve data from peak parameters
    tempol_concentrations = np.array([float(key)/10 for key in pk_pm.keys()])
    y_averages = np.array([pk_pm[key]['Avg_Int'] for key in pk_pm.keys()])
    
    x = tempol_concentrations
    y = y_averages
    
    
    
    #Linear Regression Calibration
    linreg = LinearRegression()
    x = x.reshape(-1, 1)
    linreg.fit(x, y)
    y_pred = linreg.predict(x)
    
    #Find equation
    m = float(linreg.coef_)
    b = linreg.intercept_
    print(f"m = {m}")
    print(f"b = {b}")
    print(f"Equation: y = {m}x + {b}")
    
    #r^2 value
    regressor = LinearRegression(fit_intercept= False)
    regressor.fit(x, y)
    print(f"r^2 value = {regressor.score(x, y)}")
    
    cal_params['m'] = m
    cal_params['b'] = b
    cal_params['x'] = x
    cal_params['y'] = y
    
    if cal_plot:
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


    return cal_params, pk_pm
    
