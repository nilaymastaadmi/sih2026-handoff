=== PS 26038 ===
TITLE: Explainable AI for Diabetic Retinopathy Screening in Rural India
ORG: MathWorks | DEPT: MathWorks
THEME: MedTech / BioTech / HealthTech
DATASET LINK FIELD: APTOS 2019 Blindness Detection: https://www.kaggle.com/c/aptos2019-
blindness-detection
IDRiD (Indian Diabetic Retinopathy Image Dataset): https://ieeedataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid
DRIVE (Vessel Extraction): https://drive.grand-challenge.org/
Messidor-2: https://www.adcis.net/en/third-party/messidor2/
DESCRIPTION:
Background:
India has over 77 million diabetic adults - the second highest globally. Diabetic Retinopathy (DR) affects ~18% of this population and is a leading cause of preventable blindness. Early screening can prevent90% of vision loss, but India has only ~1 ophthalmologist per 100,000 rural population, making mass manual screening infeasible. Existing AI solutions function as black boxes, lack clinical validation rigor, and fail with variable image quality from portable fundus cameras in field conditions. A robust, explainable, and validated screening system is essential for deployment in primary healthcare centres across rural India.
Description:
Design a MATLAB-based retinal image analysis pipeline for automated DR screening addressing real-world deployment challenges:
1. Image Quality Assessment and Enhancement: Automatically evaluate fundus images for adequacy (focus, illumination, field of view). Apply adaptive enhancement (CLAHE, illumination normalization, denoising) for borderline images; reject ungradeable ones with recapture feedback.
2. Retinal Structure Segmentation: Extract clinically relevant structures - optic disc/fovea localization, vessel segmentation, microaneurysm detection, exudate segmentation, hemorrhage classification, and neovascularization detection.
3. DR Severity Grading: Classify using the International Clinical DR severity scale (Levels 0-4, from no DR to proliferative DR) with clinically acceptable sensitivity (>90%) and specificity (>85%) for referable DR (Level 2+).
4. Explainability Module: Implement Grad-CAM attention maps, lesion-level evidence correlated with clinical criteria, calibrated confidence scores, and automated annotated reports - enabling ophthalmologist validation in under 30 seconds for a human-in-theloop workflow.
5. Simulink Workflow Simulation: Model the telemedicine screening pipeline in Simulink - image acquisition rates, bandwidth constraints, processing throughput, and review capacity - to optimize resource allocation for district-level programs serving 100,000+ patients annually.
This problem demands clinical validation rigor, sub-pixel microaneurysm detection, and clinically meaningful explainability
• Tools: Image Processing Toolbox, Computer Vision Toolbox, Deep Learning Toolbox, Medical Imaging Toolbox, Simulink, Statistics and Machine Learning Toolbox Expected Solution: A working prototype demonstrating: DR classification with >90% sensitivity and >85% specificity for referable DR;
explainable Grad-CAM outputs rated as clinically useful; a Simulink model optimizing screening resource allocation; and validation against published benchmarks showing the integrated pipeline outperforms any single technique approach.


=== PS 26041 ===
TITLE: AR-Based Vocational Training Simulator for Industrial Safety in Jharkhand's Mining & Manufacturing Sector
ORG: Governmcnt of Jharkhand | DEPT: Department of Higher & Technical Education
THEME: Smart Education
DATASET LINK FIELD: (empty)
DESCRIPTION:
Background:
Jharkhand is lndia's leading mineral-producing state, with coal mines, steel plants, and mica processing units employing hundreds of thousands of workers many of them young tribal recruits with no prior industrial exposure. Classroom-based safety training using static manuals has documented retention rates below 20% after one week. Live drills are operationally disruptive, and VR headset simulators are inaccessible to small-scale mines and contract workers.. The DGMS, Dhanbad, recorded 48 fatal mine accidents in Jharkhand in 2022-23, a large share involving workers with under 30 days of orientation. The Factories Act, 1948 and Mines Act, 1952 mandate periodic safety certification, yet no standardised digital training platform exists in regional languages, and physical certificates have no mechanism to verify comprehension.
Description:
Design and develop a mobile AR-based vocational training and safety certification platform running on mid-range Android smartphones (Android 10+, no external headset required), accessible to workers across Jharkhand's mining, steel, and mica sectors. The platform must deliver interactive AR training modules covering five industrial safety domains: (l) Fire & Explosion Response-exit identification, extinguisher use, and evacuation sequencing overlaid on real surroundings via phone camera; (2) Gas Leak & Confined Space Protocol-hazard zone recognition, PPE selection, and buddy-system procedures simulated in AR; (3) Machinery.
Expected Solution:
A working Android APK demonstrating at least two complete AR training modules, an assessment engine, QR-based certificate generation and verification, Hindi and Santali localisation, offline functionality, and a web admin compliance dashboard- submitted with a demo video and public GitHub repository.


=== PS 26042 ===
TITLE: Al-Powered Vernacular Pedagogy and Real-Time Translation Tool for Mother Tongue-Based Primary Education
ORG: Governmcnt of Jharkhand | DEPT: Department of Higher & Technical Education
THEME: Smart Education
DATASET LINK FIELD: (empty)
DESCRIPTION:
Background:
Jharkhand's PALASH Mother Tongue-Based Multilingual Education (MTB-MLE) programme has demonstrated measurable improvements in foundational literacy among tribal children. However,scaling the programme is severely bottlenecked by a shortage of teachers proficient in tribal languages including Ho, Mundari, and Santhali -languages with limited digital NLP resources. The vast majority of teachers assigned to tribal-area primary schools are Hindi-medium trained and lack the linguistic tools to deliver mother-tongue-based instruction. Without a technology bridge, the pedagogical intent of MTB-MLE cannot be realised at scale, and children in over 5,000 tribal-area primary schools continue to receive instruction in a language they do not comprehend at home.
Description:
Develop an Al-assisted translation and curriculum-generation software suite that enables non-nativespeaking primary school teachers to deliver mother-tongue-based instruction in Ho, Mundari, and Santhali without prior language training. The system must include an NLP engine capable of translating standard Hindi Foundational Literacy and Numeracy (FLN) curriculum content- including lesson scripts, activity instructions, and assessment prompts-into contextually accurate text and synthesised audio in target tribal languages. A real-time voice-to-voice translation feature must allow a teacher speaking Hindi to conduct interactive classroom dialogue with tribal-language-speaking students, with latency not exceeding three seconds. The system must auto-generate bilingual worksheets and visual flashcard sets aligned to the NIPUN Bharat learning outcomes framework.Given that most schools in the target deployment areas lack reliable internet, the entire application must function offline on low-cost tablets (?2 GB RAM, Android 9+) after initial content synchronisation.
Expected Solution:
A working software application demonstrating Hindi-to-tribal-language translation (minimum one tribal language at prototype stage), real-time voice translation with sub-3-second latency, autogenerated bilingual worksheet output, and full offline operation on a low-end Android tablet submitted with a demo video - and GitHub repository.


