=== PS 26080 ===
TITLE: Regime-Aware AI Post-Processing of Monsoon Rainfall Forecasts
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Medium Range Weather Forecasting (NCMRWF)
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Problem Statement Rainfall forecast errors over India vary with weather regimes such as active monsoon, break monsoon, monsoon lows/depressions, orographic rainfall, coastal rainfall and western disturbances. A single bias-correction method may not work equally well in all situations.The challenge is to build an AI/ML-based rainfall post-processing system that first identifies the prevailing weather regime and then applies suitable correction to the raw NWP rainfall forecast.The aim is to improve district/grid-level rainfall forecasts, especially for heavy and very heavy rainfall events.
• Expected Outcome Expected Outcome - Description:
Weather regime classifier - Classification of active, break, depression,coastal/orographic rainfall regimes Bias-corrected rainfall forecast - Improved rainfall forecast compared to raw NWP output Heavy rainfall probability - Probability of rainfall exceeding operational thresholds District-level rainfall product - User-friendly rainfall forecast table/map Verification report - Skill comparison using RMSE, ETS, CSI, POD, FAR and FSS


=== PS 26081 ===
TITLE: Hybrid AI–NWP Multi-Model Forecast Blending System
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Medium Range Weather Forecasting (NCMRWF)
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Problem Statement Different forecasting systems perform differently depending on region, season, lead time and weather situation. Physical NWP models, ensemble forecasts and AI/ML weather models may each have strengths under different conditions. Therefore, there is a need for an intelligent blending system that can dynamically combine multiple forecasts.
The challenge is to develop a hybrid AIâ€“NWP blending framework that assigns adaptive weights to different forecast sources based on historical skill, forecast lead time, region, season and weather regime. The final product should provide an optimized forecast for rainfall, temperature, wind and extreme weather indicators.
Expected Outcome - Description
• Dynamically blended forecast - Best-combined forecast from multiple model sources
• Model weight maps - Indication of which model is more reliable for each region/lead time
• Improved forecast skill - Better performance than individual models
• Extreme weather guidance - Improved signals for heavy rainfall, heat wave and high-wind events
• Operational workflow - Automated script/dashboard for routine forecast blending


=== PS 26082 ===
TITLE: Air Pollution–Weather Coupled Forecasting System (Delhi NCR Focus)
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Medium Range Weather Forecasting (NCMRWF)
THEME: Clean & Green Technology
DATASET LINK FIELD: (empty)
DESCRIPTION:
Traditional Air Quality Index (AQI) forecasting models typically treat meteorology and pollution dispersion as separate entities. However, in highly polluted urban landscapes like Delhi NCR, there is a critical, dynamic feedback loop between the weather and pollutants. During peak pollution seasons (such as the winter stubble-burning period), atmospheric inversion layers trap particulate matter close to the ground. Conversely, dense concentrations of aerosols (PM2.5) block sunlight,altering local temperatures, wind patterns, and planetary boundary layer (PBL) heights. Ignoring these coupled meteorological-chemical feedback loops leads to significant inaccuracies in standard AQI predictions. To achieve high-accuracy, actionable insights, there is an urgent need for an integrated system that simulates real-time interactions between atmospheric physics and chemical transport.
The challenge is to build a high-resolution, coupled forecasting system specifically tailored for Delhi NCR that predicts AQI for the next 72 hours.
The solution must leverage advanced weather-chemistry models (such as WRF-Chem or similar open-source coupled frameworks) to dynamically interlink meteorology with pollution dispersion(specifically PM2.5 and Ground-level Ozone). A core focus should be accurately modeling the impact of atmospheric inversion on external pollution spikes, such as regional stubble burning,and how those trapped pollutants subsequently alter local weather conditions.Implement a workflow that handles two-way feedback between meteorology (temperature, wind,PBL height) and chemistry (PM2.5, PM10, O3,NOx). A user-friendly, real-time dashboard displaying high-resolution AQI forecasts for Delhi NCR with a 72-hour outlook. Features that explicitly track atmospheric inversion strength and predict how stubble-burning plumes will disperse under prevailing weather conditions.


=== PS 26084 ===
TITLE: Convective scale nowcasting for Thunderstorms, Hail & Cloudbursts (06 hr)
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Medium Range Weather Forecasting (NCMRWF)
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
Convective storms, such as severe thunderstorms, hail, downburst winds, and cloudbursts are among Indiaâ€™s deadliest natural hazards, especially during the pre-monsoon and monsoon seasons.Despite advancements in Numerical Weather Prediction (NWP) models, traditional systems often fail to accurately capture these mesoscale extreme weather events.The primary limitation stems from spatial and temporal constraints: these violent storms develop rapidly within a window of minutes and occur at localized scales that slip through coarse grid resolutions. Current early warning infrastructures struggle to provide high-resolution, short-term forecasts (0â€“6 hours), leaving local administrations, aviation sectors, and rural farming communities vulnerable to sudden, devastating impacts.
The challenge is to build a real-time, convective-scale Nowcasting System (0â€“6 hour lead time) operating at a hyper-local 1â€“3 km spatial resolution.
Because traditional physics-based models are too computationally slow to simulate these rapid developments in real-time, participants must design a system rooted in Multi-Source Data Fusion architectures. The core objective is to ingest high-frequency, heterogeneous meteorological streams, automatically detect early convective initiation, and dynamically forecast severe storm parameters (including lightning strike density, hail probability, downburst velocity, and cloudburst thresholds).Design a robust, real-time ingestion engine that fuses data streams from multiple sources: Doppler Weather Radars (DWR - reflectivity and velocity fields), geostationary satellite imagery (INSAT-3D/3DR thermal/infrared bands), and ground-based lightning detection networks. A real-time,interactive GIS-mapped dashboard showcasing high-resolution (1â€“3 km) hazard zones with live countdown clocks for storm arrivals.


=== PS 26085 ===
TITLE: Urban Flood Nowcasting System (Drainage and Rainfall Coupling)
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Medium Range Weather Forecasting (NCMRWF)
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
Urban flooding in major Indian metros like Mumbai, Delhi, and Chennai has become an annual crisis. Traditional Numerical Weather Prediction (NWP) models fall short because knowing how much rain will fall does not automatically translate into knowing where the streets will flood.Urban flooding is a hyper-local phenomenon dictated by micro-topography, concrete imperviousness, and heavily strained, invisible drainage networks. Currently, municipal bodies lack real-time, street-level predictive systems. Consequently, cities are caught off guard by rapid water accumulation, leading to severe traffic gridlocks, economic disruption, and loss of life.
The challenge is to design a high-resolution, real-time Urban Flood Nowcasting System (0â€“3 hour lead time) capable of predicting street-level inundation before it happens.
Participants must move away from isolated weather models and instead build a coupled framework. This system must fuse real-time rainfall nowcasts with high-resolution Digital Elevation Models (DEM) and a graph-based mathematical model of the cityâ€™s underground drainage network. By mapping how water flows, accumulates, and surcharges across concrete surfaces and drainage nodes, the solution should pinpoint exactly which streets or intersections will flood.Develop a pipeline that takes high-resolution rainfall nowcasts (from Doppler Weather Radars) and instantly routes that volume across a 2D surface terrain model. Represent the city's stormwater drain network as a directed graph (nodes as manholes/inlets, edges as pipes/canals). The model must calculate hydraulic capacity and predict where blockages or overcapacity will cause backflow onto the streets. A dynamic, web-based GIS dashboard showing real-time, street-by-street flooding projections (e.g., water depth estimations in centimeters) with a 0â€“3 hour forward-looking window.An API utility that can interface with navigation maps to suggest flood-safe alternative routes for emergency services, public transit, and commuters during heavy downpours.


