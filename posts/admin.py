from django.contrib import admin

# Register your models here.
from .models import Post

class MemberAdmin(admin.ModelAdmin):
    list_display="title","content","image"

admin.site.register(Post,MemberAdmin)