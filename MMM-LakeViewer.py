import json
import requests
import sys
import geocoder
import time
from pprint import pprint

g = geocoder.ip('me')
glat = g.lat
glon = g.lng
print(glat, glon)
MelvernLake = {
    "loc_id": '15302030',
    "description": "Melvern Dam & Reservoir",

}
"""{
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

PomonaLake = {
    "office_id": "NWK",
    "loc_id": "5663030",
    "description": "Pomona Dam & Reservoir",
    "source": "CWMS",
    "lat": "38.6512842",
    "lon": "-95.5582047"
}


CurrentLocation = {
    "bounding_box": g.latlng,
    'url': f"https://waterservices.usgs.gov/nwis/iv/?format=JSON&bBox={round(glon-.1,4)},{round(glat-.1,4)},{round(glon+.1,4)},{round(glat+.1,4)}&parameterCd=00060,00065&siteStatus=all",
#     "loc_id": ,
#     "description": 
}


RoaringRiver = {
    'url':"https://waterservices.usgs.gov/nwis/iv/?format=json&sites=07050152&parameterCd=00060,00065&siteStatus=all"
}
lakes = {
    'MelvernLake':MelvernLake,
    # 'CurrentLocation': CurrentLocation
}
rivers = {
    'RoaringRiver': RoaringRiver,
    'CurrentLocation' : CurrentLocation,
}
data = {
    'message':'HERE_IS_DATA',
    'Response':200,
    'lakes':lakes,
    'rivers':rivers
}
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
    y = requests.get(URL+urlextensions[urlextension])
    return y.json()

def printme():

    for val in lakes.values():
        #For outflow levels:
        lakeJSON = get_lake_data('reportURL', val['loc_id'])
        val['outflow'] = lakeJSON[1]['Outflow'][-1]['value']
        # #for temp
        tempJSON = get_lake_data('wqReportURL', val['loc_id'])
        val['temp'] = tempJSON[0]['Water Temperature'][-1]['value']

    for r in rivers.values():
        flow = requests.get(r['url'])
        flow=flow.json()
        print(len(flow['value']['timeSeries']))
        # for i in flow['value']['timeSeries']:
        #     sitecode = flow['value']['timeSeries'][i]['sourceInfo']['siteCode'][0]['value']
        #     tempdict = {}
        #     tempdict['description'] = flow['value']['timeSeries'][0]['sourceInfo']['siteName']
        #     tempdict['flow'] = flow['value']['timeSeries'][0]['variable']['variableCode'][0]['value'].lstrip('0')
        #     tempdict['height'] = flow['value']['timeSeries'][1]['values'][0]['value'][0]['value']
        #     r[sitecode] = tempdict
        for i in flow['value']['timeSeries']:
            sitecode = i['sourceInfo']['siteCode'][0]['value']
            tempdict = {}
            tempdict['description'] = i['sourceInfo']['siteName']
            tempdict['flow'] = i['variable']['variableCode'][0]['value'].lstrip('0')
            tempdict['height'] = i['values'][0]['value'][0]['value']
            r[sitecode] = tempdict

data['rivers'] = {'rivers':rivers}

    #https://maps.waterdata.usgs.gov/mapper/index.html?MapCenterX=-96.0&MapCenterY=36.0&MapZoom=4.

printme()
print(json.dumps(data))
