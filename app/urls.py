from django.conf.urls import url, include, patterns
import app.views

urlpatterns = [    
    url(r'^ajaxexample$', 'app.views.main'),
    
    
]