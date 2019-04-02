from .entry import Entry

class CsvEntry(Entry):

  def __init__(self):
    Entry.__init__(self)

  def __repr__(self):
    return str(self.currency) + "," + str(self.date) + "," + str(self.rate) + "," + str(self.deposit) + "," + str(self.cost) + "," + str(self.withdrawl) + "," + str(self.proceeds) + "," + str(self.average_cost_basis) + "," + str(self.fee) + "," + str(self.fee_cost) + "," + str(self.sell_fee) + "," + str(self.network_fee) + "," + str(self.running_deposits) + "," + str(self.running_total_cost) + "," + str(self.running_average_cost) + "," + str(self.note
)