from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from score_bat_highlights.models import BatHighlight
from score_bat_highlights.serializers import BatHighlightsSerializer
from score_bat_highlights import utils
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from score_bat_highlights.models import BatHighlight
import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import BatHighlight

def highlight_list(request):
    page_number = request.GET.get('page', 1)  # Get the page number from query params
    items_per_page = 20  # Number of items per page
    highlights = BatHighlight.objects.all().order_by('-date')  # Order by date (most recent first)
    paginator = Paginator(highlights, items_per_page)

    try:
        page_obj = paginator.get_page(page_number)
    except Exception:
        return JsonResponse({"error": "Invalid page number"}, status=400)

    highlights_data = [
        {
            "id": h.id,
            "title": h.title,
            "competition": h.competition,
            "date": h.date,
            "embed_video": h.embed_video,
        }
        for h in page_obj
    ]

    return JsonResponse({
        "highlights": highlights_data,
        "total_pages": paginator.num_pages,
        "current_page": page_obj.number,
        "has_next": page_obj.has_next(),
        "has_previous": page_obj.has_previous(),
    })


@csrf_exempt
def delete_first_n_highlights(request):
    if request.method == "DELETE":
        try:
            # Parse the request body for the number of rows to delete
            data = json.loads(request.body)
            n = int(data.get("n", 0))

            if n <= 0:
                return JsonResponse({"error": "Please provide a valid positive integer for 'n'."}, status=400)

            # Fetch IDs of the first n rows
            highlight_ids = list(BatHighlight.objects.values_list('id', flat=True)[:n])
            count = len(highlight_ids)

            # Delete the rows by their IDs
            BatHighlight.objects.filter(id__in=highlight_ids).delete()

            return JsonResponse({"message": f"Successfully deleted {count} rows."}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid HTTP method. Use DELETE."}, status=405)


def get_highlights(request):
    return HttpResponse("first highlits")


def get_and_store_new_highlights(request):
    try:
        # Try fetching and storing highlights
        utils.fetch_and_store_bat_highlights()
        return HttpResponse("New highlights have been fetched and stored.")
    except Exception as e:
        # If an error occurs, return an error response
        return HttpResponse(f"An error occurred: {str(e)}", status=500)


class BatHighlightsViewSet(viewsets.ModelViewSet):
    queryset = BatHighlight.objects.all()
    serializer_class = BatHighlightsSerializer
