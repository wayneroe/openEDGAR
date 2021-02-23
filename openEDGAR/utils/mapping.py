import requests
from requests.structures import CaseInsensitiveDict
from cached_property import cached_property


class Mapper(object):
    """
    This class creates a map for
    name -> CIK
    ticker -> CIK
    Only when needed and caches them
    """

    @cached_property
    def ticker_to_cik(self) -> CaseInsensitiveDict:
        r = requests.get("https://www.sec.gov/include/ticker.txt")
        ticker_to_cik = CaseInsensitiveDict()

        for row in r.text.split("\n"):
            ticker, cik = row.split("\t")
            ticker_to_cik[ticker] = int(cik)

        return ticker_to_cik

    @cached_property
    def name_to_cik(self) -> CaseInsensitiveDict:
        r = requests.get("https://www.sec.gov/Archives/edgar/cik-lookup-data.txt")
        name_to_cik = CaseInsensitiveDict()

        for row in r.text.split("\n"):
            if row:
                split_index = row.rfind(":", 0, -1)
                name = row[:split_index]
                cik = row[split_index + 1:-1]
                name_to_cik[name] = int(cik)
        return name_to_cik
