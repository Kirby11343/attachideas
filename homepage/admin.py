from django.contrib import admin

from .models import Post



# Register your models here.


admin.site.register(Post)

# class ImageInline(admin.StackedInline):
#     model = Image
#     extra = 0

# class PostAdmin(admin.ModelAdmin):
#     form = PostForm
#     inlines = [ImageInline]

#     def save_model(self, request, obj, form, change):
#         super(PostAdmin,self).save_model(request, obj, form, change)
#         # obj.save()

#         for afile in request.FILES.getlist('photos_multiple'):
#             obj.images.create(file=afile)
