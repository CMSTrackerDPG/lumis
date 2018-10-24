import json

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from runregistry.tracker.lumis import LumiSectionsRetriever


class IndexView(TemplateView):
    template_name = "lumisapp/index.html"

    def get(self, request, *args, **kwargs):
        run_min = request.GET.get("run_min", None)
        run_max = request.GET.get("run_max", None)

        if run_min and run_max:
            lumis = LumiSectionsRetriever()

            all_lumis = lumis.get_lumis(run_min, run_max)
            good_lumis = lumis.get_lumis(run_min, run_max, good_runs_only=True)

            bad_lumis = {}
            for key, value in all_lumis.items():
                if key not in good_lumis:
                    bad_lumis[key] = value

            all = json.dumps(all_lumis)
            good = json.dumps(good_lumis)
            bad = json.dumps(bad_lumis)

            return render(
                request,
                self.template_name,
                {"all_lumis": all, "good_lumis": good, "bad_lumis": bad},
            )
        return render(request, self.template_name)
