from django.contrib import admin
from blogging.models import Post, Category

# This was not fun.....
# Create cat in post
class CategoryInPostInline(admin.TabularInline):
    model = Category.posts.through

# add in line
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInPostInline,
    ]

# add admin cat
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

