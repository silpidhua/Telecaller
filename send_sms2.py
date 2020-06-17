import http.client
import urllib
import urllib.request

class SendSms:
    def send_my_sms(self,msg,number):
        if len(number)==11:
            number = number[1:]
        params = urllib.parse.urlencode({'message': msg, 'msisdn': number})
        print(params)
        url = 'https://global.datagenit.com/API/sms-api.php?auth=D!~3784gzsmL1yNOo&senderid=Infsms&'+params
        with urllib.request.urlopen(url) as something:
            r = something.read()
            print(r)
        return r
if __name__ == '__main__':
    send_sms = SendSms()
    send_sms.send_my_sms('hello world', '08892472497')