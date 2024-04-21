from pyfcm import FCMNotification

def send_push_notification(user, message_title, message_body):
    from login.models import DeviceToken  # Import here to avoid circular imports

    # Create an instance of FCMNotification with your server key
    push_service = FCMNotification(api_key="AAAAC8z0aAU:APA91bHL5sPpu8Rcgj_gMfuMk4A3DaBHzz8tyVJt4byzUiRD7kfRLfV0PiVcXZIPKz-nB4R3ASNfHp28i_A9bVWclrF0oDBOwa_mKpqPeN2fTEijPww1qPKVEKbVNybUDo9UkUw2o1p6")

    # Get the device token for the user
    device_tokens = DeviceToken.objects.filter(user=user).values_list('token', flat=True)

    # Send notification
    if device_tokens:
        result = push_service.notify_multiple_devices(
            registration_ids=list(device_tokens),
            message_title=message_title,
            message_body=message_body
        )
        return result