=== PS 26043 ===
TITLE: A digital platform to crowdsource societal challenges and facilitate collaborative problem solving through universities and industry partnerships
ORG: Governmcnt of Jharkhand | DEPT: Department of Higher & Technical Education
THEME: Smart Education
DATASET LINK FIELD: (empty)
DESCRIPTION:
Background:
Communities across Jharkhand encounter numerous local challenges related to education,healthcare, agriculture, water management, sanitation, environment, rural livelihoods,accessibility, urban infrastructure, and public service delivery. While citizens are often the first to identify these issues, there is currently no structured mechanism through which they can submit such problems for systematic evaluation and innovation-driven resolution.At the same time, Higher Education lnstitutions (HEIs) possess significant academic expertise,research capabilities, and a large pool of students capable of developing practical solutions.Industries and start-ups also have technical expertise, financial resources, and implementation capabilities that can complement academic research. However, collaboration among citizens,universities, and industry remains largely fragmented and project-specific.The National Education Policy (NEP) 2020 emphasizes experiential learning, multidisciplinary research, innovation, industry collaboration, and community engagement. Establishing a technology-enabled platform that connects societal challenges with academic institutions and industry partners can foster demand-driven innovation while enabling students and researchers to work on real-world problems that create measurable social impact.
Description:
Every year, citizens across Jharkhand identiff thousands of local issues that require innovative technological or process-based solutions. These challenges often remain unresolved due to the absence of a centralized platform that enables problem collection, categorization, expert evaluation, institutional assignment, and industry collaboration.There is a need to develop a digital platform capable of:
• Allowing citizens, community organizations, local bodies, and government agencies to submit societal challenges thiough an intuitive web and mobile interface, supported by photographs, videos, location details, and relevant documents.
• Automatically categorizing submitted problems based on thematic domains such as education, agriculture, healthcare, water resources, environment, energy, urban development, accessibility, public administration, and rural livelihoods using Al-enabled classification techniques.
• Routing validated problem statements to appropriate universities based on their academic disciplines, research expertise, innovation centres, incubation facilities, and faculty specialization.
• Enabling universities to evaluate submitted challenges, constitute multidisciplinary student and faculty teams, and prepare solution proposals or research projects.
• Facilitating collaboration between universities and industry partners, startups, MSMEs,CSR organizations, research laboratories, and innovation ecosystems for mentorship,funding, prototyping, testing and deployment of solutions.
• Providing workflow management for problem review, institutional allocation, project monitoring, stakeholder communication, milestone tracking, and solution validation.
• Generating dashboards and analytics for govemment departments to monitor the number of challenges received, domain-wise distribution, institutional participation, industry engagement, project progress, and measurable social outcomes.
The platform should support a transparent and scalable innovation ecosystem that transforms community-driven challenges into research, innovation, entrepreneurship, and deployable solutions.
Expected Solution:
A comprehensive Societal Innovation Collaboration Portal comprising the following components:
• A citizen engagement module enabling individuals, community groups, Panchayati Raj Institutions, Urban Local Bodies, and government departments to submit societal challenges with multimedia evidence, geographical location, and supporting information.
• An Al-enabled problem management module capable of automatically categorizing, prioritizing, deduplication, and routing validated challenges to appropriate universities based on subject expertise and institutional capabilities.
• A university collaboration module allowing Higher Education Institutions to review assigned challenges, form multidisciplinary project teams, assign faculty mentors, manage project workflows, and submit solution proposals.
• An industry partnership module facilitating participation by industries, startups, MSMEs,CSR organizations, research institutions, and innovation hubs for mentoring, co-development, funding, prototyping, pilot implementation, and technology transfer.
• A project lifecycle management system for monitoring milestones, deliverables, approvals, documentation, testing outcomes, intellectual property generation, and implementation status.
• A visual analytics dashboard providing real-time insights on challenge submissions, university participation, industry collaborations, thematic trends, project completion rates,innovation outcomes, patents, startups created, and community impact across districts and sectors.
• A notification and communication system enabling seamless interaction among citizens,universities, industry partners, mentors, and government departments throughout the project lifecycle.


=== PS 26044 ===
TITLE: Portal for Academia - Industry collaboration for Skill Mapping, Internships and Placement
ORG: Ministry of Ayush | DEPT: All India Institute of Ayurveda
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
Background:
A significant gap exists between the skills acquired in academic institutions and the competencies expected by industries. Students often struggle to identify the skills required for their desired career paths, while industries face challenges in finding candidates with the right skill sets. Similarly, academicians have limited visibility into industry internship opportunities that could help them gain practical exposure and align teaching with current industry practices. There is a need for a unified platform that connects students, industries, and academicians, enabling seamless collaboration and skill development.
Description:
The proposed solution is a centralized Academiaâ€“Industry Collaboration Portal that serves as a one-stop platform for students, industries, and academicians.
Key features include:
• Skill Assessment: Students complete a questionnaire to evaluate their technical and soft skills shared by industry. The system generates a skill profile and identifies strengths and skill gaps based on current industry requirements.
• Skill Mapping: Based on the assessment, the platform recommends relevant industries, job roles, and skill development programs aligned with industry requirements.
• Industry Internship & Job Opportunities: Industries can post internships, projects, apprenticeships, and entry-level job openings with required skills. Students receive recommendations based on their skill profiles and can apply directly.
• Industry Learning Programs: Companies can publish training programs, certification courses, workshops, and mentorship initiatives to help students acquire in-demand skills before applying.
• Allow students to search, apply, and track internship and placement opportunities through a single platform.
• Provide a dedicated portal for academicians to explore faculty internships, industrial training, Faculty Development Programs (FDPs), consultancy opportunities, and collaborative research projects.
• Facilitate industryâ€“academia collaboration through mentorship programs, workshops, guest lectures, innovation challenges, and live industry projects.
• Enable institutions to monitor student skill development, internship participation, and placement progress through dashboards and analytics.
• Maintain a digital portfolio for students containing verified skills, certifications, projects, internships, and achievements to improve employability.
Expected solution:
The solution should provide:
The solution should provide a secure, scalable, and intelligent platform that supports the complete lifecycle of skill development, internships, and placements.
• Skill Development-
• Skill assessment through questionnaires and aptitude tests.
• Skill profiling and identification of technical and soft skill gaps.
• Personalized learning recommendations, certification programs, and industry-relevant training.
• Career guidance based on individual skills, interests, and industry demand.
• Student digital portfolios showcasing verified skills, certifications, projects, and achievements.
• Internship-
• Centralized internship portal where industries can post internship opportunities with required skills.
• Matching of students to internships based on their skill profiles and career interests.
• Internship application and tracking system for students.
• Internship opportunities for academicians, industrial training, and Faculty Development Programs (FDPs).
• Progress tracking, mentor feedback, and internship completion records.
• Placement-
• Industry portal for posting job opportunities with required qualifications and skill sets.
• Recommendation engine to match students with relevant placement opportunities.
• Candidate shortlisting based on skill compatibility and eligibility.
• Application tracking and recruitment management for students and recruiters.
• Analytics and reporting dashboards for institutions and industries to monitor placement readiness, recruitment outcomes, and skill demand trends.
Overall Platform Features-
• Role-based access for students, academicians, industries, and institutions.
• Secure document management for resumes, certificates, internship reports, and academic records.
• Collaboration features for industry mentorship, live projects, workshops, and research partnerships.
• Integration with learning platforms, certification providers, and institutional databases.
• Comprehensive analytics to support data-driven decisions for institutions, industries, and policymakers.


