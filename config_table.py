import sqlite3 


def get_table_schema(conn, table_name):
    schema = []
    ins = "PRAGMA table_info(\'" + table_name + "\')"
    print(ins)
    for row in conn.execute(ins).fetchall():
        schema.append(row[1])
    return schema


def rename_columns(request):
    response = dict()
    conn = sqlite3.connect("gcbm.db") 
    for table, config in request.items():
        response[table] = dict()
        print("TABLE IS ")
        print(table)
        print(config)
        response[table]['schema_before'] = get_table_schema(conn, table)
        for old_name, new_name in config.items():
            print(old_name, new_name)
            try:
                rename = 'ALTER TABLE '  + table +  ' RENAME COLUMN ' +  old_name + ' TO ' + new_name
                conn.execute(rename)
            except Exception:
                print("Exception occured is ", Exception)
        response[table]['schema_after'] = get_table_schema(conn, table)
        print(response)
    conn.commit()
    conn.close()
    return response
