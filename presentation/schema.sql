DROP TABLE IF EXISTS sections;
DROP TABLE IF EXISTS slides;
DROP TABLE IF EXISTS slide_blocks;
DROP TABLE IF EXISTS block_type;
DROP TABLE IF EXISTS persona;
DROP TABLE IF EXISTS use_case;;

CREATE TABLE sections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    sectionSort INTEGER NOT NULL DEFAULT 1,
    include boolean NOT NULL DEFAULT 1

);

CREATE TABLE slides (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slideNumber INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    include boolean NOT NULL DEFAULT 1,
    skippable boolean NOT NULL DEFAULT 0,
    sectionId boolean NOT NULL DEFAULT 0,
    slideTime integer NOT NULL DEFAULT 0,
    slideTimeCum integer NOT NULL DEFAULT 0
);
CREATE TABLE slide_blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    slideId INTEGER NOT NULL,
    blockNumber INTEGER NOT NULL DEFAULT 1,  
    personaId INTEGER NOT NULL,
    textCallout TEXT  NULL, -- Text the user is calling out (presented in a text balloon)
    contentType TEXT NOT NULL DEFAULT 'List',
    contentText TEXT NULL,
    blockTypeId INTEGER NOT NULL DEFAULT 1,
    blockImage TEXT NULL
);

CREATE TABLE block_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    type TEXT NOT NULL
);


CREATE TABLE persona (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    persona TEXT NOT NULL,
    avatarWoman TEXT NOT NULL,
    avatarMan TEXT NOT NULL,
    personaGender TEXT NULL,
    personaName TEXT NULL,
    include INTEGER NOT NULL DEFAULT 1
    
);


CREATE TABLE use_case (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    personaName TEXT NOT NULL,
    description TEXT NOT NULL,
    personaGender TEXT NOT NULL,
    personaId INTEGER NOT NULL DEFAULT 10

);

-- CREATE TABLE persona_user (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     firstName TEXT NOT NULL,
--     gender TEXT NOT NULL,
--     personaId INTEGER NOT NULL
-- );
