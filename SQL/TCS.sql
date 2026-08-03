DELIMITER $$
CREATE PROCEDURE t_roll(user_id INT, i_amount DOUBLE)
BEGIN
    START TRANSACTION;
    UPDATE bank SET Amount = Amount + i_amount WHERE user_id = user_id;
    SAVEPOINT s1;
    UPDATE bank SET Amount = Amount - i_amount WHERE user_id = user_id;
    ROLLBACK TO s1;
    COMMIT;
END$$