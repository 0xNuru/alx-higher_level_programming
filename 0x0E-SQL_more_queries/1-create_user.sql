-- a script that creates a user in a server

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- best practice is to FLUSH the PREVILEGES table albeit sometimes redundant
FLUSH PRIVILEGES;

