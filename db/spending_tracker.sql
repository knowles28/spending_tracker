DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    price FLOAT,
    date DATE,
    merchant_id INT NOT NULL REFERENCES merchants(id),
    tag_id INT NOT NULL REFERENCES tags(id)
)
