from runregistry.client import RunRegistryClient


def _construct_min_max_query(year, run_type, min_max):
    """
    :param year: Year of data taking
    :param run_type: Type of data taking (Collisions or Cosmics)
    :param min_max: either "min" or "max"
    :return: SQL query string
    """
    return (
        "select {}(r.runnumber) as min_run "
        "from runreg_tracker.runs r "
        "where r.RUN_CREATED > to_date('{}-01-01', 'YYYY-MM-DD') "
        "and r.run_class_name  like '%{}%'".format(min_max, year, run_type)
    )


def _get_min_max_run_number(year, run_type, min_max):
    """
    Helper function to retrieve the minimum or
    maximum run number of given year and run type
    """
    runreg = RunRegistryClient()
    query = _construct_min_max_query(year, run_type, min_max)
    return runreg.execute_query(query)["data"][0][0]


def get_min_run_number(year, run_type="Collisions"):
    """
    :param year: Year of data taking
    :param run_type: Type of data taking (Collisions or Cosmics)
    :return: First run number of given year and run type
    """
    return _get_min_max_run_number(year, run_type, "min")


def get_max_run_number(year, run_type="Collisions"):
    """
    :param year: Year of data taking
    :param run_type: Type of data taking (Collisions or Cosmics)
    :return: Last run number of given year and run type
    """
    return _get_min_max_run_number(year, run_type, "max")
