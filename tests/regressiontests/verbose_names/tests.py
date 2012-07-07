from __future__ import absolute_import

from django.utils.encoding import force_unicode
from django.utils import translation
from django.utils.unittest import TestCase

from .models import (NoMeta, LegacyOnlyVerboseName, LegacyBothVNames,
        LegacyOnlyVerboseNamePlural, LegacyOnlyVerbosenameIntl, LegacyBothIntl,
        LegacyPluralIntl, NewstyleSingular, NewstyleBoth, NewstylePlural,
        NewstyleSingularIntl, NewstyleBothIntl, NewstylePluralIntl)


class LegacyVerboseNameNoI18NTests(TestCase):
    """
    Test we don't disrupt behavior associated with legacy
    Meta.verbose_name{,_plural} attributes when translation isn't used.
    """

    def test_noi18n_no_meta_inner_class(self):
        # A model without an inner Meta class
        a = NoMeta.objects.create(name=u'Name')
        self.assertEqual('no meta', NoMeta._meta.verbose_name)
        self.assertEqual('no meta', a._meta.verbose_name)
        # Automatically generated plural form, can be bogus (note the arbitrary
        # 's' tucked at the end)
        self.assertEqual('no metas', force_unicode(NoMeta._meta.verbose_name_plural))
        self.assertEqual('no metas', force_unicode(a._meta.verbose_name_plural))

    def test_noi18n_only_verbose_name_option(self):
        a = LegacyOnlyVerboseName.objects.create(name=u'Name')
        # The verbose_name we specified
        self.assertEqual('Legacy model #1', LegacyOnlyVerboseName._meta.verbose_name)
        self.assertEqual('Legacy model #1', a._meta.verbose_name)
        # Automatically generated plural form, can be bogus (note the arbitrary
        # 's' tucked at the end)
        self.assertEqual('Legacy model #1s', force_unicode(LegacyOnlyVerboseName._meta.verbose_name_plural))
        self.assertEqual('Legacy model #1s', force_unicode(a._meta.verbose_name_plural))

    def test_noi18n_both_verbose_name_options(self):
        b = LegacyBothVNames.objects.create(name=u'Name')
        # The verbose_name we specified
        self.assertEqual('Legacy model #2', LegacyBothVNames._meta.verbose_name)
        self.assertEqual('Legacy model #2', b._meta.verbose_name)
        # The verbose_name_plural we specified
        self.assertEqual('Legacy models #2', LegacyBothVNames._meta.verbose_name_plural)
        self.assertEqual('Legacy models #2', b._meta.verbose_name_plural)

    def test_noi18n_only_verbose_name_plural_option(self):
        c = LegacyOnlyVerboseNamePlural.objects.create(name=u'Name')
        # Verbose name automatically generated from the class name
        self.assertEqual('legacy only verbose name plural', LegacyOnlyVerboseNamePlural._meta.verbose_name)
        self.assertEqual('legacy only verbose name plural', c._meta.verbose_name)
        # The verbose_name_plural we specified
        self.assertEqual('Legacy models #3', LegacyOnlyVerboseNamePlural._meta.verbose_name_plural)
        self.assertEqual('Legacy models #3', c._meta.verbose_name_plural)


