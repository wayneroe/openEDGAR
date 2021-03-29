# openEDGAR
**openEDGAR** is an easy to use library for the [EDGAR](https://www.sec.gov/edgar/about) (**E**lectronic **D**ata **G**athering, **A**nalysis, and **R**etrieval) System.
```python
>>> import openEDGAR as edgar
>>> company = edgar.from_ticker("TSLA")
>>> company.division
Manufacturing
>>> company.industry
Motor Vehicles & Passenger Car Bodies
>>> # Downloads the annual report about 2018
>>> annual_report = company.get_annual_report(2018)
>>> annual_report.statements_of_operation["Total revenues"]
21461268
>>> annual_report.balance_sheet["Total Assets"]
```
