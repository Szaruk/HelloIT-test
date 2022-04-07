from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home_page')


class Post(models.Model):
    title = models.CharField('Tytuł', max_length=255)
    header_image = models.TextField('Baner', null=True, blank=True)
    text = models.TextField('Treść', default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField('Data utworzenia', default=timezone.now)
    published_date = models.DateTimeField('Data publikacji', blank=True, null=True)
    # category = models.CharField('Kategoria', max_length=255, default='brak')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria")
    slug_field = AutoSlugField(populate_from='title', unique_with='published_date', default="")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posty"

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + " | " + str(self.author) + " | " + str(self.category)

    def get_absolute_url(self):
        return reverse('post_details', args={self.slug_field})


class RegulationsSection(models.Model):
    SectionName = models.CharField(max_length=255)

    def __str__(self):
        return self.SectionName

    def get_absolute_url(self):
        return reverse('regulations')

    class Meta:
        verbose_name = "Sekcje Regulaminu"
        verbose_name_plural = "Regulamin"


class RegulationsSectionDetail(models.Model):
    SectionName = models.ForeignKey(RegulationsSection, on_delete=models.CASCADE)
    SectionData = models.CharField('Treść', max_length=255)

    def __str__(self):
        return str(self.SectionName) + " | " + str(self.SectionData)


class Team(models.Model):
    team_name = models.CharField("Nazwa drużyny", max_length=30, default="", unique=True)

    def published(self):
        self.save()

    class Meta:
        verbose_name = "Drużyna"
        verbose_name_plural = "Drużyny"

    def __str__(self):
        return str(self.team_name)


class Position(models.Model):
    position_name = models.CharField("Stanowisko", max_length=50, default="", unique=True)

    def published(self):
        self.save()

    class Meta:
        verbose_name = "Stanowisko"
        verbose_name_plural = "Stanowiska"

    def __str__(self):
        return str(self.position_name)


class People(models.Model):
    people_name = models.CharField('Imię', max_length=30, help_text="Maks. 30 znaków")
    people_surname = models.CharField('Nazwisko', max_length=50, help_text="Maks. 50 znaków")
    people_photo = models.TextField('Zdjęcie', default="", help_text="Wymiary min. 492px x 633px,"
                                                                     " zostaw puste dla domyślnego zdjęcia", blank=True)
    people_portfolio = models.TextField('Link do portfolio',
                                        default="", blank=True,
                                        help_text="Po kliknięciu w kafelek osoby, nastąpi przekierowanie na podany link"
                                        )
    people_position = models.ForeignKey(Position, on_delete=models.CASCADE, db_column="Stanowisko",
                                        blank=True, null=True)
    is_founder = models.BooleanField('"Ojciec Założyciel"', default=False)
    is_overseer = models.BooleanField('Opiekun Koła', default=False)
    people_team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column="Drużyny",
                                    blank=True, null=True)

    def published(self):
        self.save()

    class Meta:
        verbose_name = "Osoba"
        verbose_name_plural = "Osoby"

    def __str__(self):
        return str(self.people_name) + " " + str(self.people_surname) + " | " + str(self.people_position) + \
               ", Drużyna: " + str(self.people_team)

    def get_absolute_url(self):
        return reverse('about_people')


class About(models.Model):
    div_id = models.CharField(max_length=20, help_text="Maks. 20 znaków, małe litery, zamiast spacji podkreślniki. "
                                                       "Musi być unikatowy.", unique=True)
    img = models.TextField(default="", help_text="Wysokość 150px.")
    title = models.CharField(max_length=50, help_text="Maks. 50 znaków")
    content = models.TextField(default="")

    def published(self):
        self.save()

    def __str__(self):
        return str(self.title) + " | " + str(self.div_id)


