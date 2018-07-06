from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils.functional import curry
from django_countries.fields import CountryField

# Create your models here.
class Application(models.Model):
	requestor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requestor")
	business_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="business_owner")
	name = models.CharField(max_length=254, primary_key=True)
	website = models.URLField(max_length=200)
	purpose = models.CharField(max_length=254)
	cost = models.CharField(max_length=254)
	COST_CHOICES = (
		('1', 'One time payment'),
		('M', 'Monthly'),
		('Y', 'Annually'),
	)
	cost_type = models.CharField(
		max_length=1,
		choices=COST_CHOICES,
		default='Y',
		verbose_name="Renewal"
	)
	APPLICATION_CHOICES = (
		('C', 'Cloud'),
		('M', 'Mobile'),
		('D', 'Desktop'),
		('T', 'Tablet'),
		('H', 'Hybrid'),
	)
	application_type = models.CharField(
		max_length=1,
		choices=APPLICATION_CHOICES,
		default='C',
		verbose_name="Type"
	)
	ASSESSMENT_STATUS = (
		('N', 'New'),
		('A', 'Assessing'),
		('R', 'Rejected'),
		('P', 'Approved'),
	)
	assess_status = models.CharField(
		max_length=1,
		choices=ASSESSMENT_STATUS,
		default='N',
		verbose_name="Status"
	)
	RISK_RATING = (
		('N', 'No / Negligible Risk'),
		('L', 'Low impact Risk'),
		('H', 'High Impact Risk'),
		('E', 'Extreme Risk'),
	)
	DECISION = (
		('A', 'Accept'),
		('R', 'Reject'),
		('S', 'Assessing'),
	)
	security_decision = models.CharField(
		max_length=1,
		choices=RISK_RATING,
		default='N',
	)
	security_comments = models.CharField(max_length=254, null=True, blank=True)
	privacy_decision = models.CharField(
		max_length=1,
		choices=RISK_RATING,
		default='N',
	)
	privacy_comments = models.CharField(max_length=254, null=True, blank=True)
	clinical_decision = models.CharField(
		max_length=1,
		choices=RISK_RATING,
		default='N',
	)
	clinical_comments = models.CharField(max_length=254, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('assessment:application-detail', kwargs={'pk': self.name})


class InformationClassification(models.Model):
	app = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
	medical_in_confidence = models.BooleanField(default=False, help_text="Personal health information")
	staff_in_confidence = models.BooleanField(default=False, help_text="Identifiable employee and practitioner information that is not intended for the public domain")
	commercial_in_confidence = models.BooleanField(default=False, help_text="Commercially sensitive information that needs protection from unauthorised access")
	statistical_unclassified = models.BooleanField(default=False, help_text="Statistical or financial information that is non–identifiable")
	unclassified = models.BooleanField(default=False, help_text="All other information")
	special_handling_sensitive_patient = models.BooleanField(default=False, help_text="Sensitive patient information (eg VIP’s)")
	special_handling_sensitive_disease = models.BooleanField(default=False, help_text="Sensitive categories of disease (eg Mental Health)")
	special_handling_sensitive_abuse = models.BooleanField(default=False, help_text="Sensitive subjects (violence and abuse; pandemics)")
	special_handling_sensitive_other = models.CharField(max_length=200, null=True, blank=True, help_text="Other")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class CloudQuestionnaire(models.Model):
	app = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
	disclosure_risk = models.BooleanField(default=False, verbose_name='Privacy Breach', help_text="The information is publicly available or it can be de-identified so that its release into the public domain would not compromise our obligations to a person or an organisation.")
	alteration_risk = models.BooleanField(default=False, verbose_name='Information Alteration', help_text="No person or organisation will be harmed if the information is altered by mistake or intentionally by a wrongdoer.")
	loss_risk = models.BooleanField(default=False, verbose_name='Data Loss', help_text="No person or orginastion will be harmed if the information is lost by the cloud provider OR we can easily maintain a local copy of the information.")
	continuity_risk = models.BooleanField(default=False, verbose_name='Business Continuity', help_text="We will be able to carry on our activities if the service is disrupted or is unavailable for an extended.")

	def _get_help_text(self, field_name):

		for field in self._meta.fields:
			if field.name == field_name:
				return field.help_text
	
	def _get_verbose_name(self, field_name):

		for field in self._meta.fields:
			if field.name == field_name:
				return field.verbose_name

	def __init__(self, *args, **kwargs):
		super(CloudQuestionnaire, self).__init__(*args, **kwargs)

		for field in self._meta.fields:
			method_name = "get_{0}_help_text".format(field.name)
			curried_method = curry(self._get_help_text, field_name=field.name)
			setattr(self, method_name, curried_method)
			method_v_name = "get_{0}_verbose_name".format(field.name)
			curried_v_method = curry(self._get_verbose_name, field_name=field.name)
			setattr(self, method_v_name, curried_v_method)


class ICTRiskAssessment(models.Model):
	app = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
	termsconditions_URL = models.URLField(help_text="1. Please copy and paste the apps terms and conditions from the vendors website. Make sure you get the T&Cs for the version of the app you want.")
	privacypolicy_URL = models.URLField(help_text="2. Please copy and paste the apps privacy policy from the vendors website. Make sure you get the privacy policy for the version of the app you want.")
	RECORD_CHOICES = (
		('TENS', '10s'),
		('HUNDREDS', '100s'),
		('THOUSANDS', '1,000s'),
		('TENTHOUSANDS', '10,000s'),
		('HUNDREDTHOUSANDS', '100,000s'),
	)
	dhb_record_volume = models.CharField(max_length=15, choices=RECORD_CHOICES, default='TENS', help_text="3. Provide an estimate of the number of records we expect to store in the application on an annual basis.")
	DOWNTIME_CHOICES = (
		('H', 'Hours'),
		('D', 'Days'),
		('M', 'Months'),
		('I', 'Indefinitely')
	)
	dhb_downtime_before_critical = models.CharField(max_length=1, choices=DOWNTIME_CHOICES, default='H', help_text="4. We can be without this app before our service can no longer function properly. Specify the time interval.")
	UNSURE_CHOICES = (
		('Y', 'Yes'),
		('N', 'No'),
		('U', 'Unsure'),
	)
	dhb_log_data_changes = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="5. We will be able to notice if someone accidentally or maliously alters our data stored in the cloud service.")
	CONVENIENCE_CHOICES = (
		('N', 'None'),
		('I', 'Inconvenience'),
		('D', 'Disruption'),
		('P', 'Personal Injury'),
		('S', 'Significant economic loss'),
		('H', 'Human life endangered'),
	)
	dhb_small_data_loss = models.CharField(max_length=1, choices=CONVENIENCE_CHOICES, default='N', help_text="6. The effect of someone accidentally or malciously altering a SMALL amount of our data stored in the cloud service.")
	dhb_large_data_loss = models.CharField(max_length=1, choices=CONVENIENCE_CHOICES, default='N', help_text="7. The effect of someone accidentally or malciously altering a LARGE amount of our data stored in the cloud service.")
	dhb_breach_plan = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="8. We have a plan we can put into effect if we learn that there has been a privacy or security breach concerning our data stored in the cloud service.")
	dhb_disrupt_plan = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="9. We have a plan we can put into effect if the cloud service is disrupted for an extended period.")
	dhb_perm_loss = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="10. We have a plan we can put into effect if the cloud service loses our data permanently.")

	def _get_help_text(self, field_name):

		for field in self._meta.fields:
			if field.name == field_name:
				return field.help_text
	
	def __init__(self, *args, **kwargs):
		super(ICTRiskAssessment, self).__init__(*args, **kwargs)

		for field in self._meta.fields:
			method_name = "get_{0}_help_text".format(field.name)
			curried_method = curry(self._get_help_text, field_name=field.name)
			setattr(self, method_name, curried_method)


