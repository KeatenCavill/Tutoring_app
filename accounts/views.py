from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import TutorProfile
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

# Create your views here.
class TutorListView(ListView):
    model = TutorProfile
    template_name = "home.html"
    context_object_name = "tutors"

class TutorDetailView(DetailView):
    model = TutorProfile
    template_name = "tutor_detail.html"
    context_object_name = "tutor"
    
    def get_object(self):
        return get_object_or_404(TutorProfile, id=self.kwargs['pk'])



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()

        user.first_name = self.request.POST.get("first_name", "").strip()
        user.last_name = self.request.POST.get("last_name", "").strip()
        user.email = self.request.POST.get("email", "").strip()
        user.save()

        profile, created = TutorProfile.objects.get_or_create(
            user=user,
            defaults={
                "subject": (self.request.POST.get("subject") or "").strip(),
                "description": (self.request.POST.get("description") or "").strip(),
                "mon_start": self.request.POST.get("mon_start") or None,
                "mon_end": self.request.POST.get("mon_end") or None,
                "tue_start": self.request.POST.get("tue_start") or None,
                "tue_end": self.request.POST.get("tue_end") or None,
                "wed_start": self.request.POST.get("wed_start") or None,
                "wed_end": self.request.POST.get("wed_end") or None,
                "thu_start": self.request.POST.get("thu_start") or None,
                "thu_end": self.request.POST.get("thu_end") or None,
                "fri_start": self.request.POST.get("fri_start") or None,
                "fri_end": self.request.POST.get("fri_end") or None,
            }
        )

        if not created:
            for f in [
                "subject", "description",
                "mon_start", "mon_end",
                "tue_start", "tue_end", 
                "wed_start", "wed_end",
                "thu_start", "thu_end",  
                "fri_start", "fri_end"
            ]:
                setattr(profile, f, self.request.POST.get(f) or getattr(profile, f))
            profile.save()

        return redirect(self.success_url)