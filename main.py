# coding: utf-8
import io
import urllib.parse
from threading import Thread
import struct
import time
import hashlib
import base64
import socket
import time
import pymysql
import types
import multiprocessing
import os
import sys
import getopt
import time
import threading
from fuzzywuzzy import fuzz


def search(name):
    db = pymysql.connect(host="localhost", user="user",
                         password="bupt1234", database='user')
    cursor = db.cursor()
    result = {}
    # sql = """CREATE TABLE USER (
    #          NAME  CHAR(20) NOT NULL,
    #          AGE INT,
    #          SEX CHAR(1),
    #          BALANCE FLOAT )"""
    # name="韩高轩史季同金修筠彭飞翮方飞星贺飞鸣阎奇迈熊飞文尹勇男马正德曾弘新姚博明沈乐悦戴俊喆梁英豪丁嘉誉史俊美赖子轩梁乐安冯乐意赵哲瀚赖嘉致邱兴文潘伟晔汤华美常和蔼袁天纵孟鹏飞董宜春李永新程飞鸾白敏叡谭伟祺孔炫明程祺然钱懿轩何浩穰毛宇达戴安顺何宜民白翰翮许凯复孟承教汪咏思孟承平丁嘉纳钱俊爽高天韵姜文德丁博实易宏远魏阳辉郝立诚廖睿诚郭兴学沈经武武兴生杨正祥石俊楚梁晋鹏石同光曹修伟吕星雨胡永思万德海邵天路孟涵蓄石宏峻石彬彬崔睿博戴修平姚嘉颖钟翰池彭成化龙高畅秦光辉冯翰采乔博学白昊空邱嘉懿毛景澄谭鹏天邵天翰林元化汤伟毅贾星文易兴为郑经艺陆康安林正青姜瀚玥刘玉宸郭锐利曹高岑郭兴贤潘宏硕谢建白杨嘉纳汤雅志杜浩阔秦光临彭信瑞万阳焱石泰宁汤雅志朱浦泽崔志行武逸春易德宇袁景福张弘懿朱安国谭昂雄黄乐和钱宏爽文学海金晟睿李星河顾良畴王飞捷熊兴言金欣嘉白俊捷史阳煦魏正诚任雅昶罗弘雅黎浩漫杨德业贾朋义陆建德叶宏硕常博延龙鸿飞萧星雨郑承德唐阳舒邹丰茂白鸿卓萧星驰赖智渊吴英奕周承允陈宏才邓嘉石黎承天于英喆万温瑜顾浩穰杨阳羽邵建树魏浩气潘光耀马良材魏乐咏宋志尚陈子平赵伟兆魏德佑郝嘉瑞苏弘伟赵俊茂杨永嘉田苑博徐阳德徐成文袁自珍邵欣然程华翰黄文斌董涵涤高俊驰袁英卫何飞翼江博裕汤德海许飞章蒋华皓赖鸿哲孔永年任飞跃龚良翰朱德寿许琪睿朱立群唐高超贺越彬白安易史阳秋钱建安邹成周侯宏逸张兴业许高旻任景福吕奇邃顾景铄刘安民孟阳朔程理群吕嘉澍钱致远郭彬炳顾毅然金浩大常承德彭鸿文谭和平常修永张睿思王立果张天元苏景福邹子安文建义陈文轩魏嘉茂龚弘致曹康顺罗鸿畅曹建白邹翰海梁弘致漕元纬任正业胡力言顾宏毅康阳州熊永康马建树陆景明毛烨磊朱俊英崔鸿风林浩邈任烨烁邓翔飞马鸿运傅玉宸孙彬炳常意智秦立果萧自强汪飞鸾廖理全萧志国魏黎明胡承基宋自强马翰音金玉泽王承弼漕景胜黄永宁钱乐游康和悌杜浩邈高鸿晖段康胜冯鸿飞侯博易杜阳波侯敏叡苏承嗣贾安晏顾乐心魏光济黄高峯常高驰顾阳焱康乐邦冯元德蔡鸿熙毛康成夏高飞尹冠宇许明杰曾宜民高温韦汤星光周良策冯成天邓正豪邵俊悟薛昊昊林俊发常飞文尹志专徐英哲冯修能余敏叡阎嘉谊谭锐达唐阳荣高绍元刘晗日叶浩波林乐邦吴英锐贺作人邵宏盛蒋鹏举潘博易谭文彬侯英毅朱斌蔚周建同顾英发段良工常康适吕鸿祯沈建安段经纶潘锐立董向荣邵奇思陆俊弼李飞跃万子墨许宏毅易明朗苏涵畅杨俊达白玉宸汤天禄冯庆生郝学真罗德曜孔和通彭俊健周开宇乔飞雨郑烨磊谢奇伟常学民汤阳波万阳曜谢安顺易风华姚涵映王鸿波康星纬秦光启高伟才贺阳飇田光亮白文山杜凯歌蔡昂雄曹雨华曹文耀杨峻熙袁咏德姜敏学黄睿明梁雨石吴理群潘彭祖任英纵石华池郝茂勋汤乐水蒋文瑞罗宏恺董兴昌姚良策谭天逸陈锐泽秦弘伟贾高峻曾雅达何良哲胡同光梁信鸥范睿博冯承福傅向文黎建德徐丰羽郭璞玉毛奇水郑星文白英范郝康顺史浩邈黎阳州邱德本李华采杨烨霖萧玉泽周玉堂方阳炎董鸿卓王英武罗坚诚董鸿飞姜嘉谊傅英才邓立辉董星阑苏俊健宋开霁金勇毅顾嘉庆黄哲瀚贾和惬韩弘图钱和怡冯康安薛博厚常光耀白鹏赋曾晟睿蒋宏阔毛宏富廖弘大薛安晏武雅懿魏成天杨项明邓阳炎蒋经纬朱理全彭高轩石巍昂朱智志蔡力言金文昌段承望袁经略高俊彦秦鹏鲸叶志用乔睿识邵华彩丁阳泽赵嘉许史智明廖奇略尹鹏云李嘉珍叶鹏天秦英朗潘建章任志泽贺浩穰钱涵煦冯凯定徐阳德梁嘉谊白智志范心水朱锐达唐建德姜雅惠龚安国龙嘉茂姜永元赖明远郑鸿德杨飞宇范巍然戴嘉熙朱鹏池朱鸿德薛飞航梁经义孔锐智杨伟博林弘文段高畅田建本龙意致姚英达于元纬熊正真李景胜郑哲圣孔正初王英纵张兴贤蔡才俊贺修平于星光魏天赋赖经纶汪学民卢修德钟修文戴濮存谭良平杨承嗣夏明俊黄飞捷汪文山高思博贺成周郭乐志杜玉宇石浩气常和怡易绍祺李刚洁江飞羽林宏毅高坚秉冯明朗郝浩宕赖建弼钱俊喆丁明亮谭嘉颖夏兴发武兴安薛嘉石程鹏程何和玉蔡智勇秦德业苏雅逸许建木汤华奥许瀚海谭阳嘉漕季萌袁和畅王和惬谭泽宇侯飞龙苏兴腾侯星河田宏儒江宏朗蒋明珠郭雨信张锐逸钟阳炎汪健柏于鹏鹍杜浩博阎高卓蒋博实汤锐志史乐和武刚捷丁阳焱陈高轩常成龙宋光赫马向文梁伟祺孙文轩孔鸿文阎建德傅和惬夏宜人黄锦程杨兴业郑自珍郑飞鸿顾学义宋元甲丁康时姚旭尧汪安和汤逸春曹嘉荣姚建业汤志专万阳州石乐童田信瑞冯阳华林博艺郝建柏郭雅志沈宜春袁永言赵鹏飞杜涵容钱兴运毛乐安萧君浩邵嘉泽邱奇水贾敏叡宋承颜龚飞舟戴乐邦萧和昶史子墨杜良畴龚高格陆修明文嘉慕吴鹏赋贺高杰汪兴朝范修明史瀚玥曹经艺潘和宜冯经艺曾浩壤郭英奕侯奇希贾志学朱正祥顾正诚万勇捷袁鸿运顾安邦陈明智秦泽宇金翰林范良材黄鸿卓梁奇邃叶嘉禧彭明知孟星阑郝炎彬蒋宏阔卢乐池廖理全王锐志郭弘懿吕德明熊敏才范元化李兴言孙兴旺许雅珺谭兴思萧意远程飞鹏朱高韵宋伟博郭鸿晖徐光华于永年曾翰藻熊鸿才杨安福梁飞驰潘星雨常烨磊萧明煦崔恺歌廖昊空张阳波毛和风马曾琪许景福程阳飙汪锐意程博学姚宏阔漕鸿才李天禄谭和洽周祺福姚烨霖文咏德戴涵忍林鹏池尹正业钟德厚汪高岑钱德运薛伟博郝和歌于开宇黄德寿任乐天石文瑞金华茂蒋嘉志姜鸿熙宋伟才萧奇略姚星阑史乐安邵嘉胜孙明轩沈兴昌唐浩思冯俊弼江安邦黄波涛石俊喆胡嘉瑞张元忠曾宜人彭和怡康学博崔力行傅子安曾乐家钟锐立许新立汪鹤轩姜彭泽赵志新林弘文胡永年顾蕴涵夏凯安龚宏富崔成业谭永丰文德华夏英华黄心思唐宜年金欣可郭宏邈石昂雄许飞掣段弘厚武雪峰郝和泰顾信然廖高洁石永安易子默蔡玉轩汪晗昱段涵蓄顾俊德贾俊英康康适尹建义顾浩瀚毛天空赵飞航丁嘉泽黎元亮汤彭勃曹鸿云白永嘉熊承平石逸春郭高歌龚弘和周鸿晖廖绍祺孙乐游姚力强郝宾实贾康平夏靖琪易元德秦元白唐元恺钟飞语马建修姚飞鸾董安民邹明俊张兴旺邱茂典唐德容于华翰龙毅然彭永新任良吉卢弘壮秦刚豪曹星火谢兴文秦昊英易俊美孙勇男杜凯泽黎昊英薛俊茂乔风华龚新翰江经国程鹏池叶鹏赋萧经纶潘乐志邓朋兴白溥心孟烨赫段建业胡星纬易景龙余高畅余经赋田伟晔段宜春周嘉纳白温瑜曹俊民高华辉邹昊焱夏欣德万嘉树刘思源丁元青冯乐心蒋宏富贾高远蔡哲彦赵鹏赋薛良哲顾文昌曾祺瑞傅元甲杨兴运邹成礼刘开朗蒋文石胡元洲于锐藻冯乐语谭伟懋文昊昊林明哲方高超乔欣德苏景明于博容石安顺任宏达薛兴生叶建柏孟信鸿林正雅孔永望史建本宋建同崔嘉誉汪嘉年谭乐志杜嘉致夏涵蓄钟和顺曹雨华秦博明龙天元李雪峰曾和悦龚高歌谭鸿志谭志业田睿慈周和煦薛星河邹鹏飞任兴文苏良弼谢天瑞吴弘和李星驰秦泽语陈修永何黎昕康安易沈华晖曹凯康彭锐利王天空廖子轩秦志义于茂彦徐乐悦郭鹏海杜高兴常弘厚万博涛吕修伟漕意致侯安翔汪学文方德寿邹欣怿姜新立侯天逸邵宏伟贺阳泽邱明轩崔和平方鸿哲马学林沈靖琪龚欣然徐彭彭孙元洲孔乐贤白新觉汪良哲石高丽马俊友宋安澜姚俊语何烨磊段浩壤朱睿识冯德水郑敏博江鸿志袁良骥钱德泽曾宜年龙欣可文宏旷龚安顺漕文华康康德陈乐贤黎乐山白鸿博朱康安金元基萧英叡陈锐立丁建弼彭经纬李天和郭康安石博厚蒋浩言唐阳夏蒋俊弼郑奇玮毛伟懋廖高达贺俊能吴俊喆龚永昌赖鸿禧周哲圣常元正丁乐湛乔英卓萧凯泽熊天禄毛正初曾锐藻武宏达姚高谊姜凯康夏浩波万乐贤郑信然白涵涤郝烨伟黄高澹钱彬彬邵修伟董鸿熙史德明易嘉言邓兴安萧玉书方子实苏乐水王修为吕新翰史乐天林涵映武乐邦范苑博冯承德李光熙丁皓轩林高原崔哲瀚毛巍昂陈德厚杨雅逸钱明杰曾英毅方经亘杨涵忍杨承望余志尚邹天泽江景曜方鸿博薛鸿卓方鸿晖姜和硕孟正卿易新霁张兴生阎宏畅孔弘壮任浩宕石元化秦昊焱段高昂胡雅达梁安志朱锐精蒋德馨"
    # name="漕碧玉万欣颖梁贝琳何莎莎乔语梦漕沛珊邹乐然文灵波韩小琴张紫薰董冰香薛照红马明明沈喜悦卢静香易胜花潘平和余晶灵方平和潘茉莉蒋丝琦郑津文侯清绮赵苏微蒋珠佩王乐儿马映安陈怜蕾苏韵磬胡紫雪袁梦柏江莺莺曾仙媛冯婀娜赵晓旋江瑾瑶潘绮梅汪雅宁贾夏云许怜容郝寄波汪曼云沈富霞胡叶帆邱珑玲黄泯熙金丝微陈雅辰汤赞怡陈凝海赵千山方倩冰姚菊霞何琳芳郝洲裴金凡双贺芳懿龚乐之于柔惠胡海女田怡丞邵妙珍余悦书顾凡桃姚婉清方莹然江谷蓝钱珂妍傅平春孟山晴漕薇颖钟凝心杜卿蓉龚庄丽邹成美徐涵易邱凡柔蒋暮雨段彦红宋绮文易千雁常之双董爱琴戴雯婧黄韶华王觅荷谢丽佳谢凝云龙锦诗杨瑜璟孙常红段思懿薛星晴石悦来李昱瑛龙雨旋余红梅范天心程知夏余灵卉杨嘉宝丁立芬丁施诗任妍羽钟清逸谢小妍曹采莲侯夏萱姚清懿龙名姝任奕奕廖依童郑菊华郝曲文陆冷玉魏樱花潘念芹石悦心彭怀柔曾献仪刘新蕾王东玲汪长文汪怡若方凝雨萧初翠金平蓝漕书怡廖妍芳刘冰露叶安荷秦雅晗钱千萍武紫蓝许香薇许春梅钱吉星姚晴雪叶琼思石小芬陈璇娟孟真如石映真董凝安郝忆之漕丹烟江微婉胡曼易秦溪澈秦阳阳杜思楠蔡天恩林慧君易蕙若顾柳思石春华任灵韵周娅清余冷菱苏冰之汤庆霞郑暄和孟慧秀赵曼语程臻晰胡梦洁丁思蕊郭书易陈幻灵陆彩娟薛秋露韩源源崔幻桃马凌雪许之双许寄瑶傅夏山武琴雪孟冰薇魏山晴陈霞雰曹紫琼王春绿卢倡文孙语冰蔡悦人潘知夏周珂妍乔巧玲曾琇芳谭湛娟萧凝海康忻乐任苏迷姜有芳宋慧婕姜慧瑶崔芮欣赖悠雅郭聪慧郭星星唐郁安袁悦远于云蔚龚灵松蒋琼思王菱凡龙含烟傅玉兰龙友绿孔英华范纪颖贺丹溪高舒兰贺水绿崔寒凝陈芝蓉金庄雅陆凌波孙思美尹凤婷陈从雪秦妙音吴和暄蔡梓蓓刘灵仙常书竹钟念之汤亦寒冯瑜英段天真郑秋芳顾忆梅汤庭酪金芝芳蒋幼柏汤森丽康妍青沈宝琳郭问梅陈静婉金华婉武雪萍何熙阳许又儿沈东玲段忻然梁寻芳廖慕涵武寻芹傅绿夏白寄瑶周馨蓉彭凝琴廖寻巧熊婉奕吴寄琴林凌瑶顾悦人江乐蓉张婵娟邓飞兰戴曼卉秦尔安龚君茹蔡长丽姚寻春崔微月陆昕妍蔡晓玉江玟丽黄嘉惠何凡梦冯安蕾郝司辰万竹筱董小洁田怀亦李瑞锦夏情文谢汉玲毛西贝贾慧艳曹馨荣于湛静梁琦巧康三诗赵晶霞邓逸美石如意沈若华贾兰尹孟弘丽薛乐心傅湛芳何子舒熊访卉邹翠绿贺悠柔文雨茹吴布侬曹晴霞胡幸瑶孔念之许布凡蒋凡霜蔡傲丝董玲珑方纪轩漕玄穆韩半烟傅思语郝曼云江莹玉侯书文丁荷紫戴江雪杜昕妍董恨天高林娜乔玉颖范正妍徐清芬于子帆毛秋荣余梦之孙寻琴毛梦云钟云英程妍芳曾敏叡贾岚岚丁嘉洁唐寒蕾郑叶春顾阳曦杜希蓉余善玲汤依楠梁大梅傅瑜英杜雄英贺长英乔芳洁戴莹洁林晓桐马冬灵江晓洁常笑旋董燕婉彭玉珂林雪柳郝愉心乔丹烟崔夏雪丁芳馥文瑞绣康凝竹田幻灵邓雅容吴书雪崔修敏董家美徐灵卉彭燕楠赵桂枫史宛海文欣悦漕惠琴董听莲张忆敏郭妍芳黎郁安方思莲武莎莉刘雨双姚海云杜尔珍贾静和杜思凡田宛海孔龙梅孟馨兰胡水卉顾叶飞段惠美易雨柏戴知睿蒋颖颖何杏儿陆梅红贺今歌程安娜沈吉敏夏阳阳周善芳孟梓颖曹书竹孔灵槐任夏菡罗芮欢高杨柳邵仪琳戴新梅孙秋芸赖雅惠漕幼丝赵忻畅漕伶俐孔可儿白绿蝶郭雁玉萧奥雅程采柳薛凝安蔡欣艳姚友蕊吴舒怀许谷波王妙海高佳洁汪水舞黄孟阳戴盼香李雪漫李碧玉罗畅畅金华楚崔映真于莉娉钱雅阳胡秋柳林凝竹傅雅琴尹清秋戴凌旋张瑾琳夏雍恬白尔白马从云李曼丽漕阿柒龚盼香袁水儿张苏荷熊忆远秦熙怡胡叶帆谭晔晔曾恬默易雅云胡瑾琳李绿兰白飞柏曹含双谭萧玉乔凝云邱新月孟一南龚雨寒常燕桦许沈靖韩清怡吴梦松冯丹溪王清悦孙蓉城任雅秀贺红旭钟书慧张南珍江书翠贺布侬廖睿颖顾雅楠蔡觅风吴思迪徐夏雪文菊霞何沛雯陈凡白夏半雪龙寻凝陆惠娅程淑华漕春柏漕雪曼卢庭酪田淑懿唐芫华江菁茹秦流婉叶芝英易凌寒徐玉娟万春霞何笑晴许依楠徐从阳曾晏如田清佳于微婉王娅玟龚清秋邹寒蕾汪玮艺漕杉月顾芮美易洋然赵恨之沈爱茹马婷旭杨幼怡钟雯丽黄寻雪马傲南史雅旋姚雁丝宋隽雅姚翠玉丁清秋史水蓉崔笑萍许献玉乔春华文傲柏康春嫣杨逸美于逸思任向萍常子亦秦家颖沈昭懿叶舒云常安茹段虹英曾慕儿文心宜黄书双魏树艳刘盼雁钟珺娅吕以寒龚墨玉史平霞孟沈雅文曼冬龚娴静萧双儿孙雪卉蔡美丽钟秀英彭秋月吴悠雅龚一雯方彦慧余姝瑶傅琼诗段洋然龚静晨沈水琼李采萱贺乐怡熊雅隽马琳淼陈暖暖石笑晴胡佁然龚晓曼傅秀越许明艳黄云英黎瑜敏曾爱萍田冉冉白飞丹胡青梦黄悦乐蒋舒方熊敏丽林欢欣钱长丽曹飞燕赵琪华陆夏月汪科翰萧嘉淑陈玉颖金雪艳余夜雪陈寄春江秀竹田秋芳谢芝蓉尹幻珊曹仲媛邱歌阑陈凡蕾潘秀如梁瑾萱何经文蔡闳丽罗凌萱贺芳馥于醉卉尹海桃孔许弋易雨旋侯含秀吕静慧程醉波田灵溪范焱霞黎初柳董春柔钟丹南毛舒荣易白筠乔凡双孟寻南熊映秋黄谷兰丁胜怡邱嘉懿蒋葱娟吕叶吉冯明智尹莹莹姜红叶白欣玉谢琨瑜薛瑞云邵令美任水蓉于如霜汤晓芬钟诗晗顾依秋谢晨风毛慧玲宋未央尹雅韶吕飞荷潘妙柏姜盼芙傅蕴美蒋陶宁曾辰雪尹桃尐易含玉傅书翠许修美万谷枫顾斯雅王曼丽蔡盼盼赖玲羽高叶春龚学英武晨钰程冷菱康萌运贺玲玉王忆柏丁君雅金蓝瑟武雁丝罗芳洲杜孤丝余小溪汪平彤吕沈思石翠风张代柔卢燕肖戴惜萱乔流苏吴华楚邓平惠姚翠桃苏妙婧汪春晖萧瑜然孙艳玲董从南郝恨天萧莉娜夏惠丽邱智美黄飞雪范正平任佳惠任莺语杜梓欣侯湛恩于朝旭唐燕晓薛湘云段抒怀黄桐华叶仙仪龚静娴史泯熙易蔓蔓杜吟怀龚海云廖谧辰刘初翠郭思丽姜文姝孙语彤郭春枫余寄真周叶欣马宫莹蔡晏如黎雁芙丁盈盈夏春柏余令美常美丽谢振文侯清妙贺洁玲马风间于冰枫阎梦容杜文思李则悦廖思慧赖秀美阎岚岚方冰兰陈远悦潘秋荣曾友桃蔡紫菱阎妍芳姜绮思彭悦恺李水悦韩生文程玲玲秦一禾田惜寒丁文茵苏思懿蒋映波冯岚岚任殷歌石恬畅朱诗桃易初南毛飞燕梁紫夏龚晨星尹曼容徐桐华孟悦婷潘玉轩张梦旋龚亦寒夏陈红周白容邵芸熙田希月邹紫翠吴梦安邵盼波曹霞雰丁正妍胡凌翠彭晶辉谢紫真戴平宁周盼海蔡秋荣何问薇江安露曾殷漓罗清心陆子蕙董葛菲邵令慧侯碧曼石夏寒任春柔金雁菡夏妙菱罗爰美罗凡白王芳懿蒋易烟邓白容梁谷梦尹青丝侯宁乐徐凡梅尹雅辰萧倩丽顾菀柳彭曼妮方甘雨姚沛蓝白靖柔袁小星邵智美阎依风孙茹云蔡晓楠赖北嘉许森丽段莹洁武姝美梁丹溪戴代容许安露许修敏魏莉娉杨玉娟沈敏慧钟雅静郝叶欣汪玉英田悦宜漕黛娥顾妙珍汪一凡林畅然余静芙崔婉然刘妙可秦嘉禾乔芳蕙汤琴心史惠丽刘青丝邹雅丹贺方雅丁施诗金尔白史睿敏邓饮月段端懿王娇洁萧梓燕曹悠馨谭雨蓉顾滢滢石饮香熊珠星杜琨瑜廖雁枫冯春雁龙许暖乔沛凝潘忻畅姜子怡段思彤易熙星朱锦婷漕秋春江平彤袁施然石源源孔忆敏郝芳蕤傅朗然任晴曦罗怜翠曾真洁熊小萱董悦婷田凌春邓幼萱邵香桃高兰娜曹笑南孟江红谭巧玲李婉清汤君丽姚朗然龚怡木史宛儿高半青魏北辰沈惠然董绿蓉陈忻然常寄灵戴银柳文流苏沈彦芝阎玮琪常向萍余思云唐娅芳金欣美熊蕴美崔乐怡乔丹彤邱妮子程平蝶潘天悦罗锦文余蔓菁易睿敏秦雅丽陆沛若钟夏寒尹华采萧宇芳潘如霜于子琳任义文石丝萝梁紫南蒋晏静傅梓倩唐菊华蒋卿蓉白冰旋沈千亦方水芸陆茵茵曹初珍朱若芳姚泯熙邱淳雅萧悦玮谭一凡刘嘉宝熊月桂韩凌旋曹谷雪宋君茹赵白筠韩芸欣孙海露沈明智曹新雨沈怡月范晓瑶谢琇云王乐荷罗琴轩魏帮琼熊云霞孔恨竹陈雯华李冰巧马淳静武菁茹方叶丹谢令美崔恨荷叶暖姝郝孤云陈青蓉石怜阳易梓柔朱蕴秀赵晗蕾戴兰娜罗闵雨顾小谷段芷巧汪若淑龚南霜廖小谷邹金梅文平晓谭怀柔余奥婷谢绮彤戴怜菡贺继红宋新儿高幼枫汪春姝乔楠楠潘念柏崔婷秀汪瑞彩邵飞双白谷梦田文心吕寒云汪芳馥郑瑶岑王流苏侯晓楠熊青筠萧媛媛周寒安梁敏丽方阿柒段暄婷段曼安"
    sql = "SELECT * FROM USER \
        WHERE NAME = '%s'" % (name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchone()
        result['name'] = results[0]
        result['age'] = results[1]
        result['sex'] = results[2]
        result['balance'] = results[3]
    except:
        print("Error: unable to fetch data")
    db.close()
    return result


def getName():
    db = pymysql.connect(host="localhost", user="user",
                         password="bupt1234", database='user')
    cursor = db.cursor()
    result = {}
    sql = "SELECT * FROM USER ORDER BY RAND() LIMIT 1"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchone()
        result['name'] = results[0]
        result['age'] = results[1]
        result['sex'] = results[2]
        result['balance'] = results[3]
    except:
        print("Error: unable to fetch data")
    db.close()
    return result['name']


class returnCrossDomain(Thread):
    def __init__(self, connection):
        Thread.__init__(self)
        self.con = connection
        self.isInitialize = False

    def run(self):
        while True:
            if not self.isInitialize:
                # 开始握手阶段
                header = self.analyzeReq()  # 分析请求头
                secKey = header['Sec-WebSocket-Key']
                acceptKey = self.generateAcceptKey(secKey)

                response = "HTTP/1.1 101 Switching Protocols\r\n"
                response += "Upgrade: websocket\r\n"
                response += "Connection: Upgrade\r\n"
                response += "Sec-WebSocket-Accept: %s\r\n\r\n" % (
                    acceptKey.decode('utf-8'))
                self.con.send(response.encode())
                self.isInitialize = True
                self.myClient = client()
                print('response:\r\n' + response)

                self.sendDataToClient("2019211496"+self.myClient.name)
                # 握手阶段结束

                # 读取命令阶段
            else:
                opcode = self.getOpcode()

                if opcode == 8:
                    self.con.close()
                    return
                self.getDataLength()
                clientData = urllib.parse.unquote(self.readClientData())
                print('客户端数据：' + clientData)
                # 处理数据(测试桩 测试通信)
                # ans = self.answer(clientData)
                # self.sendDataToClient(ans)
                if(self.myClient.first == True):
                    self.myClient.first = False
                    t1 = threading.Thread(
                        target=self.FirstReceive, args=(clientData,))
                    t1.start()
                self.myClient.str = clientData
                self.myClient.Listening = False
                # self.sendDataToClient(clientData)

    def FirstReceive(self, str):
        mClient = self.myClient
        while(1):
            action = StepList.stepList[mClient.stepName].actionList[mClient.num]
            if(action.id == 0):
                self.sendDataToClient(action.run(mClient.name))
                mClient.num = mClient.num+1
            elif(action.id == 1):

                mClient.Listening = True
                mClient.str = ""
                num = action.time
                while num > 0 and mClient.Listening == True:
                    num = num-1
                    time.sleep(1)
                mClient.Listening = False
                mClient.num = mClient.num+1
            elif(action.id == 2):
                if(fuzz.partial_ratio(mClient.str, action.str) == 100):
                    mClient.stepName = action.name
                    mClient.num = 0
                else:
                    mClient.num = mClient.num+1
            elif(action.id == 3):
                if(mClient.str == ""):
                    mClient.stepName = action.name
                    mClient.num = 0
                else:
                    mClient.num = mClient.num+1
            elif(action.id == 4):
                mClient.stepName = action.name
                mClient.num = 0
            elif(action.id == 5):
                self.con.close()
                return

    def analyzeReq(self):
        reqData = self.con.recv(1024).decode()
        reqList = reqData.split('\r\n')
        print(reqList)
        headers = {}
        for reqItem in reqList:
            if ': ' in reqItem:
                unit = reqItem.split(': ')
                headers[unit[0]] = unit[1]
        return headers

    def generateAcceptKey(self, secKey):
        sha1 = hashlib.sha1()
        sha1.update((secKey + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11').encode())
        sha1_result = sha1.digest()
        acceptKey = base64.b64encode(sha1_result)
        return acceptKey

    def getOpcode(self):
        first8Bit = self.con.recv(1)
        first8Bit = struct.unpack('B', first8Bit)[0]
        opcode = first8Bit & 0b00001111
        return opcode

    def getDataLength(self):
        second8Bit = self.con.recv(1)
        second8Bit = struct.unpack('B', second8Bit)[0]
        masking = second8Bit >> 7
        dataLength = second8Bit & 0b01111111
        # print("dataLength:",dataLength)
        if dataLength <= 125:
            payDataLength = dataLength
        elif dataLength == 126:
            payDataLength = struct.unpack('H', self.con.recv(2))[0]
        elif dataLength == 127:
            payDataLength = struct.unpack('Q', self.con.recv(8))[0]
        self.masking = masking
        self.payDataLength = payDataLength
        #print("payDataLength:", payDataLength)

    def readClientData(self):

        if self.masking == 1:
            maskingKey = self.con.recv(4)
        data = self.con.recv(self.payDataLength)

        if self.masking == 1:
            i = 0
            trueData = ''
            for d in data:
                trueData += chr(d ^ maskingKey[i % 4])
                i += 1
            return trueData
        else:
            return data

    def sendDataToClient(self, text):
        sendData = ''
        sendData = struct.pack('!B', 0x81)
        text = urllib.parse.quote(text)
        length = len(text)
        if length <= 125:
            sendData += struct.pack('!B', length)
        elif length <= 65536:
            sendData += struct.pack('!B', 126)
            sendData += struct.pack('!H', length)
        elif length == 127:
            sendData += struct.pack('!B', 127)
            sendData += struct.pack('!Q', length)

        sendData += struct.pack('!%ds' % (length), text.encode('utf8'))
        dataSize = self.con.send(sendData)

    def answer(self, data):
        if(data[0:1] == "啊"):
            return "hello world"
        else:
            # result=search("韩高轩")
            result = search(data[0:3])
            if("name" in result.keys()):
                return result['name']+"还有"+str(result['balance'])+"钱"
            else:
                return "说你"


class Speak:
    def __init__(self, str):
        self.id = 0
        self.str = str

    def run(self, name):
        result = search(name)
        if(result['sex'] == '男'):
            name = name[0]+"先生"
        else:
            name = name[0]+"女士"
        self.str = self.str.replace("$name", name)
        self.str = self.str.replace("$amount", str(result['balance']))
        return self.str


class Listen:
    def __init__(self, str):
        self.id = 1
        self.time = int(str)


class Branch:
    # str为用户输入的词，name为跳转步骤名称
    def __init__(self, str, name):
        self.id = 2
        self.str = str
        self.name = name


class Silence:
    def __init__(self, name):
        self.id = 3
        self.name = name


class Default:
    def __init__(self, name):
        self.id = 4
        self.name = name


class Exit:
    def __init__(self):
        self.id = 5


class Step:
    def __init__(self, name):
        self.actionList = []
        self.name = name

    def addAction(self, action):
        self.actionList.append(action)


class StepList:
    stepList = {}

    def __init__():
        return

    @classmethod
    def addStep(cls, step):
        cls.stepList[step.name] = step

    def getStep(cls, name):
        return cls.stepList[name]


class client:
    def __init__(self):
        self.name = getName()
        self.stepName = "welcome"
        self.num = 0
        self.Listening = False
        self.first = True
        self.str = ""


def ParserFile(file):
    with open(file, encoding='utf8') as mfile:
        flag = True
        for str in mfile:
            str = str.strip()
            str = str.split(' ')
            if(str[0] == 'Step'):
                if(flag == True):
                    flag = False
                else:
                    StepList.addStep(step)
                step = Step(str[1].strip())

            elif(str[0] == 'Speak'):
                step.addAction(Speak(''.join(str[1:])))
            elif(str[0] == 'Listen'):
                step.addAction(Listen(str[1]))
            elif(str[0] == 'Branch'):
                step.addAction(Branch(str[1], str[2]))
            elif(str[0] == 'Silence'):
                step.addAction(Silence(str[1]))
            elif(str[0] == 'Default'):
                step.addAction(Default(str[1]))
            elif(str[0] == 'Exit'):
                step.addAction(Exit())
        StepList.addStep(step)
    # for k in StepList.stepList.keys():
    #     for act in StepList.stepList[k].actionList:
    #         print(act.id)
    mfile.close()


def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], "-f:", ["file="])
    except getopt.GetoptError:
        sys.exit()
    for option, value in options:
        if option in ("-f", "--file"):
            ParserFile(value)
    #sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 9999))
    sock.listen(5)
    while True:
        try:
            connection, address = sock.accept()
            returnCrossDomain(connection).start()
        except:
            time.sleep(1)


if __name__ == "__main__":
    main()