=== PS 26086 ===
TITLE: Hyperlocal Monsoon Onset & Break Prediction System (Block/Village Scale)
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Medium Range Weather Forecasting (NCMRWF)
THEME: Agriculture, FoodTech & Rural Development
DATASET LINK FIELD: (empty)
DESCRIPTION:
The Indian Summer Monsoon dictates the economic livelihood of millions of farmers, particularly during the Kharif sowing season. While macro-scale monsoon forecasts across large meteorological subdivisions have improved, Indian agriculture remains highly vulnerable to the unpredictable nature of intra-seasonal variations. Specifically, the exact dates of monsoon onset,prolonged dry spells (break-monsoon phases), and subsequent revival cycles vary drastically from one district to another.
Standard regional forecasts lack the spatial granularity required for localized agricultural planning.If a farmer sows seeds during a false onset just before a major breakthrough pause, entire crops fail due to moisture stress, leading to crushing financial losses.
The challenge is to build a hybrid predictive framework capable of delivering a 7-to-30-day probabilistic outlook of monsoon behavior at the Block and Panchayat (Village cluster) scale.
The system must bridge the gap between global climate teleconnections and hyper-local weather outcomes. Participants should design a solution that ingests large-scale climate indicesâ€”such as the El NiÃ±o-Southern Oscillation (ENSO), Indian Ocean Dipole (IOD), and Madden-Julian Oscillation (MJO)â€”and downscales their signatures using advanced machine learning models to predict localized precipitation behavior, onset thresholds, and active/break durations.Develop a hybrid mathematical or machine learning model that pairs global planetary boundary conditions (ENSO, IOD, MJO phases) with regional atmospheric data to predict local rainfall anomalies. Generate dynamic, color-coded risk maps at the block/panchayat level illustrating the statistical probability percentage of monsoon onset, continuous dry spells (breaks), or heavy downpours 1 to 4 weeks in advance. Build an expert-system engine that translates rainfall probabilities into localized crop-specific agronomic advisories (e.g., advising farmers to delay sowing, prepare irrigation alternatives, or alter crop choices based on upcoming break phases). A mobile-optimized web application or automated SMS/WhatsApp API gateway that pushes clear,actionable text-based advisories in regional Indian languages directly to farmers and local agricultural extension officers.


=== PS 26089 ===
TITLE: Cooperative Gig Services Platform for Household & Community Services
ORG: Ministry of Cooperation | DEPT: National Council for Cooperative Training (NCCT)
THEME: Agriculture, FoodTech & Rural Development
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Labour Cooperative Federations and Labour Cooperative Societies possess a large pool of skilled workers such as electricians, plumbers, carpenters, painters, domestic helpers, caregivers, drivers, gardeners,cleaners, and technicians. However, they lack a structured digital platform to connect these workers with households and institutions requiring such services.Private platforms currently dominate this market, while cooperative workers often remain underutilized despite having skills and local presence.
• Problem Statement To develop a cooperative-owned digital service marketplace platform that enables Labour Cooperative Federations and Labour Cooperative Societies to provide verified household and community services while ensuring fair wages, worker welfare, and consumer trust.
• Expected Solution Features
• Service provider registration and verification
• Worker skill profiling and certification
• Customer booking and scheduling system
• Geo-location based service matching
• Digital payments and invoicing
• Rating and feedback mechanism
• Worker welfare and insurance integration
• Emergency and on-demand service booking
• Cooperative federation administration dashboard
• Multilingual mobile application
• AI-based demand forecasting and workforce allocation
• Technology Components
• Mobile Applications
• Artificial Intelligence (AI)
• Geo-Spatial Technology
• Digital Payment Systems
• Cloud Computing
• Proposed Mode Software


=== PS 26090 ===
TITLE: AI-Driven Market Linkage and Smart Cataloging Mobile Application for Marginalized Artisans
ORG: Ministry of Social Justice and Empowerment (MoSJE) | DEPT: Department of Social Justice and Empowerment
THEME: Heritage & Culture
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background The government actively supports the socio-economic upliftment of marginalized communities,particularly micro-entrepreneurs, artisans, and weavers. Financial assistance is provided to establish small-scale manufacturing and handicraft units. To help these beneficiaries sell their goods, market exposure is facilitated through periodic physical exhibitions, cluster development programs, and trade fairs (such as Shilp Samagam, Surajkund Mela, and Dilli Haat).While physical exhibitions provide a temporary boost in sales, these micro-entrepreneurs lack continuous, year-round access to broader digital markets. Transitioning to the digital economy is hindered by low digital literacy, language barriers, and a lack of technical skills required to professionally photograph, price, and catalog products for modern e-commerce.
• Challenge There is a critical need to bridge the gap between traditional craftsmanship and modern digital commerce. Beneficiaries struggle to present their products competitively online. They often fail to capture high-quality images, write compelling product descriptions, or understand dynamic market pricing.The challenge is to build an intuitive, AI-driven mobile application that acts as a 'virtual business manager' for these artisans. The app must empower them to seamlessly digitize their inventory, optimize their listings using AI, and connect directly with larger B2B buyers or government e-marketplaces without requiring advanced technical knowledge.
• Expected Solution Participants are expected to develop an AI-powered, cross-platform mobile application supported by a robust, scalable backend architecture. To ensure high adoption among low-literacy users, the application must feature a highly responsive, minimalist UI/UX design (incorporating modern, clean visual hierarchies and accessible layouts).
Key features should include:
1. AI Image Enhancer & Studio: A built-in camera module that utilizes AI to automatically remove cluttered backgrounds, correct lighting, and format product photos (e.g., textiles,handicrafts) to professional e-commerce standards.
2. Multilingual Auto-Cataloger: An NLP-based engine that allows artisans to describe their product via voice notes in regional languages. The AI should translate and generate SEO-friendly, professional product descriptions in English and Hindi.
3. Dynamic Pricing Assistant: A machine learning algorithm that analyzes the uploaded product image and description to suggest an optimal, competitive selling price based on current market trends and raw material costs.
• Impact Goals
• Provide marginalized micro-entrepreneurs with a continuous, year-round digital sales channel,reducing their dependency on periodic physical fairs.
• Drastically lower the barrier to entry for digital commerce through intuitive AI automation.
• Improve digital literacy and financial independence, ultimately increasing the average annual income of the target demographic.


