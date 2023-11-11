from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Quote
from django.http import HttpResponse
from django.contrib import admin
from .models import Contact
from django.http import HttpResponse
from .forms import ContactForm  # Import the ContactAdminForm


class QuoteAdminForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [
            "service",
            "name",
            "phone_number",
            "email",
            "company_name",
            "industry",
            "forwarded_to",
        ]

    forwarded_to = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(
            is_superuser=False
        ),  # Show 'forwarded_to' only to staff
        required=False,
        widget=FilteredSelectMultiple("Forwarded to", is_stacked=False),
    )


class QuoteAdmin(admin.ModelAdmin):
    form = QuoteAdminForm

    def get_fieldsets(self, request, obj=None):
        # Customize fieldsets based on user's role
        if request.user.is_superuser:
            fieldsets = [
                (
                    None,
                    {
                        "fields": [
                            "service",
                            "name",
                            "phone_number",
                            "email",
                            "company_name",
                            "industry",
                            "forwarded_to",
                        ]
                    },
                ),
            ]
        else:
            fieldsets = [
                (
                    None,
                    {
                        "fields": [
                            "service",
                            "name",
                            "phone_number",
                            "email",
                            "company_name",
                            "industry",
                        ]
                    },
                ),
            ]

        return fieldsets

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(forwarded_to=request.user)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        quote = Quote.objects.get(pk=object_id)
        if request.user.is_superuser or request.user in quote.forwarded_to.all():
            return super().change_view(request, object_id, form_url, extra_context)

        return HttpResponse("You are not authorized to view this quote.")


admin.site.register(Quote, QuoteAdmin)


from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Contact
from django.http import HttpResponse


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "message", "forwarded_to"]

    forwarded_to = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(is_superuser=False),  # Only show non-superusers
        required=False,
        widget=FilteredSelectMultiple("Forwarded to", is_stacked=False),
    )


class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            fieldsets = [
                (
                    None,
                    {
                        "fields": ["name", "email", "phone", "message", "forwarded_to"],
                    },
                ),
            ]
        else:
            fieldsets = [
                (
                    None,
                    {
                        "fields": ["name", "email", "phone", "message"],
                    },
                ),
            ]

        return fieldsets

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(forwarded_to=request.user)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "forwarded_to" and not request.user.is_superuser:
            kwargs["widget"] = FilteredSelectMultiple(
                db_field.verbose_name, is_stacked=False
            )
            kwargs["queryset"] = User.objects.filter(is_superuser=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        contact = Contact.objects.get(pk=object_id)
        if request.user.is_superuser or request.user in contact.forwarded_to.all():
            return super().change_view(request, object_id, form_url, extra_context)

        return HttpResponse("You are not authorized to view this contact.")


admin.site.register(Contact, ContactAdmin)
