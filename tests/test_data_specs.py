import util
import logging

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