=== PS 26045 ===
TITLE: IP-SAKTI Sahayak a multilingual, RAG-based (source-cited) AI assistant for Intellectual Property and regulatory guidance in Ayurveda, across national and international regimes.
ORG: Ministry of Ayush | DEPT: All India Institute of Ayurveda
THEME: MedTech / BioTech / HealthTech
DATASET LINK FIELD: The corpus can be assembled from open, authoritative public sources; representative examples:
•Traditional Knowledge Digital Library (TKDL) — tkdl.res.in
•Statutes & rules — India Code, indiacode.nic.in
•IP India public databases (patents/InPASS, trade marks, designs, GI Registry) — ipindia.gov.in
•National Biodiversity Authority / ABS — nbaindia.or
DESCRIPTION:
Background:
Ayurveda rests on a vast corpus of codified and community-held traditional knowledge (TK) and on therapeutics derived from plant, microbial and animal sources. Protecting and commercialising an Ayurvedic product means navigating several overlapping regimes at once: patents, geographical indications (GI), trademarks, copyright, designs, trade secrets and plant-variety rights; the Access-and-Benefit-Sharing duties that flow from Indiaâ€™s sovereignty over its biological resources; and the drug-regulatory framework that decides whether a formulation is a classical medicine, a proprietary medicine, a new drug, a phytopharmaceutical, a food or a cosmetic. Practitioners, researchers, AYUSH startups and MSMEs and cultivators routinely struggle with this. The result is twofold: legitimate Ayurvedic innovation is under-protected and under-commercialised, while Indiaâ€™s traditional knowledge remains exposed to misappropriation abroad. Recent shifts â€” the 2024 patent and biodiversity rules, the WIPO Treaty on Genetic Resources and Associated Traditional Knowledge (2024) and a fast-moving advertising and regulatory landscape â€” make authoritative, plain-language guidance more necessary than ever, yet no such tool exists for the AYUSH community.
Description:
The assistant answers IPR questions specific to Ayurveda with accuracy, source citation and jurisdictional clarity, keeping the national and the international layers distinct through an explicit jurisdiction switch so that answers are never conflated.
Because intellectual property for an Ayurvedic product is inseparable from how the product is regulated, the assistant first helps classify the formulation. It asks the minimum clarifying questions to determine whether the product is a classical/generic medicine (formulation and method drawn from a First-Schedule authoritative text), a patent-or-proprietary medicine, a new or non-classical drug requiring proof of safety and effectiveness, a phytopharmaceutical, an Ayurveda-Aahar / nutraceutical, or a cosmetic â€” and then states what each category requires and its very different IP and ABS posture. For example, a classical formulation is largely traditional knowledge that faces the Section 3(p) patenting bar and is defended through the Traditional Knowledge Digital Library, whereas a new drug gains genuine patent potential but must generate clinical evidence.
National coverage spans the Patents Act (and the 2024 Rules), the GI, Trade Marks, Designs, Copyright and Plant-Variety regimes, the Biological Diversity Act (as amended in 2023, with the 2024 Rules) and the allied drug, advertising, labelling and food/cosmetic regimes â€” the Drugs and Cosmetics Act, the Drugs and Magic Remedies (Objectionable Advertisements) Act and the FSSAI Ayurveda-Aahar regulations. International coverage separately spans TRIPS, the Convention on Biological Diversity and the Nagoya Protocol, the WIPO GRATK Treaty, the PCT, the Madrid and Hague systems, the Budapest Treaty (for micro-organism deposits) and the herbal-product market-access regimes of key export markets.
The assistant also facilitates access to authoritative sources â€” free official databases directly and the userâ€™s own paid subscriptions only with explicit, logged permission â€” so that a user can move from a question to the right registry, record or form. It must cite the specific statute, rule, treaty article or record it relies on; clearly state that it provides information and not legal advice; keep its corpus current as the law changes; and never fabricate authority.
Expected solution:
A deployable, multilingual assistant built on retrieval-augmented generation grounded in a curated, version-tracked corpus of statutes, rules, treaties, pharmacopoeial standards, registry records and case law, so that every answer is traceable to a source and hallucination is minimised. The solution should provide: a jurisdiction toggle (India vs international) with the two answer-sets kept visibly separate; routing across IP types together with the formulation-classification flow; an ABS-compliance helper and a TKDL / prior-art pointer; mandatory source citations with a confidence indicator and a path to escalate to a human IP facilitator; multilingual delivery (leveraging national language infrastructure such as Bhashini); and guardrails, a standing 'information, not legal advice' disclaimer and privacy, audit and security aligned to the Digital Personal Data Protection regime and to recognised AI-application standards. A relational knowledge graph and agentic, multi-source orchestration deepen multi-step reasoning and the build can be staged â€” a citation-grounded retrieval MVP first, then the graph and agentic layers, then paid-source connectors and the full multilingual and voice experience. The output should be evaluable on answer accuracy, citation correctness, safe abstention on out-of-scope or uncertain queries and multilingual quality.


=== PS 26046 ===
TITLE: AIIA Clinical Trials Dashboard - a real-time, cloud-based, GCP-compliant Clinical Trial Management System (CTMS) for Ayurveda research, with CDISC/FHIR-interoperable data, role-based KPIs, and integrated ethics, regulatory (CTRI / NDCT Rules 2019) and pharma covigilance tracking.
ORG: Ministry of Ayush | DEPT: All India Institute of Ayurveda
THEME: MedTech / BioTech / HealthTech
DATASET LINK FIELD: Clinical-trial data is sensitive personal data, so development should use synthetic / de-identified datasets; representative standards and public sources:
•Clinical Trials Registry – India (public trial records) — ctri.nic.in
•CDISC standards & controlled terminology (CDASH, SDTM, ADaM, Define-XML) — cdisc.org
•HL7 FHIR R4 specification & ABDM buildi
DESCRIPTION:
Background:
The All India Institute of Ayurveda (AIIA) conducts and coordinates a growing portfolio of clinical research in Ayurveda â€” interventional and observational studies, multi-centre trials â€” and, as the host of the National Pharmacovigilance Coordination Centre (NPvCC) for ASU&H drugs, it also anchors nationwide safety surveillance. This activity is governed by a demanding compliance framework: mandatory prospective registration in the Clinical Trials Registry â€“ India (CTRI); the Good Clinical Practice guidelines for ASU medicine (GCP-ASU) and the ICMR National Ethical Guidelines; the New Drugs and Clinical Trials Rules, 2019 where applicable; Institutional Ethics Committee oversight; and timely Adverse-Event / Serious-Adverse-Event reporting. Yet study status, recruitment, milestones, data quality and safety signals are typically tracked across spreadsheets and disconnected tools, with no single, real-time, auditable view. The result is delayed decisions, missed reporting timelines and avoidable compliance risk â€” precisely as Ayurveda research scales and seeks global scientific credibility.
Description:
The platform is a real-time, cloud-based Clinical Trial Management System (CTMS) and monitoring dashboard that gives AIIA a single, role-based, auditable view of its entire clinical-research portfolio.It tracks each study across its lifecycle â€” protocol and Institutional Ethics Committee approval, CTRI registration, site activation, screening, enrolment and randomization against target, visit and protocol-deviation compliance, data-query and data-quality status, study milestones and timelines, and close-out â€” surfaced as real-time Key Performance Indicators (KPIs) with configurable alerts (for example, enrolment lag, an ethics approval or CTRI update due, or an overdue monitoring visit).Because AIIA hosts the NPvCC, the dashboard integrates pharmacovigilance: it captures and routes Adverse Drug Reaction / Adverse-Event / Serious-Adverse-Event reports against regulatory reporting timelines, coded to standard dictionaries (MedDRA, WHODrug), and feeds aggregate safety signals to the Data Safety Monitoring Board and institutional leadership.Data must follow recognised clinical-research standards â€” CDISC (CDASH for data collection, SDTM for tabulation, ADaM for analysis) and HL7 FHIR R4 for interoperability with Electronic Data Capture (EDC), the hospital information system and Ayushman Bharat Digital Mission (ABDM) building blocks â€” with full ALCOA+ data integrity and an immutable, time-stamped audit trail. Access is strictly role-based (Principal Investigator, study coordinator, monitor, Ethics Committee, pharmacovigilance, administration, and read-only regulator views).The platform must comply with GCP-ASU, the ICMR ethical guidelines, the NDCT Rules 2019 and CTRI requirements, and with the Digital Personal Data Protection Act, 2023 and its 2025 Rules â€” including informed-consent management, data minimisation, encryption, and hosting on compliant, data-resident cloud infrastructure secured to ISO/IEC 27001 and CERT-In norms, since clinical-trial data is sensitive personal data.
Expected solution:
A deployable, cloud-based CTMS-and-analytics dashboard providing: a real-time portfolio view with per-study drill-down; configurable KPIs and alerting; strictly role-based access and an immutable, ALCOA+-compliant audit trail; CDISC-aligned data models and HL7 FHIR R4 / ABDM interoperability with EDC and the hospital information system; an integrated pharmacovigilance module (AE/SAE capture, MedDRA/WHO Drug coding, regulatory-timeline tracking) reflecting AIIAâ€™s NPvCC role; CTRI and ethics/regulatory milestone tracking; informed-consent and privacy controls aligned to the DPDP regime; electronic-signature and data-integrity controls consistent with GCP; and the ability to export submission-ready datasets (SDTM / ADaM, Define-XML). It should present tailored dashboards for Investigators, the Ethics Committee, pharmacovigilance and institutional leadership, and be hosted on secure, data-resident cloud infrastructure (ISO/IEC 27001, CERT-In). The build can be staged â€” a core study-tracking and KPI MVP first, then EDC/FHIR integration and the pharmacovigilance module, then full CDISC submission export and advanced analytics. The system should be evaluable on data accuracy and integrity, timeliness of safety and regulatory reporting, interoperability conformance, and access-control and audit completeness.