class LegacyVerboseNameI18NTests(TestCase):
    """
    Test we don't disrupt behavior associated with legacy
    Meta.verbose_name{,_plural} attributes when translation is used.
    """

    def setUp(self):
        translation.activate('es-ar')

    def tearDown(self):
        translation.deactivate()

    def test_i18n_no_meta_inner_class(self):
        # A model without an inner Meta class
        a = NoMeta.objects.create(name=u'Name')
        self.assertEqual('no meta', NoMeta._meta.verbose_name)
        self.assertEqual('no meta', a._meta.verbose_name)
        # Automatically generated plural form, can be bogus (note the arbitrary
        # 's' tucked at the end)
        self.assertEqual('no metas', force_unicode(NoMeta._meta.verbose_name_plural))
        self.assertEqual('no metas', force_unicode(a._meta.verbose_name_plural))

    def test_i18n_only_verbose_name_option(self):
        a = LegacyOnlyVerbosenameIntl.objects.create(name=u'Name')
        # The verbose_name we specified
        self.assertEqual('Modelo legado traducible #1', force_unicode(LegacyOnlyVerbosenameIntl._meta.verbose_name))
        self.assertEqual('Modelo legado traducible #1', a._meta.verbose_name)
        # Automatically generated plural form, can be bogus (note the arbitrary
        # 's' tucked at the end)
        self.assertEqual('Modelo legado traducible #1s', force_unicode(LegacyOnlyVerbosenameIntl._meta.verbose_name_plural))
        self.assertEqual('Modelo legado traducible #1s', force_unicode(a._meta.verbose_name_plural))

    def test_i18n_both_verbose_name_options(self):
        a = LegacyBothIntl.objects.create(name=u'Name')
        # The verbose_name we specified
        self.assertEqual('Modelo legado traducible #2', LegacyBothIntl._meta.verbose_name)
        self.assertEqual('Modelo legado traducible #2', a._meta.verbose_name)
        # The verbose_name_plural we specified
        self.assertEqual('Modelos legados traducibles #2', LegacyBothIntl._meta.verbose_name_plural)
        self.assertEqual('Modelos legados traducibles #2', a._meta.verbose_name_plural)

    def test_i18n_only_verbose_name_plural_option(self):
        a = LegacyPluralIntl.objects.create(name=u'Name')
        # Verbose name automatically generated from the class name
        self.assertEqual('legacy plural intl', LegacyPluralIntl._meta.verbose_name)
        self.assertEqual('legacy plural intl', a._meta.verbose_name)
        # The verbose_name_plural we specified
        self.assertEqual('Modelos legados traducibles #3', LegacyPluralIntl._meta.verbose_name_plural)
        self.assertEqual('Modelos legados traducibles #3', a._meta.verbose_name_plural)


class VerboseNameNoI18NTests(TestCase):
    """
    Test new verbose_names() model classmethod behavior when translation isn't
    used.
    """

    def test_backward_compatibility(self):
        """
        Test backward compatibility with legacy Meta.verbose_name{,_plural}
        attributes.
        """
        a = NewstyleSingular.objects.create(name=u'Name')
        # The verbose_name derived from the verbose_names() method we specified
        self.assertEqual('New-style model #1', NewstyleSingular._meta.verbose_name)
        self.assertEqual('New-style model #1', a._meta.verbose_name)
        # Automatically generated plural form, can be bogus (note the arbitrary
        # 's' tucked at the end)
        self.assertEqual('New-style model #1s', force_unicode(NewstyleSingular._meta.verbose_name_plural))
        self.assertEqual('New-style model #1s', force_unicode(a._meta.verbose_name_plural))

        b = NewstyleBoth.objects.create(name=u'Name')
        # The verbose_name derived from the verbose_names() we specified
        self.assertEqual('New-style model #2', NewstyleBoth._meta.verbose_name)
        self.assertEqual('New-style model #2', b._meta.verbose_name)
        # The verbose_name_plural derived from the verbose_names() method we
        # specified
        self.assertEqual('New-style models #2', NewstyleBoth._meta.verbose_name_plural)
        self.assertEqual('New-style models #2', b._meta.verbose_name_plural)

        c = NewstylePlural.objects.create(name=u'Name')
        # Verbose name automatically generated from the class name
        self.assertEqual('newstyle plural', NewstylePlural._meta.verbose_name)
        self.assertEqual('newstyle plural', c._meta.verbose_name)
        # The verbose_name_plural derived from the verbose_names() method we
        # specified
        self.assertEqual('New-style models #3', NewstylePlural._meta.verbose_name_plural)
        self.assertEqual('New-style models #3', c._meta.verbose_name_plural)

    def test_new_behavior(self):
        """
        Test sanity of new verbose_names() model classmethod.
        """
        a = NewstyleSingular.objects.create(name=u'Name')
        self.assertEqual('New-style model #1', NewstyleSingular._meta.get_verbose_name())
        self.assertEqual('New-style model #1', a._meta.get_verbose_name())
        # Fallback get_verbose_name() implementation, its return value
        # can be bogus (note the arbitrary 's' tucked at the end)
        self.assertEqual('New-style model #1s', force_unicode(NewstyleSingular._meta.get_verbose_name(0)))
        self.assertEqual('New-style model #1s', force_unicode(a._meta.get_verbose_name(0)))

        b = NewstyleBoth.objects.create(name=u'Name')
        self.assertEqual('New-style model #2', NewstyleBoth._meta.get_verbose_name())
        self.assertEqual('New-style model #2', b._meta.get_verbose_name())

        self.assertEqual('New-style models #2', NewstyleBoth._meta.get_verbose_name(0))
        self.assertEqual('New-style models #2', b._meta.get_verbose_name(0))

        c = NewstylePlural.objects.create(name=u'Name')
        # Fallback get_verbose_name() implementation: Returns a value
        # automatically generated from the class name
        self.assertEqual('newstyle plural', NewstylePlural._meta.get_verbose_name())
        self.assertEqual('newstyle plural', c._meta.get_verbose_name())

        self.assertEqual('New-style models #3', NewstylePlural._meta.get_verbose_name(0))
        self.assertEqual('New-style models #3', c._meta.get_verbose_name(0))


