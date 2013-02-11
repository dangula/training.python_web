import sqlite3
con = sqlite3.connect('/tmp/bottle.db')
con.execute("create table entries (id integer primary key autoincrement,title string not null,text string not null)")
con.commit()