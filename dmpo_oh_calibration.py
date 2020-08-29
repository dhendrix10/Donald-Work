import csv


filename = 'data/olivine_run_1.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) 
    
    fields_1, dA_dFs_1 = [], []
    for row in reader:
        field_1 = float(row[0])
        dA_dF_1 = int(row[1])
        dA_dFs_1.append(dA_dF_1)
        fields_1.append(field_1)
    
y_range_first_peak_1 = dA_dFs_1[1500:2250]
max_y_first_peak_1 = max(y_range_first_peak_1)
min_y_first_peak_1 = min(y_range_first_peak_1)
y_intensity_first_peak_1 = max_y_first_peak_1 - min_y_first_peak_1


y_range_second_peak_1 = dA_dFs_1[2250:3000]
max_y_second_peak_1 = max(y_range_second_peak_1)
min_y_second_peak_1 = min(y_range_second_peak_1)
y_intensity_second_peak_1 = max_y_second_peak_1 - min_y_second_peak_1

y_total_intensities_1 = (y_intensity_first_peak_1 +
                          y_intensity_second_peak_1)

average_1 = y_total_intensities_1 / 2
print(average_1)

       
filename = 'data/olivine_run_2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  
    
    fields_2, dA_dFs_2 = [], []
    for row in reader:
        field_2 = float(row[0])
        dA_dF_2 = int(row[1])
        dA_dFs_2.append(dA_dF_2)
        fields_2.append(field_2)
        
y_range_first_peak_2 = dA_dFs_2[1500:2250]
max_y_first_peak_2 = max(y_range_first_peak_2)
min_y_first_peak_2 = min(y_range_first_peak_2)
y_intensity_first_peak_2 = max_y_first_peak_2 - min_y_first_peak_2


y_range_second_peak_2 = dA_dFs_2[2250:3000]
max_y_second_peak_2 = max(y_range_second_peak_2)
min_y_second_peak_2 = min(y_range_second_peak_2)
y_intensity_second_peak_2 = max_y_second_peak_2 - min_y_second_peak_2

y_total_intensities_2 = (y_intensity_first_peak_2 +
                          y_intensity_second_peak_2)

average_2 = y_total_intensities_2 / 2
print(average_2)
        
filename = 'data/olivine_run_3.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  
    
    fields_3, dA_dFs_3 = [], []
    for row in reader:
        field_3 = float(row[0])
        dA_dF_3 = int(row[1])
        dA_dFs_3.append(dA_dF_3)
        fields_3.append(field_3)
        
y_range_first_peak_3 = dA_dFs_3[1500:2250]
max_y_first_peak_3 = max(y_range_first_peak_3)
min_y_first_peak_3 = min(y_range_first_peak_3)
y_intensity_first_peak_3 = max_y_first_peak_3 - min_y_first_peak_3


y_range_second_peak_3 = dA_dFs_3[2250:3000]
max_y_second_peak_3 = max(y_range_second_peak_3)
min_y_second_peak_3 = min(y_range_second_peak_3)
y_intensity_second_peak_3 = max_y_second_peak_3 - min_y_second_peak_3

y_total_intensities_3 = (y_intensity_first_peak_3 +
                          y_intensity_second_peak_3)

average_3 = y_total_intensities_3 / 2
print(average_3)



    
    