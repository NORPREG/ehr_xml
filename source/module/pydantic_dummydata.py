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
		alcohol_abuse="Aldri drukket"
	)

	function_status_data = FunctionStatus(
		ecog_grade=3,
		ecog_date=date(2014, 3, 12)
	)

	comorbidity_data = [
		Comorbidity(
			comorbidity_icd10_code = "S86.9",
			comorbidity_icd10_description="Skade på uspesifisert muskel eller sene i legg",
			comorbidity_date=date(2018, 2, 20)
		),
		Comorbidity(
			comorbidity_category = "Sykdommer i muskel-skjelettsystemet og bindevev",
			comorbidity_date=date(2020, 4, 21)
		)
	]

	primary_diagnosis_data = PrimaryDiagnosis(
		diagnosis_icd10_code="C78.4",
		diagnosis_icd10_description="Metastase i tynntarm",
		diagnosis_localisation="Proksimalt",
		diagnosis_date=date(2023, 10, 2),
		diagnosis_method="Histologisk"
	)

	staging_data = [
		Staging(
			tnm_t="T4a",
			tnm_n="N0",
			tnm_m="M0",
			tnm_type="Clinical",
			tnm_version="AJCC 8",
			is_relapse=False,
			staging_date=date(2024, 6, 10)
		),
		Staging(
			tnm_t="T4a",
			tnm_n="N1",
			tnm_m="M0",
			tnm_type="Pathological",
			tnm_version="AJCC 8",
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

	)

	return course_data