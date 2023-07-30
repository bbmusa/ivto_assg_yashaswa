
strategy used : "On Balance Volume ema's diffrance"
on days where price went up, that day's volume is added to the cumulative OBV total. If price went down, then that day's volume is subtracted from the OBV total.
Simple but effective gives good results and also work as conformation sign, Along with exit strategy gives better results.

codes:
- database: database.py
- backtest & strategy code: strategy_lib.py
- testing: test.py

outputs:
backtest:
![image](https://github.com/bbmusa/ivto_assg_yashaswa/assets/65719349/ad7e879e-06d9-4562-bb19-2aec2f6d239d)

testing
![image](https://github.com/bbmusa/ivto_assg_yashaswa/assets/65719349/43668ae0-9366-4948-aed8-e807bc0181c2)

