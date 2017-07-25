# Python Scripts
Useful scripts that run complementary to blackbird.

## Email Notifications
Tails the a given log file and sends an email when certain events are triggered i.e. Detailed summary of market entries and exits. 
Email credentials should be placed in the `consts.py`. Usage: `python3 email_notify.py log_file`
```
SENDER_EMAIL=
SENDER_PASSWORD=
RECEIVER_EMAIL=
SMTP_SERVER=
```
## Statistics
Compute various statistics including spreads of a given market pair. Usage `python stats.py log_file`

```
$ python3 stats.py blackbird.log
Kraken/Bitfinex: (131 rows)
	Max: 0.28
	95th: 0.12
	90th: 0.1
	75th: 0.07
	50th: -0.13
	25th: -0.5
	10th: -0.58
	5th: -0.65
	Min: -0.74

	Min-Max spread: 1.02
	95th-5th spread: 0.77
	90th-10th spread: 0.68
	75th-25th spread: 0.57
```
