import datetime
from django.conf import settings
from django.utils import timezone
from paypal.standard.models import ST_PP_COMPLETED
from upload.models import TranscriptDetails


def create_deadline(tat):
    days = {'24': 1, '48': 2, 'Standard': 4}.get(tat)
    new_deadline = timezone.now() + datetime.timedelta(days=days)
    return new_deadline


def payment_accepted(sender, **kwargs):
    ipn_obj = sender
    print ipn_obj
    print ipn_obj.payment_status
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        print "Payment status is: %s" % ipn_obj.payment_status
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            return 'Receiver email does not match'
        else:
            transcript_id = ipn_obj.custom.split('-')[0]
            tat = ipn_obj.custom.split('-')[1]
            deadline = create_deadline(tat)

            transcript_details = TranscriptDetails.objects.filter(id=transcript_id)
            transcript_details.update(status="InProgress", purchased_at=timezone.now(), saved=False, deadline=deadline)
    else:
        print "Payment didn't go through"


def invalid_handler(sender, **kwargs):
    ipn_obj = sender
    print "I got an invalid ipn signal"
    print ipn_obj.receiver_email
