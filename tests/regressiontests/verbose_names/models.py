from django.db import models
from django.utils.translation import ugettext_lazy as _, ungettext_lazy


class NoMeta(models.Model):
    name = models.CharField(max_length=20)

class LegacyOnlyVerboseName(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Legacy model #1'

class LegacyBothVNames(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Legacy model #2'
        verbose_name_plural = 'Legacy models #2'

class LegacyOnlyVerboseNamePlural(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Legacy models #3'

class LegacyOnlyVerbosenameIntl(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Translatable legacy model #1')

class LegacyBothIntl(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Translatable legacy model #2')
        verbose_name_plural = _('Translatable legacy models #2')

class LegacyPluralIntl(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = _('Translatable legacy models #3')

# === Models using new classmethod syntax for verbose names ==========

class NewstyleSingular(models.Model):
    name = models.CharField(max_length=20)

    @classmethod
    def verbose_names(cls, count=1):
        if count == 1:
            return 'New-style model #1'

class NewstyleBoth(models.Model):
    name = models.CharField(max_length=20)

    @classmethod
    def verbose_names(cls, count=1):
        if count == 1:
            return 'New-style model #2'
        else:
            return 'New-style models #2'

class NewstylePlural(models.Model):
    name = models.CharField(max_length=20)

    @classmethod
    def verbose_names(cls, count=1):
        if count != 1:
            return 'New-style models #3'

class NewstyleSingularIntl(models.Model):
    name = models.CharField(max_length=20)

    @classmethod
    def verbose_names(cls, count=1):
        if count == 1:
            return _('Translatable New-style model #1')

class NewstyleBothIntl(models.Model):
    name = models.CharField(max_length=20)

    @classmethod
    def verbose_names(cls, count=1):
        return ungettext_lazy('Translatable New-style model #2', 'Translatable New-style models #2', count)

class NewstylePluralIntl(models.Model):
    name = models.CharField(max_length=20)

    @classmethod
    def verbose_names(cls, count=1):
        if count != 1:
            return _('Translatable New-style models #3')
