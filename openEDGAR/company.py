import requests
from bs4 import BeautifulSoup
from cached_property import cached_property
from openEDGAR.utils.mapping import Mapper
from openEDGAR.utils.sic import *
import regex

mapper = Mapper()


class Company(object):
    """An EDGAR company
    """

  def __init__(self, cik):
    self.cik = cik
    
    params = { "action": "getcompany", "CIK": self.cik, "count": 0}
    company_webpage = requests.get("https://www.sec.gov/cgi-bin/browse-edgar", params=params)
		
    soup = BeautifulSoup(company_webpage.text, "lxml")
    # Standard Industrial Code https://en.wikipedia.org/wiki/Standard_Industrial_Classification
    title = soup.find("acronym", title="Standard Industrial Code")
    self.sic = int(title.next_sibling.next_sibling.string)
    self.division = sic_to_division[self.sic] 
    self.industry = sic_to_industry[self.sic]
    """
    self.state_location = 
    self.fiscal_year_end =
    """

        """
        self.business_adress =
        self.mailing_adress =
        """

    @cached_property
    def name(self):
        pass

    @classmethod
    def fromName(cls, name):
        return cls(mapper.name_to_cik[name])

    @classmethod
    def fromTicker(cls, ticker):
        return cls(mapper.ticker_to_cik[ticker])


c1 = Company(1318605)

print(c1.__dict__)
