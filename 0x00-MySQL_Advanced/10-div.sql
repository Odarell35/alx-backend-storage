-- Create the SafeDiv function
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    IF b = 0 THEN
        RETURN 0; -- Return 0 if the second number is 0
    ELSE
        RETURN a / b; -- Return the result of division
    END IF;
END //
DELIMITER ;

