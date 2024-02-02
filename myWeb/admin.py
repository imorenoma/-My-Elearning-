from django.contrib import admin
<<<<<<< HEAD
from .models import Post

admin.site.register(Post)
=======
from .models import Post, User

admin.site.register(Post)
admin.site.register(User)
>>>>>>> master
