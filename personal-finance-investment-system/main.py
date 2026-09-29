from datetime import date, datetime
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
class StockAnalyzer:
  def __init__(self, ticker):
    self.ticker = ticker.strip().upper()
    self.stock = yf.Ticker(self.ticker)
  def plot_chart(self, series, title):
    if series.empty:
      print("\n[!] No data available to plot.")
      return
    plt.figure(figsize=(10, 5))
    plt.plot(
        series.index,
        series.values,
        label="Close Price",
        color="#1f77b4",
        linewidth=2,
    )
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel("Date", fontsize=11)
    plt.ylabel("Price ($)", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()
  def run_menu(self):
    while True:
      print("\n" + "─" * 60)
      print(f"     ACTIVE COMPANY: [{self.ticker}]")
      print("─" * 60)
      print("  1. Company Overview & Key Statistics")
      print("  2. Recent Price History & 1-Year Matplotlib Graph")
      print("  3. Annual Income Statement")
      print("  4. Annual Balance Sheet")
      print("  5. Annual Cash Flow Statement")
      print("  6. Analyst Recommendations")
      print("  7. Valuation Measures (P/E, PEG, Price-to-Book)")
      print("  8. Profitability & Margins (Profit Margin, ROE)")
      print("  9. Financial Health & Debt (Total Debt, Current Ratio)")
      print(" 10. Dividend & Yield Details")
      print(" 11. Growth & Earnings Metrics")
      print(" 12. Analyst Price Targets & Consensus")
      print(" 13. Ownership & Short Interest")
      print(" 14.       50-Day & 200-Day Moving Averages")
      print(" 15.        VIEW ALL CATEGORIES COMBINED")

      print("─" * 60)
      print("  0. Return to Main Menu")
      print("=" * 60)
      choice = input("      Select an option (0-15): ").strip()
      if choice == "0":
        break
      try:
        info = (
            self.stock.info
            if choice in [str(i) for i in [1, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
            else {}
        )
        if choice in ["1", "15"]:
          print(
              "\n"
              + f"        COMPANY OVERVIEW: {info.get('longName', self.ticker)} "
              .center(60, "=")
          )
          print(f" • Sector         : {info.get('sector', 'N/A')}")
          print(f" • Industry       : {info.get('industry', 'N/A')}")
          print(
              " • Current Price  :"
              f" ${info.get('currentPrice', info.get('regularMarketPrice', 'N/A'))}"
          )
          mc = info.get("marketCap")
          print(
              f" • Market Cap     : ${mc:,}"
              if isinstance(mc, int)
              else " • Market Cap     : N/A"
          )
          print(f" • 52-Week High   : ${info.get('fiftyTwoWeekHigh', 'N/A')}")
          print(f" • 52-Week Low    : ${info.get('fiftyTwoWeekLow', 'N/A')}")
          print("=" * 60)
        if choice in ["2", "15"]:
          hist = self.stock.history(period="1y")
          if not hist.empty:
            print("\n" + "       RECENT PRICE TABLE (Last 10 Days) ".center(60, "-"))
            print(
                hist[["Open", "High", "Low", "Close", "Volume"]]
                .tail(10)
                .to_string()
            )
            print("-" * 60)
            self.plot_chart(
                hist["Close"], title=f"{self.ticker} Share Price Trend (1 Year)"
            )
          else:

            print("\n[!] No historical price data found.")
        if choice in ["3", "15"]:
          print("\n" + "        INCOME STATEMENT ".center(60, "-"))
          stmt = self.stock.financials
          print(stmt.head(10).to_string() if not stmt.empty else "No data.")
        if choice in ["4", "15"]:
          print("\n" + "          BALANCE SHEET ".center(60, "-"))
          bs = self.stock.balance_sheet
          print(bs.head(10).to_string() if not bs.empty else "No data.")
        if choice in ["5", "15"]:
          print("\n" + "       CASH FLOW STATEMENT ".center(60, "-"))
          cf = self.stock.cashflow
          print(cf.head(10).to_string() if not cf.empty else "No data.")
        if choice in ["6", "15"]:
          print("\n" + "        ANALYST RECOMMENDATIONS ".center(60, "-"))
          recs = self.stock.recommendations
          print(
              recs.tail(5).to_string()
              if recs is not None and not recs.empty
              else "No recommendations."
          )
        if choice in ["7", "15"]:
          print("\n" + "      VALUATION MEASURES ".center(60, "-"))
          print(f" • Trailing P/E   : {info.get('trailingPE', 'N/A')}")
          print(f" • Forward P/E    : {info.get('forwardPE', 'N/A')}")
          print(f" • PEG Ratio      : {info.get('pegRatio', 'N/A')}")
          print(f" • Price to Book  : {info.get('priceToBook', 'N/A')}")
        if choice in ["8", "15"]:
          print("\n" + "    PROFITABILITY & MARGINS ".center(60, "-"))
          print(
              " • Profit Margin  :"
              f" {info.get('profitMargins', 0) * 100 if info.get('profitMargins') else 'N/A'}%"
          )
          print(
              " • Operating Margin:"
              f" {info.get('operatingMargins', 0) * 100 if info.get('operatingMargins') else 'N/A'}%"
          )
          print(
              " • Return on Equity:"
              f" {info.get('returnOnEquity', 0) * 100 if info.get('returnOnEquity') else 'N/A'}%"
          )
        if choice in ["9", "15"]:
          print("\n" + "     FINANCIAL HEALTH & DEBT ".center(60, "-"))
          tc = info.get("totalCash")
          print(
              f" • Total Cash     : ${tc:,}"
              if isinstance(tc, int)

              else " • Total Cash     : N/A"
          )
          td = info.get("totalDebt")
          print(
              f" • Total Debt     : ${td:,}"
              if isinstance(td, int)
              else " • Total Debt     : N/A"
          )
          print(f" • Debt to Equity : {info.get('debtToEquity', 'N/A')}")
          print(f" • Current Ratio  : {info.get('currentRatio', 'N/A')}")
        if choice in ["10", "15"]:
          print("\n" + "    DIVIDEND & YIELD DETAILS ".center(60, "-"))
          print(f" • Dividend Rate  : ${info.get('dividendRate', 'N/A')}")
          print(
              " • Dividend Yield :"
              f" {info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0}%"
          )
          print(
              " • Payout Ratio   :"
              f" {info.get('payoutRatio', 0) * 100 if info.get('payoutRatio') else 0}%"
          )
        if choice in ["11", "15"]:
          print("\n" + "         GROWTH & EARNINGS METRICS ".center(60, "-"))
          print(
              " • Earnings Growth:"
              f" {info.get('earningsGrowth', 0) * 100 if info.get('earningsGrowth') else 'N/A'}%"
          )
          print(
              " • Revenue Growth :"
              f" {info.get('revenueGrowth', 0) * 100 if info.get('revenueGrowth') else 'N/A'}%"
          )
        if choice in ["12", "15"]:
          print("\n" + "        ANALYST TARGETS & CONSENSUS ".center(60, "-"))
          print(f" • Target Mean Price : ${info.get('targetMeanPrice', 'N/A')}")
          print(
              " • Recommendation Key:"
              f" {str(info.get('recommendationKey', 'N/A')).upper()}"
          )
        if choice in ["13", "15"]:
          print("\n" + "    OWNERSHIP & SHORT INTEREST ".center(60, "-"))
          so = info.get("sharesOutstanding")
          print(
              f" • Shares Outstanding: {so:,}"
              if isinstance(so, int)
              else " • Shares Outstanding: N/A"
          )
          print(

              " • Held by Insiders  :"
              f" {info.get('heldPercentInsiders', 0) * 100 if info.get('heldPercentInsiders') else 'N/A'}%"
          )
          print(
              " • Short % of Float  :"
              f" {info.get('shortPercentOfFloat', 0) * 100 if info.get('shortPercentOfFloat') else 'N/A'}%"
          )
        if choice in ["14", "15"]:
          print("\n" + "       MOVING AVERAGES (TREND ANALYSIS) ".center(60, "-"))
          print(
              f" • 50-Day Moving Average  :"
              f" ${info.get('fiftyDayAverage', 'N/A')}"
          )
          print(
              f" • 200-Day Moving Average :"
              f" ${info.get('twoHundredDayAverage', 'N/A')}"
          )
          print("=" * 60)
      except Exception as e:
        print(f"\n[!] Error fetching data: {e}")
class PortfolioTracker:
  def __init__(self):
    self.watchlist = []
    self.realized_trades = []
  def run_menu(self):
    while True:
      print("\n" + "=" * 60)
      print("      MODULE 2: ADVANCED STOCK PORTFOLIO & TRADING TRACKER")
      print("=" * 60)
      print("  1. Add Stock, Shares & Purchase Price")
      print("  2. View Live Portfolio Valuation & Unrealized P&L")
      print("  3. Sell Shares at Current Market Price")
      print("  4. View Realized Trade History")
      print("  5. View Quick Fundamental Snapshot")
      print("  6. Analyze Best & Worst Performers")
      print("  7.   View Portfolio Sector Breakdown")
      print("  0. Return to Main Menu")
      print("=" * 60)
      choice = input("      Choose an option (1-7 or 0): ").strip()
      if choice == "0":
        break
      elif choice == "1":
        ticker = (
            input(" Enter Ticker Symbol (e.g., AAPL, MSFT, TSLA): ")
            .strip()
            .upper()
        )

        if ticker:
          try:
            shares = float(
                input(f" Enter number of shares owned for {ticker}: ")
            )
            buy_price = float(
                input(f" Enter average purchase price per share ($): ")
            )
            self.watchlist.append(
                {"ticker": ticker, "shares": shares, "buy_price": buy_price}
            )
            print(f"\n[✔] Success! Added {ticker} to your portfolio.")
          except ValueError:
            print("\n[!] Invalid numeric input entered.")
        else:
          print("\n[!] Invalid ticker.")
      elif choice == "2":
        if not self.watchlist:
          print("\n[!] Your portfolio watchlist is currently empty.")
        else:
          print("\n" + "       LIVE PORTFOLIO PERFORMANCE REPORT ".center(60, "="))
          tot_inv, tot_val = 0, 0
          for i, item in enumerate(self.watchlist, 1):
            t, s, bp = item["ticker"], item["shares"], item["buy_price"]
            cb = s * bp
            try:
              stk = yf.Ticker(t)
              info = stk.info
              cp = info.get("currentPrice", info.get("regularMarketPrice", 0.0))
              if not cp:
                hist = stk.history(period="1d")
                cp = hist["Close"].iloc[-1] if not hist.empty else 0.0
              hv = s * cp
              pl = hv - cb
              ret = (pl / cb) * 100 if cb > 0 else 0
              tot_inv += cb
              tot_val += hv
              icon = " " if pl >= 0 else " "
              print(f" {i}. [{t}] — {s} Shares")
              print(f"    Buy Avg: ${bp:,.2f} | Current Price: ${cp:,.2f}")
              print(f"    Invested: ${cb:,.2f} | Market Val: ${hv:,.2f}")
              print(f"    Unrealized P&L: {icon} ${pl:+,.2f} ({ret:+.2f}%)")
              print("-" * 60)
            except Exception as e:
              print(f" {i}. [{t}] — Could not fetch live data: {e}")
          net_pnl = tot_val - tot_inv
          net_ret = (net_pnl / tot_inv) * 100 if tot_inv > 0 else 0

          s_icon = "       " if net_pnl >= 0 else " "
          print(f" PORTFOLIO SUMMARY:")
          print(f"  • Total Cost Basis  : ${tot_inv:,.2f}")
          print(f"  • Current Valuation : ${tot_val:,.2f}")
          print(f"  • Unrealized Net P&L: {s_icon} ${net_pnl:+,.2f} ({net_ret:+.2f}%)")
          print("=" * 60)
      elif choice == "3":
        if not self.watchlist:
          print("\n[!] No stocks available in portfolio to sell.")
        else:
          print("\n Select a stock to sell shares from:")
          for i, item in enumerate(self.watchlist, 1):
            print(f"  {i}. {item['ticker']} ({item['shares']} shares available)")
          try:
            sel = int(input("      Enter stock number: ").strip())
            if 1 <= sel <= len(self.watchlist):
              holding = self.watchlist[sel - 1]
              t = holding["ticker"]
              stk = yf.Ticker(t)
              info = stk.info
              cp = info.get("currentPrice", info.get("regularMarketPrice", 0.0))
              if not cp:
                hist = stk.history(period="1d")
                cp = hist["Close"].iloc[-1] if not hist.empty else 0.0
              if cp <= 0:
                print("[!] Could not fetch a valid current market price.")
                continue
              print(f" [+] Current Market Price: ${cp:,.2f} per share")
              s_sell = float(
                  input(
                      f" Enter number of shares to sell (max"
                      f" {holding['shares']}): "
                  ).strip()
              )
              if 0 < s_sell <= holding["shares"]:
                cost_sold = s_sell * holding["buy_price"]
                proceeds = s_sell * cp
                real_pnl = proceeds - cost_sold
                real_pct = (real_pnl / cost_sold) * 100 if cost_sold > 0 else 0
                self.realized_trades.append({
                    "ticker": t,
                    "shares_sold": s_sell,
                    "buy_price": holding["buy_price"],
                    "sell_price": cp,
                    "realized_pnl": real_pnl,
                })
                holding["shares"] -= s_sell
                if holding["shares"] == 0:

                  self.watchlist.pop(sel - 1)
                print(f"\n[✔] Sale Executed Successfully!")
                print(f"  • Shares Sold    : {s_sell}")
                print(f"  • Execution Price: ${cp:,.2f}")
                print(f"  • Total Proceeds : ${proceeds:,.2f}")
                print(
                    f"  • Realized P&L   : ${real_pnl:+,.2f} ({real_pct:+.2f}%)"
                )
              else:
                print("\n[!] Invalid share quantity specified.")
            else:
              print("\n[!] Invalid selection number.")
          except ValueError:
            print("\n[!] Please enter valid numbers.")
      elif choice == "4":
        if not self.realized_trades:
          print("\n[!] No completed trades recorded yet.")
        else:
          print("\n" + "       REALIZED TRADE HISTORY ".center(60, "="))
          tot_prof = 0
          for i, trade in enumerate(self.realized_trades, 1):
            icon = " " if trade["realized_pnl"] >= 0 else " "
            print(
                f" {i}. [{trade['ticker']}] — Sold {trade['shares_sold']} shares"
            )
            print(
                f"    Bought: ${trade['buy_price']:,.2f} | Sold:"
                f" ${trade['sell_price']:,.2f}"
            )
            print(f"    Realized P&L: {icon} ${trade['realized_pnl']:+,.2f}")
            print("-" * 60)
            tot_prof += trade["realized_pnl"]
          t_icon = "       " if tot_prof >= 0 else " "
          print(f" Total Cumulative Realized Profit/Loss: {t_icon} ${tot_prof:+,.2f}")
          print("=" * 60)
      elif choice == "5":
        if not self.watchlist:
          print("\n[!] Your watchlist is currently empty.")
        else:
          print("\n Select a stock from your watchlist:")
          for i, item in enumerate(self.watchlist, 1):
            print(f"  {i}. {item['ticker']}")
          try:
            sel = int(input("      Enter stock number: ").strip())
            if 1 <= sel <= len(self.watchlist):
              t = self.watchlist[sel - 1]["ticker"]
              s_info = yf.Ticker(t).info

              print(
                  "\n"
                  + f"     SNAPSHOT: {s_info.get('longName', t)} ".center(
                      60, "="
                  )
              )
              print(f" • Sector         : {s_info.get('sector', 'N/A')}")
              print(f" • Industry       : {s_info.get('industry', 'N/A')}")
              print(
                  " • Current Price  :"
                  f" ${s_info.get('currentPrice', s_info.get('regularMarketPrice', 'N/A'))}"
              )
              print(f" • Trailing P/E   : {s_info.get('trailingPE', 'N/A')}")
              print(
                  " • Profit Margin  :"
                  f" {s_info.get('profitMargins', 0) * 100 if s_info.get('profitMargins') else 'N/A'}%"
              )
              print(
                  f" • 52-Week High   : ${s_info.get('fiftyTwoWeekHigh', 'N/A')}"
              )
              print(
                  f" • 52-Week Low    : ${s_info.get('fiftyTwoWeekLow', 'N/A')}"
              )
              print("=" * 60)
            else:
              print("\n[!] Invalid selection.")
          except ValueError:
            print("\n[!] Please enter a valid number.")
      elif choice == "6":
        if not self.watchlist:
          print("\n[!] Watchlist is empty.")
        else:
          print("\n" + "        PORTFOLIO PERFORMANCE SCANNER ".center(60, "="))
          best, worst, max_r, min_r = None, None, -999999, 999999
          for item in self.watchlist:
            t, bp = item["ticker"], item["buy_price"]
            try:
              s = yf.Ticker(t)
              curr = s.info.get(
                  "currentPrice", s.info.get("regularMarketPrice", 0.0)
              )
              if not curr:
                h = s.history(period="1d")
                curr = h["Close"].iloc[-1] if not h.empty else 0.0
              if curr and bp > 0:
                ret = ((curr - bp) / bp) * 100
                if ret > max_r:
                  max_r, best = ret, (t, ret)

                if ret < min_r:
                  min_r, worst = ret, (t, ret)
            except Exception:
              pass
          if best:
            print(f"        Best Performer  : [{best[0]}] with {best[1]:+.2f}% return")
          if worst:
            print(
                f"     Worst Performer : [{worst[0]}] with {worst[1]:+.2f}%"
                f" return"
            )
          print("=" * 60)
      elif choice == "7":
        if not self.watchlist:
          print("\n[!] Watchlist is empty.")
        else:
          print("\n" + "   PORTFOLIO SECTOR ALLOCATION ".center(60, "="))
          sec_totals = {}
          for item in self.watchlist:
            try:
              s = yf.Ticker(item["ticker"])
              sec = s.info.get("sector", "Unknown")
              val = item["shares"] * s.info.get(
                  "currentPrice",
                  s.info.get("regularMarketPrice", item["buy_price"]),
              )
              sec_totals[sec] = sec_totals.get(sec, 0.0) + val
            except Exception:
              sec_totals["Unknown"] = (
                  sec_totals.get("Unknown", 0.0)
                  + item["shares"] * item["buy_price"]
              )
          tot_val = sum(sec_totals.values())
          for sec, val in sorted(
              sec_totals.items(), key=lambda x: x[1], reverse=True
          ):
            pct = (val / tot_val) * 100 if tot_val > 0 else 0
            print(f" • {sec:<25} : ${val:>10,.2f} ({pct:>5.1f}% of portfolio)")
          print("=" * 60)
      else:
        print("\n[!] Invalid choice. Try again.")
class ExpenseTracker:
  def __init__(self):
    self.expense_records = []
    self.monthly_thresholds = {}  # Stores YYYY-MM -> threshold amount
    self.recurring_expenses = []
  def parse_amount(self, prompt):

    while True:
      try:
        val = float(input(prompt).strip())
        if val > 0:
          return val
        print("[!] Amount must be greater than zero.")
      except ValueError:
        print("[!] Please enter a valid numeric amount.")
  def valid_date_or_today(self, prompt=" Enter date (YYYY-MM-DD, blank = today): "):
    while True:
      raw = input(prompt).strip()
      if not raw:
        return date.today().isoformat()
      try:
        return datetime.strptime(raw, "%Y-%m-%d").date().isoformat()
      except ValueError:
        print("[!] Invalid date. Use YYYY-MM-DD.")
  def get_next_id(self):
    return (
        max([item.get("id", 0) for item in self.expense_records], default=0) + 1
    )
  def run_menu(self):
    while True:
      print("\n" + "=" * 70)
      print("       MODULE 3: ADVANCED DAILY EXPENSE & THRESHOLD TRACKER")
      print("=" * 70)
      print("  1. Add Daily Expense")
      print("  2. View Daily Expense Report")
      print("  3. Edit / Delete Expense")
      print("  4. Search Expenses")
      print("  5. Monthly Expense Dashboard & Threshold Warning")
      print("  6. Category Spending Analytics")
      print("  7. Set Monthly Expense Threshold Limit")
      print("  8. Cash-Flow & Spending Pattern Dashboard")
      print("  9. Monthly Savings Rate Calculator")
      print(" 10. Recurring Expense Manager")
      print("  0. Return to Main Menu")
      print("=" * 70)
      choice = input("      Select an option (0-10): ").strip()
      if choice == "0":
        break
      elif choice == "1":
        self.add_expense()
      elif choice == "2":
        self.view_expenses()
      elif choice == "3":
        self.edit_or_delete()
      elif choice == "4":

        self.search()
      elif choice == "5":
        self.monthly_summary()
      elif choice == "6":
        self.category_analytics()
      elif choice == "7":
        self.set_threshold()
      elif choice == "8":
        self.cashflow_dashboard()
      elif choice == "9":
        self.savings_calculator()
      elif choice == "10":
        self.recurring_manager()
      else:
        print("\n[!] Invalid option. Try again.")
  def add_expense(self):
    print("\n" + " ADD NEW EXPENSE ".center(70, "="))
    edate = self.valid_date_or_today()
    amt = self.parse_amount(" Enter expense amount ($): ")
    cat = (
        input(" Enter category (Food, Travel, Bills, Shopping, etc.): ")
        .strip()
        .title()
        or "Other"
    )
    subcat = input(" Enter sub-category: ").strip().title() or "General"
    desc = input(" Enter description/merchant: ").strip() or "Unspecified"
    pmethod = (
        input(" Payment method (Cash/Card/UPI/Bank/Other): ").strip().title()
        or "Other"
    )
    notes = input(" Optional notes: ").strip()
    rec = input(" Is this a recurring expense? (y/n): ").strip().lower() == "y"
    record = {
        "id": self.get_next_id(),
        "date": edate,
        "time": datetime.now().strftime("%H:%M:%S"),
        "amount": amt,
        "category": cat,
        "subcategory": subcat,
        "description": desc,
        "payment_method": pmethod,
        "notes": notes,
        "recurring": rec,
    }
    self.expense_records.append(record)
    if rec:
      self.recurring_expenses.append({

          "expense_id": record["id"],
          "description": desc,
          "category": cat,
          "amount": amt,
          "frequency": (
              input(" Frequency (daily/weekly/monthly): ").strip().lower()
              or "monthly"
          ),
          "next_due": edate,
      })
    print(f"\n[✔] Expense #{record['id']} saved successfully in-memory.")
    # Check threshold warning immediately upon adding an expense
    expense_month = edate[:7]
    if expense_month in self.monthly_thresholds:
      total_spent = sum(
          r["amount"]
          for r in self.expense_records
          if r.get("date", "").startswith(expense_month)
      )
      limit = self.monthly_thresholds[expense_month]
      if total_spent >= limit:
        print(
            f"\n       [WARNING] Monthly spending limit for {expense_month} has"
            f" been EXCEEDED! Limit: ${limit:,.2f} | Spent: ${total_spent:,.2f}"
        )
      elif total_spent >= limit * 0.8:
        print(
            f"\n    [ALERT] You are close to your limit for {expense_month} (Reached"
            f" {total_spent / limit * 100:.1f}%). Limit: ${limit:,.2f} | Spent:"
            f" ${total_spent:,.2f}"
        )
  def view_expenses(self):
    sdate = self.valid_date_or_today(
        " Enter date to view (YYYY-MM-DD, blank = today): "
    )
    recs = [r for r in self.expense_records if r.get("date") == sdate]
    print("\n" + f" DAILY EXPENSE REPORT — {sdate} ".center(90, "="))
    if not recs:
      print("[!] No expenses recorded for this date.")
      return
    tot = sum(r["amount"] for r in recs)
    for r in sorted(recs, key=lambda x: x.get("time", "")):
      print(
          f" #{r['id']:>3} | ${r['amount']:>10,.2f} | {r['category']:<15} |"
          f" {r['description']:<25} | {r['payment_method']}"
      )
    print("-" * 90)

    print(f" Total Spent: ${tot:,.2f} | Transactions: {len(recs)}")
    print("=" * 90)
  def set_threshold(self):
    print("\n" + " SET MONTHLY EXPENSE THRESHOLD LIMIT ".center(80, "="))
    month = input(" Enter month (YYYY-MM): ").strip()
    try:
      datetime.strptime(month, "%Y-%m")
    except ValueError:
      print("[!] Invalid month. Use YYYY-MM.")
      return
    limit = self.parse_amount(" Enter maximum spending threshold limit ($): ")
    self.monthly_thresholds[month] = limit
    print(
        f"[✔] Threshold set: Maximum limit for {month} is set to"
        f" ${limit:,.2f}."
    )
  def monthly_summary(self):
    rmonth = input(" Enter month (YYYY-MM, blank = current month): ").strip()
    if not rmonth:
      rmonth = date.today().strftime("%Y-%m")
    try:
      datetime.strptime(rmonth, "%Y-%m")
    except ValueError:
      print("[!] Invalid month. Use YYYY-MM.")
      return
    recs = [
        r for r in self.expense_records if r.get("date", "").startswith(rmonth)
    ]
    print("\n" + f" MONTHLY EXPENSE DASHBOARD — {rmonth} ".center(90, "="))
    if not recs:
      print("[!] No expenses recorded for this month.")
      return
    tot = sum(r["amount"] for r in recs)
    # Threshold Check & Warning
    if rmonth in self.monthly_thresholds:
      limit = self.monthly_thresholds[rmonth]
      print(f" • Monthly Spending Limit : ${limit:,.2f}")
      print(f" • Total Spending         : ${tot:,.2f}")
      if tot >= limit:
        print(
            "        STATUS: LIMIT EXCEEDED! You have gone over your monthly"
            " threshold."
        )
      elif tot >= limit * 0.8:
        print(
            "     STATUS: WARNING! You have used over 80% of your monthly"
            " threshold."

        )
      else:
        print(
            "    STATUS: SAFE. Within your set monthly spending threshold."
        )
      print("-" * 90)
    else:
      print(f" Total Spending: ${tot:,.2f} | Transactions: {len(recs)}")
    cats = {}
    for r in recs:
      c = r.get("category", "Other")
      cats[c] = cats.get(c, 0.0) + r["amount"]
    print("\n CATEGORY BREAKDOWN")
    for c, a in sorted(cats.items(), key=lambda x: x[1], reverse=True):
      pct = (a / tot) * 100 if tot else 0
      print(f" • {c:<20} ${a:>12,.2f} ({pct:>6.2f}%)")
    print("=" * 90)
  def category_analytics(self):
    if not self.expense_records:
      print("\n[!] No expense records available.")
      return
    cats, counts = {}, {}
    for r in self.expense_records:
      c = r.get("category", "Other")
      cats[c] = cats.get(c, 0.0) + r["amount"]
      counts[c] = counts.get(c, 0) + 1
    g_tot = sum(cats.values())
    print("\n" + " CATEGORY SPENDING ANALYTICS ".center(80, "="))
    print(f" {'Category':<22} {'Count':>10} {'Total':>15} {'Share':>10}")
    print("-" * 80)
    for c, tot in sorted(cats.items(), key=lambda x: x[1], reverse=True):
      cnt = counts[c]
      shr = (tot / g_tot) * 100 if g_tot else 0
      print(f" {c:<22} {cnt:>10} ${tot:>14,.2f} {shr:>9.2f}%")
    print("=" * 80)
  def savings_calculator(self):
    print("\n" + "    MONTHLY SAVINGS RATE CALCULATOR ".center(80, "="))
    month = (
        input(" Enter month (YYYY-MM, blank = current month): ").strip()
        or date.today().strftime("%Y-%m")
    )
    tot_spent = sum(
        r["amount"]
        for r in self.expense_records
        if r.get("date", "").startswith(month)
    )
    print(f" Total Expenses for {month} : ${tot_spent:,.2f}")
    try:

      inc = float(
          input(" Enter your total monthly income for this month ($): ").strip()
      )
      if inc <= 0:
        return
      sav = inc - tot_spent
      rate = (sav / inc) * 100
      print("-" * 80)
      print(f" • Monthly Income  : ${inc:,.2f}")
      print(f" • Monthly Expenses: ${tot_spent:,.2f}")
      print(f" • Net Savings     : ${sav:+,.2f}")
      print(f" • Savings Rate    : {rate:.2f}% of your income")
      print("=" * 80)
    except ValueError:
      print("[!] Please enter a valid income amount.")
  def search(self):
    q = (
        input(
            " Search description, category, merchant, notes, or payment method:"
            " "
        )
        .strip()
        .lower()
    )
    if not q:
      return
    matches = [
        r
        for r in self.expense_records
        if q
        in " ".join(
            str(r.get(k, ""))
            for k in [
                "description",
                "category",
                "subcategory",
                "notes",
                "payment_method",
            ]
        ).lower()
    ]
    print("\n" + " EXPENSE SEARCH RESULTS ".center(90, "="))
    for r in matches:
      print(
          f" #{r['id']} | {r['date']} | ${r['amount']:,.2f} | {r['category']} |"
          f" {r['description']}"
      )
    print(f"Matches found: {len(matches)}")

    print("=" * 90)
  def edit_or_delete(self):
    try:
      eid = int(input(" Enter expense ID to edit/delete: ").strip())
    except ValueError:
      print("[!] Invalid ID.")
      return
    record = next((r for r in self.expense_records if r.get("id") == eid), None)
    if not record:
      print("[!] Expense ID not found.")
      return
    act = input(" Choose action: [E]dit or [D]elete: ").strip().lower()
    if act == "d":
      self.expense_records.remove(record)
      print("[✔] Expense deleted.")
    elif act == "e":
      na = input(f" Amount [{record['amount']}]: ").strip()
      if na:
        try:
          record["amount"] = float(na)
        except ValueError:
          pass
      nc = input(f" Category [{record['category']}]: ").strip()
      if nc:
        record["category"] = nc.title()
      nd = input(f" Description [{record['description']}]: ").strip()
      if nd:
        record["description"] = nd
      print("[✔] Expense updated.")
  def cashflow_dashboard(self):
    month = (
        input(" Enter month (YYYY-MM, blank = current month): ").strip()
        or date.today().strftime("%Y-%m")
    )
    recs = [
        r for r in self.expense_records if r.get("date", "").startswith(month)
    ]
    if not recs:
      print("[!] No expenses found.")
      return
    dtotals = {}
    for r in recs:
      d = r["date"]
      dtotals[d] = dtotals.get(d, 0.0) + r["amount"]
    tot = sum(dtotals.values())
    print("\n" + f" CASH-FLOW DASHBOARD — {month} ".center(90, "="))
    print(f" Total spending: ${tot:,.2f}")
    for d, a in sorted(dtotals.items()):

      bar = "█" * min(50, max(1, int(a / max(tot / 50, 1))))
      print(f" {d} | ${a:>10,.2f} | {bar}")
    print("=" * 90)
  def recurring_manager(self):
    print("\n" + " RECURRING EXPENSE MANAGER ".center(80, "="))
    if not self.recurring_expenses:
      print("[!] No recurring expenses configured.")
      return
    for item in self.recurring_expenses:
      print(
          f" ID {item['expense_id']} | {item['description']:<25} |"
          f" ${item['amount']:,.2f} | Next: {item['next_due']}"
      )
    if (
        input("\nGenerate due recurring expenses now? (y/n): ").strip().lower()
        != "y"
    ):
      return
    today = date.today()
    gen = 0
    for rec in self.recurring_expenses:
      try:
        due = datetime.strptime(rec["next_due"], "%Y-%m-%d").date()
      except ValueError:
        continue
      if due > today:
        continue
      self.expense_records.append({
          "id": self.get_next_id(),
          "date": due.isoformat(),
          "time": datetime.now().strftime("%H:%M:%S"),
          "amount": float(rec["amount"]),
          "category": rec["category"],
          "subcategory": "Recurring",
          "description": rec["description"],
          "payment_method": "Automatic",
          "notes": "Generated from schedule",
          "recurring": True,
      })
      gen += 1
      freq = rec.get("frequency", "monthly")
      days = 1 if freq == "daily" else (7 if freq == "weekly" else 30)
      rec["next_due"] = date.fromordinal(due.toordinal() + days).isoformat()
    print(f"[✔] Generated {gen} due recurring expense(s).")
def main():
  portfolio = PortfolioTracker()
  expenses = ExpenseTracker()
  while True:

    print("\n" + "=" * 60)
    print("    PERSONAL FINANCE & INVESTMENT SYSTEM (OOP) ")
    print("=" * 60)
    print("  1. Share Price & Fundamental Analyzer")
    print("  2. Advanced Stock Portfolio & Trading Tracker")
    print("  3. Advanced Daily Expense & Threshold Tracker")
    print("  0. Exit Program")
    print("=" * 60)
    choice = input("      Select an option (1, 2, 3 or 0): ").strip()
    if choice == "1":
      ticker = (
          input(
              " Enter Stock Ticker Symbol (e.g., AAPL, MSFT, TSLA,"
              " RELIANCE.NS): "
          )
          .strip()
          .upper()
      )
      if ticker:
        analyzer = StockAnalyzer(ticker)
        analyzer.run_menu()
    elif choice == "2":
      portfolio.run_menu()
    elif choice == "3":
      expenses.run_menu()
    elif choice == "0":
      print("\nExiting application. Goodbye!          ")
      break
    else:
      print("\n[!] Invalid option. Please choose 1, 2, 3, or 0.")
if __name__ == "__main__":
  main()
