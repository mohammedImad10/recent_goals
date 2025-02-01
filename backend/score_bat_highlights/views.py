from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import BatHighlight
from .serializers import BatHighlightsSerializer
from . import logic  # Import logic functions


def highlight_list(request):
    page_number = request.GET.get('page', 1)
    return logic.get_highlight_list(page_number)


@csrf_exempt
def delete_first_n_highlights(request):
    return logic.delete_first_n_highlights(request)


def get_highlights(request):
    return logic.get_highlights()


def get_and_store_new_highlights(request):
    try:
        success = logic.get_and_store_new_highlights()
        if success is True:
            return JsonResponse({"message": "New highlights have been fetched and stored."}, status=200)
        elif success is False:
            return JsonResponse({"message": "No new highlights found."}, status=200)
        else:
            return JsonResponse({"error": "An unexpected error occurred."}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


class BatHighlightsViewSet(viewsets.ModelViewSet):
    queryset = BatHighlight.objects.all()
    serializer_class = BatHighlightsSerializer
