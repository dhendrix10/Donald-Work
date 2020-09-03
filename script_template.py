import TEMPOL_functions as tf

"""A  template script  for calculating concentrations of your samples"""

#Calibration standard peaks
s_peaks = {'1':[1000,1500],
           '2':[1750,2500],
           '3':[2750,3250]
           }

#Sample peaks
d_peaks = {'1':[1500,2250],
           '2':[2250,3000]
           }

#Standard folder path
s_path = 'C:/Path/Standards

#Sample folder path
d_path = 'C:/Path/Samples

#Get calibration parameters
cal_params, s_pk_pm = tf.tmp_cal(s_path, s_peaks, cal_plot=False)

#Get peak parameters of samples
d_pk_pm = get_peak_parameters(d_path, d_peaks, conce_plot=False)

#Get sample concentrations
concentrations = calc_concentrations(d_pk_pm,cal_params)