class Project(models.Model):
    banner_img = models.TextField('Baner', default="", help_text="Baner na górze szczegółów projektu. Wysokość 400px.")
    preview_img = models.TextField('Miniaturka', default="", help_text="Grafika na kafelku projektu. "
                                                                       "Szer. 350px, wys. 200px.")
    project_name = models.CharField('Nazwa projektu', max_length=100, help_text="Maks. 100 znaków")
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Nazwa drużyny")
    short_info = models.CharField('Krótka informacja', max_length=130, help_text="Maks. 130 znaków", blank=True,
                                  null=True)
    full_info = models.TextField('Pełna informacja', default="", help_text="Pełna informacja o projekcie")
    date = models.DateTimeField('Data', default=timezone.now)
    update_date = models.DateTimeField('Aktualizacja', auto_now_add=True, auto_now=False,
                                       help_text="Automatycznie aktualizowane, nie ruszać")
    slug_field = AutoSlugField(populate_from='project_name', unique_with='date', default="")

    def published(self):
        self.save()
        self.date_posted = timezone.now()

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekty"

    def __str__(self):
        return "\"" + str(self.project_name) + "\" | " + str(self.team_name)

    def get_absolute_url(self):
        return reverse("projects_view", args={self.slug_field})


class OtherProject(models.Model):
    banner_img = models.TextField('Baner', default="", help_text="Baner na górze szczegółów projektu. Wysokość 400px.")
    preview_img = models.TextField('Miniaturka', default="", help_text="Grafika na kafelku projektu. "
                                                                       "Szer. 350px, wys. 200px.")
    project_name = models.CharField('Nazwa projektu', max_length=100, help_text="Maks. 100 znaków")
    creators_name = models.TextField('Twórca(y)', default="", help_text="Twórcy projektu", blank=True, null=True)
    short_info = models.CharField('Krótka informacja', max_length=130, help_text="Maks. 130 znaków", blank=True,
                                  null=True)
    full_info = models.TextField('Pełna informacja', default="", help_text="Pełna informacja o projekcie")
    date = models.DateTimeField('Data', default=timezone.now)
    update_date = models.DateTimeField('Aktualizacja', auto_now_add=True, auto_now=False,
                                       help_text="Automatycznie aktualizowane, nie ruszać")
    slug_field = AutoSlugField(populate_from='project_name', unique_with='date', default="")

    def published(self):
        self.save()
        self.date_posted = timezone.now()

    class Meta:
        verbose_name = "Projekt Indywidualny"
        verbose_name_plural = "Projekty Indywidualne"

    def __str__(self):
        return "\"" + str(self.project_name) + "\" | " + str(self.creators_name)

    def get_absolute_url(self):
        return reverse("projects_view2", args={self.slug_field})


class ProjectImg(models.Model):
    reference = models.ForeignKey(Project, on_delete=models.CASCADE,
                                  help_text="Wybierz do którego postu chcesz dodać sekcję")
    img = models.CharField('Obrazek', default="", help_text="To samo się skaluje.", max_length=255)
    help_title = models.CharField('Nazwa obrazka', max_length=50,
                                  default="", help_text="Pomocniczy tytuł do bazy danych. Max. 50 znaków")

    def published(self):
        self.save()

    class Meta:
        verbose_name = "Zdjęcie do projektu"
        verbose_name_plural = "Zdjęcia do projektu"

    def __str__(self):
        return "Projekt: " + str(self.reference) + ", tytuł pomocniczy: " + str(self.help_title)

    def get_absolute_url(self):
        return reverse("projects")


class OtherImg(models.Model):
    reference = models.ForeignKey(OtherProject, on_delete=models.CASCADE,
                                  help_text="Wybierz do którego postu chcesz dodać sekcję")
    img = models.CharField('Obrazek', default="", blank=True, help_text="To samo się skaluje.", max_length=255)
    help_title = models.CharField('Tytuł pomocniczy',
                                  default="", max_length=50, help_text="Pomocniczy tytuł do bazy danychMax. 50 znaków")

    def published(self):
        self.save()

    class Meta:
        verbose_name = "Zdjęcie do innego projektu"
        verbose_name_plural = "Zdjęcia do innego projektu"

    def __str__(self):
        return "Post: " + str(self.reference) + ", tytuł pomocniczy: " + str(self.help_title)

    def get_absolute_url(self):
        return reverse("projects")
