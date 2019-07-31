def extract_fields(req, resp, resource, params):
    fields = req.get_param('fields', False) or None
    if fields is None:
        params['fields'] = None
    else:
        # Skip empty, strip. Dots may be needed for marshmallow
        params['fields'] = [v for v in map(str.strip, fields.split(',')) if v]
