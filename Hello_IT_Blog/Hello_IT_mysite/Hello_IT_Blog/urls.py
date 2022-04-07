from django.urls import path, include
from . import views
from .views import HomeView, PostDetailView, PeopleAboutView, ProjectsView, ProjectDetails
from .views import AddPostView, UpdatePostView, DeletePostView, AddCategoryView, category_view, AddPerson, ModifyPerson
from .views import DeletePerson, AddProject, UpdateProject, DeleteProject, AddImg, UpdateImg, DeleteImg
from .views import OtherProjectDetails, AddOtherProject, UpdateOtherProject, DeleteOtherProject, AddOtherImg
from .views import UpdateOtherImg, DeleteOtherImg, ChooseProject, ChooseSection, SecretLoginPanel, RegulationsNew
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name="home_page"),
    path('post/<slug:slug_field>', PostDetailView.as_view(), name="post_details"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('post/edit/<slug:slug_field>', UpdatePostView.as_view(), name="update_post"),
    path('post/delete/<slug:slug_field>', DeletePostView.as_view(), name="delete_post"),
    path('category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:categories>/', category_view, name="category"),
    path('statute/', RegulationsNew.as_view(), name="regulations"),
    path('about/', PeopleAboutView.as_view(), name="about_people"),
    path('projects/', ProjectsView.as_view(), name="projects"),
    path('our_projects/<slug:slug_field>', ProjectDetails.as_view(), name="projects_view"),
    path('other_projects/<slug:slug_field>', OtherProjectDetails.as_view(), name="projects_view2"),
    path('contact/', views.contact, name="contact"),
    path('add_person/', AddPerson.as_view(), name="add_person"),
    path('edit_person/<int:pk>', ModifyPerson.as_view(), name="update_person"),
    path('delete_person/<int:pk>', DeletePerson.as_view(), name="delete_person"),
    path('add_project/', AddProject.as_view(), name="add_project"),
    path('update_project/<slug:slug_field>', UpdateProject.as_view(), name="update_project"),
    path('delete_project/<slug:slug_field>', DeleteProject.as_view(), name="delete_project"),
    path('our_projects/add_section/', AddImg.as_view(), name="add_img"),
    path('our_projects/update_img/<int:pk>', UpdateImg.as_view(), name="update_img"),
    path('our_projects/delete_img/<int:pk>', DeleteImg.as_view(), name="delete_img"),
    path('add_other_project/', AddOtherProject.as_view(), name="add_other_project"),
    path('update_other_project/<slug:slug_field>', UpdateOtherProject.as_view(), name="update_other_project"),
    path('delete_other_project/<slug:slug_field>', DeleteOtherProject.as_view(), name="delete_other_project"),
    path('other_projects/add_img/', AddOtherImg.as_view(), name="add_other_img"),
    path('other_projects/update_img/<int:pk>/', UpdateOtherImg.as_view(), name="update_other_img"),
    path('other_projects/delete_img/<int:pk>/', DeleteOtherImg.as_view(), name="delete_other_img"),
    path('choose_project_type', ChooseProject.as_view(), name="choose_project_type"),
    path('choose_img_type', ChooseSection.as_view(), name="choose_img_type"),
    path('super_secret_login_panel', SecretLoginPanel.as_view(), name="super_secret_login_panel")
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


