import os

MTA_KEY       = os.environ.get('MTA_KEY')
STATIONS_FILE = os.environ.get('STATIONS_FILE', './data/stations.json')
CROSS_ORIGIN  = os.environ.get('CROSS_ORIGIN', '*')
MAX_TRAINS    = int(os.environ.get('MAX_TRAINS', 10))
MAX_MINUTES   = int(os.environ.get('MAX_MINUTES', 30))
CACHE_SECONDS = int(os.environ.get('CACHE_SECONDS', 60))
THREADED      = True if os.environ.get('THREADED', 'True') == 'True' else False
DEBUG         = True if os.environ.get('DEBUG', 'False') == 'True' else False
