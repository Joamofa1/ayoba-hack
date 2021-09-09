import datetime
from config import *
import sqlite3

class Database():
	def __init__(self, name='test.db'):
		self.name = name

		self.connection = sqlite3.connect(self.name)
		self.cursor = self.connection.cursor()

		# creating tables
		try:
			self.cursor.execute(
				"""
				CREATE TABLE PATIENT 
				(ID TEXT PRIMARY KEY,NAME TEXT NOT NULL,AGE INTEGER NOT NULL,
				GENDER TEXT NOT NULL,EMAIL TEXT,CONTACT TEXT NOT NULL,
				ADDRESS TEXT NOT NULL,PASSWORD TEXT)
				"""
			)


			self.cursor.execute(
				"""
				CREATE TABLE PATIENT_DATA
				(PATIENT_ID TEXT PRIMARY KEY,
				WEIGHT INTEGER DEFAULT 'Not Uploaded',
				HEIGHT INTEGER DEFAULT 'Not Uploaded',
				SYSTOLIC INTEGER DEFAULT 'Not Uploaded',
				DIASTOLIC INTEGER DEFAULT 'Not Uploaded',
				RED_BLOOD INTEGER DEFAULT 'Not Uploaded',
				WHITE_BLOOD INTEGER DEFAULT 'Not Uploaded',
				SICKLING TEXT DEFAULT 'Not Uploaded',
				BLOOD_GROUP TEXT DEFAULT 'Not Uploaded',
				PH REAL DEFAULT 'Not Uploaded',
				LEFT_EYE INTEGER DEFAULT 'Not Uploaded',
				RIGHT_EYE INTEGER DEFAULT 'Not Uploaded',
				STD TEXT DEFAULT 'Not Uploaded',
				HAEMO INTEGER DEFAULT 'Not Uploaded',
				GRAVITY INTEGER DEFAULT 'Not Uploaded',
				GLUCOSE INTEGER DEFAULT 'Not Uploaded',
				X_RAY TEXT DEFAULT 'Not Uploaded',
				REMARK TEXT DEFAULT 'Not Uploaded',
				STAGE_1 TEXT DEFAULT 'Not Completed',
				STAGE_2 TEXT DEFAULT 'Not Completed',
				STAGE_3 TEXT DEFAULT 'Not Completed',
				FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(ID) ON DELETE CASCADE)
				"""
			)

			self.cursor.execute(
				"""
				CREATE TABLE STAFF
				(ID TEXT PRIMARY KEY,
				NAME TEXT NOT NULL,
				TITLE TEXT NOT NULL,
				CONTACT TEXT NOT NULL)
				"""
			)

			self.cursor.execute(
                """
                CREATE TABLE MEDICATION
                (BATCH_NO CHAR(10) PRIMARY KEY,
                CATEGORY TEXT NOT NULL,
                NAME TEXT NOT NULL,
                EXPIRY_DATE TIMESTAMP NOT NULL,
                IN_STOCK INTEGER NOT NULL)
                """
            )

			self.cursor.execute(
				"""
				CREATE TABLE APPOINTMENTS
				(ID CHAR(7) PRIMARY KEY,
				DATEOF TIMESTAMP NOT NULL,
				STAFF TEXT NOT NULL,
				PATIENT TEXT NOT NULL,
				TIMEOF TEXT NOT NULL,
				FOREIGN KEY(PATIENT) REFERENCES PATIENT(ID) ON DELETE CASCADE,
				FOREIGN KEY(STAFF) REFERENCES STAFF(ID) ON DELETE CASCADE)
				"""
			)

			self.cursor.execute(
				"""
				CREATE TABLE PRESCRIPTIONS
				(ID CHAR(7) NOT NULL,
				BY TEXT NOT NULL,
				FOR TEXT NOT NULL,
				DATEOF TIMESTAMP NOT NULL,
				MEDICINE_NAME TEXT NOT NULL,
				FOREIGN KEY(BY) REFERENCES STAFF(ID) ON DELETE CASCADE,
				FOREIGN KEY(FOR) REFERENCES PATIENT(ID) ON DELETE CASCADE)
				"""
			)

			self.cursor.execute(
				"""
				CREATE TABLE AUTH 
				(ADMIN TEXT,
				PASSWORD TEXT)
				"""
			)

		except sqlite3.OperationalError as e:
			print(e)

		finally:
			self.connection.commit()
			if self.connection:
				self.connection.close()



	def add_patient(self, iD, name, age, gender, email, comtact, address):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				INSERT INTO PATIENT
				(ID, NAME, AGE, GENDER, EMAIL, CONTACT, ADDRESS)
				VALUES
				('{iD}', '{name}', '{age}', '{gender}', '{email}', '{comtact}', '{address}')
				"""
			)

			self.cursor.execute(
				f"""
				INSERT INTO PATIENT_DATA
				(PATIENT_ID)
				VALUES 
				('{iD}')
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return True

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	
	

	def validate_patient(self, iD):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
			f"""
			SELECT * FROM PATIENT WHERE ID='{iD}'
			"""
			)

			try:
				a = len(self.cursor.fetchone())

				return True

			except:
				return False

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()

	def add_patient_wh(self, iD, weight, height):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				UPDATE PATIENT_DATA SET WEIGHT='{weight}', HEIGHT='{height}'
				WHERE PATIENT_ID='{iD}'
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return True

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def add_remark(self, iD, remark):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				UPDATE PATIENT_DATA SET REMARK='{remark}' WHERE PATIENT_ID='{iD}'
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return True

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

			



	def add_patient_bp(self, iD, sys, dias):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				UPDATE PATIENT_DATA SET SYSTOLIC='{sys}', DIASTOLIC='{dias}' WHERE PATIENT_ID='{iD}'
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return True

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()



	def add_patient_eye(self, iD, right, left):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				UPDATE PATIENT_DATA SET LEFT_EYE='{left}', RIGHT_EYE='{right}' WHERE PATIENT_ID='{iD}'
				"""
			)

			self.cursor.execute(
				f"""
				UPDATE PATIENT_DATA SET STAGE_1='Completed' WHERE PATIENT_ID='{iD}'
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return True

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def add_patient_blood(self, iD, red_blood, white_blood, sickling, blood_group, haemo, std):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				UPDATE PATIENT_DATA SET RED_BLOOD='{red_blood}', WHITE_BLOOD='{white_blood}', SICKLING='{sickling}', BLOOD_GROUP='{blood_group}', HAEMO='{haemo}', STD='{std}' WHERE PATIENT_ID='{iD}'
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return True

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def add_patient_urinalysis(self, iD, ph, gravity):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				UPDATE PATIENT_DATA SET PH='{ph}', GRAVITY='{gravity}' WHERE PATIENT_ID='{iD}'
				"""
			)

			self.cursor.execute(
				f"""
				UPDATE PATIENT_DATA SET STAGE_2='Completed' WHERE PATIENT_ID='{iD}'
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return True

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def count_patient(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				SELECT COUNT(*) FROM PATIENT
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return self.cursor.fetchone()[0]

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def add_auth(self, username, passw):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				INSERT INTO AUTH
				(ADMIN, PASSWORD)
				VALUES
				('{username}','{passw}')
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return True

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def retrieve_patients(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				SELECT * FROM PATIENT ORDER BY NAME ASC
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			return self.cursor.fetchall()

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def retrieve_patient_data(self, iD):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			items = []

			self.cursor.execute(
				f"""
				SELECT * FROM PATIENT WHERE ID='{iD}'
				"""
			)

			items.append(self.cursor.fetchone())

			self.cursor.execute(
				f"""
				SELECT * FROM PATIENT_DATA WHERE PATIENT_ID='{iD}'
				"""
			)

			items.append(self.cursor.fetchone())

		except sqlite3.OperationalError as e:
			return e

		else:
			return items

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def add_x_ray(self, iD, remark):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()
			self.cursor.execute(
				f"""
				UPDATE PATIENT_DATA SET STAGE_3='Completed', X_RAY='{remark}' WHERE PATIENT_ID='{iD}'
				"""
			)
			return True
		except sqlite3.OperationalError as e:
			return e
		finally:
			self.connection.commit()
			if self.connection:
				self.connection.close()

	def validate_login(self, username, password):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
			f"""
			SELECT * FROM AUTH WHERE ADMIN='{username}' AND PASSWORD='{password}'
			"""
			)

			try:
				a = len(self.cursor.fetchone())
				return True

			except:
				return False

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()

	def add_medication(self, category, name, expiry, stock, bat):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			EXEC = """
			INSERT INTO MEDICATION
			(BATCH_NO, CATEGORY, NAME, EXPIRY_DATE, IN_STOCK)
			VALUES
			(?, ?, ?, ?, ?)
			"""

			DATA = (bat, category, name, expiry, stock)

			self.cursor.execute(EXEC, DATA)

			return True

		except sqlite3.OperationalError as e:
			return e

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def add_staff(self, name, title, staff_id, contact):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			EXEC = """
			INSERT INTO STAFF
			(ID ,NAME ,TITLE ,CONTACT)
			VALUES
			(?, ?, ?, ?)
			"""

			DATA = (staff_id, name, title, contact)

			self.cursor.execute(EXEC, DATA)

			return True

		except sqlite3.OperationalError as e:
			return e

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def add_appointment(self, PATIENT, staff, date, time):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			EXEC = """
			INSERT INTO APPOINTMENTS
			(ID, DATEOF, PATIENT, STAFF, TIMEOF)
			VALUES
			(?, ?, ?, ?, ?)
			"""

			DATA = (gen_id(5), date, PATIENT, staff, time)

			self.cursor.execute(EXEC, DATA)

			return True

		except sqlite3.OperationalError as e:
			return e

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def add_prescription(self, PATIENT, staff, medicine_name):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			EXEC = """
			INSERT INTO PRESCRIPTIONS
			(ID, BY, FOR, DATEOF, MEDICINE_NAME)
			VALUES
			(?, ?, ?, ?, ?)
			"""

			DATA = (gen_id(6), staff, PATIENT, datetime.datetime.today().date(), medicine_name)

			self.cursor.execute(EXEC, DATA)

			return True

		except sqlite3.OperationalError as e:
			return e

		finally:
			self.connection.commit()

			if self.connection:
				self.connection.close()

	def count_med(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				"""
				SELECT COUNT(*) FROM MEDICATION
				"""
			)

			return self.cursor.fetchone()[0]

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()

	def count_appointment(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				"""
				SELECT COUNT(*) FROM APPOINTMENTS
				"""
			)

			return self.cursor.fetchone()[0]

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()

	def retrieve_staff(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				SELECT * FROM STAFF
				"""
			)

			return self.cursor.fetchall()

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()


	def retrieve_med(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				SELECT * FROM MEDICATION
				"""
			)

			return self.cursor.fetchall()

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()


	def retrieve_staff_data(self, iD):
		print(iD)
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()
			items = []
			self.cursor.execute(
				f"""
				SELECT * FROM STAFF WHERE ID='{iD}'
				"""
			)

			items.append(self.cursor.fetchall())
			
			self.cursor.execute(
				f"""
				SELECT * FROM PRESCRIPTIONS WHERE BY='{iD}'
				"""
			)
			items.append(self.cursor.fetchall())
			self.cursor.execute(
				f"""
				SELECT * FROM APPOINTMENTS WHERE STAFF='{iD}'
				"""
			)
			items.append(self.cursor.fetchall())
			
			return items

		except sqlite3.OperationalError as e:
			print('Error here')
			return e

		finally:
			if self.connection:
				self.connection.close()


	def validate_staff(self, staff_id):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				SELECT * FROM STAFF WHERE ID='{staff_id}'
				"""
			)

			try:
				a = len(self.cursor.fetchone())

				return True

			except:
				return False

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()



	def retrieve_appointment(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				f"""
				SELECT * FROM APPOINTMENTS
				"""
			)

			return self.cursor.fetchall()

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()



	def update_stock(self, batch):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(f"SELECT IN_STOCK FROM MEDICATION WHERE BATCH_NO='{batch}'")

			updated = int(self.cursor.fetchone()[0])

			if updated > 0:
				updated -= 1
			else:
				return 'empty'

			self.cursor.execute(
			f"""
			UPDATE MEDICATION SET IN_STOCK='{updated}' WHERE BATCH_NO='{batch}'
			"""
			)

		except sqlite3.OperationalError as e:
			return e

		finally:
			self.connection.commit()
			if self.connection:
				self.connection.close()



	def validate_batch(self, batch_no):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
			f"""
			SELECT * FROM MEDICATION WHERE BATCH_NO='{batch_no}'
			"""
			)

			try:
				a = len(self.cursor.fetchone())
				return True

			except:
				return False

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()



	def validate_login(self, username, password):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
			f"""
			SELECT * FROM AUTH WHERE ADMIN='{username}' AND PASSWORD='{password}'
			"""
			)

			try:
				a = len(self.cursor.fetchone())
				return True

			except:
				return False

		except sqlite3.OperationalError as e:
			return e

		finally:
			if self.connection:
				self.connection.close()
