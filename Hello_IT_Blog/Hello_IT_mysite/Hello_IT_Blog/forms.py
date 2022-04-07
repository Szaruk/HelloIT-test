from django import forms
from .models import Post, Category, People, Project, ProjectImg, OtherProject,\
    OtherImg, Team, Position

# choices = [('C#', 'C#'), ('Python', 'Python')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'text', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('people_name', 'people_surname', 'people_photo', 'people_portfolio',
                  'people_position', 'is_founder', 'is_overseer', 'people_team')

        widgets = {
            'people_name': forms.TextInput(attrs={'class': 'form-control'}),
            'people_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'people_photo': forms.TextInput(attrs={'class': 'form-control'}),
            'people_portfolio': forms.TextInput(attrs={'class': 'form-control'}),
            'people_position': forms.Select(attrs={'class': 'form-control'}),
            'is_founder': forms.CheckboxInput(),
            'is_overseer': forms.CheckboxInput(),
            'people_team': forms.Select(attrs={'class': 'form-control'}),
        }


class ProjectEdit(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('banner_img', 'preview_img', 'project_name', 'team_name', 'short_info',
                  'full_info')

        widgets = {
            'banner_img': forms.TextInput(attrs={'class': 'form-control'}),
            'preview_img': forms.TextInput(attrs={'class': 'form-control'}),
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'team_name': forms.Select(attrs={'class': 'form-control'}),
            'short_info': forms.TextInput(attrs={'class': 'form-control'}),
            'full_info': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ProjectEditData(forms.ModelForm):
    class Meta:
        model = ProjectImg
        fields = ('reference', 'img', 'help_title')

        widgets = {
            'reference': forms.Select(attrs={'class': 'form-control'}),
            'img': forms.TextInput(attrs={'class': 'form-control'}),
            'help_title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class IndProjectEdit(forms.ModelForm):
    class Meta:
        model = OtherProject
        fields = ('banner_img', 'preview_img', 'project_name','creators_name', 'short_info')

        widgets = {
            'banner_img': forms.TextInput(attrs={'class': 'form-control'}),
            'preview_img': forms.TextInput(attrs={'class': 'form-control'}),
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'creators_name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_info': forms.TextInput(attrs={'class': 'form-control'}),
            'full_info': forms.Textarea(attrs={'class': 'form-control'}),
        }


class IndProjectEditData(forms.ModelForm):
    class Meta:
        model = OtherImg
        fields = ('reference', 'img', 'help_title')

        widgets = {
            'reference': forms.Select(attrs={'class': 'form-control'}),
            'img': forms.TextInput(attrs={'class': 'form-control'}),
            'help_title': forms.TextInput(attrs={'class': 'form-control'}),
        }
