import json
import os
import glob
import logging

log = logging.getLogger(__name__)


def get_table_schemas_list():
    table_schemas_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../table_schemas'
    )
    files = glob.glob(f"{table_schemas_path}/**/*", recursive=True)
    table_schema_files = filter(lambda x: x[-5:] == '.json', files)
    table_schema_names = map(os.path.basename, table_schema_files)
    table_schema_names = map(lambda x: x[:-5], table_schema_names)
    return list(table_schema_names)


def package_schemas_generator():
    package_schemas_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../package_schemas'
    )
    files = glob.glob(f"{package_schemas_path}/**/*", recursive=True)
    package_schema_files = filter(lambda x: x[-5:] == '.json', files)

    def schema_generator():
        for file in package_schema_files:
            try:
                with open(file, 'r') as json_file:
                    yield {'filename': file, 'schema': json.load(json_file)}
            except Exception as e:
                log.error(f"Error loading json from {file}")
                log.exception(e)

    return schema_generator
