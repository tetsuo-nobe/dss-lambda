import json
import time

# ハンドラ関数の外側で3秒間sleep
#time.sleep(3)

def lambda_handler(event, context):
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