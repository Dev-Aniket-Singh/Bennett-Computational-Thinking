# Personal Finance and Investment System

A console-based Python project for stock information, portfolio and trade tracking, and daily expense management.

## Files

- main.py - source code for all three application modules.
- Project_Report.pdf - project report following the supplied course format, with pseudocode and a flowchart.
- requirements.txt - third-party Python packages used by the source.

## Run

Use Python 3, then install the dependencies and start the program:

    python -m pip install -r requirements.txt
    python main.py

Choose a module from the main menu. The stock analyzer accepts ticker symbols such as AAPL, MSFT, or RELIANCE.NS.

## Notes

- The program requests market information through yfinance; values may be unavailable when the external service does not return data.
- Holdings, trades, expenses, and recurring schedules are stored in memory and are cleared when the program exits.
- The dollar formatting in the supplied program is fixed, including for tickers that may trade in another currency.
- The project is an educational tracker and does not provide investment advice.
- The report includes screenshot and test-result placeholders for the team to complete after running the program.

## Team

- **Aniket Singh** - Project idea proposer; requirements and project documentation.
- **Utkarsh Vijay** - Project Leader; coordinates integration across the market-data, stock-analysis, portfolio, charting, and menu features.
- **Parth Mishra** - Stock and investment fundamentals.
- **Kumar Udayaditya Prakash** - Fundamental and technical stock analysis.
- **Md Hossen Shahin Rana** - Expense Tracker.
