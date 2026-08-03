DELIMITER $$
CREATE TRIGGER User_logs
AFTER INSERT ON users
FOR EACH ROW
BEGIN
     INSERT INTO user_logs (user_id, action, action_time) VALUES (NEW.user_id, 'INSERT', NOW());
END$$
DELIMITER ;