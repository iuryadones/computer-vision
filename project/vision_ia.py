import cv2
import numpy as np
import pylab as plt
import pandas as pd

import PIL
from PIL import Image

import io
from io import StringIO
from io import BytesIO

import matplotlib.pyplot as plt

from pymongo import MongoClient


settings = {
    'client':{
        'host': 'localhost',
        'port': 34120,
    },
    'db': {
        'name': 'tribunais_extracao'
    }
}

connect = MongoClient(**settings['client'])
db = connect.get_database(**settings['db'])
xcoll = 'fs.chunks'

print(f'Captchas\nTotal: {db[xcoll].count()}')
data = list(db[xcoll].find({}).skip(547517).limit(1))[0]['data']

pp = PIL.Image.open(BytesIO(data))
# pp.save('./captcha.png',format='png')
plt.figure()
plt.xticks([])
plt.yticks([])
plt.imshow(pp)
plt.tight_layout()
plt.show()

image = cv2.imread('../db_images/jpeg/captcha.jpeg')
plt.figure()
plt.title("BGR")
plt.xticks([])
plt.yticks([])
plt.imshow(image)
plt.tight_layout()
plt.show()
