
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for qh_to_love
-- ----------------------------
DROP TABLE IF EXISTS `qh_to_love`;
CREATE TABLE `qh_to_love` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `msg` varchar(2048) NOT NULL,
  `counts` int(12) NOT NULL DEFAULT '0' COMMENT '发送次数',
  `status` int(12) NOT NULL DEFAULT '1' COMMENT '默认：1：可用，0：不可用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=256 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of qh_to_love
-- ----------------------------
INSERT INTO `qh_to_love` VALUES ('1', '我什么时候能变成风，然后就可以一直吻你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('2', '遇见喜欢，大概就像一艘从来不靠岸的船终于找到港湾。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('3', '没有一种不通过蔑视，忍受和奋斗就可以征服的命运。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('4', '只是想和你在一起简单平淡足以。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('5', '俄只是觉得喜欢和爱不同，仅此而已。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('6', '找你害怕烦到你，不找你，我真的很想你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('7', '每一杯普通的水，和喜欢的人在一起就会变成雪碧。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('8', '你是我的东，你是我的西，你是我的南，你是我的北。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('9', '小的时候不懂爱‘但心中却充满爱，N年后明白了什么叫爱‘所以再也没爱过。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('10', '生活中值得高兴的事情太多，别把目光都盯在那些让你不愉快的事情上。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('11', '爱的时候想着一个人是快乐的。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('12', '据说手机24小时从不关机的，人心中都有一个让他牵挂的人。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('13', '爱你的人不会轻易离开，轻易离开你的人也许没那么爱你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('14', '幸福是，两双眼睛，看一个未来。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('15', '爱会磨平你一身的棱角，褪去你一身的骄傲。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('16', '不能阻止他人的非议，自己活得自在才好！只要你相信你自己是善良的，那就OK了。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('17', '借我一刻光阴，把你看的真切，绾正青丝白雪。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('18', '喜欢你的声音，喜欢你爱我，他其实，是她一直的梦想。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('19', '爱一个人，爱到八分刚刚好，所有的期待和希望希望都只有七，八分，剩下的两三分用来爱自己。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('20', '被你喜欢过，真的很难觉得别人有那么喜欢我。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('21', '面对着白纸，却不知道该怎么抒写我们的感情。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('22', '如果下一秒就要分离，上一秒我也要努力吻你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('23', '用手挡住射进眼里的阳光，就像挡住对你的思念，挡不住。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('24', '我只希望我们都好好的。好好的笑，好好的过，好好的一辈子。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('25', '我愿用我一世容颜换你半世流离。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('26', '很多时候，都是最后才领悟，而爱情，却不能重头再来。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('27', '我的生活朴实无华，但正是因为有了你而变得豪华。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('28', '你如果觉得我的爱是枷锁，我宁可背上所有，也要牢牢的铐住你让你离不开我。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('29', '我愿化作你的天使，永远守候在你的身边。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('30', '希望有一天，我可以不用对着手机屏幕和你说晚安，你就在我身边。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('31', '不管我们之前遇到过什么人，现在只想你是我的最后一个故事。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('32', '爱你就像呼吸，有时调皮地憋一会儿，可终究知道对于停止爱你，我无能为力。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('33', '我爱你，如鲸向海、鸟投林，不可避免，退无可退。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('34', '把前半生都给你，后半生我就潦草收场吧。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('35', '当你驯服我，我将赠予你，虔诚的爱恋，以及不悔的决心。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('36', '一辈子住在一个地方，一辈子睡在一个人身边。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('37', '被爱着的她，连撑伞的样子都像捧着一束玫瑰花。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('38', '爱让我义无反顾扮演了硬派，也让我们歇斯底里变成病态。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('39', '你说是我们相见恨晚，我说为爱你不够勇敢。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('40', '我的幸福，就是和你温暖的过一辈子。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('41', '爱你就算会经历暴风雨，还是不离不弃陪着你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('42', '你笑起来的样子最好看，你的声音最好听，更令人开心的是你是我的。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('43', '不管怎样我都觉得你是最好的，这就是偏爱，偏爱是不需要理由的。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('44', '把你的名字刻在烟上，吸进肺里，留在离我心里最近的地方。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('45', '多陪陪女朋友，她没有篮球，没有游戏，只有你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('46', '你最好的给予，就是还能让我留在你的身边。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('47', '不再甜言蜜语，不是感情淡了，而是成熟了，知道要用行动兑现自己的承诺。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('48', '把自己当衣服给你穿，换你暖，遮你羞，避你寒，悉心装扮，衬你好看。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('49', '有哪本教科书，可以教我如何留住你的心？', '0', '1');
INSERT INTO `qh_to_love` VALUES ('50', '整个世界，我最爱的地方就是你的左右。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('51', '十指连心，我握住了你的手指，是不是也能握住你的心？', '0', '1');
INSERT INTO `qh_to_love` VALUES ('52', '我的心很完整是因为，你在里面。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('53', '爱的如此虚伪，伤的如此彻底。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('54', '爱就要在一起，不爱就会放弃。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('55', '喜欢你的人除了我还有很多，但我只有你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('56', '待我白发苍苍，你会不会依旧如此，给我倾世温柔？', '0', '1');
INSERT INTO `qh_to_love` VALUES ('57', '我穿越四季只为融化在你怀里，谢谢你敢与我相爱。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('58', '累了吗，停在我怀里吧，我给你一生的安定。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('59', '我们谁都没有联系谁，可是我却一直在想你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('60', '如果可以，我想陪你一起疯，就像陪你蹲下做一只蘑菇一样。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('61', '和你说话时，你可要好好看看，我脑海中的弹幕，因为，里面全是爱你的小句子。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('62', '白昼与黑夜将无法阻挡我俩的深深思念', '0', '1');
INSERT INTO `qh_to_love` VALUES ('63', '不管今世也来世也好，我所要的只有你', '0', '1');
INSERT INTO `qh_to_love` VALUES ('64', '不论天涯海角只要你需要我的时候我就会飞回你的身边', '0', '1');
INSERT INTO `qh_to_love` VALUES ('65', '喝了你酿的爱情的酒，我愿意沉醉而不愿醒。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('66', '铃声是我的问候，歌声是我的祝福，雪花是我的贺卡，美酒是我的飞吻，清风是我的拥抱，快乐是我的礼物。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('67', '你的微笑，是我这辈子见过最美的景色，我想收藏这样的风景一辈子。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('68', '你开心的时候，我的心情艳阳高照;你悲伤的时候，我的心情雷雨交加。因为我爱你，所以我愿感受你所有的感受。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('69', '你是一颗种子，落在我心底生根发芽，我会因你快乐而快乐，因你幸福而幸福，我会珍惜你在我心里的位置，今生来世都不许你挪地!', '0', '1');
INSERT INTO `qh_to_love` VALUES ('70', '其实天很蓝，阴云总要散;其实海不宽，此岸连彼岸;其实泪也甜，当你心如愿;其实我要你快乐每一天!', '0', '1');
INSERT INTO `qh_to_love` VALUES ('71', '牵你的手，朝朝暮暮，牵你的手，等待明天，牵你的手，走过今生，牵你的手，生生世世。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('72', '亲爱的，我爱你就像喝白开水，吃饭一样，就像呼吸一样的自然，不眠不息，温温柔柔，所以我会永远爱你!', '0', '1');
INSERT INTO `qh_to_love` VALUES ('73', '如果能用一辈子换你停留在我视线中..我将毫不保留', '0', '1');
INSERT INTO `qh_to_love` VALUES ('74', '如果生活是一条双行道，就请你让我牵着你的手，穿行在茫茫人海里，永远不会走丢。我爱你!', '0', '1');
INSERT INTO `qh_to_love` VALUES ('75', '时间的巨轮无法抹去我对你的思念纵使海枯石烂，你的身影永存于我心中', '0', '1');
INSERT INTO `qh_to_love` VALUES ('76', '万紫千红百事顺，朝气蓬勃事正成，百炼成钢有耐心，过硬本领苦中求，八面受敌是模范，愿你更上一层楼。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('77', '我爱你，所以我的眼里只能看见你，我爱你，所以我的世界只围绕着你转。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('78', '我爱你的心是直到世界末日也不变', '0', '1');
INSERT INTO `qh_to_love` VALUES ('79', '我不想做你人生的插曲，我想成为你一生的主题曲。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('80', '我的人生放荡不羁，不曾为谁停留，但自从遇到你，我会用余生来守护你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('81', '我希望几十年后，你还陪在我的身边，在我的臂弯，像个孩子。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('82', '我要你知道，在这个世界上，总有一个人是会永远等着你的。无论什么时候，无论在什么地方，总会有这么一个人。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('83', '我与你不需要任何的琐碎来证明在乎的分量，只有不言而喻的默契。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('84', '无论这山水有多么的遥远，都不能阻断我以你的思念，请你记住，我的心总是在你的身边，为你祝愿，直到永远!', '0', '1');
INSERT INTO `qh_to_love` VALUES ('85', '与你的相识，我才知道缘分是多么的奇妙，让我来照顾你，我会珍惜我们遇见的每一分每一秒。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('86', '遇到你，是缘分;喜欢你，是命中注定;爱上你，是我情非得已;想念你，是我逼不得已。我会用心去爱你，我爱你!', '0', '1');
INSERT INTO `qh_to_love` VALUES ('87', '这一生我只牵你的手……因为今生有你早已足够', '0', '1');
INSERT INTO `qh_to_love` VALUES ('88', '总是在老歌里，我才会充分意识到自己的温情。流金岁月，配上简单的老歌，也便配上了真实的悲欢。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('89', '不敢正视你的眼睛，我怕我每个眼神都像是在表白', '0', '1');
INSERT INTO `qh_to_love` VALUES ('90', '对你,不管阴晴圆缺,也不变。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('91', '就是想粘着 还想给你很多很多的爱', '0', '1');
INSERT INTO `qh_to_love` VALUES ('92', '你对我而言太珍贵了，珍贵到你在我身边的每一分钟我都当做最后一分钟去过，所以我才要马不停蹄的去拥抱你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('93', '你让我道歉，还是让我告白。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('94', '你是我的乍见之欢，你是我的眼神所向，你是我的温柔的归宿，你是我的嘴角扬起的理由。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('95', '你是我今生渡不过的劫 多看一眼就心软 拥抱一下就沦陷', '0', '1');
INSERT INTO `qh_to_love` VALUES ('96', '你有多特别呢，万千人中走过，即便近视也能一眼望到你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('97', '怦然心动无非就是恋爱了，感觉全世界只有我们。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('98', '恰似无边心海，我身陷其中，唯有你能渡我。恰似烈日灼灼，我喉咙干涩，唯有你能解渴。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('99', '人生不长，该珍惜就别保持不近不远，我只想再抱你紧一点。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('100', '如果你不怕麻烦的话那就麻烦你跟我在一起吧', '0', '1');
INSERT INTO `qh_to_love` VALUES ('101', '如果你觉得不开心的话，你就尽情的欺负我好了，反正我很喜欢你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('102', '如果你愿意，我就喜欢你，如果你不愿意，我就单相思，你愿意吗？', '0', '1');
INSERT INTO `qh_to_love` VALUES ('103', '如果我不讨你喜欢，你直接爱上我好了。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('104', '世界上最温暖的两个字是从你口中说出的晚安。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('105', '世上最浪漫和最自私的话就是：你是我一个人的。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('106', '事情总刚要分先后，你先全世界后', '0', '1');
INSERT INTO `qh_to_love` VALUES ('107', '说不过你，但喜欢你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('108', '我把思念都告诉了心跳，心里的你有没有偷听到。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('109', '我还是会笑 只是笑中不再温暖 带着冷漠与疏离', '0', '1');
INSERT INTO `qh_to_love` VALUES ('110', '我觉得我一点都不蠢至少在喜欢你这件事上我无师自通。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('111', '我就是喜欢你，你就是我的', '0', '1');
INSERT INTO `qh_to_love` VALUES ('112', '我躺在你睫毛上的时候你能不能别眨眼睛。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('113', '雪糕的甜味你有，九月清晨的美好你有，总之，我喜欢的样子你都有', '0', '1');
INSERT INTO `qh_to_love` VALUES ('114', '一直忘了告诉你，我有多幸运，遇见的是你。想有一天挽着你的手，去敬各位来宾的酒。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('115', '众生皆苦，你是草莓味。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('116', '星星爱着月亮，于是与月亮围绕；蝴蝶爱着花朵，于是与花朵缠绵；鸟儿爱着森林，于是与森林盘旋；我爱着你，于是与你相伴，一辈子。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('117', '伱要恋爱，为何我很难过，以为伱会是我的，原来是一厢情愿。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('118', '体会过那种滋味，让我明白了思念是一种幸福也是一种煎熬。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('119', '你就是我一生等待的最爱，我要一生一世来爱你，纵然一生平平淡淡同尝甘与苦，我只愿能为你挡风遮雨共度朝与暮。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('120', '我寂寞时常常想起你，不是由于寂寞才想起你，是因为寂寞时想起的只有你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('121', '现实很残酷，我也会跟着你的脚步；梦想很虚无，我也会陪你在路途；再大的困难险隘，也抵不过我对你的信赖；不要说看不明白，因为你心里早有由来。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('122', '细数曾经相濡以沫的岁月，才发现，最傻的是自己，对不起，没有好好爱过你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('123', '如果我的名字是你拒绝别人的理由，那么我定会愿意为你放弃所有。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('124', '不准你做世界上第一幸福的人，因为有你我才是最幸福的。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('125', '每天我的动力就是见到你，并和你说说话。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('126', '没有人能像你一样，第一眼就让我为你心动。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('127', '想着你，是浪漫的甜蜜，思绪朦胧成些许的希冀；念着你，是温馨的旋律，情谊铺垫在心底，如诗如画的爱意，在我的梦幻里，给你幸福我会竭尽全力！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('128', '学会了与人分享爱，还必须学会不要紧捉着所爱不放，最伟大的爱就是做些对所爱的人，最有利的事，即使那会令你心疼。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('129', '你知道吗？上帝要我在你和水两个里面选择一个，另一个将永远消失，我毫不犹豫地选择了你，因为对于我来说，需要你，就好像我需要水一样。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('130', '请你从我梦里出去，或者，再也不要离开。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('131', '我把思念的歌唱给海洋听，海洋把这心愿交给了天空，天空又托付流云，化作小雨轻轻的飘落在你窗前，你可知道最近为何多变化吗？全都是因为我在想你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('132', '只要有一丝希望我就绝不放弃希望！我就是一个不轻易认输！不轻易放弃希望的人！所以我一直在拼搏在努力！自从与你相爱以来我就有了梦想！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('133', '曾经的甜蜜是何其珍贵，相拥的怀抱还有丝丝余味，离去的你已不再与我分甘同味，任凭爱的花朵枯萎，你也不再会给丝毫安慰！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('134', '你的笑颜，如一道清泉，流动清澈的情缘，漂洗我心的蜜甜，触动我情的涅？，爱你是我最大的选择权，永远是不变的宣言。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('135', '帅气的你，美丽的我，蓝蓝的月亮，傻傻的笑容，喜欢你的好，喜欢你的坏，幽幽的湖边，清清的湖水，我决定爱你到底！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('136', '你们可知南湘是席城的梦，你们可知顾里是顾源的命，你们可知林萧是崇光的未来，你们可知友情是唐宛如的全部。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('137', '白昼与黑夜将无法阻挡我俩的深深思念。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('138', '和你一起我不介意天天喝白开水、啃面包，只要开水是你亲手倒的，面包是你亲手切的。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('139', '读它你欠我一个拥抱；删除它欠我一个吻；储存它欠我一个约会；如回复你欠我全部；如不回你就是我的。亲爱的选一项吧！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('140', '怪你过分的美丽，令我无法早点把爱说出口。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('141', '也许是我不懂你，是我的任性让你不肯回头看我多一眼。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('142', '请别把我当傻瓜，有些事不是我不知道，只是我看在眼里，埋在心里。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('143', '在你遇到最困难的时候，我一定会说：别怕，还有我呢！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('144', '如果可以，我愿意把所有关于你我的记忆一口喝掉，任凭它在我的胃里反复反复的发酵。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('145', '清水在冰块的心里，微风在白云的心里，星星在长夜的心里，你在我的心里。虽然隔山隔水，相思没有距离，感觉到了吗？我的心时时与你在一起！想你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('146', '我执君之手，共担丽日风雨；今生愿为醇酒，润君之喉绵绵无休；为你做颗红烛，照亮你的前途；爱如双手，永伴你的左右。512吾要爱：我要爱你永久！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('147', '曾几何时众里寻她，所为伊人在何方。时光如风不停留，千山万水情相连。山山水水也有情。亲爱的，好想你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('148', '当岁月老去，我依然记得曾经夕阳下我们美好的誓言！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('149', '习惯你爱我，习惯你宠我，习惯你给的全部的全部。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('150', '你是我最爱的人，可你爱的却不是我，我也只希望你幸福、快乐！也希望你不要阻止我对你永远的关心，呵护！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('151', '没有一支歌曲比你更甜美，没有一首诗篇比你更恬谈，没有一处风景比你更清新，没有一缕月光比你更温柔。你就是我生命里永远的爱人。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('152', '我对你的爱犹如滔滔江水，连绵不绝，恰逢天降甘露，充入小溪，你恰路过，口渴饮水，我入你肚，无法遁逃，自此你中有我，我中有你，永不分离。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('153', '即使已经知道，你早已不爱我。却还是依然想你留在我身边。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('154', '对不起，我一直在欺骗自己，原来我一直爱的是你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('155', '钱可以存到银行，你可以寸到我心里，没钱的时候才想起银行，而你存在我心里，时时刻刻都在想你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('156', '我的世界很简单，只有我在乎的跟不在乎的，以及爱的你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('157', '你知道吗，你的一举一动都在牵动着我的心。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('158', '风陪着柳絮掠过脸颊，恰似你的温柔偎依在我怀下。淡雅的体香随着情话，任凭妩媚浪漫飘下。轻声细语，呢喃心话，要你开心一下。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('159', '原本阴雨绵绵，忽然阳光初现；原本平静无波，忽然风急浪涌；原本生活苍白，忽然充满色彩。一切，都是因为你的出现，让我的世界瞬间充满活力和精彩！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('160', '曾经的我不懂的珍惜，现在的我谈不上有多爱你，但我会用我的一切来证明我对你的爱。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('161', '我想你时你想我了吗？不管我们相距多远前面的路多长，我只想说认识你真好。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('162', '你的脸是那么靓，你的人是那么棒，想你想得心慌慌，爱你爱得好紧张，不知怎么把口张。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('163', '我很想知道，当我的名字滑过你耳朵，你脑海中会闪现些什么。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('164', '不管与你的路有多苦，擦干眼泪告诉自己不许哭；不管我的心里有多痛楚，爱！我都会用一生去呵护。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('165', '让我牵着你的手，陪你一起走。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('166', '桃花开，杏花开，朵朵鲜艳惹人爱，枝头开，心中开，开的世界充满爱，想出来，做出来，时间到了说出来，一句我爱你，和春天同步。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('167', '我用一万句谎言扎成一束风骚的媚眼向你扫射过去，你倒在血泊中，千疮百孔的身子嵌满丘比特的子弹', '0', '1');
INSERT INTO `qh_to_love` VALUES ('168', '曾经我是一个任性的孩子，任性的以为你只属于我，我只属于你。谢谢你告诉我，这个世界上谁都不是谁的，我们终究只会，属于我们自己。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('169', '远远的你好似一只风筝，用心来放飞你，线系在你身上，握在我手里。也许风起时细细的线会断，但总会有或长或短的一段，一如往昔的系着你、系着我。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('170', '我们在轻雾缭绕的清晨分别。露，莹莹的，像你纯真的眼睛；雾，蒙蒙的，像我浓浓的离愁。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('171', '早已过了花季年华，不在誓言天长地久，但求我们曾经拥有了这样一份实实在在的真情。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('172', '我心灵并不空虚，但我的心里总有一个空的位置。没有人可以使用，因为那是你的专用座椅。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('173', '你让我明白暗恋原来是这么一回事。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('174', '柔柔月色，为你挥洒一地浪漫；艳艳玫瑰，为你奉上一腔真情；真真情感，为你厮守一生幸福；痴痴话语，为你表白一世真爱：亲爱的，我爱你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('175', '当一个女孩向你倾诉她的烦恼，那不是抱怨，那是她对你的信任。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('176', '茫茫人海遇见你；大街小巷认识你；相识万千独为知己。缘分让我们漫步，我们的眼神碰触，我们的心相属！512吾要爱日，牵手一生，可否？', '0', '1');
INSERT INTO `qh_to_love` VALUES ('177', '我心里有个小秘密你想不想知道？让风悄悄告诉你，我喜欢你，真的好喜欢。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('178', '你就像池塘里的荷随意绽放，让我扑朔迷离；那一池满是醉人的眼波，让思念止不住流淌；我愿做那池塘里的水，让这一生的幸福，留住你和我。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('179', '星月不误，因为你已离去；清风不语，因为我在哭泣；我也不语，因为还在想你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('180', '一直以为我们可以从今直至永远，可是那只是我以为。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('181', '不因寂寞才想你，而因想你才寂寞。孤独的感觉之所以如此之重，只是想你太深。书不尽言，言不尽意，意不尽情，情不自禁地对你说声：我真的好想你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('182', '我只是想对你说我有一颗爱你的心，这已足以。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('183', '如果你选择我，那么我一定会珍惜你一辈子。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('184', '对你视而不见，对你眷眷爱恋，对你长长思念，对你，只为了偷偷爱你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('185', '如果没有遇见你，我将会是在哪里，如果没有遇见你，我又会过的怎么样？是否还会有浇不尽的相思和躲不开的寂寞？因为遇见你，我感到很幸福！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('186', '我的日子因你而璀璨，我的心因你而辽阔，我的感情因你而充实，我的生活因你而美满。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('187', '此时此刻，我在想你；不露声色，藏在心底。未经准许，谁碰碎我的涟漪？你总是可以轻易走进我的梦里。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('188', '情浓意浓，所有的思念，化作在无边的等待中。你侬我侬，所有的语言，融在了温暖的问候中。月圆月半，所有的爱恋，存在于彼此的心中。爱你永不变。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('189', '思念是一种习惯，距离是一份考卷，测量相爱的誓言。就算有时短暂分开，也让我们勇敢面对没有彼此的孤单，因为爱会让我们变得勇敢。想你，爱你到永远！。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('190', '花儿艳艳，如同你美丽的容颜；雨丝飘飘，恰似你似水的柔情；轻风阵阵，就是你入微的体贴；每时每刻我都想告诉你：我真的好爱你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('191', '我不曾认识你，你不曾认识我。命运本就是巧合。我与你相遇在一起。不是爱情在悬崖陡峭，而是幸福就在你我的弹指之间。屏幕后面的你，知道我在想你么？', '0', '1');
INSERT INTO `qh_to_love` VALUES ('192', '爱是一个约定，直到相守终身；爱情不是游戏，总得付出真情；爱是张信用卡，得不断充值；爱情是个苹果，要外表，更要甜的内心。祝真爱伴你一生！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('193', '我一定要拿回那个月光宝盒带你一起回去跟他们说清楚。我不管别人怎么说我，我也不怕后世会有千千万万的人对我唾骂，我要一个人承担下来。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('194', '轻轻的一个吻让我难以忘怀。亲吻的味道真甜美，那是美好幸福的记忆。你的爱像火苗把我的心燃烧。你的情似柔水，把我来拥抱。亲吻节，让爱飞翔让情燃烧！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('195', '遇见你是我的缘，想念你是我的情，此情时时有，此爱无绝期。月有阴晴圆缺，人有悲欢离合，对你的想念不停歇。海内存知己，天天在想你。我想你，发个短信祝福你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('196', '爱着你，就像沐浴日光一般的温暖，看你纯净的眼神，就可以抵挡人生所有的微尘；迷上你，就像迷上灿烂的星辰，听你温柔的耳语，就可停住幸福的时针！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('197', '走过岁月，经历沧桑，暮然回首，依然不忘的是你那可爱的笑颜。20海誓山盟日，许下永久不变的誓言。牵着你的手，恋着你的情，一生永远不改变。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('198', '见你英俊的姿容已经一个星期了，真如七年一样。在这七天里，你的倩影无时不刻在我心海浮现！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('199', '我们是并肩的两棵小树，我们是相互交错的两条小路，我们是二重唱的两个声部，宝贝，我们好好相处，一定会幸福！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('200', '日里想着你，夜里念着你，梦里绕着你，眼里望着你，手里握着你，心里爱着你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('201', '饭菜有盐才香甜，蝶儿有意双翩跹，你我有爱把手牵，海枯石烂心不变，生生世世情相连，此情此意比金坚，发条短信表诺言，爱你直到一万年！亲爱的，你的腿是不是很酸啊？你可在我的脑海里跑了一整天！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('202', '记得那默默的一瞬间，你悄悄地把我的心取走，从此我热血沸腾的心，全都交给了你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('203', '远方的你是否无恙？在这个思念的季节里，改变的是我的容颜，不变的是永远牵挂你的心！真心愿你快乐！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('204', '亲吻父母乐滋滋，父母心中多甜蜜；亲吻孩子笑嘻嘻，笑脸如花多美丽；亲吻爱人笑咪咪，幸福如火多亲密。14亲吻情人节，祝你爱情永远，亲情无限！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('205', '短信代表我的心，网络传达我的情；佳人何日能相会，千百里外有知音。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('206', '相思，是首歌，缠绵悱恻，浪漫无限；相恋，是杯酒，回味悠长，悦动心弦；相爱，是块糖，甜蜜幸福，有滋有味；表白，是真心：爱你无悔，一生一世！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('207', '想念一个人需要冲动的感觉；思念一个人需要深刻的烙印；接近一个人需要满怀的诚意；爱上一个人需要十足的勇气；忘记一个人谈何容易！我还是想你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('208', '你给了我脉脉温情，似水柔情，如火激情，深深痴情，一腔纯情，无限热情，一片真情，你是我朝思梦想的情人！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('209', '夜不再寂寞，因为惦记你，爱不再遥远，因为牵挂你，夜风来，带来了凉爽却带不来你的笑脸，夜风走，带走了对你的祝福却带不走对你的思念！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('210', '在一起的日子，久久不能忘怀。离开的日子，久久不能适应。记挂你的心，久久不能平静。对你的思念，久久不能停歇。久久日，心有灵犀，因为有你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('211', '你的青春一枝潇洒的红荷，唱着一支鲜嫩鲜嫩的恋歌。我深湖般的眼神便爬满了你绿叶的脉络。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('212', '一往情深只为你，痴心不改锁定你，真心真意不曾变，爱你在心永不变。527爱妻日，我愿我妻更快乐，开心幸福到永远！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('213', '不管阳光明媚还是阴雨霏霏，我都愿为你撑起花伞；不管灯火通明还是黑暗笼罩，我都愿为你点燃蜡烛；请你给我这个机会，让我好好爱你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('214', '如果爱你是错的话，我不想对；如果对是等于没有你的话，我宁愿错一辈子，无奈，爱已决堤，你能明白我，感觉到那份情怀吗？', '0', '1');
INSERT INTO `qh_to_love` VALUES ('215', '相识是缘起，相知是缘续，相守是缘定。是缘使我们相遇。希望我们一直走下去，从缘起到缘续，从缘续走到缘定，从缘定到永远！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('216', '今天情人节，最庸俗的是送花送草，最无聊的是逛街乱跑，最愚蠢的是胡吃喝倒，最实惠的是回家搂搂抱抱！不知道你打算怎么过呢？呵呵，情人节快乐！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('217', '离开你，象突然失去地球引力，心儿随你的背影远去，不再属于自己；想念你，相信你的心可以触及，幸福在不远处待机，只要一丁点的勇气，我就将永远的属于你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('218', '要知道，那些信签写的誓言，只不过是白纸黑字的表演。我的誓言没有那么华丽而浪漫，只是简单的：我爱你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('219', '我扬一把散沙粒粒想念漫天纷飞带给我对你的祝福，我洒下一瓢涟水滴滴飘洋流到你的心海，爱你，今生无悔，牵了你的情，爱了你的人，我会努力呵护你。一生一世！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('220', '茫茫人海，一个“缘”字，你我相逢；来来往往，一个“真”字，你我相识；平平常常，一个“诚”字，你我相知；风风雨雨，一个“心”字，你我相伴春夏秋冬。亲爱的，漫漫人生，有你相伴，无比幸福。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('221', '你粉红的笑靥，可是我五百年回眸的定格你窈窕的身子；可是我九万万次痴情的期待。太阳，铁环般滚过我的生命，请问画语呵。你能否给我花朵骤然开放般的情爱。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('222', '陷入热恋就好比从很高的屋顶往下跳，脑袋清醒的告诉你：你疯了；可心里却说：没事，我会飞的。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('223', '漫天飞舞的是谷雨时节的绵绵细雨，默默传递的是谷雨时节的默默祝福，真心祈祷的是要你永远开心快乐，谷雨时节送祝福，愿你幸福！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('224', '是你给了我无限的爱，是你抚平了我心灵的创伤，是你开化了我绝望的念头，是你执着的情感让我迷醉，是你的关爱体贴叫我留恋。老婆我好爱你哟！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('225', '快乐是一只执着的飞鸟。他不随便停住在别人的窗容，也不轻易露出笑脸，只要你能把心打开，快乐将围绕在你身旁！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('226', '我把思念的歌唱给海洋听，海洋把这心愿交给了天空，天空又托付流云，化作小雨轻轻的飘落在你窗前，最近天气为何多变？全是因为我在想你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('227', '没有拥抱敌人的勇气，没有拥抱困难的魅力，没有拥抱小三的底气，你可以拥着爱人喘口气，1214拥抱情人节，据说拥抱能带给你好运气，不过得拥对了人才会顺利！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('228', '如果可以，我愿自己是你最信赖的港湾，风雨飘摇时等着你靠岸；如果可以，我愿是你最期待的风景线，孤独寂寞时等着你期盼，爱你就要等着你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('229', '孤单并非与生俱来的，从爱上一个人的那一刻开始，与她在一起会觉得时间不够用，不与她在一起会觉得时间用不完，与她相守会有说不完的话题，与她分开后却不愿多说半句，这就是所谓的爱情。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('230', '遇到你我失去了爱情免疫力，令我相思成疾，为了惩罚你，我要进行一场爱情战役，把你困进爱情漩涡里，用柔情蜜语好好折磨你，一生一世绝不放你出去。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('231', '蝴蝶翻飞，成双成对，花间翩翩舞姿美；鸳鸯戏水，成双成对，相偎相依心沉醉；轿车四轮，成双成对，同行海角并肩飞。可愿与我双飞。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('232', '想起你是我浓浓的真心，牵挂你，是我美美的情怀，惦念你，是我久久的心思，思念你，是我绵绵的企盼，爱着你，是我不变的主题。最近怎么样？', '0', '1');
INSERT INTO `qh_to_love` VALUES ('233', '你对我的诱惑让我不能自拔，你对我的吸引让我情不自禁，你对我的引诱让我不能自已，亲吻情人节到了，我要对你进行狂吻～～好吃的冰淇淋，呵呵，亲吻情人节到了，要开心哟。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('234', '你是夜空，我是眼睛，愿陪你一起数星星；你是带刺的玫瑰，我是蝴蝶，愿为你伤身伤心；你是永恒，想你的感觉，像爱人民币一样坚定，只为博得你的欢心！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('235', '外面风大雨大，屋子里有人，这是我爱你的感觉，我要让火红的玫瑰为你夜夜绽放！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('236', '你笑颜如花，我深深迷恋，你柔情凝视，我日日温暖，1214拥抱情人节，发条短信送给伊人，字字表达我心意，句句话语温暖你，声声祝福送给你，拥抱情人节，只愿与你携手到老！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('237', '真爱就像一本写满人生的小说，不经意地阅读，很有可能会错过；认真地品味，多数时候会流泪；顺其自然点就会很好。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('238', '珠穆朗玛，我的爱在哪里安了家，死海深沟，我的情在哪里发了芽，企鹅的家，那也是我思念的家，北极熊的窝，那也是我追求的后方，包纳四海为了啥，就为了给你谈个情，说个爱，你也就别再拘谨啦！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('239', '有了你，于是我就拥有了一份快乐；有了你，于是我少了许多的烦恼；有了你，于是我有了一份牵挂；有了你，于是我信了情，信了缘；有了你，我这辈子都该知足了。亲，我爱你！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('240', '如果说，我的每一次思念可以化做天上飘落的尘埃，那么不久，这个世界上将出现第二个撒哈拉沙漠。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('241', '走在匆忙的路上，幸好有你相伴，隔不断的是牵挂，弥足珍贵的是温暖心头的是那份感动，难以抗拒是彼此的清澈惦念，亲，祝福你天天开心，一切安好。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('242', '用鲜花铺成情路！用我的柔情甜甜地呵护你，用我的蜜意柔柔地缚着你，我会让你永远沉浸在幸福之中。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('243', '岁月更迭，素年锦时，稚嫩始终是青春的剪影，为了你我愿是个长不大的孩子，常常把寻情的风筝放飞在爱的天空，把那些爱意系在线上，放飞爱情，于是生活中便多了幸福的牵挂。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('244', '爱太重，很难再移动。情太深，反而难成真。为爱所困，为爱而心碎！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('245', '一片云代表我的情，一颗露珠代表我的爱！你问我爱你有多深，我会告你：“一生爱你永不移！”爱情是人生中最美好的东西。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('246', '如果你是山，我愿是小河，我绕你；如果你是茶叶我愿是开水，我泡你；如果你是云，我愿是风，我追你。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('247', '我把我的思念变成文字，我知道这文字并不优美，但却代表我这彻骨的爱恋，如果爱一个人是一段苦乐参半的旅程，我也愿意一直这样走下去。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('248', '短信不贵，牵挂无价，想念不多，想到最真，相距再远，电波牵线，此刻想你，我的心声，如果不信，打开短信，快乐送你，想念给我，友情长存。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('249', '誓要爱，和幸福一世相约，和美满一生相伴。和真情一路同行，和爱恋一眼万年。最重要的是一辈子和你不离不散，亲爱的，我发誓爱你一辈子，412快乐。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('250', '给你的思念，用信封包起来让邮局帮我送给你；给你的礼物，用快递装起来让物流帮我送给你；对你的祝福，我用短信记下来，让移动帮我传过去。天天快乐。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('251', '我知道寒流来到，你遭遇风霜。我知道如今的日子，你有太多的苦恼。我知道所有的语言，都无法安慰你的悲伤。只轻轻的告诉你，生活中会有美好！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('252', '你当我是个风筝，要不把我放了，要不然就收好带回家，别用一条看不见的情思拴着我，让我心伤。', '0', '1');
INSERT INTO `qh_to_love` VALUES ('253', '缘是爱的开始，情是爱的过程，就让我们共同在缘和情的海洋里寻找爱的结果吧！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('254', '365天天天想着你，8760时时梦见你，525600分分拥抱你，31536000秒秒吻着你！亲爱的，嫁给我吧！', '0', '1');
INSERT INTO `qh_to_love` VALUES ('255', '即便满心孤寂满泪忧郁，我也会把半数的忧伤揉进甜蜜，把真爱植入我行囊中的记忆，从此不论我走到哪里去，只要你一句深情地话语，我都将飞进你梦里！', '0', '1');
