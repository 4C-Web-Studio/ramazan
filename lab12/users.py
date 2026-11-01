import sqlite3
import re
class UserRegistry:
    def __init__(self):
        self.db=sqlite3.connect(':memory:')
        self.db.row_factory=sqlite3.Row
        self.db.execute('CREATE TABLE people(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,email TEXT UNIQUE COLLATE NOCASE)')
    def add(self,name,age,email):
        name=name.strip()
        if not any(c.isalpha() for c in name):raise ValueError('name')
        if not 2<=len(name)<=80 or not all(c.isalpha() or c in ' -' for c in name):raise ValueError('name')
        if type(age) is not int or not 1<=age<=100:raise ValueError('age')
        if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',email):raise ValueError('email')
        try:
            cur=self.db.execute('INSERT INTO people(name,age,email) VALUES(?,?,?)',(name,age,email.casefold()));self.db.commit()
        except sqlite3.IntegrityError as error:raise ValueError('duplicate') from error
        return self.get(cur.lastrowid)
    def get(self,identifier):
        row=self.db.execute('SELECT * FROM people WHERE id=?',(identifier,)).fetchone()
        return dict(row) if row else None
    def find(self,email):
        row=self.db.execute('SELECT * FROM people WHERE email=?',(email,)).fetchone()
        return dict(row) if row else None
    def all(self):return [dict(r) for r in self.db.execute('SELECT * FROM people ORDER BY id')]
    def delete(self,identifier):
        cur=self.db.execute('DELETE FROM people WHERE id=?',(identifier,));self.db.commit();return cur.rowcount==1
    def clear(self):self.db.execute('DELETE FROM people');self.db.commit()
    def close(self):self.db.close()
