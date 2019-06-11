import matplotlib.pyplot as plt
import pyimgur
import numpy as np
def glucose_graph(food, ug):
    t = np.linspace(0, 180, 1801)
    plt.figure()
    plt.rcParams['savefig.dpi'] = 50 #图片像素
    plt.rcParams['figure.dpi'] = 50 #分辨率
    plt.title(food+"'s Glucose image")
    plt.plot(t,ug)
    plt.savefig('send.png')
    CLIENT_ID = "233a2069365aee6"
    PATH = "send.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Glucose Image")
    print(uploaded_image.link)
    return uploaded_image.link

