import xmlrpc.client
import pandas as pd

odoo_url = "https://edu-eduvibe.odoo.com/"

db_name = "edu-eduvibe"

username = "Noman Memon"

password = "Jhonplayer@000a"

odoo_model = "account.analytical.line"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_url ))
common.version()


uid = common.authenticate(db_name, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(odoo_url))

all_fields = models.execute_kw(db_name, uid, password,
    odoo_model, 'fields_get', [], {'attributes': ['string', 'help', 'type']})

fields_to_retrieve = list(all_fields.keys())

data_types = {field: field_info['type'] for field, field_info in all_fields.items()}

records_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])

records = models.execute_kw(db, uid, password, 'res.partner', 'read', [records_ids], {'fields': ['name', 'country_id', 'comment']})

""" this will convert into dataframe """
df = pd.DataFrame(records)

for field, data_types in data_types.items():
    if data_types == "integer":
        df[field] = pd.to_numeric(df[field], errors='coerce', downcast='integer')
    elif data_types == "float":
        df[field] = pd.to_numeric(df[field], errors='coerce', downcast='float')
    elif data_types == "datetime":
        df[field] = pd.to_datetime(df[field], errors='coerce')

print("\n df============", df)