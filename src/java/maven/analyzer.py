
import xml.etree.ElementTree as ET


from  src.utils.common import serch_vlun

def run(files):
    all_dependency = {}
    for file in files:
        tree = ET.parse(file)
        root = tree.getroot()
        properties_dict = {}
        walk_node(root, properties_dict, all_dependency)
    return all_dependency


def walk_node(node, properties_dict, all_dependency):
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
            if vendor not in all_dependency:
                all_dependency[vendor] = {}
            if product not in all_dependency[vendor]:
                all_dependency[vendor][product] = []
            if version:
                all_dependency[vendor][product].append(version)

        else:
            walk_node(child, properties_dict, all_dependency)


if __name__ == '__main__':
    run('')