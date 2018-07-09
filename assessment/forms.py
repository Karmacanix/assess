#from allauth.account.models import EmailAddress
#from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_select2.forms import Select2MultipleWidget
from django import forms
from .models import Application, InformationClassification, CloudQuestionnaire, ICTRiskAssessment, ICTVendorAssessment, PrivacyAssessment

class ApplicationForm(forms.ModelForm):
	
	class Meta:
		model = Application
		fields = ['name', 'purpose', 'application_type', 'website', 'cost', 'cost_type', 'requestor', 'business_owner', 'dhbs']
		widgets = {			
			'name': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
			'purpose': forms.Textarea(attrs={'class' : 'w3-input w3-border', 'cols': '40', 'rows': '3'}),
			'cost_type': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'requestor': forms.Select(attrs={'class' : 'w3-select w3-border', 'empty_value' : 'Choose a business owner'}),
			'business_owner': forms.Select(attrs={'class' : 'w3-select w3-border'}),
			'application_type': Select2MultipleWidget(attrs={'class' : 'w3-input w3-border', }),
			'dhbs': Select2MultipleWidget(attrs={'class' : 'w3-input w3-border', }),
			'cost': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
			'website': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
		}


class ApplicationSubmitForm(forms.ModelForm):
	
	class Meta:
		model = Application
		fields = ['assess_status']
		widgets = {			
			'assess_status': forms.Select(attrs={'class' : 'w3-select w3-border', 'hidden' : True,}),
		}


class ApplicationSecurityDecisionForm(forms.ModelForm):
	
	class Meta:
		model = Application
		fields = [
			'security_decision',
			'security_comments',
		]
		widgets = {			
			'security_decision': forms.RadioSelect(attrs={'class' : 'w3-option w3-border',}),
			'security_comments': forms.Textarea(attrs={'class' : 'w3-input w3-border', 'cols': '40', 'rows': '3'}),
		}


class ApplicationPrivacyDecisionForm(forms.ModelForm):
	
	class Meta:
		model = Application
		fields = [
			'privacy_decision',
			'privacy_comments',
		]
		widgets = {			
			'privacy_decision': forms.Select(attrs={'class' : 'w3-select w3-border',}),
			'privacy_comments': forms.Textarea(attrs={'class' : 'w3-input w3-border', 'cols': '40', 'rows': '3'}),
		}


class ApplicationClinicalDecisionForm(forms.ModelForm):

	class Meta:
		model = Application
		fields = [
			'clinical_decision',
			'clinical_comments',
		]
		widgets = {			
			'clinical_decision': forms.Select(attrs={'class' : 'w3-select w3-border',}),
			'clinical_comments': forms.Textarea(attrs={'class' : 'w3-input w3-border', 'cols': '40', 'rows': '3'}),
		}


class InformationClassificationForm(forms.ModelForm):
	
 	class Meta:
 		model = InformationClassification
 		fields = '__all__'
 		widgets = {			
			'special_handling_sensitive_other': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
			'medical_in_confidence': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'staff_in_confidence': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'commercial_in_confidence': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'statistical_unclassified': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'unclassified': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'special_handling_sensitive_patient': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'special_handling_sensitive_disease': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'special_handling_sensitive_abuse': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
		}


class CloudQuestionnaireForm(forms.ModelForm):
	
 	class Meta:
 		model = CloudQuestionnaire
 		fields = '__all__'
 		widgets = {			
			'disclosure_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'alteration_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'loss_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'continuity_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
		}


class ICTRiskAssessmentForm(forms.ModelForm):
	
 	class Meta:
 		model = ICTRiskAssessment
 		fields = '__all__'
 		widgets = {			
			'termsconditions_URL': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
			'privacypolicy_URL': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
			'dhb_record_volume': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'dhb_downtime_before_critical': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'dhb_log_data_changes': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'dhb_small_data_loss': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'dhb_large_data_loss': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'dhb_breach_plan': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'dhb_disrupt_plan': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'dhb_perm_loss': forms.RadioSelect(attrs={'class': 'w3-ul'}),
		}
		

class ICTVendorAssessmentForm(forms.ModelForm):
	
 	class Meta:
 		model = ICTVendorAssessment
 		fields = '__all__'
 		widgets = {
 			'host_country': forms.Select(attrs={'class' : 'w3-select w3-border'}),
 			'host_service': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
			'host_deploy': forms.CheckboxSelectMultiple(attrs={'class': 'w3-ul'}),
			'devices': forms.CheckboxSelectMultiple(attrs={'class': 'w3-ul'}),
			'encrypt_transmit': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'encrypt_stored': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'anonimised': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'back_up': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'extract': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'restore': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'log_admin': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'log_access': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'shares_data': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'notify_breach': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'patches': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'testing': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'advise_legal_issues': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'ownership': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'penalty_breach': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'penalty_outage': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'report_outages': forms.RadioSelect(attrs={'class': 'w3-ul'}),
			'backgroud_checks': forms.RadioSelect(attrs={'class': 'w3-ul'}),
		}

		# app, host_country,host_service, host_deploy, devices, encrypt_transmit, encrypt_stored, anonimised, back_up, extract, restore, 
		# log_admin, log_access, shares_data, notify_breach, patches, testing, advise_legal_issues, ownership, penalty_breach, penalty_outage,
		#  report_outages, backgroud_checks

class PrivacyAssessmentForm(forms.ModelForm):
	
	class Meta:
		model = PrivacyAssessment
		fields = ['app','pia_upload']


class CATMeetingForm(forms.ModelForm):
	pass


class IPSGMeetingForm(forms.ModelForm):
	pass