from lxml import etree

def generate_xsd(cls):
	namespace = "http://ous-hf.no/nortreg/clinical-schema"
	nsmap = {
		None: namespace,
		"xs": "http://www.w3.org/2001/XMLSchema"
	}

	root = etree.Element('{%s}schema' % namespace, nsmap=nsmap)
	root.set("targetNamespace", namespace)
	# 	root.set("xmlns:tns", namespace)
	root.set("elementFormDefault", "qualified")

	print(etree.tostring(root, pretty_print=True).decode("utf-8"))

	def add_element(parent, name, typ, is_complex=False):
		if is_complex:
			element = etree.SubElement(parent, "xs:complexType", name=name)
			seq = etree.SubElement(element, "xs:sequence")
			return seq
		else:
			element = etree.SubElement(parent, "xs:element", name=name)
			if typ == "str":
				element.set("type", "xs:string")
			if typ == "int":
				element.set("type", "xs:integer")
			if typ == "list":
				element.set("type", "xs:string") # complexType?
			return element

	user_element = add_element(root, "User", "complex")

	add_element(user_element, "name", "str")
	add_element(user_element, "age", "int")
	add_element(user_element, "email", "str")
		
	address_element = add_element(root, "Address", "complex")
	add_element(address_element, "street", "str")
	add_element(address_element, "city", "str")
	add_element(address_element, "zip_code", "str")

	return etree.tostring(
			root, 
			pretty_print=True,
			xml_declaration=True,
			encoding="UTF-8"
	)