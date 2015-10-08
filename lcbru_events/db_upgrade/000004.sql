ALTER TABLE genvasc_collaborators_delegate
ADD meetingId INTEGER NOT NULL
;

CREATE INDEX idx_genvasc_collaborators_delegate_meeting_id
ON genvasc_collaborators_delegate (meetingId)
;

ALTER TABLE genvasc_collaborators_delegate
ADD CONSTRAINT fk_genvasc_collaborators_delegate_meeting_id
FOREIGN KEY (meetingId)
REFERENCES genvasc_collaborators_meeting(id)
;