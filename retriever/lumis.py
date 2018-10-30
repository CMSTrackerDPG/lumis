from runregistry.client import RunRegistryClient
from retriever.utilities import build_dcs_query_string
from runregistry.utilities import build_range_where_clause


def _convert_data_to_lumi_section_dict(data):
    # element structure: [<run_number>, <section_from>, <section_to>]
    return {
        run_number: [
            [element[1], element[2]]
            for element in list(filter(lambda entry: entry[0] == run_number, data))
        ]
        for run_number in {element[0] for element in data}
    }


class LumiSectionsRetriever:
    def __init__(self):
        self.run_type = "Collisions"
        self.reco_type = "Prompt"
        self.dcs_list = ["Tibtid", "TecM", "TecP", "Tob"]

    def _construct_query(self, runs_where_clause, good_runs_only=False):
        query = (
            "select r.rdr_run_number, r.rdr_section_from, r.rdr_section_to "
            "from runreg_tracker.dataset_lumis r"
        )

        if good_runs_only:
            query += ", runreg_tracker.datasets l"

        query += " where {} ".format(runs_where_clause)

        if good_runs_only:
            query += (
                "and r.rdr_run_number = l.run_number "
                "and l.rda_cmp_pixel = 'GOOD' "
                "and l.rda_cmp_strip = 'GOOD' "
                "and l.rda_cmp_tracking = 'GOOD' "
                "and r.rdr_rda_name = l.rda_name "
            )

        query += (
            "and r.beam1_stable = 1 "
            "and r.beam2_stable = 1 "
            "and r.cms_active = 1 "
            "and {} ".format(build_dcs_query_string(self.dcs_list, "r"))
            + "and r.rdr_rda_name != '/Global/Online/ALL' "
            "and r.rdr_rda_name like '%{}%' ".format(self.run_type)
            + "and r.rdr_rda_name like '%{}%' ".format(self.reco_type)
            + "order by r.rdr_run_number, r.rdr_rda_name, r.rdr_range"
        )

        return query

    def get_lumis(self, run_min, run_max, good_runs_only=False):
        """
        Example:
        >>> retriever = LumiSectionsRetriever()
        >>> retriever.get_lumis("323840", "323842")
        {323841: [[46, 54], [55, 57], [58, 60], [61, 133], [134, 135], [136, 143], [144, 510]]}
        """
        client = RunRegistryClient()
        where_clause = build_range_where_clause(run_min, run_max, "r.rdr_run_number")
        query = self._construct_query(where_clause, good_runs_only)
        response = client.execute_query(query)
        return _convert_data_to_lumi_section_dict(response["data"])

    def get_dcs_off_runs(self, run_min, run_max):

        pass