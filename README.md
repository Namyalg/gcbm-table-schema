# GCBM Table Schema configuration

This repository demonstrates a sample API endpoint to configure the input tables as required to run the GCBM simulation

The idea used here is to enforce a one-to-one mapping between the user tables and the tables required for the configuration. 

The user will provided information about the tables, their attributes and functionalities in a format similar to [this PR](https://moja-global-documentation--179.org.readthedocs.build/en/179/Understanding-FLINT/FLINT-Inputs/tables.html)

## Working of endpoint

The API is designed to accept a `POST` method.

The payload is passed in the format : 

```{
    table_name_1 : {
        old_attribute_1 : new_attribute_1,
        old_attribute_2 : new_attribute_2,
        old_attribute_3 : new_attribute_3,
    },
    table_name_2 : {
        old_attribute_1 : new_attribute_1,
        old_attribute_2 : new_attribute_2,
        old_attribute_3 : new_attribute_3,
    } 
}
```

Only the attributes that require to be changed are passed table-wise
