import pyodbc
import json

server = 'tcp:194.87.238.203,1433'
database = 'oilcasedb'
username = 'oilcase'
password = 'aaaaaa'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

mail_template = {
    "Team_name": None,
    "Game_step": None,
    "Well_id": None,
    "Well_line": [[None, None, None], [None, None, None], [None, None, None]],
    "Well_status": None,
}


class TeamInfo:
    def __init__(self):
        self.Team_name = None
        self.Game_step = None
        self.Well_id = None
        self.Well_line = [[None, None, None], [None, None, None], [None, None, None]]
        self.Well_status = None

    def extrac_from_user_data(self, data: [str]):
        pass

    def extrac_from_user_info(self, data: [str]):
        pass


if __name__ == '__main__':
    capitan_id_query = "SELECT [Id], [orgname] FROM [OILCASEDB].[dbo].[User] where rolename = 'capitan' and orgname in ('t1', 't2','t3','t4')"
    cursor.execute(capitan_id_query)
    data_user = cursor.fetchall()
    print(data_user)
    capitan_ids = f"({', '.join([str(i[0]) for i in data_user])})"

    target_data_query = f"SELECT * FROM [OILCASEDB].[dbo].[UserData] where userid in {capitan_ids}"
    cursor.execute(target_data_query)
    target_data = cursor.fetchall()
    print(target_data)
    x = [i[4] for i in target_data]
    y = x[1]
    x = json.loads(x[1])

    import json

    with open('data.json', 'w') as f:
        json.dump(x, f)

    print(x)


#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
