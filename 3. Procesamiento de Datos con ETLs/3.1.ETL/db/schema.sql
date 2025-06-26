/* agg_data */

CREATE TABLE agg_data (
  id SERIAL PRIMARY KEY,
  store INT NOT NULL,
  date date NOT NULL,
  revenue decimal(10,2) DEFAULT NULL
);
