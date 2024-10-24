from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import date, datetime

class Metadata(BaseModel):
	xml_timestamp: datetime
	version_major: int = 0
	version_minor: int = 1

class Demographics(BaseModel):
	rt_center: str
	referring_hf: str
	birth_year: int
	sex: Literal["mann", "kvinne"]
	weight_at_diagnosis_kg: float
	height_cm: float
	patient_id_fnr: str

class Social(BaseModel):
	education_level: Literal[
		"Ingen utdanning",
		"Grunnskole",
		"Videregående",
		"Universitet / høyskole < 4 år",
		"Universitet / høyskole >= 4 år",
		"Ukjent"
	]

	martial_status: Literal[
		"Ugift",
		"Gift / Registrert partner",
		"Enke / enkemann / gjenlevende partner",
		"Skilt",
		"Separert",
		"Ukjent"
	]

	living_arrangements: Literal[
		"Ikke i parforhold",
		"Samboer/lever i parforhold",
		"Parforhold, lever ikke sammen / særbo",
		"Ukjent"
	]

class Stimulantia(BaseModel):
	smoking_status: Literal[
		"Aldri røykt",
		"Røyker",
		"Tidligere røyker"
	]

	pack_years: int
	month_since_stopping: Optional[int] = None
	non_smoking_tobacco_status: Literal[
		"Aldri brukt",
		"Nåværende bruker",
		"Tidligere bruker"
	]
	
	alcohol_abuse: Literal[
		"Drikker",
		"Drukket tidligere",
		"Aldri drukket"
	]

class FunctionStatus(BaseModel):
	ecog_grade: Literal[0,1,2,3,4,5]
	ecog_date: date

class Comorbidity(BaseModel):
	comorbidity_icd10_code: Optional[str] = None
	comorbidity_icd10_description: Optional[str] = None
	comorbidity_category: Optional[str] = None
	comorbidity_comment: Optional[str] = None
	comorbidity_date: date

class PrimaryDiagnosis(BaseModel):
	diagnosis_icd10_code: str
	diagnosis_icd10_description: str
	diagnosis_laterality: Optional[str] = None
	diagnosis_localisation: Optional[str] = None
	diagnosis_date: date
	diagnosis_method: str
	diagnosis_comment: Optional[str] = None


class Staging(BaseModel):
	tnm_t: str
	tnm_n: str
	tnm_m: str
	tnm_version: str
	tnm_type: str
	other_type: Optional[str] = None
	other_grade: Optional[str] = None
	is_relapse: bool
	staging_date: date


class Metastasis(BaseModel):
	metastasis_diagnosed: bool
	metastasis_localisation: Optional[str]

class Histology(BaseModel):
	histological_celltype_code: str
	histological_celltype_description: str
	topographical_mapping_code: str
	topographical_mapping_description: str

class Genetics(BaseModel):
	amino_acid_changes: str

class PreviousCancerItem(BaseModel):
	previous_cancer_icd10_code: str
	previous_cancer_icd10_description: str
	previous_cancer_laterality: Optional[str] = None
	previous_cancer_localisation: Optional[str] = None
	previous_cancer_diagnosis_year: int
	previous_cancer_rt_given: bool
	previous_cancer_comment: Optional[str] = None

class PreviousCancer(BaseModel):
	is_previous_cancer: bool
	previous_cancer: List[PreviousCancerItem]

class TreatmentRadiotherapy(BaseModel):
	course_id: str
	procedure_nkpk_code: str
	procedure_nkpk_description: str
	comment: Optional[str] = None

class TreatmentSurgery(BaseModel):
	procedure_nkpk_code: str
	procedure_nkpk_description: str
	surgery_target: Literal[
		"Primærtumor",
		"Lokalt residiv og primærtumor",
		"Metastase"
	]
	surgery_date: date
	comment: Optional[str] = None

class TreatmentSystemic(BaseModel):
	"""Legemiddel versus MKB?"""

	systemic_name: str # navn på legemiddel / virkestoff / kur
	category: Literal[
		"Kjemoterapi",
		"Immunterapi",
		"Hormonell behandling",
		"Målrettet terapi / small molecules"
	]

	therapeutic_intent: Literal[
		"Preoperativt",
		"Postoperativt"
	]

	total_dosage_value: float
	total_dosage_unit: str
	dosage_start_date: date
	dosage_stop_date: date
	comment: Optional[str] = None

class TreatmentSummary(BaseModel):
	treatment_intention: Literal[
		"Kurativt",
		"Ikke kurativt (livsforlengende)",
		"Ikke kurativt (symptomlindrende)",
		"Ikke kurativt (lokalkontroll)"
	]
	treatment_type: Literal[
		"Neoadjuvant", 
		"Konkomitant", 
		"Adjuvant", 
		"Neoadjuvant + konkomitant", 
		"Neoadjuvant + adjuvant", 
		"Konkomitant + adjuvant", 
		"Neoadjuvant + konkomitant + adjuvant"
	]

	treatment_radiotherapy: Optional[TreatmentRadiotherapy] = None
	treatment_systemic: Optional[TreatmentSystemic] = None
	treatment_surgery: Optional[TreatmentSurgery] = None


class Course(BaseModel):
	metadata: Metadata
	demographics: Demographics
	social: Social
	stimulantia: Stimulantia
	function_status: FunctionStatus
	comorbidity: List[Comorbidity]
	primary_diagnosis: PrimaryDiagnosis
	staging: List[Staging]
	metastasis: Metastasis
	histology: List[Histology]
	genetics: List[Genetics]
	previous_cancer: PreviousCancer
	treatment_summary: List[TreatmentSummary]