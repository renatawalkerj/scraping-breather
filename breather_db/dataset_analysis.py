# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

datset = pd.read_csv('final_dataframe.csv', index_col=[0])

dataset = datset.dropna()

yogamat = dataset[dataset['Yoga mat']==1]
airconditioning = dataset[dataset['Air conditioning']==1]
airtame = dataset[dataset['Airtame']==1]
appletv = dataset[dataset['Apple TV']==1]
bathrooms = dataset[dataset['Bathroom on premises']==1]
blinds = dataset[dataset['Blinds']==1]
cateringallowed = dataset[dataset['Catering allowed']==1]
dishwasher = dataset[dataset['Dishwasher']==1]
elevatoraccess = dataset[dataset['Elevator access']==1]
ensuitekitchenette = dataset[dataset['Ensuite kitchenette']==1]
fireplace = dataset[dataset['Fireplace']==1]
freecoffee = dataset[dataset['Free coffee']==1]
freewater = dataset[dataset['Free water']==1]
googlechromebox = dataset[dataset['Google Chromebox']==1]
greatview = dataset[dataset['Great view']==1]
kitchenetteonpremises = dataset[dataset['Kitchenette on premises']==1]
lobbystaff = dataset[dataset['Lobby staff']==1]
microwave = dataset[dataset['Microwave']==1]
minifrige = dataset[dataset['Mini fridge']==1]
mirror = dataset[dataset['Mirror']==1]
onsitecatering = dataset[dataset['On-site catering']==1]
parking = dataset[dataset['Parking']==1]
phonecharger = dataset[dataset['Phone charger']==1]
premiumbuilding = dataset[dataset['Premium building']==1]
projectorscreen = dataset[dataset['Projector Screen']==1]
skylight = dataset[dataset['Skylight']==1]
speakers = dataset[dataset['Speakers']==1]
teapoint = dataset[dataset['Tea point']==1]
thunderbolt = dataset[dataset['Thunderbolt']==1]
usbmultiport = dataset[dataset['USB-C Multiport']==1]
waitingroom = dataset[dataset['Waiting room']==1]
waterforsale = dataset[dataset['Water for sale']==1]
webcam = dataset[dataset['Webcam']==1]
wheelchairaccess = dataset[dataset['Wheelchair accessible']==1]
whiteboard = dataset[dataset['Whiteboard']==1]
wifi = dataset[dataset['WiFi']==1]
wepresent = dataset[dataset['wePresent']==1]

nowifi = dataset[dataset['WiFi']==0]

dataset.sort_values(by='hourly_price_usd',inplace=True)
means = dataset.mean(axis='rows')