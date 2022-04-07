from django.contrib import admin
from .models import Post
from .models import People
from .models import About
from .models import Project, ProjectImg, Category, OtherProject, OtherImg, \
    RegulationsSection, RegulationsSectionDetail, Team, Position

admin.site.register(Post)
admin.site.register(People)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(OtherProject)
admin.site.register(OtherImg)
admin.site.register(Team)
admin.site.register(Position)


class RegulationsSectionDetailsAdmin(admin.StackedInline):
    model = RegulationsSectionDetail


@admin.register(RegulationsSection)
class RegulationsSectionAdmin(admin.ModelAdmin):
    inlines = [RegulationsSectionDetailsAdmin]
    list_display = ('SectionName',)


class ProjectImgAdmin(admin.StackedInline):
    model = ProjectImg


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImgAdmin]
    list_display = ('project_name', 'team_name',)
