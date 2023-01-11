from django.urls import path, include
from . import views


urlpatterns = [
    path('add_feature/', views.add_feature, name='add_feature'),
    path('add_label/', views.add_label, name='add_label'),
    path('features/', views.get_features, name='get_features'),
    path('labels/', views.get_labels, name='get_labels'),
    path('features/add', views.AddFeatureView.as_view(), name='add_feature_view'),
    path('labels/add', views.AddLabelView.as_view(), name='add_label_view'),
    path('labels/create', views.LabelCreateAPIView.as_view(), name='label_create'),
    path('features/create', views.FeatureCreateAPIView.as_view(), name='add_feature'),
 ]
