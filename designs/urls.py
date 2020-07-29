from django.urls import path
from . import views
from designs.views import DesignCreateView, DesignListView, DesignDetailView

urlpatterns = [
	path('', DesignListView.as_view(), name='designs-index'),
	path('new', DesignCreateView.as_view(), name='designs-create'),
	path('details/<int:pk>/', DesignDetailView.as_view(), name='designs-detail'),
]