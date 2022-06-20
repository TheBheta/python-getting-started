from django.urls import path, include

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path("styles.css", hello.views.index, name="styles.css"),
    path("db/", hello.views.db, name="db"),
    path("start-game/", hello.views.start_game, name="start-game"),
    path("reset-game/", hello.views.reset_game, name="reset-game"),
    path("submit-guess/", hello.views.submit_guess, name="submit-guess"),
    path("submit-chat/", hello.views.submit_chat, name="submit-chat"),
    path("update-guesses/", hello.views.update_guesses, name="update-guesses"),
    path("get-hint/", hello.views.get_hint, name="get-hint"),
    path("update-chat/", hello.views.update_chat, name="update-chat"),
    path("game-status/", hello.views.game_status, name="game-status"),
    path("admin/", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()