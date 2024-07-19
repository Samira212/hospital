from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields: tuple[str, str] = ('specialty', 'education')

