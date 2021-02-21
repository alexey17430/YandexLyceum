import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    id = cur.execute('''
    select id from main.genres
    where title = "комедия"
    ''').fetchone()[0]
    cur.execute(f'''
    delete from films
    where genre = {id}
    ''')
    con.commit()
