CREATE TABLE `products` (
`productID` char(10) NOT NULL,
PRIMARY KEY (`productID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `users` (
`userID` char(14) NOT NULL,
`profileName` varchar(255) NOT NULL,
PRIMARY KEY (`userID`)
)  ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `reviews` (
`reviewId` int(10) unsigned NOT NULL AUTO_INCREMENT,
`userId` char(14) NOT NULL,
`productId` char(10) NOT NULL,
`helpfulness` float DEFAULT NULL,
`helpful` int(3) DEFAULT NULL,
`total` int(3) DEFAULT NULL,
`score` int(1) DEFAULT NULL,
`ts` timestamp DEFAULT 0,
`summary` varchar(255) DEFAULT NULL,
`text` text DEFAULT NULL,
PRIMARY KEY (`reviewId`),
UNIQUE KEY `user_product` (`userId`, `productId`),
KEY `productId` (`productId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

