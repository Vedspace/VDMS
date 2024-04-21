from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAC8z0aAU:APA91bHL5sPpu8Rcgj_gMfuMk4A3DaBHzz8tyVJt4byzUiRD7kfRLfV0PiVcXZIPKz-nB4R3ASNfHp28i_A9bVWclrF0oDBOwa_mKpqPeN2fTEijPww1qPKVEKbVNybUDo9UkUw2o1p6")

def send_push_notification(token, title, message):
    result = push_service.notify_single_device(
        registration_id=token,
        message_title=title,
        message_body=message
    )
    return result
