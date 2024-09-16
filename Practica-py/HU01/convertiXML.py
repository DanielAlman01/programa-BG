import xml.etree.ElementTree as ET

    # Convertir los usuarios a formato XML
def convertir_a_xml(usuarios):
    root = ET.Element("usuarios")
    for usuario in usuarios:
        usuario_elem = ET.SubElement(root, "usuario")
        ET.SubElement(usuario_elem, "nombre").text = usuario[0]
        ET.SubElement(usuario_elem, "edad").text = str(usuario[1])
        ET.SubElement(usuario_elem, "extranjero").text = str(usuario[2])
    return ET.tostring(root, encoding='utf8', method='xml')