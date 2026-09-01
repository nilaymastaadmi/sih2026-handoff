=== PS 26164 ===
TITLE: Enterprise Cryptographic Discovery & Analysis Tool (ECDAT)
ORG: National Technical Research Organisation (NTRO) | DEPT: National Technical Research Organisation (NTRO)
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: Standard Open source datasets for source code repositories (eg:Github), libraries (eg: Openssl) may be used.
DESCRIPTION:
• Background Transitioning to Post Quantum Cryptography based solutions requires preparedness, risk assessment and financial and operational investment. Towards this, discovery and inventory of Cryptographic Artefacts is the critical first step, that will enable the transition.
• Description i. Identify and catalogue all cryptographic artefacts (algorithms, keys, certificates, protocols, libraries, hardware modules, cloud services) across internal and external facing applications, products and infrastructure.
ii. The tool should perform a comprehensive quantum risk assessment and identify systems prone to potential quantum attacks, and highlight risks to sensitive data.
iii. Classify all the artefacts by type, lifetime and business criticality. Apply structured frameworks such as Moscaâ€™s algorithm (compare data lifetime plus migration time against expected arrival of cryptographic relevant quantum computer) to identify and categorize risks.
iv. Recommend suitable alternatives (PQC/ Hybrid algorithms) for applications based on risk profile, latency, cost, etc.
• Expected Solution/Deliverables:
A Comprehensive CBOM analytics tool that can scan Source code repositories, binaries, libraries and container images, for assessing risks (due to quantum computers), classifying artefacts and suggesting alternatives: - Produce a report displaying all cryptographic assets including versions/ modes in standardised formats Interactive GUI platform to visualise the scan, risks and results


=== PS 26167 ===
TITLE: SatQuery AI - An Interactive Vision-Language Assistant for Multimodal Remote Sensing Image Analysis through Text Queries
ORG: Indian Space Research Organisation(ISRO) | DEPT: Department of Space / Indian Space Research Organisation
THEME: Space Technology
DATASET LINK FIELD: Training / Fine-Tuning Dataset_x000D_
BigEarthNet.txt â€” primary dataset for remote-sensing adaptation using co-registered Sentinel-1 SAR, Sentinel-2 multispectral imagery, and diverse text annotations. Link: https://arxiv.org/abs/2603.29630. All datasets are available online open source._x000D_
Public Evaluation Benchmarks_x000D_
â€¢ VRSBench â€” for
DESCRIPTION:
Background Remote-sensing imagery is widely used for agricultural monitoring, disaster management, urban planning, forest monitoring, water-resource assessment, infrastructure mapping, and environmental analysis. However, most existing remote-sensing AI solutions are developed as isolated applications for a single predefined task, such as land-cover classification, object detection, visual question answering, or change detection. These systems often require users to understand satellite-data characteristics, GIS workflows, model selection, and task-specific parameters. Consequently, non-expert users may find it difficult to obtain meaningful information from satellite imagery through simple natural-language queries.
Many operational remote-sensing questions cannot always be answered reliably using a single optical image. Relevant information may be distributed across paired or multiple observations acquired at different times or by different sensors. Optical and multispectral imagery provides spectral and contextual information, whereas synthetic aperture radar (SAR) provides complementary structural information and supports day-and-night acquisition through cloud cover. Multitemporal image pairs are required to identify and interpret changes over time, while co-registered opticalâ€“SAR pairs can provide more complete and reliable information than either modality alone.
A general-purpose large language model (LLM) or vision-language model (VLM) cannot be expected to perform these specialised tasks reliably without adaptation to remote-sensing imagery, sensor characteristics, and domain-specific terminology. The proposed solution must therefore include remote-sensing fine-tuning or domain adaptation and may employ multiple specialised models for different tasks. BigEarthNet.txt will serve as the primary dataset for adapting imageâ€“text representations to multisensor remote-sensing data. VRSBench and RSVQA will be used to evaluate single-image captioning, grounding, and visual question answering, while CDVQA will be used to evaluate multitemporal change-based visual question answering.
The novelty of SatQuery AI lies in its agentic, query-driven framework. Instead of applying a single generic VLM, the system selects and executes suitable remote-sensing specialist models, validates inputs, combines their outputs, and returns an evidence-grounded response.
Description The objective is to develop SatQuery AI, a software-based agentic vision-language assistant for analysing single and paired remote-sensing images through natural-language queries. Single-image understanding is a mandatory baseline, while the principal focus is joint reasoning over paired cross-modal and multitemporal imagery.
Defined Input Scope
• Single image: One optical/multispectral or SAR image for captioning, visual question answering, and text-guided region grounding.
• Cross-modal pair: Co-registered optical/multispectral and SAR images of the same geographic area for joint information extraction and cross-modal analysis.
• Bi-temporal pair: Two spatially corresponding images of the same geographic area acquired at different times for change detection, change description, and change-based visual question answering.
• Supported formats: GeoTIFF or TIFF for geospatial imagery. PNG and JPEG inputs may be accepted only for the prescribed public benchmark datasets.
Mandatory Functional Scope
• Remote-sensing adaptation: At least one visual or vision-language component must be fine-tuned or otherwise adapted using BigEarthNet.txt or the any open source training data.
• Single-image baseline: Visual question answering shall be mandatory. Each solution must additionally implement either captioning/scene description or text-guided region grounding.
• Multi-image change analysis: Change description or change-based visual question answering from a bi-temporal image pair shall be mandatory. A spatial change map may also be generated where reference masks are available.
• Cross-modal pair analysis: The system must extract complementary information from a co-registered optical/multispectral and SAR image pair.
• Agentic orchestration: The system must automatically select, sequence, and execute the appropriate specialist models or tools according to the query and input configuration.
Representative Queries
• 'Describe the land-cover and major objects visible in this image.'
• 'Highlight the water body referred to in the query.'
• 'What changed between these two dates, and where did the change occur?'
• 'Use the optical and SAR images together to identify built-up and water-covered regions.'
• 'Has the built-up area increased, decreased, or remained unchanged?'
Agentic Model and Tool Orchestration The system may use multiple specialised components, such as a remote-sensing VQA or captioning model, a grounding model, a change-understanding or change-VQA model, and an opticalâ€“SAR fusion or information-extraction model.
• interpret the query and classify the requested task;
• check the number, modality, format, metadata, and compatibility of the input images;
• select one or more models or tools from a predefined registry;
• configure only permitted task parameters and execute the selected workflow;
• combine textual and spatial outputs, estimate confidence, and return visual evidence; and
• provide an auditable execution summary containing the selected task, model/tool names, and key parameters.
The controller may perform internal task planning; however, only the observable execution trace, including the selected task, models or tools, permitted parameters, and outputs will be evaluated. Internal reasoning text is neither required nor evaluated.
Expected Solution The expected solution is an interactive GUI or web application with an agentic remote-sensing AI backend. It should accept supported image inputs and natural-language queries, select the appropriate specialist workflow, and return evidence-grounded textual and visual results.
The solution should include:
• Input upload and compatibility checking.
• A remote-sensing-adapted vision-language component.
• Specialist tools for VQA, captioning or grounding, change understanding, and opticalâ€“SAR analysis.
• An agentic controller for task routing, tool execution, and output integration.
• Visual evidence, confidence information, execution summaries, and downloadable reports.
Each solution must demonstrate single-image VQA, one additional single-image task, multitemporal change understanding, opticalâ€“SAR paired-image analysis, and agentic model/tool orchestration. A generic LLM or VLM without remote-sensing adaptation will not satisfy the requirements.
Deliverables An interactive GUI or web application with an agentic remote-sensing AI backend, Codes and models including test and demonstration.
Implementation Scope The system shall support single optical/multispectral or SAR images, co-registered opticalâ€“SAR pairs, and bi-temporal pairs in GeoTIFF/TIFF or approved benchmark formats. It must perform single-image VQA, one additional single-image task, change analysis, opticalâ€“SAR joint analysis, and agentic model/tool selection through an interactive GUI or web application.
Evaluation/Judging Criteria Final evaluation will use prescribed public benchmark test subsets and an ISRO/SAC evaluation dataset. Scores will be normalised before combining different metrics.
Add 'Evaluation/Judging Criteria' table here Public benchmarks will be evaluated using the prescribed test splits. The ISRO/SAC evaluation set will contain pre-georeferenced and co-registered Cartosat-2S optical and RISAT SAR image pairs, with task-specific reference answers, labels, bounding boxes, or masks, as applicable. Evaluation annotations will not be disclosed to participating teams.