=== PS 26091 ===
TITLE: AI-Driven Hyper-Local Business Advisory and Financial Structuring Assistant for Rural Micro-Entrepreneurs
ORG: Ministry of Social Justice and Empowerment (MoSJE) | DEPT: Department of Social Justice and Empowerment
THEME: Agriculture, FoodTech & Rural Development
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background The government actively promotes the economic empowerment of marginalized communities by providing concessional credit for income-generating activities. Under various schemes,beneficiaries are required to contribute a small margin money fractionâ€”typically 10% of the total project costâ€”while the State Channelizing agencies (SCAs) Channelizing agencies(CAs) provide the remaining 90% as a concessional loan. For example, if an entrepreneur wishes to establish a ?10,00,00 enterprise, they must possess ?1,00,00 as their 10% contribution, making them eligible for a ?9,00,00 loan.
These loans are categorized into specific tiers:
? Micro Finance Scheme: For small units with a project cost up to ?1.40 lakh. The funding agency provides up to 90% (maximum ?1.25 lakh) at a concessional interest rate of 6.5% per annum for the beneficiary, to be repaid over 3 years (including a 3-month moratorium).
? Term Loan Scheme: For larger projects costing between ?1.40 lakh and ?50.00 lakh. The agency provides up to 90% (maximum ?45 lakh) at an interest rate of 8% per annum, to be repaid over 7 years (including a 6-month moratorium).
However, despite the availability of capital, many first-time rural entrepreneurs face a high rate of business stagnation. This is due to a profound lack of formal market research tailored to their specific geographical reality, compounded by poor financial literacy regarding loan structuring,margin requirements, and repayment schedules.
• Challenge Beneficiaries often select business activities based on anecdotal success rather than data-driven market demand, and they struggle to calculate exactly how much capital they need or which scheme they qualify for. A prospective entrepreneur in a specific Gram Panchayat (village) lacks the analytical tools to determine local market saturation, optimal pricing, localized threats, and their precise financial eligibility.
There is a critical need for an intelligent tool that democratizes institutional-grade business consulting. The challenge is to build a hyper-local AI Assistant accompanied by a Smart Scheme Calculator that guides the user through a comprehensive business feasibility study and financial structuring plan before they apply for funding.
• Expected Solution Participants are required to develop an NLP-powered, multilingual AI Business Advisory Assistant tailored for rural and semi-urban geographies. The system should take basic inputs from the user:
Geographic Location (Village/Block/District), Available Margin Capital (e.g., ?1,00,000), and the Proposed Business Category (e.g., Dairy, Retail, Textiles etc).
The application must feature two core modules:
Module 1: Hyper-Local Business Feasibility Report The AI must dynamically generate a localized strategy encompassing:
1. Market Reach: Estimating the immediate consumer base within a 5â€“10 km radius of the village/block and identifying primary distribution channels.
2. Opportunity Analysis: Highlighting unserved or underserved niches within the chosen business sector in that specific local economy.
3. General Business Analysis (SWOT): A foundational breakdown of Strengths, Weaknesses,Opportunities, and Threats tailored to the specific micro-enterprise budget.
4. Threats Identification: Pinpointing local risks such as supply chain bottlenecks, seasonal demand fluctuations, or dependency on single buyers.
5. Competitor Mapping: Using localized demographic and economic data to estimate the density of existing similar businesses in the block.
6. Product Market Value: Suggesting optimal pricing strategies and predicting the local market value of the goods/services based on regional purchasing power.
Module 2: Smart Financial Calculator & Scheme Router An integrated financial engine that automatically processes the user's 'Available Margin Capital' to output a clear financial roadmap: 7.
Financial Structuring:
Automatically calculates the total feasible Project Cost (Available Margin / 10%) and the Maximum Loan Amount (90% of Project Cost).
Example: If the user inputs ?1,00,00 as available capital, the tool establishes a ?10,00,00 Project Cost and a ?9,00,00 loan eligibility.
Scheme Auto-Selection:
Routes the user to the correct scheme based on the calculated Project Cost.
Logic A: If Project Cost ? ?1.40 Lakh -> Selects Micro Finance Scheme (6.5% interest, 3-year tenure, 3-month moratorium).
Logic B: If Project Cost > ?1.40 Lakh and ? ?50.00 Lakh -> Selects Term Loan Scheme (8% interest, 7-year tenure, 6-month moratorium).
EMI & Moratorium Generator: Outlines the expected quarterly repayment schedule, operational costs, and working capital requirements, factoring in the specific moratorium periods.
• Impact Goals ? Reduce the failure rate of newly funded micro-enterprises by ensuring beneficiaries choose viable, locally relevant business models based on data.
? Eliminate financial confusion by clearly mapping a beneficiary's available cash (10%) to their maximum borrowing capacity (90%) and exact repayment obligations.
? Empower marginalized youth with enterprise intelligence, fostering a culture of data-backed, financially sound entrepreneurship at the grassroots level.


