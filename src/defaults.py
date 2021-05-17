from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]

plant_fuels = {
    "Biomass Power Plant": "biomass",
    "CSP with Storage": "solar",
    "CSP without Storage": "solar",
    "Coal Power Plant": "coal",
    "Gas Power Plant (CCGT)": "gas",
    "Gas Power Plant (SCGT)": "gas",
    "Geothermal Power Plant": "geothermal",
    "Large Hydropower Plant (Dam) (>100MW)": "hydro",
    "Light Fuel Oil Power Plant": "LFO",
    "Light Fuel Oil Standalone Generator (1kW)": "LFO",
    "Medium Hydropower Plant (10-100MW)": "hydro",
    "Nuclear Power Plant": "uranium",
    "Offshore Wind": "wind",
    "Oil Fired Gas Turbine (SCGT)": "HFO",
    "Onshore Wind": "wind",
    "Small Hydropower Plant (<10MW)": "hydro",
    "Solar PV (Distributed with Storage)": "solar",
    "Solar PV (Utility)": "solar",
}


units = {
    "ProcessName": ["Unit"],
    "RegionName": ["-"],
    "Time": ["Year"],
    "Level": ["-"],
    "CO2f": ["kt/PJ"],
    "biomass": ["PJ/PJ"],
    "coal": ["PJ/PJ"],
    "gas": ["PJ/PJ"],
    "geothermal": ["PJ/PJ"],
    "hydro": ["PJ/PJ"],
    "HFO": ["PJ/PJ"],
    "LFO": ["PJ/PJ"],
    "crude_oil": ["PJ/PJ"],
    "solar": ["PJ/PJ"],
    "uranium": ["PJ/PJ"],
    "wind": ["PJ/PJ"],
    "electricity": ["PJ/PJ"],
    "heat": ["PJ/PJ"],
}
