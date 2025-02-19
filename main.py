from flask import Flask, jsonify, request
from db import connect

app = Flask(__name__)


def _parse_query_params(_query_params):
    _sql_query_params = []
    # sql-kyselyn pohja
    _sql_query = "SELECT users.id, users.name, users.email, departments.name FROM users INNER JOIN departments ON users.department_id = departments.id"
    # jos query parametreissa on department, lisätään WHERE deppart.name = 'departmentin nimi'
    # sql-kyselyyn
    if 'department' in _query_params:
        _sql_query += " WHERE departments.name = ?"
        _sql_query_params.append(_query_params['department'])
    _sql_query += " ORDER BY users.id"
    if 'page' in _query_params:
        _sql_query += " LIMIT ? OFFSET ?"
        limit = 10
        page = int(_query_params['page'])
        if page < 1:
            page = 1
        page -= 1
        offset = page * limit

        _sql_query_params.append(limit)
        _sql_query_params.append(offset)

        return _sql_query, _sql_query_params


@app.route('/users')
def get_users():
    with connect() as conn:
        cur = conn.cursor()
        _sql_query_params = []
        # parametrit dictionaryna:
        # esim. {'department': 'Engineering'}
        _query_params = request.args.to_dict()
        _sql_query, _sql_query_params = _parse_query_params(_query_params)

        cur.execute(_sql_query, tuple(_sql_query_params))

        users = cur.fetchall()
        users_json = []
        for user in users:
            users_json.append({'id': user[0], 'name': user[1], 'email': user[2], 'department': user[3]})
        cur.close()
        return jsonify(query=_sql_query, sql_query_params=_sql_query_params, users=users_json)


if __name__ == '__main__':
    app.run(debug=True)
