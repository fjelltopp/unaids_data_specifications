# unaids_data_specifications

Specifications for data inputs requested by UNAIDS

### ckan_package_schemas

These schemas define the structure of data packages in the ['AIDS Data
Repository'](https://adr.unaids.org). The packages are made up of a collection
of resources and metadata as defined by the json files.  See the docs of the
CKAN extension "Scheming"
(['ckanext-scheming'](https://github.com/ckan/ckanext-scheming)) for the
specification of these schemas.

Schemas are organised in sub directories by data package.  Each version of a
package schema that has been used in production must be seperately saved so
that historical data packages remain well defined.

### table_schemas

These schemas are based on Frictionless Data table schemas and are used to
define the tabular data requested by UNAIDS.  For more information see the ['table schema docs'](https://specs.frictionlessdata.io/table-schema/).

As with the package schemas, it is important that every complete version of a table
schema used in production is saved as a separate file so that historical data remains
well defined. The schemas are therefore organised into subdirectories by table type.

### meta_indicators

These tables defines all of the indicators for inputs and outputs.

The fields _accuracy_, _scale_, _prefix_, and _suffix_ define how numerical
data are displayed following the [`scales`](https://scales.r-lib.org/) R
package.

### tests

This repository includes tests to check the validity of the data specifications.
The tests can be run locally using nosetests.  There is also a travis build configured.

## TODO:

- [ ] Where should this live.
- [ ] `art_current` versus `art_num_attend` indicator.
- [ ] Language localisation.
- [ ] Confirm if okay to drop integer `*_id` columns with Avenir.
- [ ] Option for country / indicator / level specific numerical displays?
