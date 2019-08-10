"""
The DEFAULT configuration is loaded when the named _CONFIG dictionary
is not present in your settings.
"""

CONFIG_NAME = 'JOBPOST_CONFIG'    # must be uppercase!



DEFAULT = {

    # ReST help_text in the admin
    'restructuredtext_help':  '''This will be processed as
<a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html" target="_blank">
ReStructuredText</a>.''',
}


from django.conf import settings


def get(setting):
    """
    get(setting) -> value

    setting should be a string representing the application settings to
    retrieve.
    """
    assert setting in DEFAULT, 'the setting %r has no default value' % setting
    app_settings = getattr(settings, CONFIG_NAME, DEFAULT)
    return app_settings.get(setting, DEFAULT[setting])


def get_all():
    """
    Return all current settings as a dictionary.
    """
    app_settings = getattr(settings, CONFIG_NAME, DEFAULT)
    return dict([(setting, app_settings.get(setting, DEFAULT[setting])) \
                 for setting in DEFAULT])
