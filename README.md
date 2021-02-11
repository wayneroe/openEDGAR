# openEDGAR
**openEDGAR** is an easy to use library for the [EDGAR](https://www.sec.gov/edgar/about) (**E**lectronic **D**ata **G**athering, **A**nalysis, and **R**etrieval) System.
```python
>>> import openEDGAR as edgar
>>> company = edgar.Company("TESLA MOTORS INC")
>>> company.fiscal_year_end
1231
>>> company.cik
0001318605
>>> annual_report = company.get_annual_report(2018)
>>> annual_report.statements_of_operation["Total revenues"]
21461268
```
