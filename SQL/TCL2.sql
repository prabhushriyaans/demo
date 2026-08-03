-- USE  Project;
DELIMITER $$
CREATE PROCEDURE transection_db(IN id INT, IN debit DOUBLE, OUT user_n VARCHAR(50),OUT OLD_Amount DOUBLE,OUT NEW_Amount DOUBLE)

BEGIN
-- SELECT user_name, Amount FROM users as u INNER JOIN bank as b
-- ON u.user_id=b.user_id WHERE u.user_id=id;
    
    DECLARE c_balance DOUBLE;
    SELECT user_name INTO user_n FROM users WHERE user_id=id;
    SELECT Amount INTO OLD_Amount FROM bank WHERE user_id=id;
    SELECT Amount INTO c_balance FROM bank WHERE user_id=id;
    IF c_balance < debit THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSUFICIENT BALANCE';
    ELSE 
    UPDATE bank SET Amount =c_balance - debit
    WHERE user_id=id;
    SELECT Amount INTO NEW_Amount FROM bank WHERE user_id=id;
END IF;
END $$
DELIMITER ;

