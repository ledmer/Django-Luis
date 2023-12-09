from django.contrib import admin
from blog.models import Post, Comment


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','body','image']
    list_display = ['current_time','slug']
    list_filter = ['current_time']
    inlines = [CommentItemInline]
    prepopulated_fields = {"slug": ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','current_time','post']



  

class BlogAdminArea(admin.AdminSite):
    site_header = "IAP Blog Admin Area"

blog_site = BlogAdminArea(name="BlogAdmin")
blog_site.register(Post, PostAdmin)
#blog_site.register(Post)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


# Register your models here.
#admin.site.register(Post)
#blog_site.register(models.Post)
