# Excel templates for goodtables schemas

## Summary
Goodtables schemas are a great way to validate and manage data.
JSON file formats might be a barrier for less tech savvy users. 

This work is a draft of a script which transforms our goodtable schemas for CKAN resources
into an Excel template.
## Example:
### Schema for antiretroviral therapy (ART):
Below is an excel template describing the data requirents.
![alt text][logo]

[logo]: ./art_excel_example.png "Excel schema for antiretroviral therapy (ART)"
Below in file `art_programmatic.json` is a raw goodtables json schema used to generate the above example.
```json
{
  "fields": [{
      "name": "area_id",
      "title": "Area ID",
      "description": "Must be an area_id from the agreed area hierarchy.",
      "type": "string",
      "constraints": {
        "required": true
      }
    },
    {
      "name": "area_name",
      "title": "Area Name",
      "description": "Area name corresponding to area_id (optional).",
      "type": "string"
    },
    {
      "name": "sex",
      "title": "Sex",
      "description": "Biological sex.  Must be \"male\", \"female\",  or \"both\" where sex stratification is not available.",
      "type": "string",
      "constraints": {
        "required": true,
        "enum": ["male", "female", "both"]
      }
    },
    {
      "name": "age_group",
      "title": "Age Group",
      "description": "The age group.",
      "type": "string",
      "constraints": {
        "required": true,
        "enum": ["00-14", "15+", "00+"]
      }
    },
    {
      "name": "year",
      "title": "Year",
      "description": "The year.",
      "type": "integer",
      "constraints": {
          "required": true,
          "minimum": 1970,
          "maximum": 2021
      }
    },
    {
      "name": "current_art",
      "title": "Number on ART",
      "description": "Number currently receiving ART at the end of reporting period (year).",
      "type": "number",
      "constraints": {
        "required": true,
        "minimum": 0
      }
    }
  ],
  "require_field_order": false,
  "primaryKey": ["area_id", "sex", "age_group", "year"],
  "foreignKeys": [{
    "fields": "area_id",
    "reference": {
      "resource": "geographic_location_hierarchy",
      "fields": "area_id"
    }
  }]
}
```

### Running the script:
Install the requiremnts:
```shell script
✗ pip3 install -r requirments.txt
```
Then run the script by passing the path to goodtable json schema as an argument:
```shell script
✗ python3 create_template.py ../table_schemas/art/3_art_inputs.json
```
And the excel output file should be created in the script directory:
```shell script
✗ ls -l
3_art_inputs.xlsx <<<
create_template.py
README.md
```