=== PS 26169 ===
TITLE: Development of an AI-Based Virtual Camera Tracking System for Coarse Alignment of Mobile Free Space Optical Communication (FSOC) Terminals
ORG: Indian Space Research Organisation(ISRO) | DEPT: Department of Space / Indian Space Research Organisation
THEME: Smart Automation
DATASET LINK FIELD: Additional Information Regarding PS
https://drive.google.com/file/d/1AWRWChSMKU8FI38XxfFyQJfCRp3gqkF6/view?usp=drive_link
DESCRIPTION:
Background Free Space Optical Communication (FSOC) offers unprecedented advantages for next-generation mobile networks, including gigabit-to-terabit data rates, license-free spectrum operation, high immunity to electromagnetic interference, etc. However, deploying FSOC links between mobile platforms (satellites, UAVs presents a severe challenge of pointing, acquisition and tracking (PAT) of highly narrow laser beams. PAT typically happens in two stages: coarse alignment and fine alignment. Coarse alignment is one of the key challenges of PAT, where the transmitting terminal must first locate and maintain the remote terminal within its camera Field-of-View (FOV).
Developing and testing such algorithms on real hardware requires expensive cameras, pan-tilt mechanisms, and optical components & equipment. A software based virtual camera tracking provides an inexpensive and accessible platform for algorithm development and learning.
Description Unlike conventional radio-frequency systems, FSOC relies on a highly directional optical beam. Even a small angular error can prevent successful communication. Before fine pointing mechanism can take over, a coarse alignment stage must:
• Observe the surrounding environment,
• Acquire and detect the remote terminal or beacon,
• Estimate the position, and
• Continuously adjust the pointing direction to maintain visibility.
The participants shall develop this coarse alignment process in software, allowing to develop and validate tracking algorithms without specialized hardware and setup. The following section provides reference parameters and performance criteria to be considered for the software development.
Parameters and Specifications Functional Objective: Develop a software system that autonomously detects, identifies, and continuously tracks a designated moving target within a virtual scene by controlling a virtual camera viewport.
Add 'Parameters and Specifications' table here Expected Solution Participants shall develop an AI-assisted camera tracking system capable of automatically detecting and continuously tracking a moving optical beacon in a simulated video stream while controlling a virtual pan-tilt camera.
The developed software shall be able to:
• Generate a configurable virtual environment,
• Generate one or more moving targets,
• Implement a movable virtual camera,
• Detect the target beacon automatically,
• Track the beacon continuously using computer vision,
• Control and reposition the virtual camera,
• Generate and introduce disturbances due to atmospheric turbulence, platform vibrations, camera motion, noise, etc., in the virtual camera feed,
• Display tracking performance and statistics in real-time Deliverables Each participating team shall submit the following mandatory deliverables:
Software Application A standalone executable application implementing the complete virtual camera tracking system. The application shall provide all the mandatory functions and features as described above.
Source Code Complete source code with proper documentation. The code shall be modular and adequately commented.
Technical Report The technical report (about 10-15 pages) containing problem understanding, system architecture, description of software modules, tracking methods, AI methods (if used), test methodology, performance analysis and future improvements shall be submitted.
User Manual The user manual with the description of installation of software, application operation, parameter configuration, GUI description, etc. shall be submitted. A 3â€“5 minutes video may also be provided as an optional deliverable for demonstration of the application.
Performance Log The software should be capable of automatically generating a performance report containing simulation duration, FPS, acquisition time, average and maximum tracking error, lock retention rate, processing time, etc.
Evaluation Method and Criteria The solutions developed by participating teams will be evaluated using multi-layered evaluation method. The following table describes stages of evaluation, their weightage and methods.
Add 'Evaluation Method and Criteria' table here


=== PS 26170 ===
TITLE: AI-Driven Anomaly Detection in Component Burn-In & Screening
ORG: Indian Space Research Organisation(ISRO) | DEPT: Department of Space / Indian Space Research Organisation
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
Background In high-reliability sectors (like space) electronic components undergo rigorous environmental stress screening (ESS), including Burn-In testing (operating components at elevated temperatures, e.g., 125Â°C for extended periods).
Traditional screening relies on static parametric pass/fail limits. However, 'latent defects'â€”components that pass the absolute limits but exhibit subtle, anomalous drift over timeâ€”often escape into final payloads, leading to catastrophic field failures.
Description Development of a predictive machine learning model that analyzes time-series parametric data (e.g., standby current Iddq, leakage currents, or propagation delays measured at intervals like 0h, 24h, 96h, and 168h to detect anomalous components.
Expected Solution Module A: The outlier detection system Static limits catch obvious failures. Participants need to develop a 'Dynamic' outlier detection system. If a lot has an average leakage current of 10ÂµA, a part showing 45 ÂµA is a massive anomaly, even if the absolute datasheet maximum limit is 50 ÂµA.
Module B: Time-Series Drift Predictor Build a predictive regression model that takes Value_0h and Value_24h as inputs and forecasts Value_168h. If the predicted 168h drift rate exceeds a calculated safety slope, the system flags the component for early rejection.
Evaluation Metrics:
• Anomaly Detection Score: a False Negative (missing a defective part) is catastrophic, penalizing teams that let bad parts escape.
• Drift Prediction Accuracy : The mean absolute error between the predicted Value_168h and the actual hidden ground-truth values.
• Explainability : Can the model justify its classification to a QA inspector, or is it a complete black box?


=== PS 26173 ===
TITLE: iTantra -Indian Multilingual TTS & STT Aided Neural Transceiver Radio Access for low bitrate links
ORG: Indian Space Research Organisation(ISRO) | DEPT: Department of Space / Indian Space Research Organisation
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
Background As vocal audio information is very data intensive making it difficult to transmit through low data rate links. In alert and distress based scenarios Transmitting Audio information is critical instead of written message as it will be more inclusive and will cater to everyone even if they are literate or not.
Description Build an Android App with lightweight, highly accurate STT and TTS models for 10 Indian Languages (Hindi, Gujarati, Marathi, Kannada, Malayalam, Tamil, Telugu, Odia, Bengali, English) that runs locally on a low-power device. The systemâ€™s STT module when activated after detecting pauses and stoppages should form the sentences detected and must instantly and efficiently stream the data through wifi/Bluetooth connected embedded device or another phone with same application with minimal latency. The systems TTS module when activated after receiving the Text data should convert it into intelligible speech which will be played as a voice note and alert type messages will be announced at highest volume non-interruptible. To verify the complete loop two phones with same app one in TTS mode and another in STT mode can be connected via wifi or Bluetooth and it should work like a walkie talkie using push to talk feature, if turned off it should work like a phone.
Key Metrics for Evaluation
• Efficiency: Model size, App size (RAM/Flash footprint) and CPU usage during idle listening. (20%)
• Accuracy: Low Word Error Rate for STT and High human legibility and flow for TTS. (40%)
• Latency: The Time delay between the Words said and STT completion, Time delay between the text received and audio processed and played for TTS along with RTF (Real Time Factor). The time delta between the sentence said and the same sentence started as audio in another phone. (20%)
Software & Framework Restrictions
• Open-Source Only: The use of proprietary, closed-source, or commercial voice-activation SDKs is strictly prohibited.
• Allowed Frameworks: Teams must build their pipelines using open-source machine learning and TinyML frameworks. Recommended tools include TensorFlow Lite for Microcontrollers, PyTorch Mobile or similar.
• Fully Offline Working: Model or pipeline should work fully offline only and no internet hosted API based solutions are expected and encouraged for the STT or TTS.
Expected Solution Teams are expected to deliver a robust, deployable system architecture. A successful submission must strictly satisfy the following technical boundaries:
• Hardware & Runtime Environment: The Android application must run smoothly on Low and Mid rage mobile phones.


=== PS 26174 ===
TITLE: AI Human Activity Recognition for On-board BAS Experiments
ORG: Indian Space Research Organisation(ISRO) | DEPT: Department of Space / Indian Space Research Organisation
THEME: Space Technology
DATASET LINK FIELD: This problem requires synthetic dataset generation. Teams have to build a custom, highly focused local dataset (even just using a webcam) replicating a specific experiment. For this particular problem, following is the sequence of steps in a sample experiment:
Sample Experiment
You are given a box that contains two smaller boxes of color red and yello
DESCRIPTION:
Background As humanity aims for space missions such as BAS and lunar missions, real-time ground support becomes impossible due to communication delays. An AI-based HAR system acts as an on-board assistant that supports the execution of scientific experiments, ensuring the success of science beyond Earth's orbit.
In the space environment, AI-based HAR system may act as mission-critical support for astronauts. By tracking astronaut movements and activities in real time, HAR ensures scientific experiments and related protocols are executed flawlessly without requiring constant, high-bandwidth communication with mission control.
Description Challenge is to design and train an AI model that recognizes and validates the sequence of a pre-defined experiment using human activity recognition techniques.
Standalone operation: Space stations operate on restricted data bandwidth to Earth. Rather than streaming raw video to ground control, data is processed locally at the 'edge.' Inputs are given from fixed-payload cameras.
Dataset generation to train model for object detection, pose estimation and hand-object interaction based on the steps of the experiment.
Optional: Another challenge is that Standard 2D or ground-based 3D posture models fail because astronauts do not have a fixed 'up' or 'down' orientation. The AI model should use orientation-agnostic 3D Human Mesh Recovery (HMR) to track the astronautâ€™s body relative to the payload rack, not the floor.
Expected Solution
• The software should continuously process local video feeds to track the sequence of experiment.
• At the start or after each step, the model should suggest the next step to be performed.
• It should alert when a step is skipped or an out of sequence step is added. It should be a voice based alert.
• Using the live video, it should generate a timestamped and structured lightweight text file of the conducted steps with outcomes/ status.
• Stream the video of the experiment to specific IP and also store the video locally.
• A graphical user interface for monitoring the above activities.
• Deliverable: A trained AI model that runs on offline standalone system


=== PS 26175 ===
TITLE: DepthWizard - Single-View Height Estimation and 3D Flythrough
ORG: Indian Space Research Organisation(ISRO) | DEPT: Department of Space / Indian Space Research Organisation
THEME: Disaster Management
DATASET LINK FIELD: Any high-resolution remote-sensing dataset openly available on the internet may be used for development. Reference dataset: https://github.com/IMG-PROCESS-SAC/SIH2026/. A lower-resolution DEM source such as SRTM 30 m may be used to map scale-agnostic depth features to absolute metric elevations. During final evaluation, ISRO RGB-band optical satellite i
DESCRIPTION:
Background Accurate Digital Elevation Models (DEMs) and Digital Surface Models (DSMs) are fundamental to urban planning, disaster management, and military reconnaissance. Traditionally, elevation data is acquired through stereo-imaging pairs, LiDAR, or Interferometric Synthetic Aperture Radar (InSAR). These approaches can be cost-prohibitive, dependent on specific sensor availability, and computationally intensive. Single-view height estimation offers an agile alternative, but foundational monocular depth models are trained largely on natural egocentric imagery and predict relative depth. When applied to remote sensing, they face domain gaps, structural variations, and a lack of absolute-scale mapping. Converting relative depth into metric elevation remains a critical challenge, alongside the operational need to transform static elevation profiles into interactive 3D assets that can be navigated in real time.
Description Develop an end-to-end software pipeline that transforms single-view optical RGB remote-sensing images into high-precision elevation maps. The framework must support both non-georeferenced and georeferenced imagery.
• Non-Georeferenced RGB Imagery (for example, PNG or JPG): Produce a Relative Digital Surface Model (rDSM) for images without spatial metadata.
• Georeferenced RGB Imagery (for example, GeoTIFF): Produce an Absolute Digital Surface Model (DSM) with metric height values for images containing coordinate-system metadata.
The solution should use a pre-trained monocular depth-estimation backbone to generate initial relative-depth maps. For georeferenced imagery, a lower-resolution DEM source such as SRTM or a limited set of Ground Control Points may be used to map scale-agnostic depth features to absolute metric elevations. For non-georeferenced imagery, relative height may be used directly in the visualization stage.
After computing the elevation map, the system should project the original optical image onto a generated 3D terrain mesh and integrate the result with a rendering engine such as Unity, Three.js, or Babylon.js. The interface should support seamless first-person navigation and analysis of structural heights and slopes from arbitrary aerial perspectives.
Key Milestones
• Elevation Extraction: Use a robust pre-trained monocular depth model to extract geometric and structural representations from single-view optical imagery.
• Scale Calibration: Develop a module that converts relative depth to absolute height using scene-level statistics, low-resolution DEMs, semantic priors, or minimal Ground Control Points for georeferenced inputs.
• Visualization Layer: Build an immersive, preferably interactive, rendering pipeline that converts the optical texture and derived depth map into a navigable 3D environment deployable as a standalone application.
Evaluation Criteria:
• DSM Estimation - Accuracy and Validation (50%): Evaluate RMSE, MAE, and correlation against LiDAR or reference data, including performance stability across urban, sparse, hilly, and forested landscapes.
• Visualization - Rendering Quality and User Experience (50%): Assess projection accuracy, visual fidelity, navigability of the 3D flythrough, interface intuitiveness, software stability, and successful standalone deployment.
Expected Solution Deliver a fully integrated software suite with complete source code and technical documentation. The solution must be deployable as a unified module containing the following components:
• Elevation Estimation Module: Accept single-view optical satellite imagery in PNG, JPG, or TIFF format and output a high-fidelity DSM in a standard geospatial format.
• Interactive Visualization Platform: Provide a user-friendly 3D flythrough experience that lets users upload imagery, visualize reconstructed terrain, and validate estimated height values against reference datasets.


=== PS 26182 ===
TITLE: Automated Attribution of Unknown Cryptocurrency Wallets to Nearest Virtual Asset Service Providers (VASPs) through Blockchain Intelligence APIs
ORG: Ministry of Home Affairs | DEPT: Indian Cyber Crime Coordination Centre (I4C),CIS Division
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background The rapid adoption of Virtual Digital Assets (VDAs) and decentralized blockchain ecosystems has significantly increased the complexity of cybercrime investigations globally. Law Enforcement Agencies (LEAs) frequently encounter cryptocurrency wallet addresses linked to cyber frauds, ransomware, investment scams, darknet activities, and laundering of crime proceeds.
Under the existing investigation workflow, LEAs raise lawful information disclosure requests through the SAHYOG Portal to Virtual Asset Service Providers (VASPs) such as crypto exchanges, custodial wallet providers, and trading platforms. However, in many cases, the suspect wallet identified during investigations belongs to an unhosted wallet or a wallet for which the associated VASP is unknown. This creates major delays in attribution, freezing of assets, and identification of the beneficial owner.
Blockchain transactions generally pass through multiple intermediary wallets before reaching centralized exchanges. Identifying the 'nearest direct deposit accepting exchange' manually through blockchain analysis is time-consuming and requires specialized expertise.
• Description The proposed system envisages development of an Automated Blockchain Intelligence & VASP Attribution Engine integrated with the SAHYOG Portal through APIs.
The system should:
• Automatically analyze suspect cryptocurrency wallet addresses reported during investigations on the Sahyog Platform
• Automatically trace blockchain transaction paths to identify:
o nearest centralized exchange, o custodial wallet service, o or VASP receiving direct deposits from the suspect wallet.
• Map blockchain of deposit addresses and transaction flows across multiple blockchain networks such as:
o Bitcoin, o Ethereum, o Tron, o BNB Chain, o Solana, o Polygon o and other major chains.
• Support identification of:
o exchange clusters, o hot wallets, o deposit wallets, o mixers/tumblers, o DeFi bridges, o and cross-chain swap services.
• Integrate Sahyog with blockchain intelligence APIs and graph analytics engines.
• Provide automated tagging and confidence scoring for suspected VASPs.
• Generate investigation-ready reports for LEAs.
• Assist investigators in automatically routing lawful disclosure or freezing requests to the correct VASP through the SAHYOG Portal.
The system may additionally support:
• visualization of fund movement,
• cross-chain transaction mapping,
• risk scoring,
• identification of laundering typologies,
• and alerting for high-risk wallets linked to ransomware, darknet, terrorism financing, or fraud ecosystems.
• Expected Solution A software-based blockchain intelligence platform integrated with the SAHYOG ecosystem capable of:
• Automated identification of nearest VASP/exchange linked to unknown wallets.
• API-driven blockchain tracing and attribution support.
• Multi-chain transaction analysis and visualization.
• Real-time generation of investigative intelligence.
• Risk classification of wallets and transaction flows.
• Dashboard for LEAs with case-based analytics and reporting.
• Scalable architecture capable of handling large-volume blockchain transaction analysis.
The solution should aim to:
• reduce investigation time,
• improve asset freezing efficiency,
• enhance attribution capabilities,
• and strengthen cross-border cybercrime investigations involving VDAs


=== PS 26183 ===
TITLE: Real-Time Identification of Fraud-Linked Cryptocurrency Exchanges from Victim-Reported Suspect Wallet Addresses through Automated Blockchain Analytics
ORG: Ministry of Home Affairs | DEPT: Indian Cyber Crime Coordination Centre (I4C),CIS Division
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Cyber fraud victims increasingly report suspect cryptocurrency wallet addresses used by fraudsters for collection of funds in cases involving:
• investment scams,
• task-based frauds,
• sextortion,
• ransomware,
• phishing,
• darknet transactions,
• and organized cyber-enabled financial crimes.
During investigations, the reported wallet addresses are often:
• non-custodial wallets,
• temporary burner wallets,
• or intermediary wallets used for layering and laundering.
The inability to quickly identify the cryptocurrency exchange or VASP associated with these wallets delays:
• freezing of assets,
• preservation of evidence,
• tracing of fund flows,
• and victim fund recovery.
Manual blockchain tracing requires significant technical expertise and time, particularly in cases involving:
• multi-chain transfers,
• DeFi protocols,
• mixers/tumblers,
• bridges,
• and privacy-enhancing mechanisms.
• Description The proposed solution envisages a Real-Time Crypto Fraud Attribution System capable of automatically analyzing victim-reported wallet addresses and identifying the nearest exchange or VASP receiving direct deposits.
The system should:
• ingest wallet addresses reported through cybercrime complaint systems,
• automatically perform blockchain tracing,
• identify associated exchanges or VASPs,
• detect fund movement patterns,
• and generate actionable intelligence for investigators.
Key features may include:
• blockchain transaction graph analysis,
• clustering of exchange wallets,
• detection of intermediary laundering wallets,
• identification of cross-chain fund movement,
• integration with SAHYOG and NCRP platforms,
• automated alert generation,
• and risk categorization of wallets.
The system should support multiple blockchain ecosystems and provide:
• real-time tracing capability,
• automated investigative recommendations,
• and analytics dashboards for law enforcement agencies
• Expected Solution A software platform capable of:
• real-time blockchain intelligence generation,
• automated VASP identification,
• tracing of suspect wallets,
• cross-chain transaction analytics,
• fund-flow visualization,
• integration with LEA systems,
• and generation of standardized investigation reports.
The system should:
• reduce response time in cyber fraud investigations,
• improve freezing of proceeds of crime,
• enhance coordination with VASPs,
• and strengthen digital evidence collection capabilities.
The platform should further support:
• API integrations,
• scalable blockchain indexing,
• AI/ML-assisted risk detection,
• and automated pattern recognition for fraud typologies.


=== PS 26184 ===
TITLE: Development of a Predictive Analytics Framework for Cybercrime Complaints to Forecast Likely Cash Withdrawal Locations in Advance, Enabling Generation of Actionable Intelligence for Timely and Proactive Cybercrime Intervention.
ORG: Ministry of Home Affairs | DEPT: Indian Cyber Crime Coordination Centre (I4C),CIS Division
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background The National Cybercrime Reporting Portal is the centralized Portal, which is serving the whole country. Currently, the Portal facilitates citizens in filing complaints, LEAs act on complaints, Banking/Financial Institutions for their actions along with reports/graphs being pulled on daily basis. Presently, the Portal is receiving approximately 8000 complaints on daily basis. The number of complaints has increased manifold during the past months, and this will continue to rise in future. To address the issue of increasing cybercrimes, the proactive approach shall be adopted.
• Description This framework focuses on the mitigation of cybercrimes by adopting a proactive approach. The framework's output will enable the prediction of likely cash withdrawal locations, which, in turn, will allow law enforcement agencies (LEAs)
at the state and local levels, coordinated by I4C, to implement proactive interventions. These interventions could include deploying special teams or alerting local banks and ATMs in high-risk areas. The intelligence generated would also help banks and financial institutions (FIs) through the Citizen Financial Cyber Fraud Reporting and Management System, enabling faster fund blocking and increasing the chances of recovery. By supporting real-time actionable intelligence sharing across jurisdictions, law enforcement agencies and Banks/FIs will be able to respond faster and more effectively to cyber threats. This approach goes beyond merely reacting to complaints and creates a powerful, data-driven defense against financial cyber frauds, strengthening India's overall cybersecurity posture.
Enhancing coordination between law enforcement and financial entities will ensure better detection and prevention of financial crimes, creating a more unified and efficient approach to combating cybercrime.
• Key Deliverables Component:- Description a. Predictive Analytics Engine :-AI/ML-based system to analyse historical cybercrime and financial data to predict potential withdrawal hotspots. Features include pattern detection, geospatial risk modelling, and real-time alerts.
b. Risk Heatmap Dashboard:-GIS-enabled dashboard visualizing real-time and potential risk zones with drill-down filters by time, location, and crime category etc.
c. Law Enforcement Interface:-Secure interface for investigators to access alerts, intelligence reports, and evidence documentation.
d. Alert & Notification System:-Real-time notifications to law enforcements, banks, and I4C officers via SMS,email, API, or dashboard triggers.


=== PS 26186 ===
TITLE: AI-Based Predictive Personnel Stress and Welfare Monitoring System for Uniformed Forces
ORG: Ministry of Home Affairs | DEPT: Central Reserve Police Force (CRPF), Police II Division
THEME: MedTech / BioTech / HealthTech
DATASET LINK FIELD: Anonymized HR datasets, deployment records, leave history, wellness
survey data, workload data, and simulated behavioral datasets.
DESCRIPTION:
• Background Personnel serving in Central Armed Police Forces (CAPFs), Armed Forces, and other uniformed services operate under physically demanding, psychologically stressful, and often hazardous conditions.Extended deployments, operational pressures, separation from families,irregular working hours, and exposure to traumatic incidents can significantly impact mental well-being.Currently, stress identification largely depends on manual observation and self-reporting, which may delay timely intervention. There is a need for a proactive, technology-driven solution that can identify early indicators of stress, burnout, and psychological distress while maintaining privacy and organizational trust.
• Description The proposed solution aims to develop an AI-powered Personnel Stress and Welfare Monitoring System capable of identifying potential indicators of stress, burnout, emotional fatigue, and welfare concerns through analysis of organizational and voluntarily provided wellness data.The system should:
• Analyze HR-related indicators such as leave patterns,deployment history, duty schedules, transfer frequency, training commitments, and workload trends.
• Support optional self-reporting and wellness assessments through a secure mobile application.
• Incorporate voluntary biometric and wellness data, where authorized and legally permissible.
• Detect behavioral patterns associated with elevated stress risk.
• Generate risk assessments and welfare recommendations for authorized welfare officers and commanders.
• Enable proactive counseling, welfare interventions, and workload balancing measures.
The system must be designed with strong privacy safeguards and focus on welfare support rather than disciplinary actions.
• Expected Solution Develop an AI-driven predictive analytics platform comprising:
• Personnel Wellness Monitoring Dashboard.
• Mobile-based Wellness and Self-Assessment Application.
• Predictive Behavioral Analytics Engine.
• Stress and Burnout Risk Prediction Models.
• Welfare Intervention Recommendation System.
• Role-based Access Control and Privacy Management Framework.
• Automated Alerts for authorized welfare personnel.
• Data anonymization and secure storage mechanisms.
The solution should identify trends and risk factors while ensuring that individual dignity, confidentiality, and data protection requirements are maintained.
• Expected Benefits 1. Early identification of personnel requiring welfare support.
2. Reduction in stress-related incidents and operational fatigue.
3. Improved mental well-being and workforce resilience.
4. Enhanced readiness and operational effectiveness.
5. Better workload distribution and personnel management.
6. Improved retention and job satisfaction.
7. Data-driven welfare planning and resource allocation.
8. Reduction in incidents arising from prolonged occupational stress.
• Preliminary Scope 1. Development of predictive behavioral analytics algorithms.
2. Mobile-based wellness self-reporting platform.
3. AI-driven stress and burnout risk assessment engine.
4. Commander and Welfare Officer dashboard.
5. Automated intervention recommendation system.
6. Secure integration with HRMS and personnel management systems.
7. Privacy-preserving analytics and role-based access controls.
• Key Technical Challenges 1. Ensuring privacy and confidentiality of sensitive personnel data.
2. Preventing stigmatization of personnel identified as potentially at risk.
3. Minimizing false positives and false negatives in risk prediction.
4. Ensuring ethical and transparent AI decision-making.
5. Securing highly sensitive psychological and welfare-related information against cyber threats.
6. Building trust among personnel regarding system usage and data protection.
• Strategic Importance
• Enhances force readiness and personnel welfare.
• Supports evidence-based welfare management.
• Strengthens organizational resilience and operational effectiveness.
• Promotes preventive mental health care rather than reactive interventions.
• Creates an indigenous capability tailored to the unique operational and cultural environment of Indian CAPFs and Armed Forces.
• Potential Market 1. Central Armed Police Forces (CAPFs).
2. Indian Armed Forces.
3. State Police Organizations.
4. Disaster Response and Emergency Services.
5. Government Organizations with high-stress workforces.
6. Corporate Human Resource and Employee Wellness Platforms.
7. International security and workforce welfare markets.
• Expected Impact The proposed AI-enabled Personnel Stress and Welfare Monitoring System will help transform welfare management from a reactive process to a proactive and preventive framework. By enabling early identification of stress indicators and facilitating timely interventions,the solution can improve personnel well-being, enhance operational effectiveness, and strengthen the long-term resilience of uniformed services while maintaining the highest standards of privacy, ethics, and data security.


=== PS 26187 ===
TITLE: AI-Based Intelligent Video Analytics Platform for Border Surveillance using existing CCTV Infrastructure.
ORG: Ministry of Home Affairs | DEPT: Sashastra Seema Bal (SSB), Police II Division
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Border security forces deploy CCTV cameras at Border Out Posts(BOPs), check posts, border roads, and other strategic locations for surveillance and monitoring. However, conventional CCTV systems primarily provide video recording and live monitoring capabilities,requiring continuous human observation. Advanced surveillance functionalities such as Facial Recognition Systems (FRS), Automatic Number Plate Recognition (ANPR), intrusion detection, and object tracking often require specialized hardware and proprietary solutions,making large-scale deployment costly and difficult, particularly in remote border areas.
• Description The proposed solution aims to develop an AI-driven software platform capable of transforming existing CCTV infrastructure into an intelligent surveillance network without requiring dedicated FRS, ANPR, or smart-camera hardware. The platform shall ingest live video streams from standard IP-based CCTV cameras and perform real-time video analytics using Artificial Intelligence and Computer Vision techniques.
The solution should provide capabilities such as:
• Human detection and tracking
• Vehicle detection and classification
• Face detection
• Automatic Number Plate Recognition (ANPR)
• Virtual fence intrusion detection
• Suspicious activity detection
• Night-time movement detection
• Real-time alert generation and event logging
• Expected Solution The proposed system should leverage Artificial Intelligence, Machine Learning, Computer Vision, and Video Analytics to create a software-defined surveillance platform capable of extracting actionable intelligence from existing CCTV infrastructure.
The solution should:
• Eliminate dependence on expensive dedicated surveillance hardware.
• Enable intelligent monitoring through AI-powered video analytics.
• Provide real-time alerts for security incidents and border intrusions.
• Support facial recognition, vehicle identification, and behavioral analytics through software.
• Improve situational awareness and response time for border security forces.
• Support integration with existing command and control systems.
• The final solution should be cost-effective, scalable, and suitable for deployment across remote border locations and strategic installations.
• Possible Project Name IBVAP â€“ Intelligent Border Video Analytics Platform


=== PS 26188 ===
TITLE: Al-Based Fake Identity & Document Screening System
ORG: Ministry of Home Affairs | DEPT: Sashastra Seema Bal (SSB), Police II Division
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Common challenges faced at border checkpoints:
• Fake passports and visas
• Altered photographs
• Modified dates of birth
• Tampered visa stamps
• Identity impersonation
• Multiple identities used by the same person Expired or blacklisted travel documents
• High passenger volume causing delays Current verification methods rely heavily on human inspection and basic database lookups.
• Detailed Description Border checkpoints process thousands of identity documents every day,including passports, visas, national identity cards, permits, and travel authorizations. Manual verification is time-consuming, prone to human error, and often unable to detect sophisticated forgeries, tampering, or identity fraud.Develop an Al-powered document screening platform that automatically analyzes identity and travel documents, detects signs of tampering or forgery, validates information against rules and databases,and generates a risk score to assist border security personnel in making faster and more accurate decisions.
• Expected Solution
• Module 1: OCR Extraction
• Module 2: Document Validation
• Module 3: Tampering Detection
• Module 4: Face Detection Module 1: OCR Extraction Objective: Automatically extract all relevant information from identity documents.
Inputs:
• Passport image
• Visa image
• National ID image
• Driving license
• Permit documents Extracted Fields:
Passport
• Name
• Passport Number
• Nationality
• Date of birth
• Date of expiry
• Gender Visa
• Visa Number
• Visa Type
• Entry Validation
• Stay Duration Module 2: Document Validation Objective: Verify whether the extracted information follows official document standards.
Module 3: Tampering Detection (Core AI Innovation)
Objective: Detect digitally or physically altered documents.
Use Cases:
• Photo Replacement
• Text Manipulation
• Stamp Forgery Detection
• Image Metadata Analysis Module 4: Face Verification Objective: Ensure document owner matches the presented individual.
• Expected Impact
• Reduce document verification time from several minutes to a few seconds.
• Improve detection of forged and tampered documents.
• Standardize screening decisions across checkpoints.
• Enable data-driven risk assessment instead of purely manual inspection.
• Create a digital trail for investigations and intelligence analysis.
Possible Project Name Al-Based Fake Identity & Document Screening System.


=== PS 26189 ===
TITLE: AI-Powered Criminal Network Analysis System
ORG: Ministry of Home Affairs | DEPT: National Crime Records Bureau (NCRB), Women Safety Division
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Modern criminal activities are increasingly organized and interconnected. Criminals often operate through networks involving associates, intermediaries, financial channels, communication links,locations, and events. Law enforcement agencies collect large volumes of data from sources such as:
• FIRs and police reports
• Call Detail Records (CDRs)
• Financial transaction records
• Surveillance reports
• Social media intelligence
• Criminal history databases
• Intelligence agency reports Despite having access to this information, investigators frequently face challenges in identifying hidden relationships among suspects because the data is fragmented, unstructured, and distributed across multiple systems. Manual analysis can be slow, labor-intensive, and prone to missing critical connections.With advances in Artificial Intelligence (AI), Machine Learning (ML),Natural Language Processing (NLP), and Graph Analytics, it is now possible to automatically discover relationships, detect patterns, and generate insights that can assist investigators in understanding criminal networks more effectively.
• Description The objective is to develop an AI-powered system that can analyze large volumes of criminal and intelligence-related data to uncover hidden networks and relationships among individuals, organizations, locations,and events.
The system should:
• Collect and process data from multiple sources.
• Extract important entities such as people, locations, vehicles, phone numbers, and organizations.
• Build relationship maps showing how different entities are connected.
• Identify key individuals who play influential roles within criminal networks.
• Detect suspicious patterns and unusual activities.
• Assist investigators by providing visual and analytical insights.
• Expected Solution Develop an AI-powered system that automatically analyzes structured and unstructured crime-related data to uncover criminal networks,identify key influencers, detect suspicious patterns, and provide actionable intelligence for investigators.


=== PS 26190 ===
TITLE: Secure Digital Document Management System for Legal and Investigation Documents
ORG: Ministry of Home Affairs | DEPT: National Crime Records Bureau (NCRB), Women Safety Division
THEME: Blockchain & Cybersecurity
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Law enforcement agencies, courts, legal departments, and investigative organizations handle vast amounts of sensitive documents throughout the lifecycle of a case. These documents may include:
• FIRs and police reports
• Investigation records
• Witness statements
• Charge sheets
• Court filings
• Evidence records
• Forensic reports
• Legal notices and judgments Many organizations still rely on paper-based systems or fragmented digital storage solutions. This often leads to challenges such as:
• Difficulty in locating documents quickly
• Unauthorized access to confidential information
• Document tampering risks
• Lack of version control
• Inefficient collaboration between departments
• Delays in legal and investigative processes
• Poor auditability and compliance tracking As the volume of legal and investigation-related data continues to grow,there is an increasing need for a secure, centralized, and intelligent document management system that ensures data integrity, accessibility,confidentiality, and efficient case management.Modern technologies such as Cloud Computing, Artificial Intelligence (AI), Blockchain, Digital Signatures, and Secure Access Control can significantly improve the management and security of legal and investigative documents.
• Description The objective is to develop a Secure Digital Document Management System (DMS) that enables law enforcement agencies, legal institutions, and investigative departments to securely store, organize, manage,retrieve, and share sensitive legal and investigation documents.
The system should:
• Digitize and centralize document storage.
• Ensure secure access and confidentiality.
• Prevent unauthorized modifications.
• Maintain a complete audit trail of document activities.
• Enable efficient document search and retrieval.
• Support collaboration among authorized stakeholders.
• Ensure compliance with legal and regulatory requirements.
The challenge is to create a secure, scalable, and intelligent platform that streamlines document handling while preserving legal validity and evidentiary integrity.
• Expected Solution Develop a system to monitor and manage police assets throughout their lifecycle.


=== PS 26191 ===
TITLE: Intelligent Identification of Hazard-Based Red Zones, Carrying Capacity Assessment, and Immediate Relocation Needs for Vulnerable Habitations
ORG: Ministry of Home Affairs | DEPT: National Disaster Response Force (NDRF), DM Division
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Indiaâ€™s disaster-prone regions face recurring hazards such as landslides,floods, coastal erosion, and cloudbursts. Vulnerable habitations often remain in unsafe zones, leading to repeated loss of lives and property.Current relocation efforts are largely reactive, initiated after disasters strike, rather than proactively planned.
• Description The initiative seeks to develop an intelligent, GIS-enabled decision support platform. This platform will dynamically identify and update multi-hazard Red Zones (areas unsuitable for permanent habitation),assess the carrying capacity of safer alternative sites, and prioritize vulnerable habitations for relocation. The system will integrate hazard intensity, population vulnerability, and disaster history to guide evidence-based decisions.
• Expected Solution A robust, AI-driven GIS platform that Maps and updates hazard-based Red Zones in real time, assesses suitability and carrying capacity of safer relocation sites, prioritizes vulnerable habitations for immediate,short-term, and medium-term relocation and provides actionable insights to State Disaster Management Authorities for proactive planning.


=== PS 26192 ===
TITLE: Flash Flood Prediction System for Hilly Regions using Multi-Source Data Theme
ORG: Ministry of Home Affairs | DEPT: National Disaster Response Force (NDRF), DM Division
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Hilly states in India are highly vulnerable to landslides and flash floods,which often occur with very short warning times. These sudden events result in significant loss of lives and property, and current early warning mechanisms are inadequate for hyper-local prediction and timely evacuation.
• Description The proposed initiative aims to develop a predictive system that integrates multiple data sources - rainfall data, soil moisture sensors,slope stability models, historical landslide inventories, and real-time IoT inputs. By combining these datasets, the system will generate hyper-local forecasts at the village or ward level, providing sufficient lead time for evacuation and risk mitigation.
• Expected Solution A comprehensive flash flood prediction system that Integrates rainfall,soil moisture, slope stability, and historical disaster data, utilizes IoT sensors for real-time monitoring, issues hyper-local early warnings at village/ward level, and provides actionable lead time for evacuation and disaster preparedness.


=== PS 26229 ===
TITLE: Kabadiwala Connect – Bringing the Informal Collector into the Formal Recycling Chain
ORG: Ministry of Mines (MoM) | DEPT: Jawaharlal Nehru Aluminium Research Development and Design Centre (JNARDDC)
THEME: Clean & Green Technology
DATASET LINK FIELD: (empty)
DESCRIPTION:
Background:
The overwhelming majority of India’s end-of-life electronics is collected through informal scrap dealers, waste-pickers, and local aggregators due to their extensive last-mile reach and low collection costs.
However, these informal collectors remain largely outside the formal recycling ecosystem. The E-Waste (Management) Rules, 2022 established a formal Extended Producer Responsibility (EPR) framework involving authorized recyclers, but there is currently limited access for informal collectors to participate in this formal recycling chain.
As a result, material collected by informal aggregators may undergo unsafe backyard processing such as open-air cable burning, acid leaching of printed circuit boards, and manual desoldering without proper extraction facilities. While materials such as copper and small quantities of gold may be recovered, valuable materials including lithium, cobalt, neodymium, tantalum, gallium, and indium may be lost.
These practices also expose workers to significant health and safety risks. The fundamental gap is not only technological but also informational and institutional. Informal collectors may not know the prevailing fair price of materials, which nearby recyclers are authorized, how to complete a compliant material handover, or how to obtain a documented record of the transaction. Consequently, there is limited incentive for collectors to prefer the formal recycling route
Problem:
Design and develop a vernacular, low-literacy, offline-tolerant mobile platform that enables informal scrap collectors to discover fair prices, connect directly with authorized recyclers, complete a documented and traceable handover of collected materials, and receive payment. The platform should make the formal recycling channel an economically attractive and convenient option for informal collectors rather than creating an additional compliance burden
The platform should:
• Allow collectors to photograph, categorize, and create digital lots of collected materials such as CRTs, LCD panels, PCBs, cables, batteries, motors and magnet-bearing assemblies, and mixed plastics, enter approximate weight, and receive an instant value estimate.
• Provide a price discovery and historical price dataset containing material category, sub-category,location, date, prevailing buying price, unit of measurement, approximate market range, and recycler/aggregator offered price. The system should use this dataset to provide transparent and current price information to collectors and identify basic price trends.
• Maintain a material and transaction dataset containing lot/reference ID, material category, material description, photograph/image reference, approximate weight, estimated value, quoted price, final sale value, date and time of collection, collection location, recycler details, and transaction status. This dataset should enable traceability of material from collection to authorized recycling.
• Maintain an authorized recycler/aggregator dataset containing recycler/aggregator name, facility location, materials accepted, authorization/registration details, authorization status, contact details, offered rates, pickup availability, and service area. The platform should use this information to identify and rank suitable authorized recyclers for a collector's lot.
• Use the collected material image, category, weight, location, historical price, and transaction data to support AI/ML-based features such as material classification, approximate valuation, recycler matching, and identification of abnormal or inconsistent transaction values, wherever sufficient training data is available.
• Provide current buying rates for different material categories and locations through a simple price board, including spoken price information and basic price trends.
• Match collected lots with nearby authorized recyclers or aggregators based on location, material category, offered rate, pickup availability, and authorization status.
• Generate a digital and verifiable handover/transfer record containing photographs, weight, timestamp, GPS/location details, and a unique reference that can be confirmed by the recycler.
• Maintain an easy-to-understand earnings ledger showing transactions, payments, and pending dues, thereby building a usable financial and transaction history for collectors.
• Provide pictorial and/or audio-based safety guidance on hazardous practices, including improper burning or opening of materials and safe handling of batteries and CRTs.
• Support Marathi and Hindi at a minimum and provide a genuinely usable interface for users with limited literacy.
• Operate in low-connectivity environments through an offline-first architecture, allowing core activities to be completed offline and synchronized when connectivity becomes available.
• Support entry-level Android devices with a small application size and low memory requirements. Allow cash-based transactions while keeping digital payment optional and not making it a prerequisite for using the platform.
Dataset Requirements:
The solution should be designed to create and utilize structured datasets generated through field operations and platform transactions. The minimum dataset should cover the following:
• Material Dataset: Material category, sub-category, material description, image, approximate weight, condition, source type, and estimated value.
• Price Dataset: Material category, location, date/time, buying price, selling/quoted price, unit, recycler/aggregator, and historical price information.
• Recycler Dataset: Recycler/facility name, location, materials accepted, authorization status/details,contact information, offered rate, pickup availability, and service area.
• Transaction Dataset: Unique lot ID, collector ID, material category, quantity/weight, quoted price, final price, recycler ID, collection location, handover location, date/time, payment status, and transaction status.
• Traceability Dataset: Lot ID, photographs, weight, timestamp, GPS/location, handover reference number, recycler confirmation, and subsequent transaction status.
• Collector Dataset: A minimal profile containing collector ID, preferred language, general operating location, transaction history, and earnings history. The system should avoid collecting unnecessary personal information.
• AI/ML Training Dataset: Where AI/ML functionality is proposed, teams should develop or use appropriately sourced datasets containing material images, material categories, weights, prices, locations, and transaction records for model training and validation. Teams should clearly identify the source, quality, size, and limitations of such datasets.
• The dataset should support data cleaning, validation, anonymization where required, historical analysis, price prediction, material classification, recycler recommendation, and transaction-level traceability.
• Teams should demonstrate how the dataset is generated, stored, validated, updated, and used by the application rather than treating the dataset as a static database.
Expected Outcome:
The proposed solution should create a simple digital bridge between informal collectors and the formal recycling ecosystem, improving price transparency, enabling traceable material handovers, connecting collectors with authorized recyclers, promoting safer handling practices, and encouraging greater participation in the formal recycling chain. The solution should include a working mobile application, recycler-side interface, structured datasets for materials, prices, recyclers and transactions, field research involving at least two working scrap collectors or aggregators, and a live usability demonstration. Teams should also provide a short unit-economics assessment comparing the collector's existing earnings with the potential earnings through the proposed platform and explaining how the platform can sustain its operations.


