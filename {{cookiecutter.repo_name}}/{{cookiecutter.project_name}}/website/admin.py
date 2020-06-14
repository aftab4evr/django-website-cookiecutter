from django.contrib import admin

# Register your models here.

from staticcontent.models import AboutUs, TermsConditions, PrivacyPolicy, ContactUs


class AboutUsAdmin(admin.ModelAdmin):
    """
        AboutUs Model admin with display liast,link,read only feilds and search option.
    """
    icon = '<i class="material-icons">account_circle</i>'
    list_display = ['id', 'title', ]


admin.site.register(AboutUs, AboutUsAdmin)


class TermsConditionsAdmin(admin.ModelAdmin):
    """
        TermsConditions Model admin with display liast,link,read only feilds and search option.
    """
    icon = '<i class="material-icons">account_circle</i>'
    list_display = ['id', 'title', ]


admin.site.register(TermsConditions, TermsConditionsAdmin)


class PrivacyPolicyAdmin(admin.ModelAdmin):
    """
        PrivacyPolicy Model admin with display liast,link,read only feilds and search option.
    """
    icon = '<i class="material-icons">account_circle</i>'
    list_display = ['id', 'title', ]


admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    """
        ContactUs Model admin with display liast,link,read only feilds and search option.
    """
    icon = '<i class="material-icons">account_circle</i>'
    list_display = ['id', 'email', ]


admin.site.register(ContactUs, ContactUsAdmin)
