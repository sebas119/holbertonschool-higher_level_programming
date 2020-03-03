-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
USE `hbtn_0d_usa`;
SELECT cities.id `id`, cities.name `name` FROM cities
    WHERE state_id = (SELECT states.id `id` FROM states WHERE states.name = 'California')
    ORDER BY cities.id;
