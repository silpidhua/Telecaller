from flask import Flask,make_response, jsonify,request
from flask_cors import CORS
from send_sms import SMSSender
import os
app = Flask(__name__)
CORS(app,expose_headers=["Content-Disposition"])
@app.route('/')
def root():
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'
    CallSid=request.args.get('CallSid')
    CallFrom=request.args.get('CallFrom')
    CallTo=request.args.get('CallTo')
    CallType=request.args.get('CallType')
    From=request.args.get('From')
    To=request.args.get('To')
    msg = 'CallSid:'+CallSid+' CallFrom:'+CallFrom+' CallTo:'+CallTo+' CallType:'+CallType+' From:'+From+' To:'+To
    smsSender = SMSSender()
    response = smsSender.sendPostRequest(URL, 'Z26N1SVHHEL3CMGLFZTO1LAZQRR9ZVJM', 'W8XGKT0M20A5JTXI', 'stage', CallFrom, 'ABC123', msg )
    print (response.text)
    print(msg)
    return make_response(jsonify(response.text),200)
if __name__ =='__main__':
    #application = Application()
    #application.run()
    port= int(os.getenv('PORT',8080))
    app.run(port=port, host="0.0.0.0",debug=True)


