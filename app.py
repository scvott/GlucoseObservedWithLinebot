from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
#glucose analysis image
#imgur
from imgurpython import ImgurClient
import tempfile, os
import draw_rader

import matplotlib.pyplot as plt
#find gi value import
import json

import Hovorka

# Channel Access Token
line_bot_api = LineBotApi('***********')
# Channel Secret
handler = WebhookHandler('**************')
#User ID
to = "*************"

# imgur key
client_id = '**********'
client_secret = '**********'

app = Flask(__name__, static_url_path = "/images" , static_folder = "./images/")
#app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
#find glucose
def glucose_data(a):
    with open('FoodData.json') as file:
        file_data = file.read()
    jdata = json.loads(file_data)
    GlucoseData = {}
    for st in jdata:
        food, GI, GL, CHO = st["FoodName"], st["Glycemic"], st["Glycemic Load"], st["Available"]
        GlucoseData[food] = (GI, GL, CHO)
    gl_key = GlucoseData.keys()
    if a in gl_key:
        return (GlucoseData[a][0], GlucoseData[a][1], GlucoseData[a][2])
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = event.message.text.split()
    if len(message_text) == 1:
        if event.message.text == "help" or event.message.text == "Help":
            help_message = "這是一個簡易式觀測血糖變化的聊天機器人\n指令說明:\n\
help:  觀測此機器人的功能\n\
food name '吃的分量': 注意這個格式是固定的\n\
舉例:\n\
    white rice 200，表示吃 white rice 200 gram\n\
    麵條 500 ， 表示吃 麵條 200 克"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(help_message))
    else:
        food_weight = event.message.text.split()#input format = foodname weight
        if len(food_weight)==4:
            food_name = food_weight[0]+" "+food_weight[1]+" "+food_weight[2]
            sid = food_weight[0]+food_weight[1]+food_weight[2]
            try:
                answer = glucose_data(food_name)
                glucose_change = int(answer[2])*int(food_weight[3])/100
                message1 = TextSendMessage(text="GI value is {}".format(answer[0]))
                message2 = TextSendMessage(text="GL value is {}".format(answer[1]))
                message3 = TextSendMessage(text="Per {}g this food has {}g CHO".format(food_weight[3],str(glucose_change)))
                eat = Hovorka.Hovorka_Meal(glucose_change)                
                img_url = draw_rader.glucose_graph(sid, eat)
                glcouse = max(eat)
                message4 = TextSendMessage(text="Glucose will rise {:.2f}mmol in blood".format(glcouse))
                message5 = ImageSendMessage(original_content_url=img_url+'.png',preview_image_url=img_url+'.png')
                message = (message1, message2, message3, message4, message5)
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage("Input Error"))
        elif len(food_weight)==3:
            food_name = food_weight[0]+" "+food_weight[1]
            sid = food_weight[0]+food_weight[1]
            try:
                answer = glucose_data(food_name)
                glucose_change = int(answer[2])*int(food_weight[2])/100
                message1 = TextSendMessage(text="GI value is {}".format(answer[0]))
                message2 = TextSendMessage(text="GL value is {}".format(answer[1]))
                message3 = TextSendMessage(text="Per {}g this food has {}g CHO".format(food_weight[2],str(glucose_change)))
                eat = Hovorka.Hovorka_Meal(glucose_change)
                img_url = draw_rader.glucose_graph(sid, eat)
                glcouse = max(eat)
                message4 = TextSendMessage(text="Glucose will rise {:.2f}mmol in blood".format(glcouse))
                message5 = ImageSendMessage(original_content_url=img_url+'.png',preview_image_url=img_url+'.png')
                message = (message1, message2, message3, message4, message5)
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage("Input Error"))
        else:
            food_name = food_weight[0]
            sid = food_weight[0]
            try:
                answer = glucose_data(food_name)
                glucose_change = int(answer[2])*int(food_weight[1])/100
                message1 = TextSendMessage(text="GI value is {}".format(answer[0]))
                message2 = TextSendMessage(text="GL value is {}".format(answer[1]))
                message3 = TextSendMessage(text="Per {}g this food has {}g CHO".format(food_weight[1],str(glucose_change)))
                eat = Hovorka.Hovorka_Meal(glucose_change)
                glcouse = max(eat)
                message4 = TextSendMessage(text="Glucose will rise {:.2f}mmol in blood".format(glcouse))
                img_url = draw_rader.glucose_graph(sid, eat)
                message5 = ImageSendMessage(original_content_url=img_url,preview_image_url=img_url)
                message = (message1, message2, message3, message4, message5)
                line_bot_api.reply_message(event.reply_token, message) #line_bot_api.push_message(to, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage("Input Error"))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)