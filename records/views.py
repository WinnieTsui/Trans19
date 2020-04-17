from django.views.generic import TemplateView, ListView
from records.models import Patient, Location

class ViewingLocation(TemplateView):
	template_name = "location_list.html"
	def get_context_data(self, **kwargs):
		patient = self.kwargs['patient']
		context = super().get_context_data(**kwargs)
		context['location_list'] = Location.objects.filter(patient__pk = patient)
		context['patient'] = Patient.objects.get(pk = patient)
		return context

class ViewingPatient(ListView):
	template_name = "patient_list.html"
	model = Patient