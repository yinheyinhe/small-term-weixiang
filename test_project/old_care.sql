/*
 Navicat Premium Data Transfer

 Source Server         : Jackson
 Source Server Type    : MySQL
 Source Server Version : 50022
 Source Host           : localhost:3000
 Source Schema         : old_care

 Target Server Type    : MySQL
 Target Server Version : 50022
 File Encoding         : 65001

 Date: 11/07/2021 20:38:59
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for employee_info
-- ----------------------------
DROP TABLE IF EXISTS `employee_info`;
CREATE TABLE `employee_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ORG_ID` int(11) NULL DEFAULT 1,
  `CLIENT_ID` int(11) NULL DEFAULT 1,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
  `gender` char(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别',
  `phone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `id_card` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `birthday` datetime NULL DEFAULT NULL,
  `hire_date` datetime NULL DEFAULT NULL,
  `resign_date` datetime NULL DEFAULT NULL,
  `imgset_dir` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '/images/employee/',
  `profile_photo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '/static/image/pic.jpg',
  `DESCRIPTION` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ISACTIVE` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '1',
  `CREATED` datetime NULL DEFAULT NULL,
  `CREATEBY` int(11) NULL DEFAULT NULL,
  `UPDATED` datetime NULL DEFAULT NULL,
  `UPDATEBY` int(11) NULL DEFAULT NULL,
  `REMOVE` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of employee_info
-- ----------------------------
INSERT INTO `employee_info` VALUES (1, 1, 1, '测试1', '男', '15987452322', '362151185421301', '2021-07-11 00:00:00', '2021-07-11 11:01:02', NULL, '/images/employee/', '/static/images/pic.jpg', NULL, '1', '2021-07-11 11:01:13', NULL, '2021-07-11 20:37:28', NULL, NULL);
INSERT INTO `employee_info` VALUES (2, 1, 1, '测试2', '女', '15987452322', '3695574122121', '2021-07-11 11:00:54', '2021-07-11 11:01:02', NULL, '/images/employee/', '/static/images/pic.jpg', NULL, '1', '2021-07-11 11:01:13', NULL, '2021-07-11 11:43:53', NULL, NULL);
INSERT INTO `employee_info` VALUES (3, 1, 1, '测试3', '女', '15987452322', '362151185421301', '2021-07-11 00:00:00', '2021-07-11 11:01:02', NULL, '/images/employee/', '/static/images/pic.jpg', NULL, '1', '2021-07-11 11:01:13', NULL, '2021-07-11 12:03:38', NULL, NULL);

-- ----------------------------
-- Table structure for event_info
-- ----------------------------
DROP TABLE IF EXISTS `event_info`;
CREATE TABLE `event_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_type` int(11) NULL DEFAULT NULL COMMENT '事件类型',
  `event_date` datetime NULL DEFAULT NULL,
  `event_location` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `event_desc` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `oldperson_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of event_info
-- ----------------------------

-- ----------------------------
-- Table structure for oldperson_info
-- ----------------------------
DROP TABLE IF EXISTS `oldperson_info`;
CREATE TABLE `oldperson_info`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ORG_ID` int(11) NULL DEFAULT NULL,
  `CLIENT_ID` int(11) NULL DEFAULT NULL,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
  `gender` char(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别',
  `phone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `id_card` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `birthday` datetime NULL DEFAULT NULL,
  `checkin_date` datetime NULL DEFAULT NULL,
  `checkout_date` datetime NULL DEFAULT NULL,
  `imgset_dir` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '/images/oldperson/',
  `profile_photo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '/static/images/pic.jpg',
  `room_number` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `firstguardian_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `firstguardian_relationship` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `firstguardian_phone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `firstguardian_wechat` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `secondguardian_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `secondguardian_relationship` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `secondguardian_phone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `secondguardian_wechat` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `health_state` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `DESCRIPTION` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ISACTIVE` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '1',
  `CREATED` datetime NULL DEFAULT NULL,
  `CREATEBY` int(11) NULL DEFAULT NULL,
  `UPDATED` datetime NULL DEFAULT NULL,
  `UPDATEBY` int(11) NULL DEFAULT NULL,
  `REMOVE` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`ID`)
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of oldperson_info
-- ----------------------------
INSERT INTO `oldperson_info` VALUES (1, NULL, NULL, '测试1', '男', '1853667952', '3625442052544', '2021-07-11 13:21:36', '2021-07-11 13:21:40', NULL, '/images/oldperson/', '/static/images/pic.jpg', '1182', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '良好', NULL, '1', '2021-07-11 13:21:46', NULL, '2021-07-11 20:23:54', NULL, NULL);
INSERT INTO `oldperson_info` VALUES (2, NULL, NULL, '测试2', '女', '1853667952', '3625442052544', '2021-07-11 13:21:36', '2021-07-11 13:21:40', NULL, '/images/oldperson/', '/static/images/pic.jpg', '1182', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '良好', NULL, '1', '2021-07-11 13:21:46', NULL, NULL, NULL, NULL);
INSERT INTO `oldperson_info` VALUES (3, NULL, NULL, '测试3', '女', '1853667952', '3625442052544', '2021-07-11 13:21:36', '2021-07-11 13:21:40', NULL, '/images/oldperson/', '/static/images/pic.jpg', '1182', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '良好', NULL, '1', '2021-07-11 13:21:46', NULL, NULL, NULL, NULL);
INSERT INTO `oldperson_info` VALUES (4, NULL, NULL, '测试4', '男', '1853667952', '3625442052544', '2021-07-11 13:21:36', '2021-07-11 13:21:40', NULL, '/images/oldperson/', '/static/images/pic.jpg', '1182', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '良好', NULL, '1', '2021-07-11 13:21:46', NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ORG_ID` int(11) NULL DEFAULT 1,
  `CLIENT_ID` int(11) NULL DEFAULT 1,
  `UserName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
  `Password` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密码',
  `REAL_NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `SEX` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `EMAIL` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `PHONE` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `MOBILE` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `DESCRIPTION` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ISACTIVE` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '1',
  `CREATED` datetime NULL DEFAULT NULL,
  `CREATEBY` int(11) NULL DEFAULT NULL,
  `UPDATED` datetime NULL DEFAULT NULL,
  `UPDATEBY` int(11) NULL DEFAULT NULL,
  `REMOVE` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '0',
  `DATAFILTER` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `theme` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `defaultpage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '登录成功页面',
  `logoimage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '显示不同logo',
  `qqopenid` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '第三方登录的凭证',
  `appversion` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '检测app的版本号',
  `jsonauth` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT ' app权限控制',
  PRIMARY KEY USING BTREE (`ID`)
) ENGINE = InnoDB AUTO_INCREMENT = 67 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES (62, 1, 1, 'admin', 'admin', NULL, '男', NULL, NULL, NULL, NULL, '1', NULL, NULL, '2021-07-11 07:36:22', NULL, '0', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `sys_user` VALUES (63, 1, 1, 'JacksonYuu', '123456', NULL, '男', NULL, '1524792300', NULL, NULL, '1', '2021-07-10 15:35:59', NULL, '2021-07-10 20:30:44', NULL, '0', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `sys_user` VALUES (65, 1, 1, 'jackson', '123456', NULL, '女', '111@qq.com', '15935745552', NULL, NULL, '1', '2021-07-11 07:57:07', NULL, '2021-07-11 11:56:52', NULL, '0', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `sys_user` VALUES (66, 1, 1, '测试5', NULL, NULL, '男', NULL, '19896255332', NULL, NULL, '1', '2021-07-11 10:09:15', NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for volunteer_info
-- ----------------------------
DROP TABLE IF EXISTS `volunteer_info`;
CREATE TABLE `volunteer_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ORG_ID` int(11) NULL DEFAULT 1,
  `CLIENT_ID` int(11) NULL DEFAULT 1,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '姓名',
  `gender` char(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别',
  `phone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `id_card` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `birthday` datetime NULL DEFAULT NULL,
  `checkin_date` datetime NULL DEFAULT NULL,
  `checkout_date` datetime NULL DEFAULT NULL,
  `imgset_dir` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '/images/volunteer/',
  `profile_photo` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '/static/images/pic.jpg',
  `DESCRIPTION` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ISACTIVE` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '1',
  `CREATED` datetime NULL DEFAULT NULL,
  `CREATEBY` int(11) NULL DEFAULT NULL,
  `UPDATED` datetime NULL DEFAULT NULL,
  `UPDATEBY` int(11) NULL DEFAULT NULL,
  `REMOVE` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of volunteer_info
-- ----------------------------
INSERT INTO `volunteer_info` VALUES (1, 1, 1, '测试1', '女', '15978639563', '362151185421301', '2021-07-11 00:00:00', '2021-07-11 10:58:27', NULL, '/images/volunteer/', '/static/images/pic.jpg', NULL, '1', '2021-07-11 10:58:36', NULL, '2021-07-11 12:06:07', NULL, NULL);
INSERT INTO `volunteer_info` VALUES (2, 1, 1, '测试2', '女', '15978639563', '3695411223155', '2021-07-11 10:58:25', '2021-07-11 10:58:27', NULL, '/images/volunteer/', '/static/images/pic.jpg', NULL, '1', '2021-07-11 10:58:36', NULL, NULL, NULL, NULL);
INSERT INTO `volunteer_info` VALUES (3, 1, 1, '测试3', '男', '15978639563', '3695411223155', '2021-07-11 10:58:25', '2021-07-11 10:58:27', NULL, '/images/volunteer/', '/static/images/pic.jpg', NULL, '1', '2021-07-11 10:58:36', NULL, NULL, NULL, NULL);
INSERT INTO `volunteer_info` VALUES (5, NULL, NULL, '测试4', '女', '18632574225', '362151185421301', '2021-07-11 00:00:00', '2021-07-11 12:07:24', NULL, '/images/volunteer/', '/static/images/pic.jpg', NULL, NULL, '2021-07-11 12:07:24', NULL, '2021-07-11 12:07:34', NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
