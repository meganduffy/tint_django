from django.conf import settings
from django.utils import timezone
from paypal.standard.models import ST_PP_COMPLETED
from upload.models import TranscriptDetails


def payment_accepted(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        print "Payment status is: %s" % ipn_obj.payment_status
        print ipn_obj
        transcript_id = ipn_obj.custom.split('-')[0]
        transcript_details = TranscriptDetails.objects.filter(id=transcript_id)
        if ipn_obj.reciever_email != settings.PAYPAL_RECEIVER_EMAIL:
            return
        else:
            transcript_details.update(status="In Progress", purchased_at=timezone.now())
    else:
        print "Payment didn't go through"


def invalid_handler(sender, **kwargs):
    ipn_obj = sender
    print "I got an invalid ipn signal"
