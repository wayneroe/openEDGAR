import requests
from cached_property import cached_property
from utils.mapping import Mapper

mapper = Mapper()

class Company(object):
  """An EDGAR company

  """

  def __init__(self, cik):
    self.cik = cik

  @cached_property
  def name(self):
    pass

  @classmethod
  def fromName(cls, name):
    return cls(mapper.name[name])

  @classmethod
  def fromTicker(cls, ticker):
    return cls(mapper.ticker[ticker])

"""
c1 = Company.fromName("TESLA MOTORS INC")
c2 = Company(1318605)
c3 = Company.fromTicker("TSLA")

print(c1.cik, c2.cik, c3.cik)
"""
