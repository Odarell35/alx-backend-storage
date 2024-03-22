-- Create the stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE average_weighted_score FLOAT;
    
    -- Compute total weighted score and total weight
    SELECT SUM(score * weight), SUM(weight)
    INTO total_weighted_score, total_weight
    FROM scores
    WHERE user_id = user_id;
    
    -- Compute average weighted score
    IF total_weight > 0 THEN
        SET average_weighted_score = total_weighted_score / total_weight;
    ELSE
        SET average_weighted_score = 0;
    END IF;
    
    -- Insert or update average weighted score for the user
    INSERT INTO average_weighted_scores (user_id, average_score)
    VALUES (user_id, average_weighted_score)
    ON DUPLICATE KEY UPDATE average_score = average_weighted_score;
END //
DELIMITER ;

