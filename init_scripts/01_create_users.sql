-- Create administrator
CREATE USER adminuser WITH PASSWORD 'adminpassword' SUPERUSER;

-- Create read-only users
CREATE USER user1 WITH PASSWORD 'user1password' ;
CREATE USER user2 WITH PASSWORD 'user2password';

-- Grant SELECT privilege on all existing tables
GRANT SELECT ON ALL TABLES IN SCHEMA public TO user1;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO user2;

-- Grant USAGE privilege on all existing sequences
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO user1;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO user2;

-- Grant CONNECT privilege to the database
GRANT CONNECT ON DATABASE mydatabase TO user1;
GRANT CONNECT ON DATABASE mydatabase TO user2;