import io
from io import StringIO
from io import BytesIO

import os

import cv2
import numpy as np
import pylab as plt
import pandas as pd

import PIL
from PIL import Image

import matplotlib.pyplot as plt

from pymongo import MongoClient


settings = {
    'client':{
        'host': 'localhost',
        'port': 27017,
    },
    'db': {
        'name': 'tribunais_extracao'
    }
}

connect = MongoClient(**settings['client'])
db = connect.get_database(**settings['db'])
xcoll_1 = 'fs.chunks'
xcoll_2 = 'captchas'

print(f'Captchas\nTotal: {db[xcoll_1].count()}')


for info in db[xcoll_2].find({}):
    if info['correct'] and info['answer'].isdigit():
        print(info['answer'])
        print(info['correct'])
        print(info['_id'])

        data = db[xcoll_1].find({'files_id':info['_id']})[0]

        d = data['data']

        pp = PIL.Image.open(BytesIO(d))

        path = f"../db_images/captcha/{info['answer']}"

        if not os.path.exists(path):
            os.mkdir(path)
        else:
            pp.save(f'{path}/sample-{len(os.listdir(path)) + 1}.png',
                    format='png')

        cv2.imshow('image', np.array(pp))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# pp.save('./captcha.png',format='png')
# plt.figure()
# plt.xticks([])
# plt.yticks([])
# plt.imshow(pp)
# plt.tight_layout()
# plt.show()

# image = cv2.imread('../db_images/jpeg/captcha.jpeg')
# plt.figure()
# plt.title("BGR")
# plt.xticks([])
# plt.yticks([])
# plt.imshow(image)
# plt.tight_layout()
# plt.show()
