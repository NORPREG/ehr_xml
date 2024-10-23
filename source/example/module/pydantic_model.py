from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
	street: str
	city: str
	zip_code: str


class User(BaseModel):
	name: str
	age: int
	email: str
	addresses: List[Address]