import json
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import BatHighlight
from . import utils
from datetime import datetime



def get_highlight_list(page_number, items_per_page=20):
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
            data = json.loads(request.body)
            n = int(data.get("n", 0))

            if n <= 0:
                return JsonResponse({"error": "Please provide a valid positive integer for 'n'."}, status=400)

            highlight_ids = list(BatHighlight.objects.values_list('id', flat=True)[:n])
            count = len(highlight_ids)

            BatHighlight.objects.filter(id__in=highlight_ids).delete()

            return JsonResponse({"message": f"Successfully deleted {count} rows."}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid HTTP method. Use DELETE."}, status=405)


def get_highlights():
    return HttpResponse("first highlights")


def get_and_store_new_highlights():
    data = utils.fetch_bat_highlights_from_api()
    if not data or "response" not in data:
        return False  # No new data

    new_matches = []
    for match in data["response"]:
        title = match.get("title", "")
        competition = match.get("competition", "")
        date_str = match.get("date", "")

        try:
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z").date()
        except ValueError:
            continue  # Skip invalid dates

        embed_code = match["videos"][0].get("embed", "") if match.get("videos") else ""

        if BatHighlight.objects.filter(title=title, competition=competition, date=date).exists():
            continue  # Skip existing matches

        new_match = BatHighlight(title=title, competition=competition, date=date, embed_video=embed_code)
        new_match.save()
        new_matches.append(new_match)

    return len(new_matches) > 0 
