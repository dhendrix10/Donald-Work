import matplotlib.pyplot as plt
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
        
filename = 'data/olivine_run_2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    fields_2, dA_dFs_2 = [], []
    for row in reader:
        field_2 = float(row[0])
        dA_dF_2 = int(row[1])
        dA_dFs_2.append(dA_dF_2)
        fields_2.append(field_2)
        
filename = 'data/olivine_run_3.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    fields_3, dA_dFs_3 = [], []
    for row in reader:
        field_3 = float(row[0])
        dA_dF_3 = int(row[1])
        dA_dFs_3.append(dA_dF_3)
        fields_3.append(field_3)

plt.style.use('seaborn-white')
fig, ax = plt.subplots()


ax.plot(fields_1, dA_dFs_1, label = 'Run 1')
ax.plot(fields_2, dA_dFs_2, label = 'Run 2')
ax.plot(fields_3, dA_dFs_3, label = 'Run 3')
ax.tick_params(axis = 'both', length = 10, width = 2, direction = 'out',
               labelsize = 18)

leg = ax.legend();
ax.legend(frameon = True, loc = 'lower right', fontsize = 18)


plt.title("Olivine DMPO-OH", fontsize = 24)
plt.xlabel("Field (mT)", fontsize = 18)
plt.ylabel("dA/dF", fontsize = 18)
plt.axis([332,340,8000,24000])
ax.set_xticks()


plt.show()
