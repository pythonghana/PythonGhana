from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
from .models import Team
from .forms import TeamForm
from hitcount.views import HitCountDetailView


class TeamListView(ListView):
   model = Team
   template_name = 'team_list.html'
   context_object_name = 'teams'

class TeamDetailView(HitCountDetailView):
    model = Team
    template_name = 'team_details.html'
    context_object_name = 'team'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_teams': Team.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context


def team_new(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.author = request.user
            team.published_date = timezone.now()
            team.save()
            return redirect('team_detail', team)
    else:
        form = TeamForm()
    return render(request, 'team_edit.html', {'form': form})


def team_edit(request, pk):
    team = get_object_or_404(Team, slug)
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save(commit=False)
            team.author = request.user
            team.published_date = timezone.now()
            team.save()
            return redirect('team_detail', team)
    else:
        form = TeamForm(instance=team)
    return render(request, 'team_edit.html', {'form': form})
 