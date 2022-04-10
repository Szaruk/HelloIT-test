from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from .models import Post
from .models import People
from .models import About
from .models import Project, ProjectImg, Category, OtherProject, OtherImg, \
    RegulationsSection, RegulationsSectionDetail
from .forms import PostForm, PeopleForm, ProjectEdit, ProjectEditData, IndProjectEdit, IndProjectEditData, Team
from django.core.mail import send_mail
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = "index.html"
    ordering = ['-id']
    paginate_by = 6

    def get_context_data(self, *args, object_list=None, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


# NIGDY WIĘCEJ NIE CHCĘ WIDZIEĆ WIDOKU TYPU "def"!!!!
# PRZYSIĘGAM, ŻE JAK JESZCZE RAZ BĘDĘ MUSIAŁ MODYFIKOWAĆ BAZĘ DANYCH I MODELE
# I ŻEBY WPROWADZIĆ JEDNĄ MAŁĄ, ALE PRZYDATNĄ ZMIANĘ BĘDĘ MUSIAŁ EDYTOWAĆ WIDOK
# I ZOBACZĘ "def", TO ZNAJDĘ PROJEKTANTA I MU WYTŁUMACZĘ KILKA RZECZY!
def category_view(request, categories):
    category_posts = Post.objects.filter(category__name=categories).order_by('-create_date')
    # Aby widok działał z ForeignKey, musiałem zmienić "category" na "category__name"
    # Szukałem rozwiązania 3 GODZINY!!!
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_new.html', {'categories': categories.title(), 'category_posts': category_posts,
                                               'cat_menu_list': cat_menu_list})


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail_new.html"
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')[:4]  # Wyświetlanie 4 postów
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    # fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "add_category.html"
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "update_post.html"
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"
    # fields = ["title", "text", "header_image"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"
    success_url = reverse_lazy('home_page')


class RegulationsNew(ListView):
    template_name = 'statute.html'
    context_object_name = 'regulations_new'

    def get_context_data(self, **kwargs):
        context = super(RegulationsNew, self).get_context_data(**kwargs)
        context['regulations'] = RegulationsSection.objects.all()
        context['regulations_section'] = RegulationsSectionDetail.objects.all()
        return context

    def get_queryset(self):
        return RegulationsSection.objects.update() and RegulationsSectionDetail.object.update()


class PeopleAboutView(ListView):
    context_object_name = "about_people"
    template_name = "about_us_new.html"

    def get_context_data(self, **kwargs):
        context = super(PeopleAboutView, self).get_context_data(**kwargs)
        context['abouts'] = About.objects.all().order_by('-id')
        context['peoples'] = People.objects.all().order_by('id')
        context['people_group'] = People.objects.exclude(people_team__isnull=True).order_by(F('people_photo').desc(nulls_last=True))
        return context

    def get_queryset(self):
        return People.objects.update()


class ProjectsView(ListView):
    context_object_name = "projects"
    template_name = "projects_new.html"
    ordering = ['id']
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['otherprojects'] = OtherProject.objects.all()
        return context

    def get_queryset(self):
        return Project.objects.update() and OtherProject.objects.update()


class ProjectDetails(DetailView):
    model = Project
    template_name = "project_details_new.html"
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"

    def get_context_data(self, **kwargs):
        context = super(ProjectDetails, self).get_context_data(**kwargs)
        context['images'] = Project.objects.all()
        return context


class OtherProjectDetails(DetailView):
    model = OtherProject
    template_name = "project_details2_new.html"
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"

    def get_context_data(self, **kwargs):
        context = super(OtherProjectDetails, self).get_context_data(**kwargs)
        context['otherimg'] = OtherImg.objects.all()
        return context


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subject
            f"""Mail osoby do kontaktu: " {message_email}
            {message}""",  # message
            message_email,  # form email
            ['hit.helloit@gmail.com'],  # to email
        )
        return render(request, 'contact_new.html', {'message_name': message_name})
    else:
        return render(request, 'contact_new.html', {})


class AddPerson(CreateView):
    model = People
    form_class = PeopleForm
    template_name = "add_person.html"


class ModifyPerson(UpdateView):
    model = People
    form_class = PeopleForm
    template_name = "update_person.html"


class DeletePerson(DeleteView):
    model = People
    template_name = "delete_person.html"
    success_url = reverse_lazy('about_people')


class AddProject(CreateView):
    model = Project
    form_class = ProjectEdit
    template_name = "add_projects.html"


class UpdateProject(UpdateView):
    model = Project
    form_class = ProjectEdit
    template_name = "update_projects.html"
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"


class DeleteProject(DeleteView):
    model = Project
    template_name = "delete_projects.html"
    success_url = reverse_lazy('projects')
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"


class AddImg(CreateView):
    model = ProjectImg
    form_class = ProjectEditData
    template_name = "add_section.html"


class UpdateImg(UpdateView):
    model = ProjectImg
    form_class = ProjectEditData
    template_name = "update_section.html"


class DeleteImg(DeleteView):
    model = ProjectImg
    template_name = "delete_section.html"
    success_url = reverse_lazy('projects')


class AddOtherProject(CreateView):
    model = OtherProject
    form_class = IndProjectEdit
    template_name = "add_projects2.html"


class UpdateOtherProject(UpdateView):
    model = OtherProject
    form_class = IndProjectEdit
    template_name = "update_projects2.html"
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"


class DeleteOtherProject(DeleteView):
    model = OtherProject
    template_name = "delete_projects2.html"
    success_url = reverse_lazy('projects')
    slug_url_kwarg = "slug_field"
    slug_field = "slug_field"


class AddOtherImg(CreateView):
    model = OtherImg
    form_class = IndProjectEditData
    template_name = "add_section2.html"


class UpdateOtherImg(UpdateView):
    model = OtherImg
    form_class = IndProjectEditData
    template_name = "update_section2.html"


class DeleteOtherImg(DeleteView):
    model = OtherImg
    template_name = "delete_section2.html"
    success_url = reverse_lazy('projects')


class ChooseProject(TemplateView):
    template_name = "choose_project.html"


class ChooseSection(TemplateView):
    template_name = "choose_section.html"


class SecretLoginPanel(TemplateView):
    template_name = "secret_login_panel.html"
