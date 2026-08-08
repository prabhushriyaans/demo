DELIMITER $$
CREATE PROCEDURE Payment_Procedures_s(IN ID INT,IN SP_ID INT,IN Money DOUBLE,IN flag VARCHAR(5))
BEGIN
 DECLARE  AMO DOUBLE;
 SELECT Amount INTO AMO FROM bank WHERE user_id=ID;
 IF flag="yes" OR flag="YES" THEN
 START TRANSACTION;
 UPDATE BANK SET Amount=Amount-Money WHERE user_id=ID;
 UPDATE BANK SET Amount=Amount+Money WHERE service_id=(SELECT service_id FROM services WHERE service_p_id=SP_ID);
 IF Money>=AMO THEN
 ROLLBACK;
 SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT="Max Limit Reached";
 ELSEIF Money >=100000 THEN
 ROLLBACK;
 SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT="Can't transfer more than 100000";
 ELSE
 COMMIT;
 END IF;
 ELSE
 SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT="Transection not set.";
 END IF;
 SELECT user_name,B_acc as Account_number,Amount FROM users as u
 INNER JOIN service_provider as sp ON u.user_id=sp.user_id INNER JOIN Bank as b 
 ON u.user_id=b.user_id WHERE u.user_id=ID;
 SELECT service,service_request,B_acc as Account_number,Amount FROM services as s
 INNER JOIN service_provider as sp ON s.service_p_id=sp.service_p_id INNER JOIN
 Bank as b ON s.service_id=b.service_id WHERE sp.service_p_id=SP_ID;
END$$
DELIMITER ;



 

