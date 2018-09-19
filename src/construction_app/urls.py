from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ActivityDownloadcsv,ActivityDateView

urlpatterns = {
    url(r'^activity/$', ActivityDownloadcsv.as_view()),
    url(r'^activitydates/(?P<activity>.*)$', ActivityDateView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
