from enum import IntEnum
class Metric(IntEnum):
  KILO = 1000

class Energy():
  def __init__(self, temp_start, temp_end):
    self.temp_start = temp_start
    self.temp_end = temp_end
  
  def get_delta(self):
   self.delta_temp = self.temp_end - self.temp_start  
  
  def calculate_total_energy(self, wat, time_sec):
    self.total_energy = wat * time_sec

  def calculate_used_energy(self, mass = 1):
    self.used_energy = round(((mass * 4.18) * self.delta_temp) * Metric.KILO)
  
  def calculate_thermal_efficiency(self):
    self.efficiency = self.used_energy / self.total_energy
  
  def print_used_energy(self):
    print(self.used_energy)
  def print_total_energy(self):
    print(self.total_energy)
  def print_efficiency(self):
    print("{0:.2f}".format(self.efficiency * 100))
    


temp_dict = {
  "microwave": [15, 30],
  "boiler": [17.6, 59],
  "stove": [18.2, 44.4]
}

wat_dict = {
  "microwave": 700,
  "boiler": 1600,
  "stove": 2500
}


# Puts all the data into one area
def LoopDict(temp_dict, wat_dict):
  result_dict = {}
  for key in temp_dict:
    result_dict[key] = (Energy(temp_dict[key][0], temp_dict[key][1]))
    result_dict[key].get_delta()
    result_dict[key].calculate_used_energy()
    result_dict[key].calculate_total_energy(wat_dict[key], 120)
    result_dict[key].calculate_thermal_efficiency()

  return result_dict

def PrintDict(result_dict):
  for key in result_dict:
    print('''
    Heat source: {0}
    Used energy: {1}\n
    Total energy: {2}\n
    Thermal efficiency: {3:.2f}%\n

    '''.format(key, result_dict[key].used_energy, result_dict[key].total_energy, result_dict[key].efficiency*100))


PrintDict(LoopDict(temp_dict, wat_dict))

