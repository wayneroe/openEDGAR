from unittest import TestCase
from openEDGAR.utils.mapping import Mapper


"""
mapping = Mapper()
print(mapping.ticker["TSLA"])
print(mapping.ticker["TsLa"])
print(mapping.name["tesla motors inc"])
print(mapping.name["TeSlA mOtOrS iNc"])
print(mapping.name["11:11 CAPITAL CORP."])
"""


class TestMapper(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._mapper = Mapper()

    def test_ticker_to_cik(self):
        self.assertTrue(self._mapper.ticker_to_cik["TSLA"], 1318605)
        self.assertTrue(self._mapper.ticker_to_cik["TsLa"], 1318605)
        try:
            self._mapper.ticker_to_cik["a;lsn;e"]
        except KeyError:
            pass
        except Exception:
            self.fail("unexpected exception raised")
        else:
            self.fail("ExpectedException not raised")

    def test_name_to_cik(self):
        self.assertTrue(self._mapper.name_to_cik["tesla motors inc"], 1318605)
        self.assertTrue(self._mapper.name_to_cik["TeSlA mOtOrS iNc"], 1318605)
        self.assertTrue(self._mapper.name_to_cik["11:11 CAPITAL CORP."], 1463262)
