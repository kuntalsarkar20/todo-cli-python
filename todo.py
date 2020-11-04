from database import Database
import datetime

print("-----------------Welcome to Todo------------------")
print("Create/Edit/Delete/Manage your todo's in one place.\n")

#connecting to database
db = Database()

#Loop until user exits the program
while True:
	print("\n1. Create new Task.")
	print("2. View All Tasks")
	print("3. Update existing Task.")
	print("4. Delete Task.")
	print("Press Enter if you want to exit\n")

	user_input = input("Enter your choice: ")

	#checking is user wants to exit
	if(user_input == ''): break

	if(int(user_input) == 1):
		#inserting new task
		todo_name = input("Enter the task details: ")
		db.insert(todo_name,datetime.datetime.now())
		
	elif(int(user_input) == 2):
		#displaying all the task
		results = db.selectAll()
		if(len(results)==0): print("No tasks...")
		else:
			print(str(len(results)),"tasks found.")
			for row in results:
				print(row)

	elif(int(user_input) == 3):
		#updating an existing task
		results = db.selectAll()
		for row in results:
			print(row)
		task_id = int(input("Enter the task id: "))
		todo_name = input("Enter the task details: ")
		db.update(todo_name,task_id,datetime.datetime.now())

	elif (int(user_input) == 4):
		#Deleting a task
		results = db.selectAll()
		for row in results:
			print(row)
		task_id = int(input("Enter the task id: "))
		db.delete(task_id)


