import sqlite3
 
def HW_Feb13_db():
    
    conn = sqlite3.connect("HW_Feb13.db") 
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE employees (№ ID integer PRIMARY KEY, 
                                              'name' text NOT NULL, 
                                              'surname' text, 
                                              'sex' text NOT NULL, 
                                              'age' text NOT NULL)""")
    cursor.execute("""INSERT INTO employees VALUES ('1', 'Mircea', 'Lucescu', 'M', '74')""")
    employees = [('2', 'Marian', 'Aliuțe', 'M', '42'),
                ('3', 'Ionuț Costinel', 'Mazilu', 'M', '38'),
                ('4', 'Cosmin', 'Bărcăuan', 'M', '41'),
                ('5', 'Alexandru', 'Tudose', 'M', '32')]
    cursor.executemany("INSERT INTO employees VALUES (?,?,?,?,?)", employees)
    conn.commit()
    cursor.close()
    conn.close()
    
    conn = sqlite3.connect("HW_Feb13.db") 
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE salaries ('№ ID' integer FOREIGN KEY, 
                                              'name' text NOT NULL, 
                                              'surname' text PRIMARY KEY, 
                                              'salary 2019, €' varchar2 NOT NULL, 
                                              'salary 2020, €' varchar2 NOT NULL),
                                              FOREIGN KEY (№ ID) REFERENCES employees (№ ID)""")
    cursor.execute("""INSERT INTO salaries VALUES ('1', 'Mircea', 'Lucescu', 20000, 27000)""")
    salaries = [('2', 'Marian', 'Aliuțe', 8000, 8500),
                ('3', 'Ionuț Costinel', 'Mazilu', 11000, 14000),
                ('4', 'Cosmin', 'Bărcăuan', 7000, 9200),
                ('5', 'Alexandru', 'Tudose', 5000, 5800)]
    cursor.executemany("INSERT INTO salaries VALUES (?,?,?,?,?)", salaries)
    conn.commit()
    cursor.close()
    conn.close()
    
    conn = sqlite3.connect("HW_Feb13.db") 
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE positions (№ ID integer FOREIGN KEY, 
                                              'name' text NOT NULL, 
                                              'surname' text PRIMARY KEY, 
                                              'current position' varchar2 NOT NULL, 
                                              'position on a pitch' varchar2 NOT NULL),
                                              FOREIGN KEY (№ ID) REFERENCES employees (№ ID)""")
    cursor.execute("""INSERT INTO positions VALUES ('1', 'Mircea', 'Lucescu', 'antrenor', 'atacant')""")
    positions = [('2', 'Marian', 'Aliuțe', 'director sportiv', 'mijlocaș'),
                ('3', 'Ionuț Costinel', 'Mazilu', 'asistent antrenorului', 'atacant'),
                ('4', 'Cosmin', 'Bărcăuan', 'selecționerul', 'fundaș'),
                ('5', 'Alexandru', 'Tudose', 'antrenorul echipei de rezervă', 'fundaș')]
    cursor.executemany("INSERT INTO positions VALUES (?,?,?,?,?)", positions)
    conn.commit()
    cursor.close()
    conn.close()
       
HW_Feb13_db()# Homework-Feb-18
# Homework-Feb-18
