from django import forms

from resume import models
from django.utils.translation import gettext_lazy as _

from django.forms.models import inlineformset_factory
class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = models.PersonalInfo
        gender = forms.ChoiceField(widget=forms.RadioSelect(
            attrs={'required': 'required', 'class': "form-check-input", 'type': "radio"})
                                   )

        fields = ['firstname', 'middlename', 'lastname', 'email', 'dob', 'gender', 'phone', 'country', 'state', 'city','image', 'template','facebook','twitter', 'github','linkedin','youtube']
        widgets = {

            'firstname': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "First Name"}),
            'middlename': forms.TextInput(
                attrs={'class': 'form-control ','placeholder': "Middle Name"}),
            'lastname': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required', 'placeholder': "Last Name"}),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Email"}),
            'dob': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': " Date of birth "}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Phone"}),
            'country': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Country"}),
            'state': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "State"}),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "city"}),
            
            'facebook': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Facebook"}),
            
            'twitter': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Twitter"}),
            
            'github': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Github"}),
            
            'youtube': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Youtube"}),

            'linkedin': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "LinkedIn"}),
        }



class EducationalForm(forms.ModelForm):
    class Meta:
        model = models.EducationalInfo
        fields = ['program', 'institution', 'course', 'edate1', 'edate2']
        widgets = {

            'program': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Enter program"}),
            'institution': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': "Enter Institution "}),
            'course': forms.TextInput(
                attrs={'class': 'form-control ','placeholder': "Enter Course"}),
            'edate1': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Starting Date "}),
            'edate2': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Ending Date "}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("edate1")
        end_date = cleaned_data.get("edate2")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = models.ExperienceInfo
        fields = ['company', 'title', 'course', 'startingDate', 'endingDate', 'experienceInfo']

        widgets = {

            'company': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Enter Company"}),
            'title': forms.TextInput(
                attrs={'class': 'form-control ','placeholder': "Enter Job Title "}),
            'course': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': "Enter Course / Project"}),
            'startingDate': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Starting Date "}),
            'endingDate': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Ending Date "}),
            'experienceInfo': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "Enter Company"}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("startingDate")
        end_date = cleaned_data.get("endingDate")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")



class SkillForm(forms.ModelForm):
    class Meta:
        model = models.Skills
        fields = ['skill']

        widgets = {

            'skill': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Skills seperated by comma , "})
        }


class CertificateForm(forms.ModelForm):
    class Meta:
        model = models.Certificate
        fields = ['certificate', 'certificateDate']
        widgets = {

            'certificate': forms.TextInput(
                attrs={'class': 'form-control','placeholder': "Certificate Name "}),
            'certificateDate': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Certified Date "}),
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = ['language']

        widgets = {

            'language': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Language"})
        }


class PersonalDescriptionForm(forms.ModelForm):
    class Meta:
        model = models.PersonalDescription
        fields = ['about','Job_title']

        widgets = {
            'Job_title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Your Main Job Title"}),
            'about': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "About YourSelf"})

        }


class OthersForm(forms.ModelForm):
    class Meta:
        model = models.Others
        fields = ['title','introduction']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Title"}),
            'introduction': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "Description"})
        }


EducationalFormset = inlineformset_factory(models.PersonalInfo,
                                   models.EducationalInfo, form=EducationalForm, extra=1, can_delete=True)
ExperienceFormset = inlineformset_factory(models.PersonalInfo,
                                              models.ExperienceInfo, form=ExperienceForm, extra=1, can_delete=True)
SkillFormset = inlineformset_factory(models.PersonalInfo,
                                            models.Skills, form=SkillForm, extra=1, can_delete=True)
CertificateFormset = inlineformset_factory(models.PersonalInfo,
                                   models.Certificate, form=CertificateForm, extra=1, can_delete=True)
LanguageFormset = inlineformset_factory(models.PersonalInfo,
                                              models.Language, form=LanguageForm, extra=1, can_delete=True)
OthersFormset = inlineformset_factory(models.PersonalInfo,
                                            models.Others, form=OthersForm, extra=1, can_delete=True)
                                            
PersonalDescriptionFormset = inlineformset_factory(models.PersonalInfo,
                                            models.PersonalDescription, form=PersonalDescriptionForm)


class MessagesForm(forms.ModelForm):
    class Meta:
        model = models.Messagebox
        exclude =['created_date']
        widgets = {
            'full_Name': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Full Name"}),
            'email': forms.TextInput(
                attrs={'class': 'form-control ','placeholder': "Email"}),
            'subject': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Subject"}),
            'message': forms.Textarea(
                attrs={'class': 'form-control ',"rows":5, "cols":20,  'placeholder': "Your Message"}),
        }