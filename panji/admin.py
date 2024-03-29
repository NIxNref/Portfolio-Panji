from django.contrib import admin
from .models import Home, About, Profile, Skills, Portfolio

# Register all models
admin.site.register(Home)
admin.site.register(Portfolio)

# Profile inline for About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

# About admin
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]

# Skills admin
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass
