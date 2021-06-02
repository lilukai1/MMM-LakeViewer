import json
import requests
import sys
Lake = {
    'message':'HERE_IS_DATA',
    'Response':200,
    "loc_id": '15302030',
    "description": "Melvern Dam & Reservoir",

}
"""        {
            "office_id": "NWK",
            "loc_id": "15302030",
            "description": "Melvern Dam & Reservoir",
        
#all info, index 1 is outflow, 0 is elevation, 2 is inflow, 3 is conservation storage,  4 is flood storage, 5 is timezone, 6 is
# location levels, so if flooding or conserving, 7 doesnt exist
reportURL = "CWMS_CRREL.cwms_data_api.get_report_json?p_location_id="+loc_id+"&p_parameter_type=Flow%3AStor%3APrecip%3AStage%3AElev&p_last=5&p_last_unit=days&p_unit_system=EN&p_format=JSON"      
#wqreport shows temp
wqReportURL = "CWMS_CRREL.cwms_data_api.get_wq_report_json?p_location_id="+loc_id+"&p_parameter_type=Conc%3ACond%3ApH%3APower%3ATemp&p_last=5&p_last_unit=days&p_unit_system=EN&p_format=JSON"
#gives pool data
damSummaryURL = "CWMS_CRREL.cwms_data_api.get_dam_summary_json?p_location_id="+loc_id+"&p_unit_system=EN&p_format=JSON"
#no use? inflow outflow maybe
locSummaryURL = "CWMS_CRREL.cwms_data_api.get_loc_summary_json?p_location_id="+loc_id+"&p_source=CWMS&p_unit_system=EN&p_format=JSON"
annualVariabilityURL = "CWMS_CRREL.cwms_data_api.get_annual_variability_json?p_id="+loc_id
"source": "CWMS",
            "lat": "38.51064906",
            "lon": "-95.70822557"
        },
        """


def get_lake_data(urlextension, loc_id):
    URL = "https://water.usace.army.mil/a2w/"

    urlextensions = {
    'reportURL' : "CWMS_CRREL.cwms_data_api.get_report_json?p_location_id="+loc_id+"&p_parameter_type=Flow%3AStor%3APrecip%3AStage%3AElev&p_last=5&p_last_unit=days&p_unit_system=EN&p_format=JSON",    
    #wqreport shows temp
    'wqReportURL' : "CWMS_CRREL.cwms_data_api.get_wq_report_json?p_location_id="+loc_id+"&p_parameter_type=Conc%3ACond%3ApH%3APower%3ATemp&p_last=5&p_last_unit=days&p_unit_system=EN&p_format=JSON",
    #gives pool data
    'damSummaryURL' : "CWMS_CRREL.cwms_data_api.get_dam_summary_json?p_location_id="+loc_id+"&p_unit_system=EN&p_format=JSON",
    #no use? inflow outflow maybe
    'locSummaryURL' : "CWMS_CRREL.cwms_data_api.get_loc_summary_json?p_location_id="+loc_id+"&p_source=CWMS&p_unit_system=EN&p_format=JSON",
    'annualVariabilityURL' : "CWMS_CRREL.cwms_data_api.get_annual_variability_json?p_id="+loc_id
    }
    print(URL+urlextension)
    y = requests.get(URL+urlextensions[urlextension])
    return y.json()

def printme():
    #For outflow levels:
    lakeJSON = get_lake_data('reportURL', Lake['loc_id'])
    Lake['outflow'] = lakeJSON[1]['Outflow'][-1]['value']

    #for temp
    tempJSON = get_lake_data('wqReportURL', Lake['loc_id'])
    Lake['temp'] = tempJSON[0]['Water Temperature'][-1]['value']

    #printstring = "Lake temp is: ",temp," degrees. \nOutflow is: ",outflow," cfm."
    #print(printstring)
    # data = {
    #     'temp':temp,
    #     'description':Lake['description'],
    #     'outflow':outflow,
    #     'message':'HERE_IS_DATA',
    #     'Response':200
    # }
    print(json.dumps(Lake))
    

printme()