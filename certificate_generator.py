from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

#pip install PIP
#pip install pillow
#pip install pandas
#pip install os

df = pd.read_csv('certificate.csv') #Read from .csv file
font = ImageFont.truetype('fonts/MLSJN.ttf',60) #Font style and size

for index,j in df.iterrows():
    img = Image.open('certificate.jpg') #Open the .jpg file
    draw = ImageDraw.Draw(img)

    if len(j['name'])<=10:
        draw.text(xy=(500,400),text='{}'.format(j['name']),fill=(0,0,0),font=font) #for name of length <=10

    elif len(j['name'])>10 and len(j['name'])<=13:
        draw.text(xy=(430,400),text='{}'.format(j['name']),fill=(0,0,0),font=font) #for name of length > 10 and <=13

    elif len(j['name'])>13 and len(j['name'])<=16:
        draw.text(xy=(400,400),text='{}'.format(j['name']),fill=(0,0,0),font=font) #for name of length>13 and <=16

    elif len(j['name'])>16:
        draw.text(xy=(320,400),text='{}'.format(j['name']),fill=(0,0,0),font=font) #for name of length>16

    img.save('Generated-Certificates/{}.jpg'.format(j['name']))
