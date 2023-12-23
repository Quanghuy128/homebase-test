-- Create a stored procedure for managing blog posts
DELIMITER //

CREATE PROCEDURE ManageBlogPost(
    IN action VARCHAR(10),  -- Action: 'add', 'get', 'update', 'delete'
    IN post_id INT,
    IN title VARCHAR(255),
    IN content TEXT,
    IN user_id INT
)
BEGIN
    -- Add a new blog post
    IF action = 'add' THEN
        INSERT INTO posts (title, content, user_id, created_at, updated_at)
        VALUES (title, content, user_id, NOW(), NOW());

    -- Retrieve post details
    ELSEIF action = 'get' THEN
        SELECT * FROM posts WHERE id = post_id;

    -- Update a blog post
    ELSEIF action = 'update' THEN
        UPDATE posts
        SET title = title, content = content, updated_at = NOW()
        WHERE id = post_id;

    -- Delete a blog post
    ELSEIF action = 'delete' THEN
        DELETE FROM posts WHERE id = post_id;

    END IF;
END //

# DROP PROCEDURE IF EXISTS ManageBlogPost;

CREATE PROCEDURE ManageComment(
    IN action VARCHAR(10),  -- Action: 'add', 'get', 'update', 'delete'
    IN comment_id INT,
    IN post_id INT,
    IN user_id INT,
    IN content TEXT
)
BEGIN
    -- Add a comment to a blog post
    IF action = 'add' THEN
        INSERT INTO comments (post_id, user_id, content, created_at)
        VALUES (post_id, user_id, content, NOW());

    -- Retrieve comments for a blog post
    ELSEIF action = 'get' THEN
        SELECT * FROM comments WHERE post_id = post_id;

    -- Update a comment
    ELSEIF action = 'update' THEN
        UPDATE comments
        SET content = content
        WHERE id = comment_id;

    -- Delete a comment
    ELSEIF action = 'delete' THEN
        DELETE FROM comments WHERE id = comment_id;

    END IF;
END //


DELIMITER ;

-- posts
CALL ManageBlogPost('add', NULL, 'New Post Title', 'Post Content', 1);

CALL ManageBlogPost('get', 1, NULL, NULL, NULL);

CALL ManageBlogPost('update', 1, 'Updated Post Title', 'Updated Post Content', 1);

CALL ManageBlogPost('delete', 1, NULL, NULL, NULL);

-- comments
CALL ManageComment('add', NULL, 2, 2, 'Comment Content');

CALL ManageComment('get', NULL, 1, NULL, NULL);
