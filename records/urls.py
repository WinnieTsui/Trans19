from django.urls import path 
from records import views

urlpatterns = [ 
  path('patientLocation/<int:patient>',
  	views.ViewingLocation.as_view(),
  	name='patient-location'),
  path('patient',
  	views.ViewingPatient.as_view(),
  	name='patient'),
]