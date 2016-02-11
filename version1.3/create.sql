CREATE TABLE `products` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `Titles` varchar(255) COLLATE utf8_bin NOT NULL,
    `Prices` double(255) COLLATE utf8_bin NOT NULL,
    `Dates` varchar(255) COLLATE utf8_bin NOT NULL,
    `Image` varchar(255) COLLATE utf8_bin NOT NULL,
    `Shipping` varchar(255) COLLATE utf8_bin NOT NULL,
    `Ship_From` varchar(255) COLLATE utf8_bin NOT NULL,
    `Auction` varchar(255) COLLATE utf8_bin NOT NULL,
    `Bids` int(255) COLLATE utf8_bin NOT NULL,
    `Bids_Text` varchar(255) COLLATE utf8_bin NOT NULL,
    `Link` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;
