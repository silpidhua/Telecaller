from flask import Flask,make_response
from flask_cors import CORS
from send_sms import SMSSender
import os
app = Flask(__name__)
CORS(app,expose_headers=["Content-Disposition"])
@app.route('/')
def root():
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'
    smsSender = SMSSender()
    response = smsSender.sendPostRequest(URL, 'Z26N1SVHHEL3CMGLFZTO1LAZQRR9ZVJM', 'W8XGKT0M20A5JTXI', 'stage', '8892472497', 'ABC123', 'Hello World' )
  
    return make_response(response,200)
if __name__ =='__main__':
    #application = Application()
    #application.run()
    port= int(os.getenv('PORT',8080))
    app.run(port=port, host="0.0.0.0",debug=True)