class ICTVendorAssessment(models.Model):
	app = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
	UNSURE_CHOICES = (
			('Y', 'Yes'),
			('N', 'No'),
			('U', 'Unsure'),
		)
	TECH_CHOICES = (
		('M', 'Mobile device'),
		('P', 'PC'),
		('C', 'Citrix terminal'),
		('M', 'Modality'),
	)
	INSTALL_CHOICES = (
		('M', 'Install an app on a mobile device'),
		('P', 'Install an app on a PC or Citrix Terminal'),
		('B', 'Build a server'),
		('D', 'Install a modality'),
		('H', 'The DHB does not have to do anything'),
	)
	TIME_CHOICES = (
		('H','Hours'), 
		('D', 'Days'),
		('M', 'Months'),
		('N', 'Does not'),
	)
	host_country = CountryField(help_text="1. What country or countries is the service hosted in?")
	host_service = models.CharField(max_length=120, help_text="2. Name any 3rd party suppliers used by the vendor to supply this service e.g. Microsoft Azure, Amazon Web Services.")
	host_deploy = models.CharField(max_length=1, choices=INSTALL_CHOICES, default='B', help_text="3. The service requires the customer to do the following work")
	devices = models.CharField(max_length=1, choices=TECH_CHOICES, default='P', help_text="4. Users access the service using the following technology")
	encrypt_transmit = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="5. The data is encrypted when it is being transmitted to the cloud service")
	encrypt_stored = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="6. The customer’s data is encrypted inside the cloud service data store")
	anonimised = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="7. The data is de-identified BEFORE  it is sent to the cloud service")
	back_up = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="8. The vendor backs up the data stored in the cloud service")
	extract = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="9. The vendor provides a means for the customer to download a copy of the  data stored  the cloud service")
	restore = models.CharField(max_length=1, choices=TIME_CHOICES, default='U', help_text="10. The vendor undertakes to re-instate the service in the event of an outage in")
	log_admin = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="11. The vendor logs sys admin access to  the  data stored in the cloud service")
	log_access = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="12. The vendor logs end user access to  the data stored in the cloud service")
	shares_data = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="13. The vendor allows 3rd parties to access the data stored in the cloud service")
	notify_breach = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="14. The vendor will tell the customer if there has been a security or privacy  incident concerning the data stored in the cloud service")
	patches = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="15. The vendor regularly applies  security patches to applications, devices, servers and hypervisors  ")
	testing = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="16. The vendor undertakes regular  security testing / certification")
	advise_legal_issues = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="17. The vendor will tell the customer if there has been a Court Order concerning the data stored in the cloud service")
	ownership = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="18. The vendor’s terms of service give the vendor ownership rights over the data stored in the cloud service")
	penalty_breach = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="19. The vendor will pay compensation if the customer suffers a loss as a result of a privacy or security breach of data stored in the cloud service")
	penalty_outage = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="20. The vendor will  pay compensation if the  customer suffer a loss as a result of the cloud service being unavailable for any length of time")
	report_outages = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="21. The vendor provides a means for the customer to complain in the event of a privacy breach or service disruption")
	backgroud_checks = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="22. The vendor’s HR procedures include background vetting of employees and contractors")

	def _get_help_text(self, field_name):

		for field in self._meta.fields:
			if field.name == field_name:
				return field.help_text
	
	def __init__(self, *args, **kwargs):
		super(ICTVendorAssessment, self).__init__(*args, **kwargs)

		for field in self._meta.fields:
			method_name = "get_{0}_help_text".format(field.name)
			curried_method = curry(self._get_help_text, field_name=field.name)
			setattr(self, method_name, curried_method)

# class PrivacyAssessment