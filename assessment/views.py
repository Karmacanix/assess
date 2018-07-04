# django
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

# this app
from .models import Application, InformationClassification, CloudQuestionnaire, ICTRiskAssessment, ICTVendorAssessment
from .forms import ApplicationForm, ApplicationSubmitForm, ApplicationSecurityDecisionForm, ApplicationPrivacyDecisionForm, ApplicationClinicalDecisionForm, InformationClassificationForm, CloudQuestionnaireForm, ICTRiskAssessmentForm, ICTVendorAssessmentForm #, PrivacyAssessmentForm, NonFunctionalsForm

# Create your views here.
class ApplicationList(ListView):
    model = Application

    def get_context_data(self, **kwargs):
        context = super(ApplicationList, self).get_context_data(**kwargs)
        context['rejected_list'] = Application.objects.filter(assess_status='R')
        context['accepted_list'] = Application.objects.filter(assess_status='P')
        return context


class ApplicationAssessList(ListView):
    model = Application
    template_name = "assessment/applicationassess_list.html"

    def get_context_data(self, **kwargs):
        context = super(ApplicationAssessList, self).get_context_data(**kwargs)
        context['security_list'] = Application.objects.filter(assess_status='A', security_decision='S')
        context['privacy_list'] = Application.objects.filter(assess_status='A', privacy_decision='S')
        context['clinical_list'] = Application.objects.filter(assess_status='A', clinical_decision='S')
        return context


class ApplicationRequestList(ListView):
    model = Application
    template_name = "assessment/applicationrequest_list.html"

    def get_context_data(self, **kwargs):
        context = super(ApplicationRequestList, self).get_context_data(**kwargs)
        context['assessing_list'] = Application.objects.filter(assess_status='A')
        context['new_list'] = Application.objects.filter(assess_status='N')
        return context


class ApplicationDetail(DetailView):
    model = Application

    def get_context_data(self, **kwargs):
        context = super(ApplicationDetail, self).get_context_data(**kwargs)
        a = Application.objects.get(pk=self.kwargs['pk'])
        if hasattr(a, 'informationclassification'):
            context['ic'] = True
        else:
            context['ic'] = False

        if hasattr(a, 'cloudquestionnaire'):
            context['cl'] = True
        else:
            context['cl'] = False
        
        if hasattr(a, 'ictriskassessment'):
            context['bc'] = True
        else:
            context['bc'] = False
        
        if hasattr(a, 'ictvendorassessment'):
            context['va'] = True
        else:
            context['va'] = False
        
        return context


class ApplicationSecurityAssess(SuccessMessageMixin, UpdateView):
    model = Application
    form_class = ApplicationSecurityDecisionForm
    template_name = "assessment/application_assess.html"
    success_message = 'Application ICT security assessment decision successfully updated!'

    def get_context_data(self, **kwargs):
        context = super(ApplicationSecurityAssess, self).get_context_data(**kwargs)
        a = Application.objects.get(pk=self.kwargs['pk'])
        
        if hasattr(a, 'informationclassification'):
            context['ic'] = True
        else:
            context['ic'] = False

        if hasattr(a, 'cloudquestionnaire'):
            context['cl'] = True
        else:
            context['cl'] = False
        
        if hasattr(a, 'ictriskassessment'):
            context['bc'] = True
        else:
            context['bc'] = False
                
        if hasattr(a, 'ictvendorassessment'):
            context['va'] = True
        else:
            context['va'] = False

        return context

    def get_success_url(self):
        return reverse('assessment:application-list')


class ApplicationPrivacyAssess(SuccessMessageMixin, UpdateView):
    model = Application
    form_class = ApplicationPrivacyDecisionForm
    template_name = "assessment/application_assess.html"
    success_message = 'Application privacy assessment decision successfully updated!'

    def get_context_data(self, **kwargs):
        context = super(ApplicationPrivacyAssess, self).get_context_data(**kwargs)
        a = Application.objects.get(pk=self.kwargs['pk'])
        
        if hasattr(a, 'informationclassification'):
            context['ic'] = True
        else:
            context['ic'] = False

        if hasattr(a, 'cloudquestionnaire'):
            context['cl'] = True
        else:
            context['cl'] = False
        
        if hasattr(a, 'ictriskassessment'):
            context['bc'] = True
        else:
            context['bc'] = False
        
        if hasattr(a, 'ictvendorassessment'):
            context['va'] = True
        else:
            context['va'] = False

        return context

    def get_success_url(self):
        return reverse('assessment:application-list')


