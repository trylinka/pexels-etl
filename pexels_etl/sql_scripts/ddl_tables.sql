-- ddl for photos table
DROP TABLE IF EXISTS photo_sources;
DROP TABLE IF EXISTS photos;

CREATE TABLE IF NOT EXISTS photos(
    id               INTEGER PRIMARY KEY,
    width            INTEGER,
    height           INTEGER,
    url              TEXT,
    photographer     TEXT,
    photographer_url TEXT,
    photographer_id  INTEGER,
    avg_color        TEXT,
    liked            INTEGER,
    alt              TEXT
);

-- ddl for photo sources table
CREATE TABLE IF NOT EXISTS photo_sources(
    id       INTEGER PRIMARY KEY,
    photo_id INTEGER,
    size     TEXT,
    url      TEXT,
    FOREIGN KEY (photo_id) references photos (id)
);
