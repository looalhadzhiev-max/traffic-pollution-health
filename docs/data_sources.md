\# Data Sources and Research Design



\## Project Concept



This project studies a multi-step relationship: 



Traffic intensity → Air pollution → Estimated health risk 



The goal is not to prove direct causality, but to estimate a plausible statistical pathway linking urban traffic to health outcomes through air pollution.



Source 1: Traffic, Weather, and Air Pollution Dataset

Description



This dataset integrates approximately 10 years of daily observations from Norway’s six largest cities.



It includes:



* traffic intensity
* PM2.5
* PM10
* NO₂
* temperature
* humidity
* wind-related variables
* Official publication



Scientific Data article: https://www.nature.com/articles/s41597-024-03583-8?utm\_source=chatgpt.com



Main role in the project



Used to model: Traffic -> Pollution



Advantages

* long time horizon
* multiple cities
* integrated environmental variables
* peer-reviewed publication





Limitations



* limited geographic scope
* no direct medical observations





Source 2: European Environment Agency (EEA) Health Risk Data

Description



The European Environment Agency provides air pollution health-risk assessment datasets for pollutants such as:



* PM2.5
* PM10
* NO₂
* O₃



The dataset includes health-risk calculations at country, city, and regional levels.



Official source



https://www.eea.europa.eu/data-and-maps/data/air-quality-health-risk-assessments



Main role in the project



Used to model: Pollution → Estimated Health Risk



Advantages

* official EU-level source
* epidemiologically validated
* widely used in environmental policy





Limitations



* not directly synchronized with traffic dataset
* used mainly for health-risk estimation methodology



Source 3: WHO AirQ+ Methodology

Description



The World Health Organization (WHO) AirQ+ methodology is used to estimate health burden from air pollution exposure.



It provides:



* exposure-response relationships
* relative risk estimation
* attributable fraction formulas



Official documentation



https://iris.who.int/bitstream/handle/10665/337683/WHO-EURO-2020-1559-41310-56212-eng.pdf



Additional WHO resource:



https://www.who.int/europe/tools-and-toolkits/airq---software-tool-for-health-risk-assessment-of-air-pollution



Main role in the project



Used as mathematical and epidemiological foundation for health-risk estimation.





Integration Strategy



The datasets are not directly merged.



Instead:



* Source 1 provides empirical environmental observations
* Sources 2 and 3 provide epidemiological interpretation and health-risk estimation



The project combines them through statistical modeling.



Planned Modeling Workflow



1. Model traffic intensity and pollution relationship
2. Control for weather variables
3. Introduce lag effects
4. Estimate health risk from pollution exposure
5. Analyze indirect pathway



Key Assumptions

* urban traffic contributes to local pollution
* weather conditions influence pollution concentration
* health risk can be estimated through epidemiological formulas
* relationships are statistical rather than strictly causal



Ethical and Legal Considerations

* only publicly available datasets are used
* no personal or sensitive data is processed
* all sources will be cited appropriately

