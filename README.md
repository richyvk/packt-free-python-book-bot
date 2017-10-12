# packt-free-python-book-bot

A mega-simple bot that tweets when there is a free Python book of the day at Packt Publishing.

## Getting Started

To run, setup using the prerequisites, then run:

```
python bot.py
```

### Prerequisites

Runs on Python 3.6 (because f-strings)

1. Set up a Twitter app.

2. Add a config file that looks like this:

	```
	"""config.py"""

	#  twitter keys
	CONSUMER_KEY = '<your key>'
	CONSUMER_SECRET = '<your secret>'
	ACCESS_TOKEN = '<your token>'
	ACCESS_TOKEN_SECRET = '<your token secret>'

	# Packt free book URL
	URL = 'http://www.packtpub.com/packt/offers/free-learning/'

	# Request headers
	HEADERS = {'user-agent': '<your-user-agent>'}

	```

3. Creat virtualenv and run:

```
pip install -r requirements.txt
```

## Authors

* **Richard Vankoningsveld** - [richyvk.me](http://www.richyvk.me/)

## License

None. Public domain.
