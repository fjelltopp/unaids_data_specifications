import util
import logging
from pprint import pformat

log = logging.getLogger(__name__)


def test_required_table_schemas_exist():
    table_schemas = util.get_table_schemas_list()
    package_schemas = util.package_schemas_generator()
    missing_table_schemas = []
    for schema in package_schemas():
        package = schema['schema'].get('name')
        resources = schema['schema'].get('resources', [])
        for resource in resources:
            fields = resource.get('resource_fields')
            for field in fields:
                name = field.get('field_name')
                value = field.get('field_value')
                if name == 'schema':
                    if value not in table_schemas:
                        missing_table_schemas.append(field['field_value'])
                        log.error(f"Schema {value} referenced from {package} package not found.")
    assert missing_table_schemas == []


def test_restricted_field_in_all_schemas():
    package_schemas = util.package_schemas_generator()
    for schema in package_schemas():
        log.warning(pformat(schema.keys()))
        resource_fields = schema['schema']['resource_fields']
        restricted_fields = list(filter(
            lambda x: x['field_name'] == 'restricted',
            resource_fields
        ))
        assert len(restricted_fields) == 1
        expected = {
            "field_name": "restricted",
            "label": "Access Restriction",
            "preset": "restricted_fields",
            "display_group": "Access Restriction"
        }
        assert restricted_fields[0] == expected