=== PS 26092 ===
TITLE: AI-Driven Scheme Matching for Marginalized Entrepreneurs
ORG: Ministry of Social Justice and Empowerment (MoSJE) | DEPT: Department of Social Justice and Empowerment
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background To promote the socio-economic empowerment of the Scheduled Caste (SC) population, the government provides concessional financial assistance and educational loans. Beneficiaries with an annual family income of up to ?5.00 Lakhs are eligible for various tailored financial products covering up to 90% of their project or education costs at highly concessional interest rates (typically 6.5% to 8% per annum).
However, direct loan applications are not entertained. Instead, funds are routed through a 'Channel Finance System' comprising over 100 Channel Partners, including State Channelizing Agencies (SCAs), Public Sector Banks (PSBs), Regional Rural Banks (RRBs), and NBFC-MFIs.
• Challenge Citizens often lack awareness regarding which specific credit scheme fits their needsâ€”such as distinguishing between a Micro Finance Scheme for small projects (up to ?1.40 lakh), a Term Loan for larger projects (up to ?50.00 lakh), or an Educational Loan Scheme. Furthermore,applicants face difficulties identifying and locating the nearest authorized Channel Partner equipped to process their specific loan category. This fragmentation leads to offline confusion,misrouted applications, and delays in disbursement.The challenge is to develop an intelligent, multi-lingual digital platform or mobile application that bridges the gap between the beneficiaries and the channelizing agencies.
• Expected Solution Participants are expected to develop a comprehensive platform that includes:
1. Smart Scheme Recommender: An AI/rule-based engine that takes basic user inputs (project type, estimated cost, income level, education status) and automatically recommends the most suitable credit or educational loan scheme.
2. Financial Calculator: A dynamic tool to calculate projected EMIs, accounting for specific scheme guidelines like maximum loan limits, interest rates (e.g., 6.5% to 15% depending on the scheme), and moratorium periods (3 to 12 months).
3. Geo-Spatial Partner Locator & Router: Integration of a mapping service to identify the nearest eligible Channel Partner (SCA/Bank/NBFC-MFI) based on the user's location and the partner's current fund utilization eligibility (ensuring applications aren't sent to partners with high NPAs or overdues).
• Impact Goals
• Enhance financial literacy among the target demographic regarding concessional lending.
• Improve transparency and efficiency in the channel finance ecosystem, ensuring faster disbursements and better fund utilization.


=== PS 26093 ===
TITLE: AI-Based Real-Time Stress and Trauma Assessment Module for Victims/Complainants Accessing NHAA (14566) and Integrated Portal
ORG: Ministry of Social Justice and Empowerment (MoSJE) | DEPT: Department of Social Justice and Empowerment
THEME: MedTech / BioTech / HealthTech
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Victims and complainants belonging to Scheduled Castes and Scheduled Tribes who approach the National Helpline Against Atrocities (14566), Integrated Portal, chatbot, mobile application, IVRS, or other digital platforms often experience severe emotional distress arising from caste-based discrimination, violence, rape, gang rape, murder of family members, social boycott, displacement, threats, and prolonged legal proceedings. Presently, there is no standardized mechanism for assessing the psychological condition and vulnerability of victims at the time of first contact with authorities.
• Problem Statement Design and develop an AI-enabled Real-Time Stress and Trauma Assessment Module that can assess the psychological stress, trauma, fear, anxiety, and vulnerability levels of victims/complainants interacting through NHAA (14566), the Integrated Portal, chatbot,IVRS, mobile application, or any other approved digital interface.
• Expected Solution The solution should:
• Analyse voice interactions, speech patterns, pauses, pitch variation, emotional indicators, and textual narratives.
• Use Natural Language Processing (NLP), Speech Analytics, and Emotion AI to identify signs of trauma and distress.
• Generate a Stress Vulnerability Index (SVI) on a predefined scale.
• Categorize victims into Low, Moderate, High, and Critical Risk categories.
• Detect indicators of severe trauma, fear, depression, suicidal ideation,intimidation, social isolation, and extreme vulnerability.
• Automatically recommend counselling, legal aid, medical assistance, police intervention, witness protection, or emergency support based on risk level.
• Support multilingual interactions, including major Indian languages and dialects.
• Maintain privacy, informed consent, confidentiality, and ethical AI standards.
• Expected Outcomes
• Early identification of highly distressed victims.
• Prioritization of counselling and rehabilitation services.
• Improved victim-centric grievance redressal.
• Better allocation of support resources.
• Enhanced responsiveness of the helpline and integrated portal ecosystem.
• Stakeholders:
• Department of Social Justice and Empowerment
• National Helpline Against Atrocities (14566)
• State Governments and Union Territories
• District Administrations
• Counsellors and Mental Health Professionals
• Law Enforcement Agencies
• Rehabilitation and Welfare Authorities


=== PS 26094 ===
TITLE: AI-Powered Dynamic Mental Health Monitoring and Distress Prediction System for Victims of Atrocities
ORG: Ministry of Social Justice and Empowerment (MoSJE) | DEPT: Department of Social Justice and Empowerment
THEME: MedTech / BioTech / HealthTech
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Victims of atrocities frequently experience prolonged psychological distress after complaint registration due to threats, intimidation, repeated court appearances, delays in investigation and trial, social ostracism, economic hardship, and rehabilitation challenges.Existing mechanisms focus primarily on legal and financial support and do not provide continuous monitoring of victim well-being.
• Problem Statement Develop an AI-based Dynamic Mental Health Monitoring and Distress Prediction System that continuously monitors and predicts psychological distress among victims and complainants registered through NHAA (14566), the Integrated Portal, chatbot, mobile application, IVRS, or other approved communication channels throughout the investigation,trial, rehabilitation, and compensation process.
• Expected Solution The system should:
• Conduct periodic interactions with victims through chatbot, IVRS calls, SMS, mobile applications, web portal, or helpline follow-up mechanisms.
• Analyse voice, text, behavioural responses, and engagement patterns using NLP, Sentiment Analysis, and Emotion AI.
• Generate a Dynamic Distress Score and longitudinal trend analysis.
• Predict escalation of psychological distress before a crisis situation emerges.
• Trigger alerts to counsellors, district authorities, and designated officials when predefined risk thresholds are crossed.
• Recommend appropriate interventions such as counselling, medical treatment, witness protection, relocation support, financial assistance, legal aid, or rehabilitation measures.
• Provide dashboards at district, State, and national levels for monitoring vulnerable victims and high-risk cases.
• Ensure explainable AI, privacy protection, data security, and compliance with applicable legal and ethical standards.
• Expected Outcomes
• Continuous monitoring of victim well-being.
• Early detection and prevention of mental health crises.
• Timely deployment of counselling and rehabilitation services.
• Strengthened victim confidence in the justice delivery system.
• Evidence-based decision-making for policymakers and administrators.
• Improved coordination among welfare, counselling, and law-enforcement agencies.
• Innovation Components
• Emotion AI
• Voice Stress Analytics
• Sentiment Analysis
• Predictive Risk Modelling
• Multilingual Conversational AI
• Explainable AI
• Automated Case Prioritisation
• Real-Time Risk Alerts
• Priority Use Cases
• Victims of rape and gang rape.
• Victims of murder, grievous hurt, and arson.
• Witnesses facing intimidation or threats.
• Families affected by caste-based violence.
Beneficiaries receiving relief, compensation, rehabilitation, and protection under the provisions of the Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989.


=== PS 26095 ===
TITLE: Smart Real-Time Monitoring & Inspection Mobile App
ORG: Ministry of Social Justice and Empowerment (MoSJE) | DEPT: Department of Social Justice and Empowerment
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Problem Statement Develop a centralized mobile application for real-time monitoring, surprise inspections, CCTV surveillance integration, and random inspection assignment for projects/institutes/NGOs running under DoSJE schemes.
• Key Features
• Live CCTV feed integration from projects/institutes
• Random Video Conferencing (VC) connectivity with Project Incharge/Staff/Beneficiaries
• Real-time monitoring dashboard for Department officials
• Mobile-based inspection module for PMU/Inspection Teams
• Random assignment of inspection duties through AI/automation
• Geo-tagged inspection reports and live evidence capture
• AI-based anomaly and attendance analytics
• Stakeholders
• DoSJE Divisions
• PMU Teams
• NGOs/Institutes
• Beneficiaries
• State/District Authorities
• Expected Outcomes:
• Improved transparency and accountability
• Reduction in fake reporting and proxy functioning
• Real-time monitoring of projects
• Better inspection governance and compliance
• Enhanced citizen-centric service delivery


=== PS 26097 ===
TITLE: AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY
ORG: Ministry of Social Justice and Empowerment (MoSJE) | DEPT: Department of Social Justice and Empowerment
THEME: Agriculture, FoodTech & Rural Development
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background
• The Pradhan Mantri Anusuchit Jaati Abhyuday Yojana (PM-AJAY) aims to reduce poverty among Scheduled Caste (SC) communities through livelihood promotion, skill development, and enterprise support under its Grant-in-Aid (GIA) component. A major challenge in implementation is the identification of appropriate skill training pathways that align with both the aspirations of beneficiaries and the actual livelihood opportunities available in their local regions.
• Many target beneficiaries face barriers such as low digital literacy, limited awareness of modern trades, language constraints, and difficulty navigating text-heavy digital systems. As a result, there is often a mismatch between enrolled training programs and the beneficiaryâ€™s interests, capabilities, or local market demand, leading to high dropout rates and poor post-training employment outcomes.
• To improve inclusion and effectiveness, there is a need for an AI-enabled conversational system that can interact naturally in regional languages and dialects, understand beneficiary aspirations, assess skill gaps, and recommend suitable NSQF aligned livelihood opportunities in and around the beneficiary.
• Basic Issues under GIA Component:
• Lack of proper road map and Planning of the Perspective plans from execution to implementation
• Identification of the participants Trained and skilled Financial consultants
• Job placement issue after the skilling programme
• Coordination Issues among the corporation, Ministry/Departments
• Inadequate Technical and support team at ground level
• Detailed Description The proposed solution should be an AI-driven, multilingual, voice-based virtual livelihood assistant capable of conducting conversational interviews with beneficiaries from aspirational SC communities. Instead of relying on traditional form-filling methods, the system should use voice interactions to collect information such as:
• Educational background
• Existing or traditional family occupations
• Current livelihood activities
• Skills and interests
• Mobility and physical constraints
• Preference for self-employment or wage employment
• Local economic realities and opportunities The assistant should support regional languages and dialects to ensure accessibility for users with low literacy or limited digital exposure. The interaction should feel empathetic and conversational rather than administrative.The collected information should be analyzed using AI/MLbased profiling and recommendation mechanisms to identify:
• Suitable NSQF-aligned training programs
• Relevant trades and livelihood pathways
• Skill gaps requiring intervention
• Region-specific employment or enterprise opportunities The system should also function effectively in lowconnectivity and low-tech environments through deployment channels such as:
• IVR-based phone calls for feature phone users
• WhatsApp voice-note interfaces Lightweight mobile or kiosk-based solutions
• Expected Solution:
An AI-powered multilingual voice assistant application designed to help SC beneficiaries under PM-AJAY identify suitable skill training and livelihood opportunities.The app will support regional languages and local dialects, allowing users to interact through simple voice conversations instead of text-based forms.


=== PS 26099 ===
TITLE: AI-Driven Standardization and Harmonization of Material Codes Across CPSEs
ORG: Ministry of Petroleum & Natural Gas | DEPT: Chennai Petroleum Corporation Limited(CPCL)
THEME: Smart Automation
DATASET LINK FIELD: CPSE Material Master Data / Sample Material Master Dataset –To be provided by participating CPSEs
DESCRIPTION:
• Background Central Public Sector Enterprises (CPSEs) operating in sectors such as Oil & Gas, Power, Steel, Mining and Heavy Engineering procure and maintain a large number of similar or functionally equivalent materials. However, the same material may be assigned different material codes, descriptions, specifications, units of measurement and classification across different CPSEs.
This results in duplication of material masters, inconsistent descriptions, difficulty in identifying equivalent materials, fragmented procurement data, higher inventory levels and limited opportunities for collaborative procurement.
A unified and intelligent approach is therefore required to standardize, harmonize and rationalize material master data across CPSEs.
• Description The proposed solution envisages development of an AI-powered National Unified Material Master Framework capable of analysing material codes, descriptions, specifications, technical parameters and historical procurement data from multiple CPSEs.
The system shall use Artificial Intelligence, Machine Learning and Natural Language Processing (NLP) techniques to identify identical, duplicate, near-duplicate and functionally equivalent materials across different ERP/SAP systems.
The platform should automatically recommend standardized material descriptions, specifications, classifications and a Common National Material Code, while retaining mapping with the respective CPSE's existing material codes.
The system should provide intelligent matching and recommendation capabilities, allowing users to review, validate and approve proposed mappings. It should also support migration/mapping of legacy material codes and seamless integration with existing SAP/ERP systems.
• Expected Solution An AI-driven Unified Material Master Platform shall be developed with the following capabilities:
• AI-based matching of material descriptions and specifications across CPSEs.
• Identification of duplicate, near-duplicate and equivalent materials.
• Automated standardization of material descriptions and technical attributes.
• Intelligent classification and categorization of materials.
• Generation/recommendation of a Common National Material Code.
• Mapping of existing CPSE material codes to the common national code.
• Legacy material code rationalization and migration support.
• User validation and approval workflow for AI recommendations.
• Dashboard for material master analytics and duplicate detection.
• Audit trail and governance mechanism for material master changes.
• Integration capability with SAP/ERP systems of participating CPSEs.
The proposed solution should enable 'One Nation â€“ One Material Code' for common materials, while maintaining traceability to individual CPSE material codes.
• Key Capabilities 1. AI Material Matching & Recommendation 2. Material Standardization & Classification 3. Duplicate / Near-Duplicate Detection 4. Common National Material Code Generation 5. CPSE Code Mapping & Migration Support 6. Material Master Dashboard & Analytics 7. Audit Trail & Governance 8. SAP / ERP Integration
• Expected Impact
• One Nation â€“ One Common Material Code
• Reduction in duplicate and redundant material codes
• Improved material master data quality
• Better inventory optimization and visibility
• Reduced procurement cost through demand aggregation
• Improved inter-CPSE material identification and collaboration
• Faster procurement and specification finalization
• Better data-driven procurement decisions
• Foundation for common procurement and strategic sourcing across CPSEs


=== PS 26101 ===
TITLE: Develop an AI enabled learning platform that identifies competency gaps, recommends personalized training through integration with the iGOT Karmayogi ecosystem, and capable of generating Quizzes and Multiple choice questions (MCQs) from uploaded learning materials to strengthen capacity building in India's Official Statistical System.
ORG: MoSPI | DEPT: Data Informatics & Innovation Division (DIID)
THEME: Smart Education
DATASET LINK FIELD: nssta.gov.in, mospi.gov.in
DESCRIPTION:
• Background India's statistical system is undergoing rapid technology advancement with increasing adoption of Artificial Intelligence (AI), Machine Learning (ML), Big Data Analytics, GIS, cloud computing, and modern statistical methodologies. Officials engaged in data collection, processing, analysis, dissemination, and policy support require continuous upskilling to meet evolving technological and domain-specific requirements.
While the iGOT Karmayogi platform offers a vast repository of learning resources, officials often face challenges in identifying the most relevant courses aligned with their job roles, current competencies, and future skill requirements. Presently, there is no intelligent mechanism that performs comprehensive skill-gap assessment and recommends personalized learning pathways specifically for professionals working in Official Statistics.
Artificial Intelligence (AI) and emerging digital technologies are rapidly transforming the way organizations operate, deliver services, and make decisions. However, many organizations face challenges such as limited AI awareness, skill gaps, inadequate technical expertise, and the absence of structured, scalable training mechanisms.
Traditional training approaches often lack personalization, continuous assessment, and real-time learner support, making it difficult to meet diverse learning needs.
An AI enabled Learning Management System can assess learners existing competencies through learnerâ€™s profile, identify skill gaps, and recommend personalized training through integration with the iGOT Karmayogi platform based on job roles, experience levels, and organizational requirements. Through adaptive learning modules, AI powered virtual assistants, automated assessments, and realtime feedback mechanisms, learners receive targeted training that improves engagement and learning outcomes. The LMS supports continuous capacity building by offering structured courses, hands-on exercises, virtual labs on emerging technologies such as Artificial Intelligence, Data Science, Cloud Computing, Cybersecurity, and Automation. AI driven analytics and dashboards enable organizations to monitor learner progress, evaluate training effectiveness, predict future skill requirements, and make informed decisions regarding workforce development. By integrating personalized learning, competency mapping, performance monitoring, and intelligent content delivery, the AI enabled LMS ensures effective adoption of emerging technologies and helps create a future-ready, digitally skilled workforce.
• Detailed Description The proposed solution aims to develop an AI-enabled Skill Intelligence and Learning Platform that strengthens capacity building for officials engaged in India's Official Statistical System by integrating with the iGOT Karmayogi ecosystem. The platform should leverage Artificial Intelligence to assess competencies, identify skill gaps, and recommend personalized learning pathways aligned with each official's job role, responsibilities, and career progression.
The system should automatically create a comprehensive competency profile for every official using information such as designation, department, job role, current assignment, educational qualifications, work experience, and previous trainings.
Based on this profile, the platform should evaluate the official's existing competencies against predefined competency frameworks for Official Statistics and identify knowledge and skill gaps.
The AI engine should map competencies across multiple domains, including:
• Statistical Competencies: Survey Design, Sampling, National Accounts, Price Statistics, Labour Statistics, Agricultural Statistics, Industrial Statistics, SDG Indicators, Metadata Standards, and Data Quality Frameworks.
• Technical Competencies: Python, R, SQL, Stata, SPSS, SAS, GIS, Data Visualization, AI/ML, Cloud Computing, APIs, and Open Data.
• Digital Governance: Cybersecurity, Data Privacy, Digital Signatures, Government Cloud, and Digital Public Infrastructure.
• Behavioural and Managerial Competencies: Leadership, Communication, Project Management, Ethics, Decision Making, and Change Management.
Using AI techniques such as Machine Learning, Natural Language Processing (NLP), Large Language Models (LLMs), semantic search, and competency mapping, the platform should recommend personalized learning pathways from the iGOT Karmayogi course repository. Recommendations should consider the official's current competency level, previous learning history, departmental priorities, future job requirements, emerging technologies, and career progression.
The platform should integrate seamlessly with iGOT Karmayogi APIs to retrieve course catalogues, recommend relevant courses, monitor enrolment and completion status, and update competency scores automatically.
To support continuous learning, the solution should provide AI-powered virtual assistants for learner support, adaptive assessments, interactive learning modules, virtual laboratories, quizzes, and multilingual learning resources. The system should continuously monitor learner progress and dynamically update recommendations based on performance and newly acquired competencies.
To strengthen capacity building, the platform should support AI powered Intelligent Assessment Engine capable of generating objective type questions (MCQs), and quizzes from uploaded learning materials such as documents, presentations, videos etc. It should provide instant evaluation, explanations for correct answers, and personalized feedback to reinforce learning outcomes. This feature should enable trainers to automatically create assessments and quizzes, and evaluate learner understanding, and provide instant feedback, thereby enhancing continuous learning and competency assessment. The engine should leverage Large Language Models (LLMs), Natural Language Processing (NLP), etc.
A comprehensive analytics dashboard should be provided for both employees and administrators. The employee dashboard should display current competency levels, identified skill gaps, recommended learning paths, learning hours, and overall progress. The administrator dashboard should provide organization-wide insights into workforce competencies, training effectiveness, competency distribution, emerging skill requirements, and predictive analytics for future capacity-building needs.
The solution should be designed as a secure, scalable, cloud-ready, and interoperable web platform capable of integrating with existing government digital ecosystems through standard APIs. The platform should support role-based access control, Single Sign-On (SSO), and secure data exchange while ensuring compliance with government cybersecurity and data privacy guidelines.
The proposed AI-enabled Skill Intelligence Platform will enable data-driven workforce development by delivering personalized, competency-based learning recommendations, improving utilization of iGOT Karmayogi resources, and creating a future-ready statistical workforce equipped with modern statistical, analytical, and digital skills required for the evolving needs of India's Official Statistical System.
• Expected Solution The AI enabled platform for training and capacity building by providing personalized learning recommendations, improving competency levels of officials, enhancing utilization of iGOT Karmayogi resources, and creating a future-ready workforce equipped with modern statistical and digital skills. Additionally, AI powered generation of objective type questions and quizzes from uploaded learning content for automated assessments and self evaluation.
The solution should provide:
• AI-based competency assessment
• Automated skill-gap analysis
• Seamless iGOT integration
• Personalized learning recommendations of iGOT Course Module as well as NSSTAâ€™s TPAC recommended Training Programme
• AI powered generation of MCQ and Quizzes from uploaded learning content.
• Interactive dashboards for Learner and Administrator
• Secure, and scalable web application


=== PS 26103 ===
TITLE: Use case on web-based integrated project-monitoring platform
ORG: MoSPI | DEPT: Data Informatics & Innovation Division (DIID)
THEME: Smart Automation
DATASET LINK FIELD: The Project Monitoring Report for the month of April, 2026 may be referred for developing an understanding on the key field/ parameters through https://paimana-proj.mospi.gov.in/ReportPage
DESCRIPTION:
• Background The Infrastructure & Project Monitoring Division (IPMD), Ministry of Statistics and Programme Implementation (MoSPI) monitors the Central Sector Infrastructure Projects costing ?150 crore and above, across all the infrastructural Ministries/ Departments. The project monitoring was undertaken through the Online Computerised Monitoring System (OCMS) since 2006, which served as the primary repository of project-level information relating to project cost, expenditure, timelines and implementation status. Over nearly two decades, OCMS generated a valuable historical database capturing project implementation trends, cost overruns and time overruns across sectors. Later, OCMS was modernized to Project Assessment, Infrastructure Monitoring and Analytics for Nation-building (PAIMANA) portal, to enable a comprehensive and integrated project-monitoring ecosystem.
• PAIMANA Portal and Data Ecosystem PAIMANA is a web-based integrated project-monitoring platform designed to function as a national repository of infrastructure projects. It captures project-level information relating to approved cost, revised cost, expenditure, implementation timelines, physical progress, milestones, implementing agencies and project status. The information on infrastructure projects is updated on a monthly basis, through role-based access and APIs.
As of April 2026 , the PAIMANA project-monitoring framework tracks 1,981 ongoing infrastructure projects across 17 Central Ministries/Departments covering 22 infrastructure sectors . These projects have an aggregate original cost of approximately ?37.13 lakh crore, revised cost of approximately ?42.78 lakh crore and cumulative expenditure of approximately ?20.36 lakh crore. The monitored portfolio covers major sectors including Transport & Logistics, Energy, Water & Sanitation, Communication, Social Infrastructure, Coal, Steel and Mining.
Despite the availability of comprehensive project-monitoring data, infrastructure projects frequently encounter challenges such as cost overruns, time overruns, delays in milestone achievement, contractual and implementation bottlenecks, resource constraints and execution risks. These challenges often result in significant escalation of project costs and delays in the creation of public infrastructure assets.
While the existing PAIMANA framework provides robust capabilities for monitoring and reporting project progress, there is a growing need to move beyond descriptive monitoring towards predictive and prescriptive monitoring. The scale, diversity and continuous availability of project data provide an opportunity to strengthen infrastructure project monitoring through data-driven analytical and decision-support systems.
• AI Opportunity from PAIMANA Database The historical project-monitoring database available through OCMS combined with the recent PAIMANA portal provides a unique and comprehensive repository of infrastructure project data spanning nearly two decades. The database encompasses projects of varying sizes, sectors, geographical locations, implementing agencies, expenditure patterns and implementation timelines.
The availability of large-scale historical repository of project data together with continuously updated project information received through integrated digital systems provides a strong foundation for the application of Artificial Intelligence (AI), Machine Learning (ML) and Large Language Models (LLMs). These technologies can be leveraged to develop predictive analytics and early warning decision support systems for identifying cost overruns, schedule delays and implementation risks, thereby enabling proactive interventions and evidence-based decision-making in infrastructure project monitoring.
• Problem Statement and Scope of Work for Hackathon Under the broader theme of 'AI for Infrastructure Monitoring', the proposed use-case seeks to develop an AI-powered Predictive Analytics and Early Warning System capable of analysing the large volume of project data available at PAIMANA portal, using Open-Source Tools and Softwares, to identify projects that are likely to experience cost escalation, schedule delays and implementation risks before such issues materialise.
The solution should assist policymakers, project administrators and monitoring agencies in prioritising interventions, improving project execution outcomes and enhancing the effectiveness of infrastructure project monitoring. The use-case aims to transform project monitoring from a descriptive reporting framework into a predictive and prescriptive decision-support system capable of generating actionable insights for evidence-based decision-making. In this regard, the proposed solution may address the following technical dimensions:
a)Development and evaluation of statistical analysis and predictive models using open-source tools and methodologies for analysing project performance and forecasting cost overruns, time overruns and implementation risks.
b)Assessment of whether Artificial Intelligence (AI) and Machine Learning (ML) techniques provide significant gains over conventional statistical methods in terms of prediction accuracy, early warning capabilities and decision-support for infrastructure project monitoring.
c)Development of prediction and analytical models based on the existing Common Upload Form (CUF) fields available in the project-monitoring framework, along with an assessment of the extent to which predictive performance is attributable to the current CUF fields vis-Ã -vis additional variables that are not presently captured in the CUF.
It is suggested/ desirable that the proposed solution may leverage any of the following (using Open-Source Tools/ Softwares); (a) Artificial Intelligence (AI), (b) Machine Learning (ML), (c) Big Data Analytics, (d) Forecast Modelling and (e) Large Language Models (LLMs); to predict cost and time overruns, generate project-level risk scores, identify emerging implementation challenges, and provide early warning signals and decision-support mechanisms for timely interventions. However, these suggested techniques are only indicative and non-exhaustive. The students may adopt alternative or additional methodologies, tools, frameworks, or analytical approaches, as deemed appropriate, to achieve the stated objectives.
• Possible Expected Outcomes and Evaluation An indicative solution proposed by the student should comprise of any of the outcomes given below:
a. Cost Overrun Prediction Model;
b. Time Overrun Prediction Model;
c. Project Risk Scoring Framework;
d. Early Warning Alert System;
e. Benchmarking and Comparative Analytics Module;
f. Cost Escalation Driver Analysis Module;
g. AI-powered Monitoring Dashboard;
h. LLM-enabled Project Intelligence Assistant;
i. Documentation and deployment framework.
The above outcomes are indicative and non-exhaustive. Students may propose alternative outputs, features or solution components that effectively address the problem statement. It is desirable that only open-source tools/ software be used to achieve the stated objectives. The selection and application of such methods shall remain at the discretion of the student, subject to demonstrating their suitability, effectiveness, and alignment with the project requirements.


