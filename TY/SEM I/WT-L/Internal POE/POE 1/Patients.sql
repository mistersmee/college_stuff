PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            patient_id TEXT NOT NULL,
            patient_admit_date DATE,
            room_no INT,
            discharge_date DATE,
            clerk TEXT NOT NULL
        );
INSERT INTO patients VALUES(1,'Aseem Athale','37','2003-08-22',666,'2023-08-22','Aseem Athale');
INSERT INTO patients VALUES(2,'Vladimir Putin','4','2023-11-07',2,'2023-11-17','Aseem Athale');
INSERT INTO patients VALUES(3,'Joe Biden','3','2023-11-04',33,'2023-11-05','Aseem Athale');
INSERT INTO patients VALUES(4,'Justin Trudeau','8','2023-11-10',88,'2023-11-11','Aseem Athale');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('patients',4);
COMMIT;