class ApplicationClinicalAssess(SuccessMessageMixin, UpdateView):
    model = Application
    form_class = ApplicationClinicalDecisionForm
    template_name = "assessment/application_assess.html"
    success_message = 'Clinical Advisor decision successfully updated!'

    def get_context_data(self, **kwargs):
        context = super(ApplicationClinicalAssess, self).get_context_data(**kwargs)
        a = Application.objects.get(pk=self.kwargs['pk'])
        
        if hasattr(a, 'informationclassification'):
            context['ic'] = True
        else:
            context['ic'] = False

        if hasattr(a, 'cloudquestionnaire'):
            context['cl'] = True
        else:
            context['cl'] = False
        
        if hasattr(a, 'ictriskassessment'):
            context['bc'] = True
        else:
            context['bc'] = False
        
        if hasattr(a, 'ictvendorassessment'):
            context['va'] = True
        else:
            context['va'] = False
        
        return context

    def get_success_url(self):
        return reverse('assessment:application-list')


class ApplicationCreate(SuccessMessageMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    success_message = 'Application successfully registered!'
    success_url = reverse_lazy('assessment:application-list')

    def get_initial(self):
        initial = super(ApplicationCreate, self).get_initial()
        initial['requestor'] = self.request.user
        return initial


class ApplicationUpdate(SuccessMessageMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    success_message = 'Application details successfully updated!'


class ApplicationSubmit(SuccessMessageMixin, UpdateView):
    model = Application
    form_class = ApplicationSubmitForm
    template_name="assessment/application_confirm_submit.html"
    success_message = 'Application submitted successfully for assessment!'

    def get_initial(self):
        initial = super(ApplicationSubmit, self).get_initial()
        initial['assess_status'] = 'A'
        return initial


class ApplicationDelete(SuccessMessageMixin, DeleteView):
    model = Application
    success_url = reverse_lazy('assessment:application-list')
    success_message = "Application deleted!"


class InformationClassificationDetail(DetailView):
    model = InformationClassification


class InformationClassificationCreate(SuccessMessageMixin, CreateView):
    model = InformationClassification
    form_class = InformationClassificationForm
    success_message = 'Information Classification successfully saved!'
    success_url = reverse_lazy('assessment:application-list')

    def get_initial(self):
        initial = super(InformationClassificationCreate, self).get_initial()
        initial['app'] = self.kwargs['pk']
        return initial


class InformationClassificationUpdate(SuccessMessageMixin, UpdateView):
    model = InformationClassification
    form_class = InformationClassificationForm
    success_message = 'Information Classification successfully updated!'

    def get_success_url(self):
        return reverse('assessment:informationclassification-detail', kwargs={'pk': self.kwargs['pk']})


class InformationClassificationDelete(SuccessMessageMixin, DeleteView):
    model = InformationClassification
    success_url = reverse_lazy('assessment:application-list')
    success_message = "Information Classification deleted!"


class CloudQuestionnaireDetail(DetailView):
    model = CloudQuestionnaire


class CloudQuestionnaireCreate(SuccessMessageMixin, CreateView):
    model = CloudQuestionnaire
    form_class = CloudQuestionnaireForm
    success_message = 'Cloud Questionnaire successfully saved!'
    success_url = reverse_lazy('assessment:application-list')

    def get_initial(self):
        initial = super(CloudQuestionnaireCreate, self).get_initial()
        initial['app'] = self.kwargs['pk']
        return initial


class CloudQuestionnaireUpdate(SuccessMessageMixin, UpdateView):
    model = CloudQuestionnaire
    form_class = CloudQuestionnaireForm
    success_message = 'Cloud Questionnaire successfully updated!'

    def get_success_url(self):
        return reverse('assessment:cloudquestionnaire-detail', kwargs={'pk': self.kwargs['pk']})


class CloudQuestionnaireDelete(SuccessMessageMixin, DeleteView):
    model = CloudQuestionnaire
    success_url = reverse_lazy('assessment:application-list')
    success_message = "Cloud Questionnaire deleted!"


class ICTRiskAssessmentDetail(DetailView):
    model = ICTRiskAssessment


class ICTRiskAssessmentCreate(SuccessMessageMixin, CreateView):
    model = ICTRiskAssessment
    form_class = ICTRiskAssessmentForm
    success_message = 'ICT Risk Assessment successfully saved!'
    success_url = reverse_lazy('assessment:application-list')

    def get_initial(self):
        initial = super(ICTRiskAssessmentCreate, self).get_initial()
        initial['app'] = self.kwargs['pk']
        return initial


class ICTRiskAssessmentUpdate(SuccessMessageMixin, UpdateView):
    model = ICTRiskAssessment
    form_class = ICTRiskAssessmentForm
    success_message = 'ICT Risk Assessment successfully updated!'

    def get_success_url(self):
        return reverse('assessment:ictriskassessment-detail', kwargs={'pk': self.kwargs['pk']})


class ICTRiskAssessmentDelete(SuccessMessageMixin, DeleteView):
    model = ICTRiskAssessment
    success_url = reverse_lazy('assessment:application-list')
    success_message = "ICT Risk Assessment deleted!"

#ICTVendorAssessment
class ICTVendorAssessmentDetail(DetailView):
    model = ICTVendorAssessment


class ICTVendorAssessmentCreate(SuccessMessageMixin, CreateView):
    model = ICTVendorAssessment
    form_class = ICTVendorAssessmentForm
    success_message = 'ICT Vendor Assessment successfully saved!'
    success_url = reverse_lazy('assessment:application-list')

    def get_initial(self):
        initial = super(ICTVendorAssessmentCreate, self).get_initial()
        initial['app'] = self.kwargs['pk']
        return initial


class ICTVendorAssessmentUpdate(SuccessMessageMixin, UpdateView):
    model = ICTVendorAssessment
    form_class = ICTVendorAssessmentForm
    success_message = 'ICT Vendor Assessment successfully updated!'

    def get_success_url(self):
        return reverse('assessment:ictvendorassessment-detail', kwargs={'pk': self.kwargs['pk']})


class ICTVendorAssessmentDelete(SuccessMessageMixin, DeleteView):
    model = ICTVendorAssessment
    success_url = reverse_lazy('assessment:application-list')
    success_message = "ICT Vendor Assessment deleted!"
# class PrivacyAssessmentDetail(DetailView):
#     model = PrivacyAssessment


# class PrivacyAssessmentCreate(SuccessMessageMixin, CreateView):
#     model = PrivacyAssessment
#     form_class = PrivacyAssessmentForm
#     success_message = 'Privacy Assessment successfully saved!'
#     success_url = reverse_lazy('assessment:application-list')

#     def get_initial(self):
#         initial = super(PrivacyAssessmentCreate, self).get_initial()
#         initial['id'] = self.kwargs['pk']
#         return initial


# class PrivacyAssessmentUpdate(SuccessMessageMixin, UpdateView):
#     model = PrivacyAssessment
#     form_class = PrivacyAssessmentForm
#     success_message = 'Privacy Assessment successfully updated!'

#     def get_success_url(self):
#         return reverse('assessment:privacyassessment-detail', kwargs={'pk': self.kwargs['pk']})


# class PrivacyAssessmentDelete(SuccessMessageMixin, DeleteView):
#     model = PrivacyAssessment
#     success_url = reverse_lazy('assessment:application-list')
#     success_message = "Privacy Assessment deleted!"
#     # def delete(self, request, *args, **kwargs):
#     #     obj = self.get_object()
#     #     messages.success(self.request, self.success_message % obj.__dict__)
#     #     return super(ApplicationDelete, self).delete(request, *args, **kwargs)
