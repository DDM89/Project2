
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    password_hash TEXT,
    restaurant_id TEXT,
    admin BOOLEAN
);

CREATE TABLE kitchen (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE menu (
    id SERIAL PRIMARY KEY,
    dish TEXT,
    allergies TEXT,
    active BOOLEAN,
    images TEXT,
    kitchen_id INTEGER
);

sql_write(
        "INSERT INTO users (email, name, password_hash, restaurants, admin) VALUES (%s, %s, %s, true)",
        [email, name, password_hash, restaurants]
    )

DELETE FROM users WHERE kitchen_id = 1;
DELETE FROM kitchen_table WHERE kitchen_id = 1;

SELECT * FROM menu WHERE kitchen_id = 7 AND active = TRUE;

-- cafe Sydney
INSERT INTO menu (dish, allergies, active, images, kitchen_id) VALUES ('Baby Octopus', '["Garlic", "Onion", "Seafood", "Gluten"]',
 true, 'https://theupsider.com.au/wp-content/uploads/2019/08/Cafe-Sydney-lunch-4.jpg', 7);

INSERT INTO menu (dish, allergies, active, images, kitchen_id) VALUES ('Vegan Dosa', 'Nuts, Onion, Garlic',
 true, 'https://images.happycow.net/venues/1024/83/77/hcmp83779_749424.jpeg', 7); 

INSERT INTO menu (dish, allergies, active, images, kitchen_id) VALUES ('Beef Tenderloin Red Wine Jus', 'Dairy, Onion, Garlic',
 true, 'https://cafesydney.com/cms_uploads/images/15_beef-tenderloin.jpg', 7);  

-- eggs flour water
INSERT INTO menu (dish, allergies, active, images, kitchen_id) VALUES ('pasta aglio e olio', 'Dairy, Onion, Garlic, Gluten',
 true, 'https://www.irishtimes.com/polopoly_fs/1.3017237.1490014825!/image/image.jpg_gen/derivatives/ratio_1x1_w1200/image.jpg', 8);

 INSERT INTO menu (dish, allergies, active, images, kitchen_id) VALUES ('Lasagna', 'Dairy, Onion, Garlic, Gluten',
 true, 'https://www.thewholesomedish.com/wp-content/uploads/2018/07/Best-Lasagna-550-500x375.jpg', 8);

 INSERT INTO menu (dish, allergies, active, images, kitchen_id) VALUES ('fettuccine alfredo', 'Dairy, Onion, Garlic, Gluten',
 true, 'https://hips.hearstapps.com/delish/assets/17/36/1504715566-delish-fettuccine-alfredo.jpg', 8);   