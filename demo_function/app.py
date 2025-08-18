import json
import time
from datetime import datetime

# ハンドラ関数の外側で3秒間sleep
#time.sleep(3)
# ハンドラ関数の外側で日時データを取得
#outside_handler = datetime.now()

def lambda_handler(event, context):
    # ハンドラ関数の内側で日時データを取得
    inside_handler = datetime.now()  
    # 取得した日時データをログ出力
    print('outside_handler :' + str(outside_handler))
    print('inside_handler  :' + str(inside_handler))

    # HTML コンテンツの出力
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Demo</title>
    </head>
    <body style="background-color: blue; color: white; font-family: Arial, sans-serif; text-align: center; padding: 50px;">
        <h1>This is version blue.</h1>
    </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html_content
    }