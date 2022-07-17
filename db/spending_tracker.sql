DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(255)
);


CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    merchant_name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id INT NOT NULL REFERENCES merchants(id),
    description VARCHAR(255),
    tag_id INT NOT NULL REFERENCES tags(id),
    price FLOAT
);