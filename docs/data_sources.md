\# Data Sources and Research Design



\## Project Concept



This project studies the relationship between air pollution, meteorological conditions, and estimated health risk.



The final design uses two independent data sources:



Measured air pollution data → Health risk interpretation



Source 1: UCI Air Quality Dataset



Official source: https://archive.ics.uci.edu/dataset/360/air+quality



This dataset contains hourly air quality measurements from an urban monitoring station in Italy.



Main variables include:



* CO
* NOx
* NO₂
* benzene
* temperature
* relative humidity
* absolute humidity



Role in project: Pollution and meteorological measurements



Source 2: World Bank Air Pollution Mortality Dataset



Official source: https://data.worldbank.org/indicator/SH.STA.AIRP.P5



Indicator: Mortality rate attributed to household and ambient air pollution, age-standardized, per 100,000 population



Role in project: Health outcome indicator related to air pollution



Methodological Reference



WHO AirQ+ methodology:



https://www.who.int/europe/tools-and-toolkits/airq---software-tool-for-health-risk-assessment-of-air-pollution



This reference supports the health-risk interpretation and the discussion of exposure-response relationships.



Integration Strategy



The datasets are independent and are not directly merged row-by-row.



Instead:



* UCI data is used for detailed pollution and meteorological analysis.
* World Bank data is used for public-health context and mortality risk comparison.
* WHO methodology is used to explain how air pollution exposure is linked to health outcomes.
* 

Key Assumptions



* NO₂, NOx, and CO can be interpreted as traffic-related pollution indicators.
* Meteorological conditions affect measured pollution concentration.
* Country-level mortality indicators provide broader health context.
* The project estimates statistical relationships and does not claim strict causality.



Ethical and Legal Considerations



* Only public datasets are used.
* No personal or sensitive data is processed.
* All external sources are documented and cited.

