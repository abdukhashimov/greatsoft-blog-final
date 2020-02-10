from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


# validates title
def validate_post_title(value):
    if len(str(value).split(' ')) < 3:
        raise ValidationError(
            _('Your title is not long enough')
        )


# validate name for category or tag
def validate_name(value):
    if len(str(value)) < 3:
        raise ValidationError(
            _('Your name is not long enough')
        )
