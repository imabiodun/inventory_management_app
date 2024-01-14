class new_job:
  def __init__(self, date_start, date_end, workmanship_amount):
#    self.place = place
    self.date_start = date_start
    self.date_end = date_end
    self.workmanship_amount = workmanship_amount
    self.workers = []
  def battery(self, name, bat_type, volts, amps, price):
    self.name = name
    self.bat_type = bat_type
    self.volts = volts
    self.amps = amps
    self.price = price
  def panel(self, name, panel_type, watt, connection, price):
    self.name = name
    self.panel = panel_type
    self.watt = watt
    self.connection = connection
    self.price = price
   
  def inverter (self, name, power, price):
    self.name = name 
    self.power = power
    self.price = price
  def controller (self, name, type_, volts, amps, price):
    self.name = name
    self.type_ = type_
    self.volts = volts
    self.amps = amps
    self.price = price
  def owner(self, name, location, building_type):
    self.name = name
    self.location = location 
    self.building_type = building_type
  def num_of_workers(self,count:int ):
    for _ in range(count):
        name = input(f'Enter name {_}')
        self.worker.append(name)
  def wires (self, panel,battery):
    self.panel = panel
    self.battery = battery 
  def total_price():
    return controller.price + inverter.price + panel.price + battery.price + self.workmanship_amount
