# FX rate reference table — TEMPLATE

Copy this file to `sources/fx_rates.md` in your project and fill in
the rates you use. Every figure in the report that involves an FX
conversion should be re-derivable from this table.

## Reference rates

| Currency | A$1 buys | A$ per 1 unit | Reference date | Source |
|---|---:|---:|---|---|
| USD | <fill> | <fill> | <date> | RBA daily F11.1 |
| EUR | <fill> | <fill> | <date> | RBA daily F11.1 |
| GBP | <fill> | <fill> | <date> | RBA daily F11.1 |
| JPY | <fill> | <fill> | <date> | RBA daily F11.1 |
| NOK | <fill> | <fill> | <date> | RBA daily F11.1 |
| RM (MYR) | <fill> | <fill> | <date> | OANDA / RBA |
| QAR | <fill> | <fill> | <date> | pegged to USD |
| (add others as needed) | | | | |

## When to use FY-average vs spot

- **Headline current-year claims**: use the spot rate on the report
  date (above).
- **Historical FY-specific figures**: use the FY-average rate for
  that year (RBA F11.2 monthly history; average across 12 months).
- **Year-over-year time series**: be consistent — either all FY-avg
  or all spot, but state which in the table header.

## Worked examples

For every figure in the report that's been converted, add a row here
so a reader can verify the conversion is right:

| Native figure | × rate | AUD figure | Used in |
|---|---|---|---|
| ... | ... | **A$...** | report.md section X.Y |

## Sensitivity

State whether the report's headline conclusions survive ±10% FX-rate
variation. If not, identify which claims are FX-sensitive.

## Primary-source links

- RBA Statistical Tables F11.1 (Daily): https://www.rba.gov.au/statistics/tables/
- RBA Statistical Tables F11.2 (Monthly): https://www.rba.gov.au/statistics/tables/xls-hist/f11.2-data.xlsx
- OANDA historical: https://www.oanda.com/currency-converter/en/

Reference date for the spot rates above: **YYYY-MM-DD**.
