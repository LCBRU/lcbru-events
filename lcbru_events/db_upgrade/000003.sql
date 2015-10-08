CREATE TABLE genvasc_collaborators_meeting (
        id INTEGER PRIMARY KEY AUTO_INCREMENT
    ,   name VARCHAR(100) NOT NULL
    ,   spaces INTEGER NOT NULL
    )
;

CREATE UNIQUE INDEX idx_genvasc_collaborators_meeting_name
ON genvasc_collaborators_meeting (name)
;
