from django.shortcuts import render
from .models import Language, Topic

languages = None
queryset = None


def fill_sidebar():
    global languages, queryset
    languages = Language.objects.all().order_by('manual_order')
    queryset = Topic.objects.filter(framework__isnull=True).select_related('language').all()


def index(request):
    fill_sidebar()
    return render(request, 'languages/index.html', {'languages': languages, 'only_language_topics': queryset})


def language_view(request, item_id, name):
    fill_sidebar()
    selected = languages.get(pk=item_id)

    return render(request, 'languages/index.html', {'languages': languages, 'only_language_topics': queryset,
                                                    'selected': selected, 'name': name})


def topic_language_view(request, language_id, name, topic_id, topic_name):
    fill_sidebar()
    selected = languages.get(pk=language_id).topic_set.get(pk=topic_id)

    return render(request, 'languages/index.html', {'languages': languages, 'only_language_topics': queryset,
                                                    'selected': selected, 'name': name, 'topic_name': topic_name})


def framework_view(request, item_id, name, framework_name):
    fill_sidebar()
    selected = languages.get(pk=item_id).framework_set.get(name=framework_name)

    return render(request, 'languages/index.html', {'languages': languages, 'only_language_topics': queryset,
                                                    'selected': selected, 'name': name,
                                                    'framework_name': framework_name})


def topic_framework_view(request, language_id, name, framework_name, topic_id, topic_name):
    fill_sidebar()
    selected = languages.get(pk=language_id).framework_set.get(name=framework_name).topic_set.get(pk=topic_id)

    return render(request, 'languages/index.html', {'languages': languages, 'only_language_topics': queryset,
                                                    'selected': selected, 'name': name,
                                                    'framework_name': framework_name, 'topic_name': topic_name})
