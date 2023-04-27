CREATE DATABASE computer_components;

USE computer_components;

CREATE TABLE components (
    component_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    brand VARCHAR(255),
    model VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    category ENUM('CPU', 'GPU', 'RAM', 'Motherboard', 'Storage', 'Power Supply', 'Cooling') NOT NULL
);

CREATE TABLE manufacturers (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    website VARCHAR(255)
);

CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    component_id INT NOT NULL,
    rating TINYINT NOT NULL,
    comment TEXT,
    FOREIGN KEY (component_id) REFERENCES components (component_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    order_date DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL
);

CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    component_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (order_id),
    FOREIGN KEY (component_id) REFERENCES components (component_id)
);

CREATE TABLE component_manufacturer (
    component_id INT NOT NULL,
    manufacturer_id INT NOT NULL,
    PRIMARY KEY (component_id, manufacturer_id),
    FOREIGN KEY (component_id) REFERENCES components (component_id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers (manufacturer_id)
);

INSERT INTO components (name, description, brand, model, price, quantity, category)
VALUES
('Intel Core i9-11900K', '11th Gen Intel Core i9 Desktop Processor', 'Intel', 'BX8070811900K', 549.99, 10, 'CPU'),
('AMD Ryzen 9 5900X', '12-core, 24-thread desktop processor', 'AMD', '100-100000061WOF', 549.99, 15, 'CPU'),
('ASUS TUF Gaming GeForce RTX 3080', 'NVIDIA Ampere Streaming Multiprocessors', 'ASUS', 'TUF-RTX3080-O10G-GAMING', 1149.99, 5, 'GPU'),
('Corsair Vengeance RGB Pro 32GB DDR4', 'High performance DDR4 memory', 'Corsair', 'CMW32GX4M2Z3600C18', 219.99, 20, 'RAM'),
('Samsung 970 EVO Plus 2TB', 'NVMe SSD for high performance storage', 'Samsung', 'MZ-V7S2T0B/AM', 399.99, 8, 'Storage');

INSERT INTO manufacturers (name, website)
VALUES
('Intel', 'https://www.intel.com/'),
('AMD', 'https://www.amd.com/en'),
('ASUS', 'https://www.asus.com/'),
('Corsair', 'https://www.corsair.com/'),
('Samsung', 'https://www.samsung.com/us/');

INSERT INTO reviews (component_id, rating, comment)
VALUES
(1, 4, 'Great processor, fast and reliable'),
(1, 5, 'Amazing performance, worth the money'),
(2, 4, 'Excellent processor, but a bit pricey'),
(3, 5, 'Awesome GPU, runs cool and quiet'),
(4, 4, 'Good RAM, looks great with RGB lighting'),
(5, 5, 'Super fast SSD, great for gaming and productivity');

INSERT INTO orders (customer_name, order_date, total)
VALUES
('John Smith', '2023-04-23', 1339.98),
('Jane Doe', '2023-04-22', 2299.97),
('Bob Johnson', '2023-04-22', 879.96);

INSERT INTO order_items (order_id, component_id, quantity)
VALUES
(1, 1, 1),
(1, 4, 2),
(2, 1, 1),
(2, 2, 1),
(2, 3, 1),
(2, 5, 1),
(3, 2, 1),
(3, 5, 2);

INSERT INTO component_manufacturer (component_id, manufacturer_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);