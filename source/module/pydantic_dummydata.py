from datetime import datetime, date

from module.pydantic_model import (
	Metadata,
	Demographics,
	Social,
	Stimulantia,
	FunctionStatus,	
	Comorbidity,
	PrimaryDiagnosis,
	Staging,
	Metastasis,
	Histology,
	Genetics,
	PreviousCancer,
	PreviousCancerItem,
	TreatmentSummary,
	TreatmentRadiotherapy,
	TreatmentSurgery,
	TreatmentSystemic,
	BiologicalSample,
	Biomarker,
	CTCAE,
	VitalStatus,
	TumorEvent,
	Consent,
	ClinicalStudy,
	Course
)

def get_course():
	metadata_data = Metadata(
		xml_timestamp=datetime.now()
	)

	demographics_data = Demographics(
		rt_center="Haukeland universitetssykehus",
		referring_hf="Voss sjukehus",
		birth_year=1956,
		sex="mann",
		weight_at_diagnosis_kg=76,
		height_cm=175,
		patient_id_fnr="01015625103"
	)

	social_data = Social(
		education_level="Videregående",
		martial_status="Skilt",
		living_arrangements="Ikke i parforhold"
	)
	
	stimulantia_data = Stimulantia(
		smoking_status="Aldri røykt",
		pack_years=0,
		month_since_stopping=None,
		non_smoking_tobacco_status="Aldri brukt",
		alcohol_abuse="TIdligere bruker"
	)

	function_status_data = FunctionStatus(
		ecog_grade=3,
		ecog_date=date(2014, 3, 12)
	)

	comorbidity_data = [
		Comorbidity(
			comorbidity_code="S86.9",
			comorbidity_term="Skade på uspesifisert muskel eller sene i legg",
			comorbidity_name="S86.9 Skade på uspesifisert muskel eller sene i legg",
			comorbidity_edition="ICD10",
			comorbidity_date=date(2018, 2, 20)
		),
		Comorbidity(
			comorbidity_category = "Sykdommer i muskel-skjelettsystemet og bindevev",
			comorbidity_date=date(2020, 4, 21)
		)
	]

	primary_diagnosis_data = PrimaryDiagnosis(
		diagnosis_code="C78.4",
		diagnosis_term="Metastase i tynntarm",
		diagnosis_name="C78.4 Metastase i tynntarm",
		diagnosis_edition="ICD10",
		diagnosis_localisation="Proksimalt",
		diagnosis_date=date(2023, 10, 2),
		multiple_primaries=True,
		diagnosis_method="Histologisk"
	)

	staging_data = [
		Staging(
			tnm_t="T4a",
			tnm_n="N0",
			tnm_m="M0",
			tnm_type="C",
			tnm_string="cT4a cN0 cM0",
			tnm_edition="AJCC 8",
			is_relapse=False,
			staging_date=date(2024, 6, 10)
		),
		Staging(
			tnm_t="T4a",
			tnm_n="N1",
			tnm_m="M0",
			tnm_string="pT4a pN1 pM0",
			tnm_type="P",
			tnm_edition="AJCC 8",
			is_relapse=False,
			staging_date=date(2024, 7, 10)
		)
	]

	metastasis_data = Metastasis(
		metastasis_diagnosed=True,
		metastasis_localisation="Upper GI"
	)

	histology_data = [
		Histology(
			histological_celltype_code="M74204",
			histological_celltype_description="mikroglandulær adenose",
			topographical_mapping_code="T51140",
			topographical_mapping_description="ganeslimhinne"
		),
		Histology(
			histological_celltype_code="M76120",
			histological_celltype_description="Dupuytrens kontraktur",
			topographical_mapping_code="T54920",
			topographical_mapping_description="gingiva i overkjeve"
		)
	]

	genetics_data = [
		Genetics(
			amino_acid_changes="SLC25A44"
		),
		Genetics(
			amino_acid_changes="ALDH4A1"
		),
		Genetics(
			amino_acid_changes="5,10-meTHF"
		)
	]

	previous_cancer_data = PreviousCancer(
		is_previous_cancer=True,
		previous_cancer=[
			PreviousCancerItem(
				previous_cancer_icd10_code="C71.7",
				previous_cancer_icd10_description="Ondartet svulst i hjernestamme",
				previous_cancer_diagnosis_year=1977,
				previous_cancer_rt_given=True
			),
			PreviousCancerItem(
				previous_cancer_icd10_code="C77.50",
				previous_cancer_icd10_description="Mikrometastase i lymfeknute i bekken",
				previous_cancer_diagnosis_year=1989,
				previous_cancer_rt_given=False
			)
		]
	)

	treatment_summary_data = [
		TreatmentSummary(
			treatment_intention="Ikke kurativt (lokalkontroll)",
			treatment_type="Konkomitant",
			treatment_radiotherapy=TreatmentRadiotherapy(
				course_id="123456",
				procedure_nkpk_code="WEOA00",
				procedure_nkpk_description="Ekstern stråleterapi, høyenergetisk (MV)"
			)
		),
		TreatmentSummary(
			treatment_intention="Kurativt",
			treatment_type="Konkomitant",
			treatment_surgery=TreatmentSurgery(
				surgery_target="Primærtumor",
				surgery_date=date(2023,7,24),
				procedure_nkpk_code="CBD11",
				procedure_nkpk_description="Åpning av lapp etter rekonstruksjon av øyelokk"
			)
		),
		TreatmentSummary(
			treatment_intention="Kurativt",
			treatment_type="Adjuvant",
			treatment_systemic=TreatmentSystemic(
				systemic_name="vorasidenib",
				category="Immunterapi",
				therapeutic_intent="Preoperativt",
				total_dosage_value=12,
				total_dosage_unit="l",
				dosage_start_date=date(2023,4,10),
				dosage_stop_date=date(2023,4,20),
			)
		)
	]

	biological_sample_data = [
		BiologicalSample(
			requisition_remissenr="12654f2",
			sample_laboratory="Haukeland universitetssykehus",
			conclusion="Ingen bukspyttkjertel funnet",
			sample_date=date(2010,1,1),
			sample_type="Vev",
			sample_anatomical_location="Bukspyttkjertel",
		),
		BiologicalSample(
			requisition_remissenr="5234536",
			sample_laboratory="Oslo universitetssykehus, Aker",
			sample_date=date(2024,1,1),
			conclusion="Positive prøver",
			sample_type="Celler (cytologi)",
			sample_anatomical_location="Bukspyttkjertel",
			sample_tumorcells_percentage=57.8
		)
	]

	biomarker_data = [
		Biomarker(
			biomarker_name="PSA",
			biomarker_value=127
		),
		Biomarker(
			biomarker_name="P16",
			biomarker_result="Positiv"
		),
		Biomarker(
			biomarker_name="ENE mikroskopisk",
			biomarker_result="Positiv",
			biomarker_value=75,
			biomarker_unit="ml/mg"
		),
		Biomarker(
			biomarker_name="Invasjonsdyp",
			biomarker_method="Målt invasjonsdyp",
			biomarker_value=2,
			biomarker_unit="mm"
		)
	]

	ctcae_data = [
		CTCAE(
			ctcae_date=date(2020,12,1),
			meddra_name="Atrial fibrillation",
			ctcae_grade=3,
			ctcae_terminology_version="5",
			meddra_terminology_version="27.1"
		),
		CTCAE(
			ctcae_date=date(2024,12,1),
			meddra_name="Retinal detachment",
			ctcae_grade=5,
			ctcae_terminology_version="5",
			meddra_terminology_version="27.1"
		),
		CTCAE(
			ctcae_date=date(2024,12,1),
			meddra_category="Endocrine disorders",
			ctcae_grade=2,
			ctcae_terminology_version="4",
			meddra_terminology_version="27.1"
		),
	]

	vital_status_data = VitalStatus(
		last_followup=date(2023,1,5)
	)

	tumor_event_data = [
		TumorEvent(
			progression_date=date(2022,4,6),
			progression_type="Residiv",
			progression_identification="Klinikk",
			progression_grade="Fjernmetastase",
		),
		TumorEvent(
			progression_date=date(2023,2,6),
			progression_type="Progresjon",
			progression_identification="Histologi",
			progression_grade="Regional progresjon"		
		),
	]

	consent_data = Consent(
		informed_patient_about_broad_consent=False,
		informed_patient_about_rt_registry=True
	)

	clinical_studies_data = [
		ClinicalStudy(
			study_name="Dahanca30 (hode-halskreft)",
			study_contact_person="testlege 1",
		),
		ClinicalStudy(
			study_name="STDHOD9 PET/CT-veiledet strålebehandling ved hode-halskreft",
			study_contact_person="testlege 2",
		)
	]

	course_data = Course(
		metadata=metadata_data,
		demographics=demographics_data,
		social=social_data,
		stimulantia=stimulantia_data,
		function_status=function_status_data,
		comorbidity=comorbidity_data,
		primary_diagnosis=primary_diagnosis_data,
		staging=staging_data,
		metastasis=metastasis_data,
		histology=histology_data,
		genetics=genetics_data,
		previous_cancer=previous_cancer_data,
		treatment_summary=treatment_summary_data,
		biological_sample=biological_sample_data,
		biomarker=biomarker_data,
		ctcae=ctcae_data,
		vital_status=vital_status_data,
		tumor_event=tumor_event_data,
		consent=consent_data,
		clinical_studies=clinical_studies_data

	)

	return course_data