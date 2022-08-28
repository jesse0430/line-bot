import requests, re, random
import pandas as pd
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)


line_bot_api = LineBotApi('K7YQWqYBaK+538DTXej0lvb4qn6/Utjeurh7b63/Nf7W+08KUPwqHryLUFsBkkNcmOmlH3Z1ihsJ6aXPl8Lwn3iyaVw6FeMl9IVOYm5i/aIz1hDxxfq6J6sFhJzG2ojhcnoYfFZ3DOSBbwVL2fR5qAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4fba40457b5c8acbd51bcf10ac99ee38')

alldf=pd.read_csv('結合.csv')
alldf.pop('Unnamed: 0')
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global txt1 #area
    global txt2 #house_type
    global txt3 #option
    global txt6
    global carousel_template_message
    global buttons_template
    txt4='30年以下,10年以下,20年以下,其他屋齡,10坪以下,20坪以下,30坪以下,40坪以下,其他坪數,500萬以下,1000萬以下,1500萬以下,2000萬以下,其他總價,20萬元以下,30萬元以下,40萬元以下,其他單價'

    try:
        if event.message.text == "我要查詢":
            carousel_template_message = TemplateSendMessage(
                alt_text='台中 template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://doqvf81n9htmm.cloudfront.net/data/crop_article/112964/52.jpg_1140x855.jpg',
                            title='台中北屯、南屯、西屯',
                            text='想看什麼地區的房子呢？',
                            actions=[
                                MessageAction(
                                    label='北屯',
                                    text='北屯'
                                ),
                                MessageAction(
                                    label='南屯',
                                    text='南屯'
                                ),
                                MessageAction(
                                    label='西屯',
                                    text='西屯'
                                )
                            ]
                        )
                ]
            )
        )
        if event.message.text == "北屯":
            txt1= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='北屯 template',
                template=ButtonsTemplate(
                    title='想看什麼類型的呢？',
                    text='請點選房型',
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXr4wQoYE2lB2WElB4m-tTY99ZQp8dmQdv0A&usqp=CAU',
                    actions=[
                        MessageTemplateAction(
                            label='公寓',
                            text='公寓'
                        ),
                        MessageTemplateAction(
                            label='電梯大樓',
                            text='電梯大樓'
                        ),
                        MessageTemplateAction(
                            label='華廈',
                            text='華廈'
                        ),
                         MessageTemplateAction(
                            label='透天',
                            text='透天'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "西屯":
            txt1= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='北屯 template',
                template=ButtonsTemplate(
                    title='想看什麼類型的呢？',
                    text='請點選房型',
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXr4wQoYE2lB2WElB4m-tTY99ZQp8dmQdv0A&usqp=CAU',
                    actions=[
                        MessageTemplateAction(
                            label='公寓',
                            text='公寓'
                        ),
                        MessageTemplateAction(
                            label='電梯大樓',
                            text='電梯大樓'
                        ),
                        MessageTemplateAction(
                            label='華廈',
                            text='華廈'
                        ),
                         MessageTemplateAction(
                            label='透天',
                            text='透天'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "南屯":
            txt1= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='北屯 template',
                template=ButtonsTemplate(
                    title='想看什麼類型的呢？',
                    text='請點選房型',
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXr4wQoYE2lB2WElB4m-tTY99ZQp8dmQdv0A&usqp=CAU',
                    actions=[
                        MessageTemplateAction(
                            label='公寓',
                            text='公寓'
                        ),
                        MessageTemplateAction(
                            label='電梯大樓',
                            text='電梯大樓'
                        ),
                        MessageTemplateAction(
                            label='華廈',
                            text='華廈'
                        ),
                         MessageTemplateAction(
                            label='透天',
                            text='透天'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "公寓":
            txt2= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='公寓 template',
                template=ButtonsTemplate(
                    title='想依什麼條件篩選？',
                    text='請點選條件',
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTODu4pe2xolLr3dj_tAWBDhmJeBxKmA2HN-w&usqp=CAU',
                    actions=[
                        MessageTemplateAction(
                            label='屋齡',
                            text='屋齡'
                        ),
                        MessageTemplateAction(
                            label='坪數',
                            text='坪數'
                        ),
                        MessageTemplateAction(
                            label='總價',
                            text='總價'
                        ),
                        MessageTemplateAction(
                            label='單價',
                            text='單價'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "電梯大樓":
            txt2= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='電梯大樓 template',
                template=ButtonsTemplate(
                    title='想依什麼條件篩選？',
                    text='請點選條件',
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlaYGrIi6ji7SlBfazuxJaBP2wUR4sS6ZPeQ&usqp=CAU',
                    actions=[
                        MessageTemplateAction(
                            label='屋齡',
                            text='屋齡'
                        ),
                        MessageTemplateAction(
                            label='坪數',
                            text='坪數'
                        ),
                        MessageTemplateAction(
                            label='總價',
                            text='總價'
                        ),
                        MessageTemplateAction(
                            label='單價',
                            text='單價'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "華廈":
            txt2= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='華廈 template',
                template=ButtonsTemplate(
                    title='想依什麼條件篩選？',
                    text='請點選條件',
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtSd1cg4FWgPBXeoTgPiz4_pLhnLJbDNBjfg&usqp=CAU',
                    actions=[
                        MessageTemplateAction(
                            label='屋齡',
                            text='屋齡'
                        ),
                        MessageTemplateAction(
                            label='坪數',
                            text='坪數'
                        ),
                        MessageTemplateAction(
                            label='總價',
                            text='總價'
                        ),
                        MessageTemplateAction(
                            label='單價',
                            text='單價'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "透天":
            txt2= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='透天 template',
                template=ButtonsTemplate(
                    title='想依什麼條件篩選？',
                    text='請點選條件',
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR7326Hj4VSpgDtUK5EvReSF5zrwwgP3FTFQ&usqp=CAU',
                    actions=[
                        MessageTemplateAction(
                            label='屋齡',
                            text='屋齡'
                        ),
                        MessageTemplateAction(
                            label='坪數',
                            text='坪數'
                        ),
                        MessageTemplateAction(
                            label='總價',
                            text='總價'
                        ),
                        MessageTemplateAction(
                            label='單價',
                            text='單價'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "屋齡":
            txt3= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='屋齡 template',
                template=ButtonsTemplate(
                    title='想看幾歲的房子呢？',
                    text='請選擇條件',
                    thumbnail_image_url='https://cw1.tw/CW/images/article/201709/article-59ba87dddac50.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='10年以下',
                            text='10年以下'
                        ),
                        MessageTemplateAction(
                            label='20年以下',
                            text='20年以下'
                        ),
                        MessageTemplateAction(
                            label='30年以下',
                            text='30年以下'
                        ),
                        MessageTemplateAction(
                            label='其他屋齡',
                            text='其他屋齡'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "坪數":
            txt3= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='坪數 template',
                template=ButtonsTemplate(
                    title='想看多大的房子呢？',
                    text='請選擇條件',
                    thumbnail_image_url='https://cw1.tw/CW/images/article/201709/article-59ba87dddac50.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='20坪以下',
                            text='20坪以下'
                        ),
                        MessageTemplateAction(
                            label='30坪以下',
                            text='30坪以下'
                        ),
                        MessageTemplateAction(
                            label='40坪以下',
                            text='40坪以下'
                        ),
                        MessageTemplateAction(
                            label='其他坪數',
                            text='其他坪數'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "總價":
            txt3= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='總價 template',
                template=ButtonsTemplate(
                    title='想依什麼條件篩選？',
                    text='請選擇條件',
                    thumbnail_image_url='https://cw1.tw/CW/images/article/201709/article-59ba87dddac50.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='1000萬以下',
                            text='1000萬以下'
                        ),
                        MessageTemplateAction(
                            label='1500萬以下',
                            text='1500萬以下'
                        ),
                        MessageTemplateAction(
                            label='2000萬以下',
                            text='2000萬以下'
                        ),
                        MessageTemplateAction(
                            label='其他總價',
                            text='其他總價'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text == "單價":
            txt3= event.message.text
            buttons_template = TemplateSendMessage(
                alt_text='單價 template',
                template=ButtonsTemplate(
                    title='想查單價多少錢的物件呢？',
                    text='請選擇條件',
                    thumbnail_image_url='https://cw1.tw/CW/images/article/201709/article-59ba87dddac50.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='20萬以下',
                            text='20萬元以下'
                        ),
                        MessageTemplateAction(
                            label='30萬以下',
                            text='30萬元以下'
                        ),
                        MessageTemplateAction(
                            label='40萬以下',
                            text='40萬元以下'
                        ),
                        MessageTemplateAction(
                            label='其他單價',
                            text='其他單價'

                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        if event.message.text in txt4:
            txt5=event.message.text
            print(txt5[-3])
            if txt5[-3] == "年":
                txt6=txt5[0:2]
                if int(txt6) <11:
                    filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) & (alldf['house_age'] <=int(txt6))
                    df=alldf.loc[filt]
                    content=''
                    try:
                        for i in range(5):
                            data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                            content += '{}\n'.format(data)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                    except:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
                if int(txt6) >12:
                    filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) &  (((int(txt6)-10)<alldf['house_age']) & (alldf['house_age']<= int(txt6)))
                    df=alldf.loc[filt]
                    content=''
                    try:
                        for i in range(5):
                            data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                            content += '{}\n'.format(data)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                    except:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
            if txt5[-2] == "屋":
                txt6=txt5
                filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) & (30<alldf['house_age'] )
                df=alldf.loc[filt]
                content=''
                try:
                    for i in range(5):
                        data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                        content += '{}\n'.format(data)
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                except:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
            if txt5[-3] == "坪":
                txt6=txt5[0:2]
                if int(txt6) <21:
                    filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) & (alldf['floor_space'] <=int(txt6))
                    df=alldf.loc[filt]
                    content=''
                    try:
                        for i in range(5):
                            data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                            content += '{}\n'.format(data)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                    except:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
                if int(txt6) >22:
                    filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) &  (((int(txt6)-10)<alldf['floor_space']) & (alldf['floor_space']<= int(txt6)))
                    df=alldf.loc[filt]
                    content=''
                    try:
                        for i in range(5):
                            data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                            content += '{}\n'.format(data)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                    except:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
            if txt5[-2] == "坪":
                txt6=txt5
                filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) & (40<alldf['floor_space'] )
                df=alldf.loc[filt]
                content=''
                try:
                    for i in range(5):
                        data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                        content += '{}\n'.format(data)
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                except:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
            if txt5[-3] == "萬":
                txt6=txt5[0:4]
                if int(txt6) <1001:
                    filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) & (alldf['price'] <=int(txt6))
                    df=alldf.loc[filt]
                    content=''
                    try:
                        for i in range(5):
                            data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                            content += '{}\n'.format(data)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                    except:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
                if int(txt6) >1002:
                    filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) &  (((int(txt6)-500)<alldf['price']) & (alldf['price']<= int(txt6)))
                    df=alldf.loc[filt]
                    content=''
                    try:
                        for i in range(5):
                            data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                            content += '{}\n'.format(data)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                    except:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
            if txt5[-2] == "總":
                txt6=txt5
                filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) & (2000<alldf['price'] )
                df=alldf.loc[filt]
                content=''
                try:
                    for i in range(5):
                        data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                        content += '{}\n'.format(data)
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                except:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
            if txt5[-3] == "元":
                txt6=txt5[0:2]
                if int(txt6) <21:
                    filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) & (alldf['per_price'] <=int(txt6))
                    df=alldf.loc[filt]
                    content=''
                    try:
                        for i in range(5):
                            data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                            content += '{}\n'.format(data)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                    except:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
                if int(txt6) >22:
                    filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) &  (((int(txt6)-10)<alldf['per_price']) & (alldf['per_price']<= int(txt6)))
                    df=alldf.loc[filt]
                    content=''
                    try:
                        for i in range(5):
                            data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                            content += '{}\n'.format(data)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                    except:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
            if txt5[-2] == "單":
                txt6=txt5
                filt = (alldf['area'] == txt1) & (alldf['house_type']==txt2) & (40<alldf['per_price'] )
                df=alldf.loc[filt]
                content=''
                try:
                    for i in range(5):
                        data=('標題：'+str(df.iloc[i,0])+'\n,類型:'+str(df.iloc[i,1])+',路段:'+str(df.iloc[i,2])+',屋齡:'+str(df.iloc[i,3])+',坪數:'+str(df.iloc[i,4])+',單價:'+str(df.iloc[i,6])+'萬'+',價格:'+str(df.iloc[i,5])+'萬\n')
                        content += '{}\n'.format(data)
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
                except:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage('查無資料，請輸入其他條件'))
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0

        if event.message.text == "aa":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(txt1+txt2+txt3+txt6))

    line_bot_api.reply_message(event.reply_token, carousel_template_message)
    except Exception as e:
       print(e)

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    print("package_id:", event.message.package_id)
    print("sticker_id:", event.message.sticker_id)
    # ref. https://developers.line.me/media/messaging-api/sticker_list.pdf
    sticker_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 100, 101, 102, 103, 104, 105, 106,
                   107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
                   126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 401, 402]
    index_id = random.randint(0, len(sticker_ids) - 1)
    sticker_id = str(sticker_ids[index_id])
    print(index_id)
    sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id=sticker_id
    )
    line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
