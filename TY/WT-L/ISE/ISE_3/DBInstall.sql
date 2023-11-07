PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        email TEXT,
        phone_number TEXT,
        department_name TEXT,
        prn TEXT
    );
INSERT INTO User VALUES(1,'Aseem Aniket Athale','athaleaseem@gmail.com','7887880897','AIML','2122000421');
INSERT INTO User VALUES(2,'A','a@a.com','3232','DS','2');
INSERT INTO User VALUES(3,'B','asas@asas.com','98989','ASA','3');
INSERT INTO User VALUES(4,'C','asaasas@asas.com','99999','sdasda','323');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('User',4);
COMMIT;
