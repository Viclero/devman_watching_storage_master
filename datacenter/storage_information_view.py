from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):

    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit_data in visits:
        non_closed_visits.append(
            {
                'who_entered': visit_data.passcard,
                'entered_at': localtime(visit_data.entered_at),
                'duration': visit_data.format_duration(),
                'is_strange': visit_data.is_visit_long()
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
