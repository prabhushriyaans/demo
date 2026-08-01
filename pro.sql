DELIMITER $$
CREATE PROCEDURE User_bank_Details()
BEGIN
     SELECT user_name, B_acc as Account_No, Amount FROM users as u INNER JOIN bank as b ON u.user_id=b.user_id; 
END$$
DELIMITER ;