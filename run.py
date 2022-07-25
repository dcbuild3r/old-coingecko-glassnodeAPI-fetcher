#!/usr/bin/env python

import requests
import json
import time
from datetime import datetime, timedelta
import sys

from merge_data import get_stats

def print_json(data: dict):
    data = json.dumps(data, indent=3)

    print(data)

argc = len(sys.argv)
if argc == 2:
    date = sys.argv[1]
    print_json(get_stats(date, display_currency='usd'))
elif argc == 3:
    date = sys.argv[1]
    display_currency = sys.argv[2]
    print_json(get_stats(date, display_currency))
else:
    print("Argument structure: ./run.py [date(%d-%m-%Y)] [display_currency(usd,native)]")
