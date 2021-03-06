DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS budgets;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    restricted BOOLEAN 
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    restricted BOOLEAN 
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id INT NOT NULL REFERENCES merchants(id),
    description VARCHAR(255),
    tag_id INT NOT NULL REFERENCES tags(id),
    price FLOAT,
    date DATE
);

CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    amount FLOAT
);