=== PS 26105 ===
TITLE: AI-Powered Continuous Cyber Risk Quantification and Investment Optimization Platform
ORG: All India Council for Technical Education (AICTE) | DEPT: Cyber Security Cell
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Enterprises and institutions invest heavily in cybersecurity tools, compliance programs, and risk management initiatives, yet cyber risk is still predominantly communicated using qualitative ratings such as 'Low','Medium', or 'High'.
These coarse categories fail to express the potential financial impact of cyber threats,making it difficult for senior management, boards, and regulators to evaluate whether current cyber investments are adequate or optimally allocated.
Cyber risk is inherently dynamic: new vulnerabilities emerge, threat actors change tactics, business services are added or retired, and security controls mature over time. Most current risk assessment practices rely on periodic, manual exercises, resulting in stale risk registers and limited visibility into the organizationâ€™s real-time cyber exposure. This gap leads to suboptimal prioritization of remediation efforts, under- or over-spending on security controls, and weak alignment between technical risk metrics and business decision-making.
• Problem Statement Design and develop an AI-powered platform that continuously quantifies cyber risk in monetary terms by correlating technical security telemetry with business asset criticality and control effectiveness. The platform must estimate the likelihood and financial impact of cyber incidents, identify key risk drivers, and recommend cost-effective mitigation strategies under explicit budget constraints.The solution should bridge the gap between technical cybersecurity metrics and business language, enabling CISOs, risk officers, and executive leadership to make informed, data-driven decisions about cyber risk and security investment.
• Proposed Solution Develop a cloud-ready cyber risk analytics platform that ingests data from multiple enterprise security and IT sourcesâ€”such as vulnerability management, SIEM, IAM, EDR, CSPM, asset inventories, and threat intelligence feedsâ€”and uses AI/ML models to compute continuous risk scores and estimated financial exposure, such as Expected Annual Loss. The system should provide interactive dashboards and decision-support tools that allow stakeholders to simulate remediation scenarios, evaluate investment options, and understand the return on security investment.The platform must be capable of mapping risk metrics to established cybersecurity frameworks, including ISO/IEC 27001, NIST Cybersecurity Framework, CIS Controls, RBI Cyber Security Framework, and SEBI Cybersecurity and Cyber Resilience Framework, supporting both regulatory reporting and internal governance.
• Key Components
• Risk Quantification Engine o Continuous aggregation and normalization of data from vulnerability scanners, SIEM, IAM, EDR,CSPM, asset inventory, and other security tools.
o Statistical and ML-based estimation of incident likelihood and potential business impact, including downtime costs, data breach costs, regulatory penalties, and reputational effects.
o Calculation of enterprise cyber risk as financial exposure metrics (for example, Expected Annual Loss and Value at Risk) at organization, business unit, and asset levels.
o Asset criticality modeling to weigh technical findings based on business importance and service dependencies.
o Control effectiveness evaluation using telemetry about configuration strength,incident history, and compliance status.
• AI Decision Support Layer o Predictive analytics for emerging threats and evolving risk based on trends in vulnerabilities, threat intelligence, and control performance.
o AI-generated mitigation recommendations that propose prioritized actionsâ€”such as patch deployment, access control tightening, network segmentation, and additional monitoringâ€”with quantified risk reduction.
o Natural language query interface for non-technical stakeholders, enabling questions like 'What is our highest financial cyber risk today?' or 'Which vulnerabilities contribute most to our expected losses?'.
o Scenario simulation tools for exploring 'what-if' analyses, such as 'What happens if MFA is implemented across all privileged accounts?' or 'How will delaying remediation by 30 days affect our financial exposure?'.
• Investment Optimization Module o Optimization models that recommend sets of controls and remediation actions delivering maximum risk reduction for a specified budget (for example, ?1 crore).
o Computation of ROSI and cost-benefit metrics for different security initiatives to support strategic planning and board-level approvals.
o Visualization of 'Investment vs. Risk Reduction' curves to highlight diminishing returns and optimal spend zones.
• Executive and Technical Dashboards o Unified views for CISOs and executives, including Enterprise Risk Score, total Financial Exposure, Risk Trend Analysis, Top Risk Contributors, and Risk Reduction Opportunities.
o Drill-down capability for technical teams to see control-level and asset-level findings, remediation backlogs, and mapping to frameworks and policies.
• Compliance and Framework Mapping o Built-in mapping against frameworks such as ISO/IEC 27001, NIST Cybersecurity Framework, CIS Controls, RBI Cyber Security Framework, and SEBI Cybersecurity and Cyber Resilience Framework.
o Support for generating evidence-based reports and dashboards for audits, regulatory filings, and internal governance committees.
• Expected Outcomes
• Continuous, near real-time visibility into enterprise cyber risk, expressed in monetary terms understandable to business stakeholders.
• Improved prioritization of cybersecurity initiatives based on quantified impact rather than subjective risk ratings.
• Enhanced communication of cyber risk to executive management, boards, and regulators through intuitive, data-driven dashboards and narratives.
• More rational and optimized cybersecurity investment decisions, maximizing risk reduction per unit of spend.
• Reduction in both the likelihood and financial impact of cyber incidents through targeted remediation and investment strategies.


