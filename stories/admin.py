from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Publication, City


@admin.register(Author)
class AuthorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("pseudonym",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("pseudonym",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "pseudonym",
                    )
                },
            ),
        )
    )


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("city",)


admin.site.register(City)
