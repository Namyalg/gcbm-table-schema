# GCBM Table Schema configuration

This repository demonstrates a sample API endpoint to configure the input tables as required to run the GCBM simulation

The idea is to enforce a one-to-one mapping between the user tables and the tables required for the configuration, hence any attribute names that have to be changed are accepted.

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

## Demonstration

The python script can be run as `python app.py` on `PORT 5000`

`gcbm.db` has a table `sample` on which the API has been tested.

The initial attributes/headers are `id`, `A_before`, `B_before`, `C_before`, `D_before`

JSON body of the POST request : 
```
{
    "sample" : {
        "A_before" : "A_after",
        "B_before" : "B_after",
        "C_before" : "C_after",
        "D_before" : "D_after"
    }
}
```

The API has been tested in Postman, it it passed as :

![image](https://user-images.githubusercontent.com/53875297/168005450-18885bf1-7dbf-4bd4-967c-58cd06aee992.png)

The response is the old and new schemas of the table : 

![image](https://user-images.githubusercontent.com/53875297/168005589-9949445e-f4a6-44e9-bc7c-e84889fd7bef.png)


