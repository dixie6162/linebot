from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('CuFnfbxcKnaej56HDko6Mx5DVnSGuMGIpk8TrbpNzgBNo2iB1LpZ+AzOK9rPNnWEcdrAaHQrPXsb5ymQd0og9pYbDmF4kyVEVf2wW43fQcv2JIVYeWPrfv9Gm1p7wjrfs/feJWm8oeSkgF/AP6Ud/QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('013dd0c0fab1f07fafff096890952053')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飽了嗎?'))


if __name__ == "__main__":
    app.run()