=== PS 26106 ===
TITLE: AI-Powered Email Threat Detection, GeoLocation and Forensic Intelligence Platform
ORG: All India Council for Technical Education (AICTE) | DEPT: Cyber Security Cell
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Email continues to be one of the most widely used communication channels in government, education, banking,and enterprise ecosystems. However, it also remains one of the most exploited attack vectors for phishing,impersonation, business email compromise, financial fraud, credential theft, and malware delivery. Threat actors increasingly use spoofed domains, deceptive sender identities, social engineering techniques, and compromised infrastructure to send highly convincing fraudulent emails that appear legitimate to end users.Traditional email security controls such as spam filters, static blacklists, and rule-based signature mechanisms are often insufficient to detect sophisticated fraudulent emails. Attackers now use AI-generated language,domain lookalikes, display-name spoofing, hidden redirection links, and relay chains to evade standard detection systems. In many cases, even when a suspicious email is identified, organizations lack the technical capability to effectively trace the source path, identify probable sender infrastructure, correlate geolocation clues, and support investigation into the origin of the email.This gap creates major challenges for cybersecurity teams, law enforcement support, fraud response units, and institutional administrators who need not only to detect malicious emails but also to investigate their source and reveal indicators that may help identify the actor or infrastructure behind the attack.
• Problem Statement Current email security ecosystems primarily focus on filtering or blocking suspicious content but provide limited intelligence for deep forensic tracing of fraudulent email origins. Existing tools often do not adequately correlate email headers, SMTP relay paths, SPF/DKIM/DMARC validation results, IP reputation, geolocation indicators, domain registration intelligence, and behavioral patterns to build a complete picture of the senderâ€™s identity or operating location.There is a need for an AI-powered platform capable of detecting phishing, spoofed, impersonated, and fraudulent emails in real time or near real time, analyzing the complete technical structure of an email, tracing its transmission path across mail servers, estimating its origin with location, and generating forensic intelligence and investigative insights that assist in identifying malicious infrastructure, compromised systems, or threat actors behind the attack.The solution should support forensic analysis, fraud prevention, institutional email security, and investigation workflows while maintaining legal, privacy, and evidentiary standards.
• Proposed Solution Develop an AI-Powered Email Threat Detection, GeoLocation and Forensic Intelligence Platform that combines Natural Language Processing (NLP), Machine Learning (ML), email header forensics, IP intelligence, domain analysis, and graph-based correlation to identify suspicious emails,detect advanced email threats, and investigate their probable origin.
The system should ingest raw email content, metadata, and headers; validate sender authentication mechanisms;
extract indicators of compromise; reconstruct relay paths; analyze originating IP addresses and associated geolocation data; and generate a confidence-based assessment of fraud risk and probable sender origin. The platform should provide actionable alerts, visual trace maps, and forensic reports for security analysts,administrators, and investigators.
• Key Components
• Fraudulent Email Detection Engine o NLP-based analysis of email subject lines, body text, urgency cues, impersonation language, and social engineering patterns.
o Detection of phishing indicators such as spoofed sender addresses, deceptive domains, suspicious attachments, malicious links, and obfuscated URLs.
o AI/ML models to classify emails as legitimate, suspicious, impersonated, phishing, or fraud-related.
o Identification of business email compromise patterns such as payment diversion, fake invoice requests, credential harvesting attempts, and executive impersonation.
• Email Header and Protocol Analysis Module o Deep analysis of email headers including Return-Path, Received headers, Message-ID, Reply-To,DKIM signatures, SPF alignment, and DMARC status.
o Detection of anomalies in mail routing, forged sender fields, relay manipulation, and spoofed transmission records.
o Validation of whether the email was sent through authorized infrastructure or suspicious relay paths.
• Origin Traceability and Location Analysis o Extraction of originating IP addresses from header chains and identification of the earliest reliable sending node.
o IP geolocation mapping to estimate the likely country, region, city, ISP, hosting provider, or proxy service associated with the email source.
o Correlation with VPN, TOR, open relay, botnet, or cloud-hosted infrastructure indicators where applicable.
o Domain intelligence analysis using WHOIS data, DNS records, MX records, hosting fingerprints,and registrar details to identify suspicious sender infrastructure.
• Identity Correlation and Attribution Support o Correlation of email indicators with known threat intelligence, blacklists, previous incidents,domain clusters, and repeated fraud campaigns.
o Graph-based relationship analysis between sender domains, IP addresses, aliases, reply chains, and linked infrastructure.
o Confidence-based investigative assessment to assist in revealing probable sender identity, associated infrastructure, or campaign-level attribution patterns.
o Support for flagging whether the email likely originated from a compromised account, spoofed domain, anonymized infrastructure, or direct malicious actor environment.
• Alerting, Dashboard, and Forensic Reporting o Real-time alerts for high-risk emails before user interaction or administrative approval.
o Analyst dashboard showing fraud score, spoofing indicators, sender trace path, geolocation map,and attribution confidence.
o Generation of structured forensic reports for institutional action, legal review, cyber incident response, and support to law enforcement agencies.
o Searchable case management view for grouping related fraudulent emails into campaigns.
• Privacy, Legal, and Compliance Safeguards o Controlled handling of personal data and metadata in accordance with organizational privacy policies.
o Logging, evidence preservation, and chain-of-custody support for investigation purposes.
oConfigurable retention and masking mechanisms for sensitive communication data.
• Expected Outcomes
• Early and accurate detection of fraudulent, spoofed, and phishing-based email attacks.
• Improved ability to trace suspicious email origin paths and identify probable source infrastructure.
• Enhanced fraud investigation capability through geolocation analysis, domain intelligence, and sender attribution support.
• Reduced financial loss, reputational damage, and unauthorized disclosure of confidential information caused by email-based fraud.
• Better institutional readiness for cyber incident response, forensic investigation, and enforcement coordination.


