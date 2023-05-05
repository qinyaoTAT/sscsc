
import xml.etree.ElementTree as ET


from  src.utils.common import serch_vlun

def run(files):
    maven_dependency = {}
    for file in files:
        tree = ET.parse(file)
        root = tree.getroot()
        properties_dict = {}
        walk_node(root, properties_dict, maven_dependency)
    return maven_dependency


def walk_node(node, properties_dict, maven_dependency):
    for child in node:
        child_tag = child.tag.split('}')[-1]
        if child_tag == 'properties':
            for sub_child in child:
                child_tag = sub_child.tag.split('}')[-1]
                value = sub_child.text
                properties_dict[child_tag] = value
        elif child_tag == 'dependency':
            vendor = ''
            product = ''
            version = ''
            for sub_child in child:
                child_tag = sub_child.tag.split('}')[-1]
                if child_tag == 'groupId':
                    vendor = sub_child.text

                elif child_tag == 'artifactId':
                    product = sub_child.text
                elif child_tag == 'version':
                    version = sub_child.text
                    if '${' in version:
                        version = version[2:-1]
                    if version in properties_dict:
                        version = properties_dict[version]
            if not vendor:
                return
            if vendor not in maven_dependency:
                maven_dependency[vendor] = {}
            if product not in maven_dependency[vendor]:
                maven_dependency[vendor][product] = []
            if version:
                maven_dependency[vendor][product].append(version)

        else:
            walk_node(child, properties_dict, maven_dependency)


if __name__ == '__main__':
    run('')