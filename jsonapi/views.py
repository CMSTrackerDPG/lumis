from django.http import JsonResponse

# Create your views here.
from retriever.lumis import LumiSectionsRetriever


def all(request):
    run_min = request.GET.get("run_min", None)
    run_max = request.GET.get("run_max", None)

    lumis_retriever = LumiSectionsRetriever()
    all_lumis = lumis_retriever.get_lumis(run_min, run_max)
    return JsonResponse(all_lumis)


def good(request):
    run_min = request.GET.get("run_min", None)
    run_max = request.GET.get("run_max", None)

    lumis_retriever = LumiSectionsRetriever()
    good_lumis = lumis_retriever.get_lumis(run_min, run_max, good_runs_only=True)
    return JsonResponse(good_lumis)


def bad(request):
    run_min = request.GET.get("run_min", None)
    run_max = request.GET.get("run_max", None)

    lumis_retriever = LumiSectionsRetriever()

    all_lumis = lumis_retriever.get_lumis(run_min, run_max)
    good_lumis = lumis_retriever.get_lumis(run_min, run_max, good_runs_only=True)

    bad_lumis = {}
    for key, value in all_lumis.items():
        if key not in good_lumis:
            bad_lumis[key] = value

    return JsonResponse(bad_lumis)


def no_dcs(request):
    run_min = request.GET.get("run_min", None)
    run_max = request.GET.get("run_max", None)

    lumis_retriever = LumiSectionsRetriever()
    dcs_ignored = lumis_retriever.get_lumis(run_min, run_max, ignore_dcs=True)
    return JsonResponse(dcs_ignored)
