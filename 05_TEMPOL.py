import matplotlib.pyplot as plt
import csv

filename = 'data/05.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    
    fields, dA_dFs = [], []
    for row in reader:
        field = float(row[0])
        dA_dF = int(row[1])
        fields.append(field)
        dA_dFs.append(dA_dF)
        
filename = 'data/10.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    
    fields_1, dA_dFs_1 = [], []
    for row in reader:
        field_1 = float(row[0])
        dA_dF_1 = int(row[1])
        dA_dFs_1.append(dA_dF_1)
        fields_1.append(field_1)
        
filename = 'data/20.csv'
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
        
filename = 'data/30.csv'
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

ax.plot(fields, dA_dFs, label = '0.5 uM')
ax.plot(fields_1, dA_dFs_1, label = '1.0 uM')
ax.plot(fields_2, dA_dFs_2, label = '2.0 uM')
ax.plot(fields_3, dA_dFs_3, label = '3.0 uM')
ax.tick_params(axis = 'both', length = 10, width = 2, direction = 'out',
               labelsize = 18)

leg = ax.legend();
ax.legend(frameon = True, loc = 'lower right', fontsize = 18)


plt.title("TEMPOL EPR Graphs- 062620", fontsize = 24)
plt.xlabel("Field (mT)", fontsize = 18)
plt.ylabel("dA/dF", fontsize = 18)
plt.axis([332,340,8000,24000])
ax.set_xticks()


plt.show()
        