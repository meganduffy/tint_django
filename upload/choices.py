STATUS_CHOICES = (
    ('Processing', 'Processing'),
    ('InProgress', 'In Progress'),
    ('Done', 'Done')
)

CATEGORY_CHOICES = (
    ('General', 'General'),
    ('Legal', 'Legal'),
    ('Medical', 'Medical'),
    ('Personal', 'Personal'),
    ('Academic', 'Academic')
)

TEXT_FORMAT_CHOICES = (
    ('IntelligentVerbatim', 'Intelligent Verbatim'),
    ('Verbatim', 'Full Verbatim')
)

NUM_SPEAKER_CHOICES = (
    ('1', '1 Speaker'),
    ('2', '2 Speakers'),
    ('3', '3 Speakers'),
    ('4', '4+ Speakers'),
    ('10', '10+ Speakers')
)

TIMESTAMP_CHOICES = (
    ('None', 'Not Required'),
    ('SpeakerChange', 'On Speaker Change'),
    ('2Minutes', 'Every Two Minutes'),
)

TAT_CHOICES = (
    ('24', '24 Hour'),
    ('48', '48 Hour'),
    ('Standard', 'Standard (Up To 4 Days)')
)

AUDIO_QUAL_CHOICES = (
    ('Bad', 'Bad'),
    ('Fair', 'Fair'),
    ('Good', 'Good')
)
