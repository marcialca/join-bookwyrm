""" handle internationalization """
import os
import gettext
import threading

localedir = os.path.join(os.path.dirname(__file__), "locale")
domain = "messages"
thread_local_data = threading.local()
thread_local_data.locale = "en_US"

locales_metadata = [
    {"code": "en_US", "name": "English (US)", "slug": ""},
    {"code": "de_DE", "name": "Deutsch", "slug": "de/"},
    {"code": "es_ES", "name": "Español", "slug": "es/"},
    {"code": "gl_ES", "name": "Galego", "slug": "gl/"},
    {"code": "fr_FR", "name": "Français", "slug": "fr/"},
    {"code": "lt_LT", "name": "lietuvių", "slug": "lt/"},
    {"code": "pt_PT", "name": "Português Europeu", "slug": "pt-pt/"},
    {"code": "pt_BR", "name": "Português do Brasil", "slug": "pt-br/"},
    {"code": "zh_Hans", "name": "简体中文", "slug": "zh/"},
]
default_locale = "en_US"

# find out all supported locales in locale directory
locales = []
for dirpath, dirnames, filenames in os.walk(localedir):
    for dirname in dirnames:
        locales.append(dirname)
    break

all_translations = {}
for locale in locales:
    all_translations[locale] = gettext.translation(domain, localedir, [locale])


def gettext(message):
    return all_translations[thread_local_data.locale].gettext(message)


def ngettext(singular, plural, n):
    return all_translations[thread_local_data.locale].ngettext(singular, plural, n)


def setLocale(locale):
    if locale in locales:
        thread_local_data.locale = locale


if __name__ == "__main__":
    # for test purpose
    for dirpath, dirnames, filenames in os.walk(localedir):
        for dirname in dirnames:
            print(dirname)
        break
