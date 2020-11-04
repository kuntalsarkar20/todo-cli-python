import sqlite3

class Database():
	def __init__(self):
		self.conn = sqlite3.connect('todo.sqlite')
		self.cur = self.conn.cursor()
		self.cur.executescript('''
			CREATE TABLE IF NOT EXISTS todo_list
			(todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
			todo_name varchar(100) NOT NULL,
			updated_at varchar(100) NOT NULL);
		 ''')
		self.conn.commit()
	def insert(self,name,time):
		self.cur.execute('''
			INSERT INTO todo_list(todo_name,updated_at)
			VALUES(?,?);''',
			(name,time))
		self.conn.commit()
		print("Inserted Successfully")

	def selectAll(self):
		self.cur.execute("SELECT * FROM todo_list")
		data = self.cur.fetchall()
		return data
	def update(self,name,id,time):
		self.cur.execute('''
			UPDATE todo_list SET todo_name = ?, updated_at = ? WHERE todo_id = ?''',
			(name,time,id))
		self.conn.commit()
		print("Updated Successfully")

	def delete(self,task_id):
		self.cur.execute(''' delete from todo_list where todo_id = ?''',(task_id,))
		self.conn.commit()
		print("Deleted Successfully")
	def __del__(self):
		self.conn.close()