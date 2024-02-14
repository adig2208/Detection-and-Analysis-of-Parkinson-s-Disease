from twilio.rest import Client


class sendsms():

    def send(name , number):

        # the following line needs your Twilio Account SID and Auth Token
        
        client = Client("AC97c237318a9b897aa14ba77982dabc3d", "a97db5f7e6e5e9efc37568a5c67a2913")

        
        # msg = name + " from " + cmpny + " is here to deliver your package. Contact Number : " +mno
        msg = name + "your test results are ready . Please login again and check your report "
        print(msg)


       
        client.messages.create(to="your number", 
                            from_="+16196333974", 
                            body=msg)