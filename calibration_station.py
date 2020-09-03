import TEMPOL_functions as tmp
import os





class Calibration_Station():
   
    def __init__(self,sample_paths,std_path,sample_names=None,std_peaks=None):

        
        self.std_path = std_path
        self.std_peaks = std_peaks
        
        
        
        self.paths = paths
        self.sample_names = sample_names
        
        self.initialize_standard()
        self.run_standard_calibration()
        
    
    
    def sample_dic_init(self):
        self.sample_dic = {}
        
        if self.sample_names and len(self.sample_names) == len(self.paths):
            for i in range(len(self.paths)):
                self.sample_dic[self.sample_names[i]] = self.paths[i]
        
        elif self.sample_names:
            print('Number of elements in paths and sample names not equal\n'
                  + 'please double check your entries')
            
            for i in range(len(self.paths)):
                self.sample_dic[str(i)] = self.paths[i]
                
        else:
            for i in range(len(self.paths)):
                self.sample_dic[str(i)] = self.paths[i]
                
    
    def initialize_standard(self):
        if not self.std_peaks:
            self.std_peaks = {'1':[1000,1500],
                              '2':[1750,2500],
                              '3':[2750,3250]
                              }
            
    
    def run_standard_calibration(self):
        
        self.std_cal_pm, self.std_pk_pm = tmp.tmp_cal(self.std_path, 
                                                      self.std_peaks)
        
        
