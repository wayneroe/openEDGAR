import requests
from requests.structures import CaseInsensitiveDict
from cached_property import cached_property


class Mapper(object):
  """
  This class creates mappers for 
  name -> CIK
  ticker -> CIK
  Only when needed (lazy loading) and caches them
  """

  def __init__(self):
    pass

  @cached_property
  def ticker(self):
    """Return a CaseInsensitiveDict that maps every ticker to it's CIK"""
    r = requests.get("https://www.sec.gov/include/ticker.txt")
    mapping = CaseInsensitiveDict()

    for row in r.text.split("\n"):
      ticker, cik = row.split("\t")
      mapping[ticker] = int(cik)
    
    return mapping

  @cached_property
  def name(self):
    """Returns a CaseInsensitiveDict that maps every name to it's CIK"""
    r = requests.get("https://www.sec.gov/Archives/edgar/cik-lookup-data.txt") 
    mapping = CaseInsensitiveDict()

    for row in r.text.split("\n"):
      """The Lines are saved like this:
      BOESE GREG:0001725953:
      BOESEL JOHN P III:0001548867:
      BOESENBERG CHARLES:0001184213:

      Because there are some companies with a colon in their name, 
      we have to search the second colon from the back and can't just
      do split(":")
      11:11 CAPITAL CORP.:0001463262: 
                         ^
      """
      if row:
        split_index = row.rfind(":", 0, -1)
        name = row[:split_index]
        # +1 and -1 to not include the colons
        cik = row[split_index + 1:-1]
        mapping[name] = int(cik)

    return mapping
"""
mapping = Mapper()
print(mapping.ticker["TSLA"])
print(mapping.ticker["TsLa"])
print(mapping.name["tesla motors inc"])
print(mapping.name["TeSlA mOtOrS iNc"])
print(mapping.name["11:11 CAPITAL CORP."])
"""
