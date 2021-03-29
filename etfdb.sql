CREATE TABLE toy(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC NOT NULL);

INSERT INTO toy (name, price)
VALUES ('duck', 1.49);



CREATE TABLE etf (
    etfid SERIAL PRIMARY KEY,
    symbol TEXT TIMESTAMP WITHOUT TIME ZONE ,
    message TEXT,
    source TEXT,
    url TEXT,
    author TEXT);

CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    name TEXT NOT NULL,
    exchange TEXT NOT NULL,
    isEtf BOOLEAN NOT NULL);

CREATE TABLE ark_etf (
    etfId INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    CONSTRAINT FK_etfId FOREIGN KEY etfID REFERENCES stock(id));

create table holding(
    etfId INTEGER NOT NULL,
    date DATE NOT NULL,
    stockId INTEGER NOT NULL,
    numShares INTEGER NOT NULL,
    marketValue INTEGER NOT NULL,
    weight NUMERIC NOT NULL,
    PRIMARY KEY (etfId, date, stockId),
    CONSTRAINT fk_etf_id FOREIGN KEY (etfId) REFERENCES stock(id),
    CONSTRAINT fk_ticker_id FOREIGN KEY (stockId) REFERENCES stock(id)
);