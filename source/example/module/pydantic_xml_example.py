from pydantic import BaseModel
from typing import List, Optional
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

class Address(BaseModel):
	street: str
	city: str
	zip_code: str

class User(BaseModel):
	name: str
	age: int
	email: str
	addresses: List[Address]


example_address_1 = Address(
	street="Bergveien 1",
	city="Oslo",
	zip_code="4535"
)

example_address_2 = Address(
	street="Bergveien 2",
	city="Bergen",
	zip_code="5643"
)

example_user = User(
	name="Line Danser",
	age=31,
	email="line_danser@nhn.no",
	addresses = [example_address_1, example_address_2]
)

xml = dicttoxml(example_user.model_dump(), custom_root="root", attr_type=True)
dom = parseString(xml)
xml_pretty = dom.toprettyxml()

with open("output.xml", "w") as out:
	out.write(xml_pretty)
