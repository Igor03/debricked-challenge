from flask_restx import fields

cpe_fields= {}
cpe_fields['cpe_23_uri'] = fields.String(attribute = 'cpe_23_uri')
cpe_fields['vendor'] = fields.String(attribute = 'vendor')
cpe_fields['product'] = fields.String(attribute = 'product')
cpe_fields['vulnerable'] = fields.Boolean(attribute = 'vulnerable')

cvssv3_fields = {}
cvssv3_fields['version'] = fields.String(attribute = 'version')
cvssv3_fields['vector_string'] = fields.String(attribute = 'vector_string')
cvssv3_fields['attack_vector'] = fields.String(attribute = 'attack_vector')
cvssv3_fields['cvss3_score'] = fields.Float(attribute = ('cvss3_score'))

cve_fields = {}
cve_fields['cve_id'] = fields.String(attribute = 'cve_id')
cve_fields['description'] = fields.String(attribute = 'description')
cve_fields['published_date'] = fields.DateTime(attribute = 'published_date')
cve_fields['last_modified'] = fields.DateTime(attribute = 'last_modified')


model_cotroller_1 = {}
model_cotroller_1['cve_id'] = fields.String(attribute = 'cve_id')
model_cotroller_1['description'] = fields.String(attribute = 'description')
model_cotroller_1['published_date'] = fields.DateTime(attribute = 'published_date')
model_cotroller_1['last_modified'] = fields.DateTime(attribute = 'last_modified')
model_cotroller_1['cpes'] = fields.List(fields.Nested(cpe_fields))
model_cotroller_1['cvssv3'] = fields.Nested(cvssv3_fields)

model_cotroller_2 = {}
model_cotroller_2['cves'] = fields.List(fields.Nested(cve_fields))

