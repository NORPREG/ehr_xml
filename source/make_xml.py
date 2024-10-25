from pydantic import BaseModel
from typing import List, Optional
from dicttoxml import dicttoxml
from xmler import dict2xml
from xml.dom.minidom import parseString
from json import loads

from module.pydantic_dummydata import get_course

example_course = get_course()

serialized_course = loads(example_course.model_dump_json())

xml = dicttoxml(
	example_course.model_dump(), 
	custom_root="course", 
	attr_type=False,
	encoding="utf-8",
	)

dom = parseString(xml)
xml_pretty = dom.toprettyxml()

"""
xml_pretty.replace(
	"<?xml version="1.0" ?>",
	"<?xml version="1.0" ?>\n",
"""

with open("output/register.xml", "w") as out:
	out.write(xml_pretty)
