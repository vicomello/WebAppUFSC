----
-- phpLiteAdmin database dump (http://www.phpliteadmin.org/)
-- phpLiteAdmin version: 1.9.7.1
-- Exported: 5:15pm on April 1, 2019 (UTC)
-- database file: /home/ubuntu/workspace/cs50_finalproject/appeople.db
----
BEGIN TRANSACTION;

----
-- Table structure for users
----
CREATE TABLE 'users' ('user_id' integer PRIMARY KEY NOT NULL, 'username' varchar(256) NOT NULL, 'hashword' varchar(256) NOT NULL, 'email' varchar(256));

----
-- Data dump for users, a total of 37 rows
----
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('1','vica','pbkdf2:sha256:50000$pCZlYKUs$f9c333687bd93fcd6617e930bc25ee27fd9692b686bb9bf8787782a78b94c0ad',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('2','teste','pbkdf2:sha256:50000$bLvd0Ch3$b949d8ad5d248e602350a76e8cab5e4f80ef9c48c77b4314a2f2c2053e1909bd',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('3','haha','pbkdf2:sha256:50000$dnU3HKqU$c19768e2c150c6390453dcfb1379ed817cc31f8231247b4b8c0a35bf68a24ab1',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('4','oi','pbkdf2:sha256:50000$7VnS8r7l$b78f10666a8d9be103d38aed0a3b9412964e2b3e0a98a62bd56d39e536bc318b',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('5','aaa','pbkdf2:sha256:50000$2pd7l6Qh$72a949dc4412a7f5af030c1ce7a7f05eff83d483120164a936ed399f65746bcc',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('6','vic','pbkdf2:sha256:50000$NoBqVw4b$c796a32dbc18662a823ffd0c5f53bb1cfa5473bb68758bdf52ad9126cac50a48',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('7','a','pbkdf2:sha256:50000$it0uvQUT$5c39eadfce5e9c3864cab6142530ec6c6116c0b0fa04b942443292c8dfa75198',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('8','b','pbkdf2:sha256:50000$G6pubzyc$505ce8894994fff6746bad8766cee449aed12fa235d8b4b6054d16028930feab',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('9','c','pbkdf2:sha256:50000$17R1hAYi$af1483fade588ca6c6a827b9fc3c7bf6f15be6ab9314d30202fb0f08f84e1964',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('10','d','pbkdf2:sha256:50000$ASCgFtta$f7bd39f5dcd57cabcba5c04777264159a2d33b90d955afaa66113911821fe8d0',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('11','s','pbkdf2:sha256:50000$qSlXhztf$c9d5f2f82ba2db0e2fb67a7600d3dcbabb8da6c30dba41e647d3977b458cc559',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('12','h','pbkdf2:sha256:50000$nj76obfm$ec06055c0724425dbded8420bccc7566ec2be87d18a84bd757616c3d03850bb0',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('13','vicosa','pbkdf2:sha256:50000$xvM6NnXj$1a171e9646d15026f0ab0a63004f82c1ba648800355c901eaec5986fc47a2733',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('14','testinho','pbkdf2:sha256:50000$FZftIag6$c7d68aebd7a7895b986bf1d1eb6fe5683b8eca4eb68a493459b22a8e55d28ec2',NULL);
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('15','lala','pbkdf2:sha256:50000$NEaJ2IDH$b7f3d26ebf489385eb99691b8715dc55c93eb63446bf509f1dfe0f027ee62513','lala@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('16','caca','pbkdf2:sha256:50000$UH6APLZJ$1e3d4e4aa706d85499a3b623836dc0180055c1a274852528b1dc8965b7c4acd5','caca@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('17','bb','pbkdf2:sha256:50000$Pc8h20Dj$bc5f98fd9c9c02568620e52b76eb666266b55712bd831c0fa04bce7e6de7c65a','bb@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('18','teste1','pbkdf2:sha256:50000$li93T4ii$b6d22673b07f2fd699211ac09a13c462bf9f877ba1e8a19b9cf8de05884f6d4e','teste1@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('19','teste2','pbkdf2:sha256:50000$fBuEm2FK$e78733a9b9ebf039530022215cd09635b1d7347222def3c323ea4cee8909ee07','teste2@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('20','victoria','pbkdf2:sha256:50000$UPYMX5bh$ecc4cf4c382d388272d561dfa79e875fc50f7052ccca58b8becc52996d9e6d1f','vic.oldemburgo@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('21','aline','pbkdf2:sha256:50000$jqdg2jPx$742d646ae81b4000aed121841039f811034862768667990d0f75d9b97fcd2555','azimerman@college.harvard.edu');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('22','cacimba','pbkdf2:sha256:50000$vQE3ERPT$dd9fd41838c3c278cd1d286ef22f58a38ab23dc9a3b155b1bed598441aeab834','a@com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('23','vicas','pbkdf2:sha256:50000$LeNhVmVy$f5942813e169f72798256f55ab7c5c64b33a78bdf10ecf5c9d634355814c77b0','vicas@com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('24','Philly','pbkdf2:sha256:50000$86Gri8Pr$582b9b564622e0135dec5cc61ed2f39e14aec8d337065fd6e6c3ff4ff603909b','nightcrawlr007@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('25','pico','pbkdf2:sha256:50000$T73XMzjU$e105c96465544fc2dd4091a8503b60b68f77a7df9f797a3901960c08588c55c8','petershagen@college.harvard.edu');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('26','vchambers','pbkdf2:sha256:50000$6asjzvw3$7903b98b920118842e981cbc9ba9068c09c6ffaf32504e10dafe6f0fe710b11f','vanessachambers6@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('27','nini','pbkdf2:sha256:50000$rnnU66VK$57327a20def410d1167e52baee96cc94ca7253ff2e70ae8a70aa7cfbdcc8628f','nini@hotmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('28','pedrowe','pbkdf2:sha256:50000$ECdfQLnW$aeeede66fe89b875e6c42cfae3650297a6b041486d74a3816255d34e6566faf6','pedrowe@uol.com.br');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('29','Foz','pbkdf2:sha256:50000$vee4kA7C$f0a73a42b10b1c2b1db66adee652a34cba4185279f51de7be0b627e774bcc88d','FouziaRaza@college.harvard.edu');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('30','Arthur Vieira','pbkdf2:sha256:50000$qruhxn4Y$754ff56fdfc3e9a840e3443949a5b7d90b97b1e98e5d57aa7ec49136b856674c','arthurgmvieira@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('31','bsaintcyr','pbkdf2:sha256:50000$9m3Y4epN$93cba8530740076698a599af5625e01958dbabfb2f8730641a5f4232b35fc3a4','brsaintcyr@fas.harvard.edu');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('32','cmarseille','pbkdf2:sha256:50000$quUu5s0j$4377c44bdc7281e6efced21ea67e04018205819c70935d132730e4ed17ed4cb3','cmarse2895@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('33','Dcaturello','pbkdf2:sha256:50000$SKQpjrjW$ad13889f72ce2adf78a163a6ccbc2220ad89b88889c0002ffb09392a3afb38ae','dcaturello@college.harvard.edu');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('34','kiyeon','pbkdf2:sha256:50000$9arwc0nT$7926208e9101c9ce7bc3a4cb2123b09993811c4b2065c608b4a13dc978a6b948','kiyeonlee@college.harvard.edu');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('35','CarlaSchroeder','pbkdf2:sha256:50000$YqSK4UQ2$55919400c7f75ca06160a1cd5fcf54c066a803a10655f21797f8dacfa5e6f926','carlaschroeder@college.harvard.edu');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('36','MoritzBonacker','pbkdf2:sha256:50000$SqM1MMDb$a536c128a63a8f04e8c7c9962409d39cf2b4603eea8c73ea86743c33488d1a9e','moritzb98@gmail.com');
INSERT INTO "users" ("user_id","username","hashword","email") VALUES ('37','testano','pbkdf2:sha256:50000$GdbPvp4A$24ac95c0a685abaa312a45f8b9b126dc8fec82f48946744562255ab77dae2ccb','testano@testano.com');

----
-- Table structure for traits
----
CREATE TABLE 'traits' ('key' integer PRIMARY KEY NOT NULL, 'EXT' integer NOT NULL DEFAULT (0), 'AGR' integer NOT NULL DEFAULT (0), 'CON' integer NOT NULL DEFAULT (0), 'EST' integer NOT NULL DEFAULT (0), 'OPN' integer NOT NULL DEFAULT (0), 'user_id' INTEGER, 'lf1' boolean DEFAULT NULL, 'lf2' boolean DEFAULT NULL, 'lf3' boolean DEFAULT NULL, 'lf4' boolean DEFAULT NULL, 'lf5' boolean DEFAULT NULL, 'lf6' boolean DEFAULT NULL, 'lf7' boolean DEFAULT NULL, 'lf8' boolean DEFAULT NULL, 'lf9' boolean DEFAULT NULL, 'lf10' boolean DEFAULT NULL, 'lf11' boolean DEFAULT NULL, 'lf12' boolean DEFAULT NULL, 'lf13' boolean DEFAULT NULL, 'lf14' boolean DEFAULT NULL, 'lf15' boolean DEFAULT NULL);

----
-- Data dump for traits, a total of 10 rows
----
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('1','5','5','5','5','5','7','0','1','0','0','0','1','0','0','0','0','0','0','0','0','0');
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('2','0','0','0','0','0','6','0','0','0','0','1','0','0','0','0','1','0','0','0','0','0');
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('3','-3','5','5','-21','11','15','0','0','0','0','1','0','0','0','0','1','0','0','0','0','0');
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('4','0','5','3','-16','10','16','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0');
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('5','0','2','2','-6','4','17','0','0','1','0','0','0','0','0','0','0','0','0','1','0','0');
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('6','0','10','10','-30','20','18','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('7','0','10','10','-30','20','19','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('8','-1','4','4','-12','8','21','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('9','-1','5','3','-11','7','20','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "traits" ("key","EXT","AGR","CON","EST","OPN","user_id","lf1","lf2","lf3","lf4","lf5","lf6","lf7","lf8","lf9","lf10","lf11","lf12","lf13","lf14","lf15") VALUES ('10','-9','-3','10','-16','28','24','1','0','1','1','0','0','0','1','0','1','0','0','0','0','1');
COMMIT;
