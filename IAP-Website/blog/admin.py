from django.contrib import admin
from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title","body"]
    prepopulated_fields = {"slug":("title",)}

class BlogAdminArea(admin.AdminSite):
    site_header = "IAP Blog Admin Area"

blog_site = BlogAdminArea(name="BlogAdmin")
blog_site.register(Post)
#blog_site.register(Post)
admin.site.register(Post,PostAdmin)


# Register your models here.
#admin.site.register(Post)
#blog_site.register(models.Post)
