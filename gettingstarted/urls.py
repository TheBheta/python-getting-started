from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("start-game/", hello.views.start_game, name="start_game"),
    path("submit-guess/", hello.views.submit_guess, name="submit-guess"),
    path("update-guesses/", hello.views.update_guesses, name="update-guesses"),
    path("game-status/", hello.views.game_status, name="game-status"),
    path("admin/", admin.site.urls),
]
