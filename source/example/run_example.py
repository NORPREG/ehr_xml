from module.generate_xsd import generate_xsd
from module.pydantic_model import User

xsd_string = generate_xsd(User)
print(xsd_string.decode("utf-8"))