=== PS 26107 ===
TITLE: Al-powered Intelligent Assistant for Indian Standards and BIS Services for Industries and Consumers
ORG: Ministry of Consumer Affairs, Food & Public Distribution | DEPT: Department of Consumer Affairs (DoCA)
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background The Bureau of Indian Standards publishes thousands of Indian Standards and provides various services such as product certification, hallmarking, laboratory recognition, Standards Clubs, training, consumer affairs, and conformity assessment.
• At present, users often struggle to identify:
• Applicable Indian Standards for their products,
• Certification requirements,
• Relevant BIS schemes,
• Licensing procedures,
• Testing requirements,
• Related standards, and
• Answers to technical queries.
Searching through multiple documents, portals, and PDFs is time-consuming, particularly MSMEs, startups, students, and consumers.
• Description Develop an Al-powered conversational assistant that enables users to obtain accurate, context-aware, and source-backed information related to Indian Standards and BIS services through natural language interactions.
The assistant should understand user queries in plain language, retrieve relevant information from authorized BIS knowledge sources, and provide responses with references to the documents or clauses which ever are applicable.
• Expected Solution The software solution consists of a Intelligent Assistant or Agent which can
• Answer questions related to Indian Standards.
• Recommend applicable standards based on product descriptions.
• Provide guidance on BIS certification schemes.
• Explain certification processes.
• Answer consumer-related queries.
• Guide users regarding hallmarking.
• Suggest relevant testing laboratories.
• Support multilingual interaction.


