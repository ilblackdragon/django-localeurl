import re
from django.conf import settings

SUPPORTED_LOCALES = dict(settings.LANGUAGES)
# Issue #15. Sort locale codes to avoid matching e.g. 'pt' before 'pt-br'
LOCALES_RE = '|'.join(
    sorted(SUPPORTED_LOCALES.keys(), key=lambda i: len(i), reverse=True))
PATH_RE = re.compile(r'^/(?P<locale>%s)(?P<path>.*)$' % LOCALES_RE)

LOCALE_INDEPENDENT_PATHS = [re.compile(p) for p in
                            getattr(settings, 'LOCALE_INDEPENDENT_PATHS', [])]

LOCALE_INDEPENDENT_MEDIA_URL = getattr(settings,
        'LOCALE_INDEPENDENT_MEDIA_URL', True)

LOCALE_INDEPENDENT_STATIC_URL = getattr(settings,
        'LOCALE_INDEPENDENT_STATIC_URL', True)

PREFIX_DEFAULT_LOCALE = getattr(settings, 'PREFIX_DEFAULT_LOCALE', True)

USE_ACCEPT_LANGUAGE = getattr(settings, 'LOCALEURL_USE_ACCEPT_LANGUAGE', False)
