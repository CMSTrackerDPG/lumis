def build_dcs_query_string(dcs_list, table, logical_connector="and"):
    """
    Example:
    >>> build_dcs_query_string(["Tibtid","TecM","TecP","Tob"], "r")
    'r.tibtid_ready = 1 and r.tecm_ready = 1 and r.tecp_ready = 1 and r.tob_ready = 1'
    >>> build_dcs_query_string(["BPIX","FPIX"], "l", "or")
    'l.bpix_ready = 1 or l.fpix_ready = 1'

    :param dcs_list: list of Detector Control Systems which should be ready
    :param table: name of the database table
    :param logical_connector: How the attributes dcs should be connected ("AND"/"OR")
    :return: SQL query string
    """
    return " {} ".format(logical_connector).join(
        ["{}.{}_ready = 1".format(table.lower(), dcs.lower()) for dcs in dcs_list]
    )
