CREATE TABLE genvasc_collaborators_practice (
        id INTEGER PRIMARY KEY AUTO_INCREMENT
    ,   practiceCode VARCHAR(50) NOT NULL
    )
;

CREATE UNIQUE INDEX idx_genvasc_collaborators_practice_practice_code
ON genvasc_collaborators_practice (practiceCode)
;

CREATE TABLE genvasc_collaborators_delegate (
        id INTEGER PRIMARY KEY AUTO_INCREMENT
    ,   practiceId INT NOT NULL
    ,   fullname VARCHAR(100) NOT NULL
    ,   email VARCHAR(200) NOT NULL
    ,   role VARCHAR(50) NOT NULL
    ,   dietary VARCHAR(200) NOT NULL
    ,   meeting VARCHAR(50) NOT NULL
	,	CONSTRAINT fk_genvasc_collaborators_delegate_practiceId FOREIGN KEY (practiceId) REFERENCES genvasc_collaborators_practice(Id)
    )
;

CREATE INDEX idx_genvasc_collaborators_delegate_practice_id
ON genvasc_collaborators_delegate (practiceId)
;
