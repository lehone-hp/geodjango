from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class OpenwispNotificationsConfig(AppConfig):
    name = 'openwisp_notifications'
    label = 'notifications'
    verbose_name = _('Notifications')