=== PS 26047 ===
TITLE: Patient Case-Taking Software
ORG: Ministry of Ayush | DEPT: All India Institute of Ayurveda
THEME: MedTech / BioTech / HealthTech
DATASET LINK FIELD: Additional Information regarding PS
https://drive.google.com/file/d/1mQ6Qp2MKL8JXdL2kJYqV-SFqcfbxSvrd/view?usp=drive_link
DESCRIPTION:
Background:
1.1 The Clinical History-Taking Bottleneck in Indian Hospitals History taking â€” the structured elicitation of a patient's presenting complaints, history of present illness, past medical and surgical history, drug and allergy history, family and personal history, and a review of systems â€” is the single most important diagnostic activity in clinical medicine. Classical teaching holds that a well-conducted history yields the correct diagnosis in 70â€“80% of cases, even before examination or investigation. Yet in India's overburdened public hospital outpatient departments (OPDs), the time available for this critical interaction has collapsed to unsustainable levels.
India operates one of the most patient-dense healthcare systems in the world. Tertiary government hospitals and apex institutions routinely register 4,000â€“10,000 OPD patients per day, with a doctor-to-patient consultation time frequently reported between 2 and 5 minutes â€” among the shortest globally (study published in BMJ Open, 2017, across 67 countries placed India's average primary-care consultation at just over 2 minutes). Within this window, the physician must simultaneously elicit history, examine the patient, review prior records, formulate a diagnosis, counsel, and prescribe. The result is systematic under-elicitation of history, missed comorbidities, repeated questioning across visits, and diagnostic error.
AYUSH institutions face an additional layer of complexity. Ayurvedic history taking (Trividha, Ashtavidha, and Dashavidha Pariksha) requires detailed assessment of Prakriti (constitution), Vikriti (current imbalance), Agni (digestive capacity), Koshtha (bowel nature), Ahara-Vihara (diet and lifestyle), Nidana (causative factors), and Samprapti (pathogenesis) â€” a far more extensive history framework than allopathic intake. Capturing this depth manually within OPD time constraints is effectively impossible, forcing practitioners to abbreviate the very assessment that defines personalized Ayurvedic care.
1.2 The Documentation and Records Fragmentation Problem Compounding the time problem is the fragmentation of patient records. Patients in India typically carry physical paper prescriptions, laboratory reports, discharge summaries, and imaging films from multiple prior providers. During consultation, the physician must manually scan through these unstructured documents â€” often handwritten, in varying languages, and chronologically disordered â€” consuming a significant fraction of the already-scarce consultation time. There is no point-of-entry mechanism to digitize, structure, and chronologically organize a patient's prior medical documents before they reach the consultation room.
The Ayushman Bharat Digital Mission (ABDM) has established the national digital health infrastructure â€” ABHA (Ayushman Bharat Health Account) IDs, the Health Information Exchange, and FHIR-based interoperability standards. However, the 'first-mile' problem remains unsolved: there is no efficient, patient-facing software platform that captures structured history and digitizes documents into the ABDM ecosystem before the clinical encounter begins.
1.3 The Opportunity: AI-Powered Digital Clinical Intake Platform Self-service kiosks have transformed high-throughput service industries â€” ATMs in banking, self-check-in terminals in aviation, and ordering kiosks in quick-service restaurants â€” by offloading structured data-entry tasks from human staff to the user, dramatically improving throughput and accuracy. In healthcare, patient check-in kiosks are now widespread in developed-country hospitals, but these are limited to administrative check-in. None perform deep, AI-driven, multimodal clinical history acquisition with medical document digitization.
The convergence of mature enabling technologies â€” robust automatic speech recognition (ASR) for Indian languages and accents (Bhashini / AI4Bharat models), large language models for conversational clinical history elicitation, high-accuracy OCR for handwritten and printed medical documents, and ABDM's FHIR interoperability â€” now makes it feasible to build an AI-powered clinical history software platform.
Description:
2.1 The Problem in Precise Terms There is no purpose-built, patient-facing software platform that enables patients to independently and comprehensively record their medical history â€” through both natural spoken conversation and guided touchscreen interaction â€” and simultaneously digitize their existing physical medical documents, generating a structured, physician-ready clinical history summary that integrates with the hospital information system and the ABDM ecosystem before the patient enters the consultation room.
2.2 Why Existing Solutions Fall Short
• Existing hospital registration systems (currently deployed in some Indian hospitals) capture only demographic and appointment data â€” name, age, department, token number. They do not elicit any clinical history or process medical documents.
• Mobile health apps and tele-triage chatbots require smartphone literacy, stable connectivity, and patient enrolment ahead of the visit â€” excluding the large elderly, rural, low-literacy, and first-visit patient populations who form the bulk of government hospital OPD load.
• Manual nurse-led triage / history desks are themselves human-resource-limited, do not scale to 5,000+ daily patients, and reintroduce the same time and transcription bottleneck the system is trying to eliminate.
• Generic document scanners digitize images but do not extract, structure, or chronologically organize clinical content, nor link it to a structured history or ABHA record.
2.3 Specific Challenges a Solution Must Overcome
• Multilingual, multi-accent voice capture in noisy hospital environments across Hindi, English, and major regional languages, for patients of varying literacy and digital comfort.
• Accessibility for low-literacy and elderly users through intuitive icon-driven UI, audio prompts, and conversational guidance â€” the software platform must be usable by a first-time, non-tech-savvy patient with zero training.
• Accurate clinical history structuring converting free-form patient narration into a standardized, physician-readable history (chief complaint, HPI, past history, drug/allergy, family, personal, review of systems) â€” and, for AYUSH settings, Dashavidha Pariksha parameters.
• Reliable medical document digitization OCR of handwritten and printed prescriptions, lab reports, and discharge summaries in multiple languages, with intelligent extraction of diagnoses, medications, and investigation values.
• Privacy, consent, and data security compliance with the Digital Personal Data Protection Act 2023 and ABDM consent framework â€” handling sensitive health data within a secure software environment.
Expected solution:
3.1 Solution Overview â€” 'MediKiosk' AI Clinical History Software Platform The proposed solution â€” tentatively designated MediKiosk â€” a software platform for an AI-powered clinical history software platform that allows any patient to record a comprehensive medical history through natural voice conversation and guided touchscreen interaction, scan and digitize their existing physical medical documents, and generate a structured, physician-ready clinical history summary that is pushed to the hospital information system (HIS) and linked to the patient's ABHA record â€” all completed before the consultation, with minimal staff assistance required.
• Insert Table*3.2 3.3 Software & AI Stack (Integrated)
Module A â€” Conversational Multimodal History Engine A conversational AI engine that conducts a structured clinical history interview through both voice and touch. The patient speaks naturally in their preferred language; the engine asks intelligent follow-up questions (e.g., on stating 'chest pain', it probes onset, character, radiation, aggravating/relieving factors â€” the SOCRATES framework) and simultaneously offers touch-based multiple-choice options for patients who prefer tapping. Built on Indian-language ASR, a dialogue manager constrained by a clinical history ontology, and text-to-speech for audio prompts.
• Adaptive questioning: dynamically branches based on chief complaint and prior answers, mirroring a physician's clinical reasoning to elicit a complete HPI and review of systems
• Dual-mode input: every question answerable by speaking OR tapping, ensuring usability across literacy and comfort levels
• AYUSH history mode: for Ayurvedic OPDs, an extended interview capturing Dashavidha Pariksha (Prakriti, Vikriti, Sara, Samhanana, Pramana, Satmya, Sattva, Ahara Shakti, Vyayama Shakti, Vaya) and Ahara-Vihara assessment
• Red-flag detection: AI flags emergency symptoms (e.g., acute chest pain with dyspnoea, stroke symptoms) and triggers immediate priority alert to triage staff rather than routine queueing Module B â€” Medical Document Digitization & Intelligence An integrated scanning and document-AI pipeline that allows the patient to upload prior prescriptions, lab reports, and discharge summaries. The system performs high-accuracy OCR (printed and handwritten, multilingual), then extract and structure clinical entities.
• Intelligent extraction: diagnoses, prescribed medications with dosages, investigation results with values and reference ranges, and procedure/surgery history
• Chronological organization: automatically dates and orders documents into a coherent medical timeline for the physician
• Abnormal-value highlighting: flags out-of-range lab values and potential drug interactions for physician attention Module C â€” Structured History Summary Generator An AI summarization engine that synthesizes the conversational history and the digitized documents into a single, concise, physician-ready clinical summary in standard format â€” presented on the consultation screen the moment the patient enters the room. The physician reads a complete, structured history in seconds rather than spending minutes eliciting it, and can edit/confirm before saving.
• Standard clinical format: Chief complaint ? HPI ? Past medical/surgical ? Drug & allergy ? Family ? Personal ? ROS ? Prior investigations summary
• Editable & verifiable: physician retains full control â€” the summary is a draft to accept, amend, or reject, never an autonomous diagnosis
• Bilingual output: patient-facing audio confirmation in local language; physician-facing summary in English/Hindi Module D â€” Consent, Privacy & ABDM Integration A robust consent and security layer compliant with the Digital Personal Data Protection Act 2023 and the ABDM consent framework. The patient authenticates via ABHA ID, grants explicit consent for data capture and sharing, and the structured history is pushed to the hospital HIS/EMR and linked to the ABHA Personal Health Record via FHIR APIs.
• Secure processing: voice and document AI are processed securely within the software platform
• Session termination: temporary session data is cleared immediately after submission
• Consent-first design: granular, revocable consent with audio explanation for low-literacy patients 3.4 End-to-End Patient Journey
• Step 1 â€” Identify: Patient logs into the software platform, enters/scans ABHA ID or Aadhaar details or registers as new; selects language; grants consent (audio-guided)
• Step 2 â€” Converse: AI conducts adaptive voice + touch history interview, capturing chief complaint, HPI, and full history; red flags trigger priority triage
• Step 3 â€” Scan: Patient uploads prior prescriptions, lab reports, and discharge summaries; AI digitizes, structures, and timelines them
• Step 4 â€” Summarize & Route: AI generates structured history summary, links to ABHA, pushes to HIS, updates the patient's digital record; summary appears on physician's screen at consultation
• Step 5 â€” Consult: Physician reviews complete history in seconds, edits/confirms, and devotes the full consultation to examination, reasoning, and counselling


=== PS 26060 ===
TITLE: Digital Platform for efficient remote management of Indian Antarctic Research Stations
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Polar andOcean Research (NCPOR)
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
Develop a Digital Twin framework for Maitri and Bharati stations integrating infrastructure, energy, logistics and environmental monitoring for efficient remote management.


=== PS 26061 ===
TITLE: AI-Driven Smart Energy Management System for Polar Research Stations
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Polar andOcean Research (NCPOR)
THEME: Clean & Green Technology
DATASET LINK FIELD: (empty)
DESCRIPTION:
Develop an intelligent energy-management system using AI for load forecasting, renewable energy integration and fuel optimization under extreme polar conditions.


=== PS 26062 ===
TITLE: Integrated Polar Expedition Logistics and Asset Management System
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Polar andOcean Research (NCPOR)
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
Develop a centralized digital platform for expedition planning, cargo tracking, inventory management, personnel movement and emergency response.


=== PS 26063 ===
TITLE: Integrated Polar Science Outreach, Knowledge Repository and Media Dissemination Portal
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Polar andOcean Research (NCPOR)
THEME: Smart Education
DATASET LINK FIELD: (empty)
DESCRIPTION:
Develop a comprehensive outreach portal that archives expedition reports, scientific datasets, publications, photographs, videos and institutional activities while generating content for websites and social media.


=== PS 26067 ===
TITLE: Develop a web-based interactive 3D visualization platform that integrates numerical ocean model outputs and in-situ observations.
ORG: Ministry of Earth Sciences (MoES) | DEPT: Indian National Centre for Ocean Information Services (INCOIS) Ocean Valley
THEME: Disaster Management
DATASET LINK FIELD: Additional Information regarding PS
https://drive.google.com/file/d/1p3mwUVPs2mmv91qW-bQMaahQnGpkL4nr/view?usp=drive_link
DESCRIPTION:
• Background India's vast Exclusive Economic Zone (EEZ) and coastline demand continuous, high-resolution monitoring of ocean state variables. INCOIS routinely generates and archives large volumes of ocean model outputs - including three-dimensional fields of temperature, salinity, current vectors,chlorophyll, etc. - as well as real-time and delayed-mode observations from autonomous instruments such as Argo profiling floats and underwater Gliders. These datasets are stored in NetCDF and ASCII/text formats and span multiple depth levels, spatial grids, and time steps.Despite the richness of this data, no integrated, web-based 3D visualization platform currently exists that can simultaneously render model fields and in-situ instrument observations in a single interactive environment. Existing tools are either desktop-bound, support only 2D plan views, or lack the ability to co-visualize model outputs alongside instrument profiles. Operational oceanographers and forecasters are therefore forced to toggle between disparate software packages,making it difficult to rapidly correlate model predictions with observational evidence.
Key gaps identified include:
? No web-based, platform-independent 3D rendering of ocean model data (temperature,salinity, currents, etc.) with depth-resolved volumetric views.
? No unified display of Argo float and Glider profile data (latitude, longitude, depth, time,temperature, salinity, chlorophyll) alongside model fields.
? Absence of interactive controls for variable selection, depth-slice navigation, time-step animation, and customizable colorbars.
? Inability to ingest new observational data streams or additional model variables without significant re-engineering.
? Lack of tools to support intuitive, rapid understanding of complex 3D ocean phenomena for operational decision-making.The absence of such a system impedes timely hazard assessment, search-and-rescue support,fishery advisories, climate monitoring, etc. - all operational mandates of INCOIS.
? Expected Solution The proposed solution is a web-based, browser-native 3D Ocean Data Visualization System that integrates ocean model outputs with observational data on a single interactive platform.
Core functional requirements:
? 3D Volumetric Rendering: Interactive visualization of ocean model fields (temperature,salinity, current vectors) across the full water column, with support for depth-slice views,isosurface extraction, and time-step animation using WebGL / Three.js or Cesium.js.
? Instrument Data Overlay: Co-display of Argo float, Glider profile, CTD and BGC data using geospatially accurate markers; users can click a float/glider to inspect a depth-vs-variable profile chart with timestamps.
? Multi-format Data Ingestion: Automated parsers for NetCDF (via PyNIO / xarray backend)and delimited text formats, with a modular architecture that allows new variables or data sources to be added with minimal code change.
? Customizable Colorbar & Variable Controls: Dynamic colorbar editor (color palette, min/max range, log/linear scale), variable selector, layer opacity controls, and vertical exaggeration slider for intuitive depth perception.
? Web-based, Scalable Architecture: Frontend built on modern JavaScript frameworks with a lightweight REST/OPeNDAP API backend, enabling Deployable on INCOIS infrastructure without any client-side dependencies.
? Extensible Design: Plugin-style module for future integration of additional sensors (e.g.,CTDs, moorings, HF-radar, Acoustic doppler current profiler (ADCP), etc.), new ocean model variables, and machine-learning derived products.
The system will follow open standards (OGC WMS/WCS, CF Conventions for NetCDF), enabling interoperability with national and international ocean data portals. The end product will empower INCOIS forecasters to perform rapid, intuitive analysis of complex 3D ocean phenomena -significantly improving the speed and accuracy of operational advisories, in the same way that 3D meteorological visualization has transformed weather forecasting workflows.Public Outreach & Science Communication: Beyond operational use, the platform will serve as a powerful science communication tool. Complex numerical ocean model outputs - which are typically inaccessible to non-specialists - can be transformed into visually intuitive, interactive 3D experiences. This makes the tool valuable for educating school and college students about ocean dynamics, engaging the general public during awareness campaigns, and supporting policymakers in understanding marine environmental conditions. INCOIS can use the platform for outreach events, exhibitions, and e-learning initiatives, bridging the gap between cutting-edge ocean science and the common person.
Insert 2 tables(Acronyms and Dataset Link) here-


=== PS 26068 ===
TITLE: WeatherGPT: Conversational AI for Weather Forecasting, Alerts, and Climate Information
ORG: Ministry of Earth Sciences (MoES) | DEPT: India Meteorological Department
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Background Weather information is often distributed through multiple portals, bulletins, satellite products, and forecast systems, making it difficult for common users, researchers, disaster managers, and government agencies to quickly obtain actionable insights.
There is a need for an intelligent conversational platform that can provide real-time weather information, forecasts, warnings, climate analysis, and decision support in natural language.
• Objective Develop an AI-powered chatbot platform named WeatherGPT that integrates meteorological datasets, forecasting models, and disaster warning systems to provide accurate, contextual, and multilingual weather intelligence through conversational interfaces.
• Key Features 1. Real-time weather information retrieval.
2. Natural language querying for weather forecasts.
3. Integration with numerical weather prediction (NWP) models such as GFS/WRF.
4. Extreme weather alerts and early warning dissemination.
5. Location-based forecasting and advisory generation.
6. Multilingual support for Indian languages.
7. Climate trend and historical weather analysis.
8. Voice-enabled interaction for rural accessibility.
• Expected Solution Participants should develop:
• A mobile-based conversational AI platform.
• Backend integration with meteorological databases, website and APIs.
• AI/LLM-based query understanding engine.
• Scalable architecture supporting real-time data ingestion.
• Suggested Technology Stack
• Python / FastAPI / Node.js
• MQTT / WIS2.0 / WebSocket
• LLMs (OpenAI, Llama, Gemini, etc.)
• GIS tools and weather APIs
• PostgreSQL / MongoDB
• Docker / Kubernetes
• Expected Outcomes
• Faster dissemination of weather information.
• Improved public accessibility to forecasts.
• Better disaster preparedness and response.
• Intelligent weather decision-support system for agriculture, aviation, marine, and urban planning.
• Possible Use Cases
• Farmers seeking crop-weather advisories.
• Aviation weather briefing.
• Flood/cyclone warning dissemination.
• Smart city weather monitoring.
• Climate analytics for researchers.
• Evaluation Parameters
• Accuracy and relevance.
• Response latency.
• Multilingual capability.
• User interface and accessibility.
• Scalability and innovation.
• Integration with real-time meteorological systems.
• Voice-enabled interaction for rural accessibility


=== PS 26069 ===
TITLE: National Weather Big Data Analytics Platform
ORG: Ministry of Earth Sciences (MoES) | DEPT: India Meteorological Department
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
Design and develop a scalable National Weather Big Data Analytics Platform capable of collecting and processing real-time weather-related information for India from multiple internet-based sources including social media platforms, public datasets, websites, APIs, and citizen reports. The platform should automatically collect weather related posts and information tagged with #IMD and other relevant weather hashtags, along with metadata such as date & time, city, state, GPS location, photos, videos, and event category, and store the information in a centralized database.
The system should leverage big data technologies and open-source tools to support large-scale real-time data ingestion, processing, storage, and visualization.
Participants are encouraged to use machine learning and AI-based techniques to identify fake or misleading reports, verify untrusted sources, remove duplicate entries, and automatically categorize weather events such as rainfall, thunderstorms, flooding, heatwaves, fog, dust storms, and strong winds.
Develop a web-based dashboard and Admin Panel for monitoring and analysing collected data with features including:
• Date-wise filtering
• Event-wise filtering
• Location-wise filtering
• Verification status tracking
• Real-time visualization and analytics


=== PS 26070 ===
TITLE: To develop an Artificial Intelligence (AI) / Machine Learning (ML) based system for identification, classification, and prediction of different tropical cyclone patterns using multi-source satellite data.
ORG: Ministry of Earth Sciences (MoES) | DEPT: India Meteorological Department
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
To develop an Artificial Intelligence (AI) / Machine Learning (ML) based system for identification, classification, and prediction of different tropical cyclone patterns using multi-source satellite data.


=== PS 26071 ===
TITLE: AI/ML-Based Integrated heavy rainfall Early Warning and Inundation Prediction System using Satellite, Radar, observational Weather and numerical weather prediction model data.
ORG: Ministry of Earth Sciences (MoES) | DEPT: India Meteorological Department
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
AI/ML-Based Integrated heavy rainfall Early Warning and Inundation Prediction System using Satellite, Radar, observational Weather and numerical weather prediction model data.


=== PS 26072 ===
TITLE: AIML based Nowcasting of thunderstorm and lightning using atmospheric observation including multiple radars, satellite, lightning and model data.
ORG: Ministry of Earth Sciences (MoES) | DEPT: India Meteorological Department
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
AIML based Nowcasting of thunderstorm and lightning using atmospheric observation including multiple radars, satellite, lightning and model data.


=== PS 26075 ===
TITLE: Participants are invited to design and develop **CAPACITY CONNECT A Digital Capacity Building and Learning Management Portal** to support organizational training, competency development, and knowledge sharing through a centralized web-based platform.
ORG: Ministry of Earth Sciences (MoES) | DEPT: India Meteorological Department
THEME: Smart Education
DATASET LINK FIELD: (empty)
DESCRIPTION:
The solution should include secure signup and login functionality with three user roles: Trainee, Trainer, and Admin. Trainees should be able to create professional profiles with qualifications, work experience, interests, skills, and certificates, enroll in courses, access learning resources, attempt subject-wise MCQ assessments, and provide feedback on courses and training content.Trainers should be able to manage their profiles, create questionnaires with deadlines, monitor trainee participation and performance, and upload recorded lectures, presentations, and study materials in a trainer library accessible to trainees.The Admin module should provide user approval and role management features along with dashboards for monitoring courses, enrollments, certifications,assessments, and participation statistics. Admins should also be able to publish notifications, announcements, achievements, and newly added learning content on the homepage.The platform should support competency mapping for identifying suitable trainers for various subjects and should be scalable, secure, user-friendly, and accessible across devices to promote efficient learning and organizational capacity building.


=== PS 26076 ===
TITLE: Development of personalized homepage for 'Mausam' mobile application:
ORG: Ministry of Earth Sciences (MoES) | DEPT: India Meteorological Department
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Health-conscious users Highlight Air Quality Index (AQI), pollen count, UV index, and humidity levels to help users manage allergies, asthma, or skin sensitivity.
• Outdoor fitness enthusiasts Show sunrise/sunset times, 'best running hours,' wind speed, and heat alerts to optimize workout planning.
• Beachgoers & surfers Display sea conditions, tide timings, wave height, and water temperature for safe and enjoyable beach activities.
• Travelers Provide quick access to saved destinations, severe weather alerts for flights, and packing suggestions (e.g., 'Carry a raincoat in London').
• Parents & families Emphasize school commute conditions, rain alerts, and severe weather warnings to plan daily routines.
• Agriculture & gardeners Show soil moisture, rainfall predictions, frost alerts, and seasonal planting guidance.
• Commuters Integrate weather with traffic updates, visibility conditions, and alerts for storms or fog that affect travel.
• Event planners Offer extended forecasts, probability of rain, and 'comfort index' for outdoor gatherings or weddings.


=== PS 26077 ===
TITLE: AI-Driven Hyper-Local Early Warning System for Severe Weather Nowcasting
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Medium Range Weather Forecasting (NCMRWF)
THEME: Disaster Management
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Problem Statement India is highly vulnerable to rapidly intensifying, localized extreme weather events such as cloudbursts, severe thunderstorms, and flash floods. Traditional physics-based Numerical Weather Prediction (NWP) models often suffer from computational latency and struggle to capture the rapid, small-scale atmospheric changes that preceded these events. There is a critical need for a real-time, hyper-local early warning system capable of 'nowcasting' severe weather 2 to 6 hours before impact, providing actionable lead time for disaster management.
• Proposed Solution We propose an advanced AI predictive engine designed for high-precision severe-weather nowcasting. Specifically, the system simultaneously predicts the onset of highly localized, rapidly intensifying events, namely severe thunderstorms, cloudbursts, and the subsequent flash floods,with an actionable lead time of 2 to 6 hours. Instead of relying on computationally intensive thermodynamic simulations, the system utilizes a spatiotemporal deep learning architecture to recognize the complex, multivariate atmospheric signatures that precede these extreme events. A critical component of this methodology is storm nowcasting using variations in integrated water vapor (IWV). By tracking rapid spatial and temporal accumulations of IWV, the model accurately identifies the concentrated moisture pools required for heavy precipitation. To predict multiple extreme events simultaneously, the engine employs a multi-task learning approach. A shared neural network backbone extracts foundational atmospheric features (moisture, instability, and lift) from the input grids. The network then branches into distinct output layers, allowing a single unified model to generate hyper-local probability risk maps for thunderstorms, cloudbursts, and flash floods simultaneously, entirely bypassing the computational latency typical of traditional numerical weather prediction (NWP) models.
Predictive Matrix: Key Atmospheric Variables Severe convective storms require three primary ingredients: moisture, instability, and lift. Our AI model tracks the critical precursors across all three categories to ensure high accuracy and low false-alarm rates:
? Moisture Availability (The Fuel): The cornerstone of our storm nowcasting is the capture of integrated water vapor (IWV) variations. By tracking rapid spatial and temporal accumulations of IWV from satellites, the model identifies the concentrated moisture pools that trigger localized cloudbursts.
? Atmospheric Instability (The Energy): The model assesses the atmosphere's thermal profile to determine if it is buoyant enough to support explosive vertical cloud growth. High Convective Available Potential Energy (CAPE) paired with eroding Convective Inhibition (CIN) serves as a prime indicator of impending severe thunderstorms.
Kinematics and Lift (The Trigger & Structure): Low-level convergence (wind vectors colliding at the surface) forces air upward, initiating the development of a storm cell.
Furthermore, tracking vertical wind shear (changes in wind speed/direction with altitude) helps the model predict whether a storm will move quickly or remain stationary.
Observational Signatures: Rapid cooling of cloud tops, measured as the Cloud Top Temperature(CTT) Drop Rate, provides real-time validation of explosive vertical updrafts within the system.
Topographic Dynamics (The Flood Catalyst): To accurately predict flash floods, the AI overlays the atmospheric probability maps onto a high-resolution Digital Elevation Model (DEM). This allows the system to calculate how terrain slope, elevation, and natural drainage basins will channel the extreme precipitation generated by a predicted cloudburst.To capture these predictors with hyper-local accuracy, the model fuses multi-modal, high resolution datasets:
IMDAA Reanalysis Data (Historical Baseline & Thermodynamics): Multi-level air temperature, specific humidity profiles (for calculating CAPE/CIN), geopotential height, and U/V wind components (for calculating shear and convergence).
Satellite Observations (INSAT-3D/3DR via MOSDAC): Water Vapor (WV) Channels. This is essential for deriving real-time Integrated Water Vapor (IWV) fluctuations necessary for our storm nowcasting.
Thermal Infrared (TIR) Channels: Utilized to calculate the rapid Cloud Top Temperature (CTT) drop rate.
Quantitative Precipitation Estimation (QPE): Satellite-derived precipitation estimates are used to monitor real-time rainfall intensity, serving as a reliable, openly accessible alternative to ground-based radar.
Digital Elevation Model (DEM): High-resolution topographical data (such as ISRO's CartoDEM or SRTM) provides a static baseline of elevation, slope, and surface drainage networks, enabling translation of atmospheric cloudburst predictions into actionable flash flood warnings on the ground.
• Technical Methodology ? Data Fusion & Alignment: Raw data from IMDAA reanalysis, INSAT-3D/3DR satellite observations, and high-resolution Digital Elevation Models (DEM) are ingested, normalized, and mapped onto a unified spatiotemporal grid (e.g., using multi-dimensional array structures). This ensures that all dynamic atmospheric predictorsâ€”such as specific humidity and cloud-top temperaturesâ€”and static surface variables align geographically and chronologically for seamless multimodal processing.
? Multi-Variate Feature Extraction & Multi-Task Inference: A shared multi-modal spatiotemporal transformer network continuously analyzes real-time satellite grids, specifically tracking critical IWV variations and CTT drop rates, against the IMDAA-derived thermodynamic baselines using cross-attention mechanisms. Utilizing a Multi-Task Learning (MTL) architecture,the network branches into distinct output 'heads.' This allows the unified model to simultaneously process the aligned data and generate distinct, hyper-local probability maps for severe thunderstorms, cloudbursts, and flash floods without computational bottlenecking.
? Automated Alerting: When the predictive matrix breaches the signature thresholds of a severe event, the engine generates a spatial risk map and pushes automated, categorized alerts via a lightweight API.
• Expected Solution The final deliverable for the Smart India Hackathon will be a fully functional, real-time prototypeof the AI-Driven Hyper-Local Early Warning System. At its core is a deployed multi-task inference engine that continuously ingests live INSAT satellite data and IMDAA thermodynamic baselines to simultaneously generate predictive risk maps for severe thunderstorms, cloudbursts, and flash floods within a 2 to 6-hour predictive window. This backend integrates with an interactive, webbased spatial dashboard designed for disaster management authorities, featuring dynamic risk maps overlaid on a Digital Elevation Model (DEM) and an Explainable AI (XAI) module that transparently displays meteorological triggers. Finally, an automated API will translate these predictive insights into immediate, categorized alerts sent directly to first responders and vulnerable communities the moment critical thresholds are breached.


=== PS 26078 ===
TITLE: AI-Driven Spatio-Temporal Tracking of Extreme Weather Anomalies in Medium-Range Forecasts
ORG: Ministry of Earth Sciences (MoES) | DEPT: National Centre for Medium Range Weather Forecasting (NCMRWF)
THEME: Smart Automation
DATASET LINK FIELD: (empty)
DESCRIPTION:
• Problem Statement Identifying and tracking the exact geographic footprints of extreme weather anomalies (such as severe cyclones, heat domes, or cold waves) within massive global Numerical Weather Prediction (NWP) outputs is computationally intensive and heavily reliant on manual interpretation. In medium-range forecasting (3 to 10 days), atmospheric chaos renders traditional deterministic models highly uncertain.
Furthermore, standard deep learning models (like standard CNNs or U-Nets) suffer from spectral smoothingâ€”they tend to 'average out' spatial data, which destroys the extreme amplitudes (the high-intensity peaks of rainfall or wind speed) that forecasters actually need to track. There is a critical gap between broad, coarse 12 km global ensemble datasets and localized, high-fidelity threat tracking.
• Proposed Solution We propose an automated, state-of-the-art AI tracking and downscaling pipeline that shifts the paradigm from manual weather data sorting to automated, physics-informed anomaly tracking.Instead of relying on a single deterministic forecast run, our system directly processes multivariable, 4D Ensemble Prediction Systems (EPS) data.The system uses a two-stage hybrid AI architecture to solve the spectral smoothing problem:First, it utilizes a graph neural network (GNN) to map atmospheric variables onto a spherical mesh,instantly isolating moving anomalies and calculating their trajectory over a 3- to 10-day forecast window.
Second, it pipes this isolated region into a generative diffusion model to perform statistical downscaling. This physics-constrained generative model mathematically derives a hyper-local 5km subgrid impact zone without flattening or blurring the severe amplitudes of the extreme weather event.
• Technical Methodology & Architecture Spherical Anomaly Tracking (Stage 1 GNN): To eliminate the geographic distortions caused by processing the spherical Earth on flat 2D pixel grids, the system maps the 12 km NCMRWF Global Ensemble (NEPS-G) grids directly onto an icosahedral mesh. The message-passing GNN calculates the Extreme Forecast Index (EFI) against a 30-year historical ERA5 baseline distribution to isolate standard deviations and draw a macro-scale temporal bounding box around the anomaly's trajectory.
Amplitude-Preserving Downscaling (Stage 2 Diffusion): The system passes the cropped, macroscale bounding box into a conditional denoising diffusion probabilistic model. Rather than optimizing for mean errors (which blurs peaks), the diffusion model learns the physical relationships between synoptic-scale features and regional topography. It iteratively generates high-resolution, high-amplitude local weather scenarios, downscaling the 12 km grid into a 5 km grid.
Physics-Informed Constraints: To ensure the model remains scientifically accurate, we embed fluid dynamics and thermodynamic conservation laws directly into the neural network's loss function. The model is mathematically penalized if it generates physically impossible weather states (e.g., severe downpours missing corresponding moisture convergence vectors).
• Datasets and Tools ? AI Frameworks: PyTorch / JAX (engineered with custom, physics-guided loss functions),Deep Graph Library (DGL) for icosahedral mesh networks, and Hugging Face Diffusers for generative downscaling.
? Data Wrangling & Geospatial Tools: Xarray and Dask for processing parallelized, multigigabyte 4D NetCDF/GRIB2 arrays; MetPy for physical meteorological equations;
Cartopy for geographical map projections.
? Training & Testing Datasets:
? Baseline: Historical IMDAA / ERA5 reanalysis data to establish the climatological norm.
? Forecast Inputs: Historical NCUM (12 km deterministic) and NEPS-G (12 km global ensemble) datasets containing documented extreme historical events (e.g., Cyclone Amphan, severe North India heatwaves).
• Expected Outcome & Key Deliverables The Tracking Core: A production-ready Spatio-Temporal GNN module that continuously processes global NWP streams to output dynamic, automated 4D bounding boxes around evolving weather threats.
The Downscaling Core: A generative diffusion module capable of ingesting a 12 km resolution anomaly slice and outputting a probabilistically sound, 5 km resolution sub-grid array that retains extreme value amplitudes.
The Visualization & Alert Dashboard: An automated system that translates the mathematical 5 km centroid arrays into clean, geographic visual layers.
The Alerting API: A lightweight, production-ready REST API that programmatically drops a pinpoint coordinate at the core of the severe anomaly and triggers categorized spatial alerts (low, moderate, and severe) across a precise 5 km geographical impact radius.
• Use Cases & Societal Impact Eliminating Alert Fatigue for the NDRF: Current weather alerts are often too broad, covering entire states or districts, which leads to public complacency. This solution allows meteorologists to issue hyper-localized, highly targeted warnings. It changes a generic'heavy rain in the district' alert into a precise 'high risk of flash flooding within your specific 5 km radius in the next 12 hours' alert, empowering first responders to deploy assets perfectly.
Protecting Rural Economies: Grants farming communities a highly accurate, 3- to 10- day lead time regarding localized catastrophic anomalies like sudden frost, hail, or heat domes. This structural foresight lets farmers alter harvesting schedules or apply cropprotection covers, shielding rural livelihoods from sudden climate shocks.
Democratizing Supercomputing Power: Once this hybrid AI pipeline is trained, it processes live inference data on a standard cloud GPU node in seconds, making high-fidelity climate forecasting highly affordable and easily accessible.


