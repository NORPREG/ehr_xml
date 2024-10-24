from pydantic import BaseModel
from typing import List, Optional
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

from module.pydantic_dummydata import get_course

example_course = get_course()

xml = dicttoxml(example_course.model_dump(), custom_root="course", attr_type=True)
dom = parseString(xml)
xml_pretty = dom.toprettyxml()

with open("output/course.xml", "w") as out:
	out.write(xml_pretty)