class VerboseNameI18NTests(TestCase):
    """
    Test new verbose_names() model classmethod behavior when translation is
    used.
    """

    def setUp(self):
        translation.activate('es-ar')

    def tearDown(self):
        translation.deactivate()

    def test_backward_compatibility(self):
        """
        Test backward compatibility with legacy Meta.verbose_name{,_plural}
        attributes.
        """
        a = NewstyleSingularIntl.objects.create(name=u'Name')
        # The verbose_name derived from the verbose_names() method we specified
        self.assertEqual('Modelo moderno traducible #1', NewstyleSingularIntl._meta.verbose_name)
        self.assertEqual('Modelo moderno traducible #1', a._meta.verbose_name)
        # Automatically generated plural form, can be bogus (note the arbitrary
        # 's' tucked at the end)
        self.assertEqual('Modelo moderno traducible #1s', force_unicode(NewstyleSingularIntl._meta.verbose_name_plural))
        self.assertEqual('Modelo moderno traducible #1s', force_unicode(a._meta.verbose_name_plural))

        b = NewstyleBothIntl.objects.create(name=u'Name')
        # The verbose_name derived from the verbose_names() we specified
        self.assertEqual('Modelo moderno traducible #2', force_unicode(NewstyleBothIntl._meta.verbose_name))
        self.assertEqual('Modelo moderno traducible #2', b._meta.verbose_name)
        # The verbose_name_plural derived from the verbose_names() method we
        # specified
        self.assertEqual('Modelos modernos traducibles #2', NewstyleBothIntl._meta.verbose_name_plural)
        self.assertEqual('Modelos modernos traducibles #2', b._meta.verbose_name_plural)

        c = NewstylePluralIntl.objects.create(name=u'Name')
        # Verbose name automatically generated from the class name -- untranslatable
        self.assertEqual('newstyle plural intl', NewstylePluralIntl._meta.verbose_name)
        self.assertEqual('newstyle plural intl', c._meta.verbose_name)
        # The verbose_name_plural derived from the verbose_names() method we
        # specified
        self.assertEqual('Modelos modernos traducibles #3', NewstylePluralIntl._meta.verbose_name_plural)
        self.assertEqual('Modelos modernos traducibles #3', c._meta.verbose_name_plural)

    def test_new_behavior(self):
        """
        Test sanity of new verbose_names() model classmethod.
        """
        a = NewstyleSingularIntl.objects.create(name=u'Name')
        self.assertEqual('Modelo moderno traducible #1', NewstyleSingularIntl._meta.get_verbose_name())
        self.assertEqual('Modelo moderno traducible #1', a._meta.get_verbose_name())
        # Fallback get_verbose_name() implementation, its return value
        # can be bogus (note the arbitrary 's' tucked at the end)
        self.assertEqual('Modelo moderno traducible #1s', force_unicode(NewstyleSingularIntl._meta.get_verbose_name(0)))
        self.assertEqual('Modelo moderno traducible #1s', force_unicode(a._meta.get_verbose_name(0)))

        b = NewstyleBothIntl.objects.create(name=u'Name')
        self.assertEqual('Modelo moderno traducible #2', NewstyleBothIntl._meta.get_verbose_name())
        self.assertEqual('Modelo moderno traducible #2', b._meta.get_verbose_name())

        self.assertEqual('Modelos modernos traducibles #2', NewstyleBothIntl._meta.get_verbose_name(0))
        self.assertEqual('Modelos modernos traducibles #2', b._meta.get_verbose_name(0))

        c = NewstylePluralIntl.objects.create(name=u'Name')
        # Fallback get_verbose_name() implementation: Returns a value
        # automatically generated from the class name -- untranslatable
        self.assertEqual('newstyle plural intl', NewstylePluralIntl._meta.get_verbose_name())
        self.assertEqual('newstyle plural intl', c._meta.get_verbose_name())

        self.assertEqual('Modelos modernos traducibles #3', NewstylePluralIntl._meta.get_verbose_name(0))
        self.assertEqual('Modelos modernos traducibles #3', c._meta.get_verbose_name(0))