=== PS 26108 ===
TITLE: AI-Powered Recommendation Engine for Identifying Applicable Indian Standards for Procurement Specifications
ORG: Ministry of Consumer Affairs, Food & Public Distribution | DEPT: Department of Consumer Affairs (DoCA)
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Government departments, Public Sector Enterprises (PSES),procurement agencies, and private organizations procure a wide range of products and services through e-procurement portals. Procurement officials are often required to prepare technical specifications that reference the appropriate Indian Standards (IS).However, identifying the correct standard(s) is challenging due to the large number of published standards, overlapping scopes, frequent revisions, and the need to consider associated or normative reference standards. Consequently, tender specifications may omit relevant standards, reference outdated versions, or include incomplete technical requirements, leading to ambiguity, reduced product quality, and procurement disputes.
An intelligent system is required that can automatically analyze a product description or technical specification and recommend the most relevant Indian Standard(s), along with allied, cross-referenced, or normative standards that should also be considered.
• Description Develop an Al-powered recommendation engine that integrates with procurement portals and assists procurement officials in identifying the most relevant Indian Standards and related standards while preparing tender specifications.
• Expected Features
• Accept product descriptions, technical specifications, or tender documents as input.
• Recommend the most relevant Indian Standard(s) based on semantic understanding rather than keyword matching.
• Identify allied standards, including normative references, test methods, terminology standards, safety standards, installation standards, and related product standards.
• Highlight the latest published version and amendments of the recommended standards.
• Suggest mandatory certification requirements, where applicable (e.g., BIS Product Certification, CRS, Hallmarking).
• Support multilingual input and natural language queries.


=== PS 26111 ===
TITLE: Smart Al-Enabled Rapid Feed and Silage Quality Testing System for Dairy Farmers
ORG: Ministry of Fisheries, Animal Husbandry & Dairying | DEPT: Department of Animal Husbandry & Dairying
THEME: Agriculture, FoodTech & Rural Development
DATASET LINK FIELD: Additional Information regarding PS
https://drive.google.com/drive/folders/1KrErp9hRfLlaWw3gqvWFo1EpQiU1qtbG
DESCRIPTION:
• Background Animal nutrition directly affects milk production, animal health, reproductive performance, and dairy profitability. Dairy farmers often face challenges due to poor-quality cattle feed,adulterated feed ingredients, fungal contamination, toxin presence, and low-quality silage.Conventional feed testing laboratories are expensive and inaccessible for many rural farmers.There is a need for rapid, portable, affordable, and digitally enabled feed quality assessment systems.Emerging technologies such as Al, loT, spectroscopy, computer vision, and biosensors can help create real-time feed testing and advisory systems for dairy farmers.
• Description Participants are required to develop a rapid digital testing solution capable of:
• Assessing nutritional quality of cattle feed and silage;
• Detecting adulteration and contamination;
• Providing instant farmer advisories and feed recommendations;
• Monitoring feed storage and silage conditions.
The solution may include:
• Portable testing devices;
• Smartphone-enabled feed analysis;
• Al-powered nutritional prediction;
• Cloud dashboards;
• QR-based authenticity systems.
The system may detect:
• Crude protein
• Moisture
• Fiber
• Energy value
• Mineral deficiencies
• Urea adulteration
• Sand/silica contamination
• Aflatoxins and mycotoxins
• Fungal contamination Silage monitoring may include:
• pH
• Fermentation quality
• Moisture
• Spoilage indicators
• Mould growth
• Expected Solution The expected solution should:
• Provide testing results within minutes;
• Be low-cost and portable;
• Support multilingual farmer interfaces;
• Work offline in rural areas;
• Generate nutritional and storage advisories;
• Enable cloud-based monitoring and traceability.
• Expected technologies
• AI/ML
• loT sensors
• NIR spectroscopy
• Mobile applications
• Computer vision
• Cloud analytics
• Predictive advisory systems
• Insert Table Here*


