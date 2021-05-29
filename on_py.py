import json
import requests

"""        {
            "office_id": "NWK",
            "loc_id": "15302030",
            "description": "Melvern Dam & Reservoir",
            """
#all info, index 1 is outflow, 0 is elevation, 2 is inflow, 3 is conservation storage,  4 is flood storage, 5 is timezone, 6 is
# location levels, so if flooding or conserving, 7 doesnt exist
reportURL = "CWMS_CRREL.cwms_data_api.get_report_json?p_location_id=15302030&p_parameter_type=Flow%3AStor%3APrecip%3AStage%3AElev&p_last=5&p_last_unit=days&p_unit_system=EN&p_format=JSON"      
#wqreport shows temp
wqReportURL = "CWMS_CRREL.cwms_data_api.get_wq_report_json?p_location_id=15302030&p_parameter_type=Conc%3ACond%3ApH%3APower%3ATemp&p_last=5&p_last_unit=days&p_unit_system=EN&p_format=JSON"
#gives pool data
damSummaryURL = "CWMS_CRREL.cwms_data_api.get_dam_summary_json?p_location_id=15302030&p_unit_system=EN&p_format=JSON"
#no use? inflow outflow maybe
locSummaryURL = "CWMS_CRREL.cwms_data_api.get_loc_summary_json?p_location_id=15302030&p_source=CWMS&p_unit_system=EN&p_format=JSON"
annualVariabilityURL = "CWMS_CRREL.cwms_data_api.get_annual_variability_json?p_id=15302030"
""" "source": "CWMS",
            "lat": "38.51064906",
            "lon": "-95.70822557"
        },
        """

URL = "https://water.usace.army.mil/a2w/"

def get_lake_data(urlextension):
    y = requests.get(URL+urlextension)
    return y.json()

def printme():
    #For outflow levels:
    lakeJSON = get_lake_data(reportURL)
    outflow = lakeJSON[1]['Outflow'][-1]['value']

    #for temp
    tempJSON = get_lake_data(wqReportURL)
    temp = tempJSON[0]['Water Temperature'][-1]['value']

    printstring = f"Lake temp is: {temp} degrees. \nOutflow is: {outflow} cfm."
    print(printstring)
    return printstring

printme()