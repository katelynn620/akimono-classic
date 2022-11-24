# ワールドアトラス版アイテムデータ 2005/01/20 由來

# このファイルはアイテムデータの定義ファイルです。
# 好きなようにカスタマイズできます。詳細はマニュアルをご覧ください。

@@DEFINE
	version	05-01-20(WA)		#★商品データバージョン表記
					# 最後の「WA」はワールドアトラス版であることを示します。
					# もしあなたが独自アイテムを目玉にした商人物語を作るなら，
					# この記号を変えるのがよいでしょう。

	scale	個			#★デフォルトの数え単位
	type0	全			#全アイテムの集合
	type1	素材
	type2	食品
	type3	調味
	type4	紡織
	type5	工藝
	type6	船舶
	type7	艦隊
	type8	航海
	type9	道具
	
	job	shipb		造船屋		#★職業コードは英小文字10文字以内
	job	pirate		海盜
	job	pros		海軍司令
	job	explore		冒險家
	job	trader		貿易商

	MaxMoney	999999999	#★最大資金
	
	set NewShopMoney	200000					#初期資金 (@@FUNCNEWにて使用)
	set NewShopTime		14*60*60				#初期持時間(秒) (@@FUNCNEWにて使用)
	set NewShopItem		展示架擴建拆卸工具:1:禮物卷:10	#初期所持商品 (@@FUNCNEWにて使用) 書式 商品名:個数:商品名:個数:...
	
	TimeEditShowcase	10m		#★展示架操作時間
	TimeShopping		20m		#★仕入時間(旧SOLD OUTとの互換性確保。今は使用せず)
	TimeSendItem		20m		#★アイテム仕入/移動時間(基本)
	TimeSendItemPlus	20s		#★アイテム仕入/移動時間(1個辺りの追加時間)
	TimeSendMoney		20m		#★資金移動時間(基本)
	TimeSendMoneyPlus	100000		#★ごみ処理時間計算用金額(この金額につきTimeSendMoney時間を消費)
	
	CostShowcase1		0		#★展示架1個時維護費
	CostShowcase2		2000	#展示架2個時維護費
	CostShowcase3		4000	#展示架3個時維護費
	CostShowcase4		8000	#展示架4個時維護費
	CostShowcase5		16000	#展示架5個時維護費
	CostShowcase6		32000	#展示架6個時維護費
	CostShowcase7		64000	#展示架7個時維護費
	CostShowcase8		128000	#展示架8個時維護費
	
	ItemUseTimeRate		0.5		#★アイテム使用時時間計算補正倍率(@USE内time,exptimeに有効)
	

#------ ここからアイテム定義 ---------------------------------


@@ITEM
	no		18
	type	航海
	code	bread
	name	麵包
	info	航海的必需品
	price	100
	limit	1000/1000
	pop	20m
	plus	20m
	base	100/100000
	scale	食
	cost	20
	point	5%
@@ITEM
	no		19
	type	航海
	code	lamb
	name	蘭姆酒
	info	航海的必需品
	price	200
	limit	500/500
	pop	40m
	plus	20m
	base	100/50000
	scale	桶
	cost	20
	point	10%

@@ITEM
	no		20
	type	航海
	code	seaman
	name	水手
	info	使船運作的人手
	price	1200
	limit	800/800
	pop	1d
	plus	20m
	base	10000/100000
	scale	人
	flag	noshowcase|human|norequest

@@ITEM
	no		1
	type	道具
	code	book-bd
	name	造船指南書
	info	解說造船方法的指南
	price	10000
	limit	1/0.1
	pop	1d
	plus	2h
	scale	本
	flag	noshowcase
	@@use
		time	120m
		exp		2%
		exptime	40m
		job		造船屋	times/1.5
		scale	回
		action	製造
		name	製造單船桅小型船
		info	製造單船桅小型船
		okmsg	單船桅小型船製造完成了
			use		1	木材
			use		1	帆布
			get		1	單船桅小型船
	@@use
		time	3h
		exp		2%
		exptime	1h
		scale	回
		action	製造
		name	製造英國式柯克帆船
		info	製造英國式柯克帆船
		okmsg	英國式柯克帆船製造完成了
		ngmsg	製作失敗了…
			needjob	造船屋
			needexp	10%
			use		1	木材
			use		1	帆布
			get		1	英國式柯克帆船	90%
	@@use
		time	6h
		exp		4%
		exptime	2h
		scale	回
		action	製造
		name	製造中型加萊排槳帆船
		info	製造中型加萊排槳帆船
		okmsg	中型加萊排槳帆船製造完成了
		ngmsg	製作失敗了…
			needjob	造船屋
			needexp	30%
			use		3	木材
			use		1	帆布
			get		1	中型加萊排槳帆船	90%
	@@use
		time	12h
		exp		4%
		exptime	4h
		scale	回
		action	製造
		name	製造中型卡拉維爾帆船
		info	製造中型卡拉維爾帆船
		okmsg	中型卡拉維爾帆船製造完成了
		ngmsg	製作失敗了…
			needjob	造船屋
			needexp	30%
			use		5	木材
			use		3	帆布
			get		1	中型卡拉維爾帆船	90%
	@@use
		time	24h
		exp		8%
		exptime	8h
		scale	回
		action	製造
		name	製造大型卡瑞克帆船
		info	製造大型卡瑞克帆船
		okmsg	大型卡瑞克帆船製造完成了
		ngmsg	製作失敗了…
			needjob	造船屋
			needexp	50%
			use		10	木材
			use		6	帆布
			get		1	大型卡瑞克帆船	90%
	@@use
		time	24h
		exp		8%
		exptime	8h
		scale	回
		action	製造
		name	製造大型蓋倫帆船
		info	製造大型蓋倫帆船
		okmsg	大型蓋倫帆船製造完成了
		ngmsg	製作失敗了…
			needjob	造船屋
			needexp	50%
			use		10	木材
			use		6	帆布
			get		1	大型蓋倫帆船	90%
	@@use
		time	36h
		exp		10%
		exptime	12h
		scale	回
		action	製造
		name	製造加萊賽排槳帆船
		info	製造加萊賽排槳帆船
		okmsg	加萊賽排槳帆船製造完成了
		ngmsg	製作失敗了…
			needjob	造船屋
			needexp	60%
			use		18	木材
			use		7	帆布
			get		1	加萊賽排槳帆船	90%

@@ITEM
	no		26
	type	艦隊
	code	convoy-aa
	name	第一冒險艦隊
	info	冒險艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索歐洲
		info	對於歐洲海域的適應性
		param	26,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索非洲
		info	對於非洲海域的適應性
		param	26,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索中東
		info	對於中東海域的適應性
		param	26,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索印度
		info	對於印度海域的適應性
		param	26,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索亞洲
		info	對於亞洲海域的適應性
		param	26,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索新大陸
		info	對於新大陸海域的適應性
		param	26,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接冒險艦隊
		info	到港口確認看看艦隊是否已經返回
		param	26
		funcb	onlyexp
		func	meetexp
		arg	nocount
@@ITEM
	no		27
	type	艦隊
	code	convoy-ab
	name	第二冒險艦隊
	info	冒險艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索歐洲
		info	對於歐洲海域的適應性
		param	27,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索非洲
		info	對於非洲海域的適應性
		param	27,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索中東
		info	對於中東海域的適應性
		param	27,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索印度
		info	對於印度海域的適應性
		param	27,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索亞洲
		info	對於亞洲海域的適應性
		param	27,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索新大陸
		info	對於新大陸海域的適應性
		param	27,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接冒險艦隊
		info	到港口確認看看艦隊是否已經返回
		param	27
		funcb	onlyexp
		func	meetexp
		arg	nocount
@@ITEM
	no		28
	type	艦隊
	code	convoy-ac
	name	第三冒險艦隊
	info	冒險艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索歐洲
		info	對於歐洲海域的適應性
		param	28,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索非洲
		info	對於非洲海域的適應性
		param	28,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索中東
		info	對於中東海域的適應性
		param	28,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索印度
		info	對於印度海域的適應性
		param	28,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索亞洲
		info	對於亞洲海域的適應性
		param	28,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索新大陸
		info	對於新大陸海域的適應性
		param	28,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接冒險艦隊
		info	到港口確認看看艦隊是否已經返回
		param	28
		funcb	onlyexp
		func	meetexp
		arg	nocount
@@ITEM
	no		29
	type	艦隊
	code	convoy-ad
	name	第四冒險艦隊
	info	冒險艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索歐洲
		info	對於歐洲海域的適應性
		param	29,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索非洲
		info	對於非洲海域的適應性
		param	29,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索中東
		info	對於中東海域的適應性
		param	29,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索印度
		info	對於印度海域的適應性
		param	29,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索亞洲
		info	對於亞洲海域的適應性
		param	29,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	派去探索新大陸
		info	對於新大陸海域的適應性
		param	29,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接冒險艦隊
		info	到港口確認看看艦隊是否已經返回
		param	29
		funcb	onlyexp
		func	meetexp
		arg	nocount

@@ITEM
	no		30
	type	艦隊
	code	convoy-ba
	name	第一貿易艦隊
	info	貿易艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往歐洲貿易
		info	對於歐洲海域的適應性
		param	30,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往非洲貿易
		info	對於非洲海域的適應性
		param	30,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往中東貿易
		info	對於中東海域的適應性
		param	30,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往印度貿易
		info	對於印度海域的適應性
		param	30,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往亞洲貿易
		info	對於亞洲海域的適應性
		param	30,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往新大陸貿易
		info	對於新大陸海域的適應性
		param	30,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接貿易艦隊
		info	到港口確認看看艦隊是否已經返回
		param	30
		funcb	onlyexp
		func	meetrtp
		arg	nocount
@@ITEM
	no		31
	type	艦隊
	code	convoy-bb
	name	第二貿易艦隊
	info	貿易艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往歐洲貿易
		info	對於歐洲海域的適應性
		param	31,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往非洲貿易
		info	對於非洲海域的適應性
		param	31,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往中東貿易
		info	對於中東海域的適應性
		param	31,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往印度貿易
		info	對於印度海域的適應性
		param	31,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往亞洲貿易
		info	對於亞洲海域的適應性
		param	31,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往新大陸貿易
		info	對於新大陸海域的適應性
		param	31,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接貿易艦隊
		info	到港口確認看看艦隊是否已經返回
		param	31
		funcb	onlyexp
		func	meetrtp
		arg	nocount
@@ITEM
	no		32
	type	艦隊
	code	convoy-bc
	name	第三貿易艦隊
	info	貿易艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往歐洲貿易
		info	對於歐洲海域的適應性
		param	32,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往非洲貿易
		info	對於非洲海域的適應性
		param	32,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往中東貿易
		info	對於中東海域的適應性
		param	32,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往印度貿易
		info	對於印度海域的適應性
		param	32,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往亞洲貿易
		info	對於亞洲海域的適應性
		param	32,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往新大陸貿易
		info	對於新大陸海域的適應性
		param	32,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接貿易艦隊
		info	到港口確認看看艦隊是否已經返回
		param	32
		funcb	onlyexp
		func	meetrtp
		arg	nocount
@@ITEM
	no		33
	type	艦隊
	code	convoy-bd
	name	第四貿易艦隊
	info	貿易艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往歐洲貿易
		info	對於歐洲海域的適應性
		param	33,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往非洲貿易
		info	對於非洲海域的適應性
		param	33,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往中東貿易
		info	對於中東海域的適應性
		param	33,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往印度貿易
		info	對於印度海域的適應性
		param	33,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往亞洲貿易
		info	對於亞洲海域的適應性
		param	33,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	派往
		name	派往新大陸貿易
		info	對於新大陸海域的適應性
		param	33,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接貿易艦隊
		info	到港口確認看看艦隊是否已經返回
		param	33
		funcb	onlyexp
		func	meetrtp
		arg	nocount

@@ITEM
	no		34
	type	艦隊
	code	convoy-ca
	name	第一武装艦隊
	info	戰鬥艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到歐洲
		info	對於歐洲海域的適應性
		param	34,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到非洲
		info	對於非洲海域的適應性
		param	34,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到中東
		info	對於中東海域的適應性
		param	34,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到印度
		info	對於印度海域的適應性
		param	34,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到亞洲
		info	對於亞洲海域的適應性
		param	34,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到新大陸
		info	對於新大陸海域的適應性
		param	34,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接武装艦隊
		info	到港口確認看看艦隊是否已經返回
		param	34
		funcb	onlyexp
		func	meetpp
		arg	nocount
@@ITEM
	no		35
	type	艦隊
	code	convoy-cb
	name	第二武装艦隊
	info	戰鬥艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到歐洲
		info	對於歐洲海域的適應性
		param	35,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到非洲
		info	對於非洲海域的適應性
		param	35,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到中東
		info	對於中東海域的適應性
		param	35,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到印度
		info	對於印度海域的適應性
		param	35,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到亞洲
		info	對於亞洲海域的適應性
		param	35,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到新大陸
		info	對於新大陸海域的適應性
		param	35,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接武装艦隊
		info	到港口確認看看艦隊是否已經返回
		param	35
		funcb	onlyexp
		func	meetpp
		arg	nocount
@@ITEM
	no		36
	type	艦隊
	code	convoy-cc
	name	第三武装艦隊
	info	戰鬥艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到歐洲
		info	對於歐洲海域的適應性
		param	36,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到非洲
		info	對於非洲海域的適應性
		param	36,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到中東
		info	對於中東海域的適應性
		param	36,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到印度
		info	對於印度海域的適應性
		param	36,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到亞洲
		info	對於亞洲海域的適應性
		param	36,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到新大陸
		info	對於新大陸海域的適應性
		param	36,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接武装艦隊
		info	到港口確認看看艦隊是否已經返回
		param	36
		funcb	onlyexp
		func	meetpp
		arg	nocount
@@ITEM
	no		37
	type	艦隊
	code	convoy-cd
	name	第四武装艦隊
	info	戰鬥艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到歐洲
		info	對於歐洲海域的適應性
		param	37,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到非洲
		info	對於非洲海域的適應性
		param	37,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到中東
		info	對於中東海域的適應性
		param	37,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到印度
		info	對於印度海域的適應性
		param	37,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到亞洲
		info	對於亞洲海域的適應性
		param	37,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣
		name	到新大陸
		info	對於新大陸海域的適應性
		param	37,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	迎接
		name	迎接武装艦隊
		info	到港口確認看看艦隊是否已經返回
		param	37
		funcb	onlyexp
		func	meetpp
		arg	nocount

@@ITEM
	no		39
	type	航海
	code	discover-a
	name	發現報告書（歐洲）
	info	冒險中發現的稀有物品
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	向王國申報
		info	將發現品向王國申報
		func	disc
		param	1
		arg	nocount
			use		1	發現報告書（歐洲）
@@ITEM
	no		40
	type	航海
	code	discover-b
	name	發現報告書（非洲）
	info	冒險中發現的稀有物品
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	向王國申報
		info	將發現品向王國申報
		func	disc
		param	2
		arg	nocount
			use		1	發現報告書（非洲）
@@ITEM
	no		41
	type	航海
	code	discover-c
	name	發現報告書（中東）
	info	冒險中發現的稀有物品
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	向王國申報
		info	將發現品向王國申報
		func	disc
		param	3
		arg	nocount
			use		1	發現報告書（中東）
@@ITEM
	no		42
	type	航海
	code	discover-d
	name	發現報告書（印度）
	info	冒險中發現的稀有物品
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	向王國申報
		info	將發現品向王國申報
		func	disc
		param	4
		arg	nocount
			use		1	發現報告書（印度）
@@ITEM
	no		43
	type	航海
	code	discover-e
	name	發現報告書（亞洲）
	info	冒險中發現的稀有物品
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	向王國申報
		info	將發現品向王國申報
		func	disc
		param	5
		arg	nocount
			use		1	發現報告書（亞洲）
@@ITEM
	no		44
	type	航海
	code	discover-f
	name	發現報告書（新大陸）
	info	冒險中發現的稀有物品
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	申報
		name	向王國申報
		info	將發現品向王國申報
		func	disc
		param	6
		arg	nocount
			use		1	發現報告書（新大陸）

@@ITEM
	no		45
	type	航海
	code	town-a
	name	新城市的地圖（歐洲）
	info	在冒險時發現的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名稱
		scale	回
		action	命名與建造
		name	建設商館
		info	將城市命名使其可進行貿易
		param	1
		func	newtown
			use		1	新城市的地圖（歐洲）
@@ITEM
	no		46
	type	航海
	code	town-b
	name	新城市的地圖（非洲）
	info	在冒險時發現的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名稱
		scale	回
		action	命名與建造
		name	建設商館
		info	將城市命名使其可進行貿易
		param	2
		func	newtown
			use		1	新城市的地圖（非洲）
@@ITEM
	no		47
	type	航海
	code	town-c
	name	新城市的地圖（中東）
	info	在冒險時發現的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名稱
		scale	回
		action	命名與建造
		name	建設商館
		info	將城市命名使其可進行貿易
		param	3
		func	newtown
			use		1	新城市的地圖（中東）
@@ITEM
	no		48
	type	航海
	code	town-d
	name	新城市的地圖（印度）
	info	在冒險時發現的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名稱
		scale	回
		action	命名與建造
		name	建設商館
		info	將城市命名使其可進行貿易
		param	4
		func	newtown
			use		1	新城市的地圖（印度）
@@ITEM
	no		49
	type	航海
	code	town-e
	name	新城市的地圖（亞洲）
	info	在冒險時發現的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名稱
		scale	回
		action	命名與建造
		name	建設商館
		info	將城市命名使其可進行貿易
		param	5
		func	newtown
			use		1	新城市的地圖（亞洲）
@@ITEM
	no		50
	type	航海
	code	town-f
	name	新城市的地圖（新大陸）
	info	在冒險時發現的貿易城市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	城市的名稱
		scale	回
		action	命名與建造
		name	建設商館
		info	將城市命名使其可進行貿易
		param	6
		func	newtown
			use		1	新城市的地圖（新大陸）

@@ITEM
	no		51
	type	工藝
	code	coin
	name	金幣
	info	王國發行的金幣。可以透過販售來取得金錢。
	price	10000
	limit	500
	base	10/20
	plus	-1h
	pop	2h
	scale	枚
	point	75%
@@ITEM
	no		52
	type	食品
	code	wine
	name	葡萄酒
	info	歐洲特產的食品
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	16h
	scale	桶
	point	300%
@@ITEM
	no		53
	type	食品
	code	cheese
	name	起司
	info	歐洲特產的食品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	3h
	scale	桶
	point	60%
@@ITEM
	no		54
	type	調味
	code	olive
	name	橄欖油
	info	歐洲特產的調味料
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	90m
	scale	桶
	point	30%
@@ITEM
	no		55
	type	紡織
	code	woolen
	name	毛紡織品
	info	歐洲特產的紡織品
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	8h
	scale	箱
	point	150%
@@ITEM
	no		56
	type	工藝
	code	stained
	name	彩色玻璃
	info	歐洲特產的工藝品
	price	8000
	limit	120
	base	10/20
	plus	-1h
	pop	12h
	scale	箱
	point	200%
@@ITEM
	no		57
	type	工藝
	code	sculpture
	name	雕塑
	info	歐洲特產的工藝品
	price	4000
	limit	250
	base	10/20
	plus	-1h
	pop	6h
	scale	箱
	point	120%
@@ITEM
	no		58
	type	工藝
	code	gun
	name	槍
	info	歐洲特產的工藝品
	price	3000
	limit	300
	base	10/20
	plus	-1h
	pop	5h
	scale	箱
	point	80%

@@ITEM
	no		59
	type	素材
	code	gold
	name	金
	info	非洲特產的素材
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	箱
	point	300%
@@ITEM
	no		60
	type	素材
	code	diamond
	name	鑽石
	info	非洲特產的素材
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	20h
	scale	箱
	point	600%
@@ITEM
	no		61
	type	素材
	code	coral
	name	珊瑚
	info	非洲特產的素材
	price	2500
	limit	400
	base	10/20
	plus	-1h
	pop	5h
	scale	箱
	point	140%
@@ITEM
	no		62
	type	素材
	code	ivory
	name	象牙
	info	非洲特產的素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		63
	type	食品
	code	coffee
	name	咖啡
	info	非洲特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	40%
@@ITEM
	no		64
	type	調味
	code	salt
	name	鹽
	info	非洲特產的調味料
	price	400
	limit	2500
	base	10/20
	plus	-1h
	pop	40m
	scale	箱
	point	15%
@@ITEM
	no		65
	type	調味
	code	tamarindo
	name	羅望子
	info	非洲特產的調味料
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	30%

@@ITEM
	no		66
	type	素材
	code	ironore
	name	鐵礦石
	info	中東特產的素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		67
	type	素材
	code	sulfur
	name	硫磺
	info	中東特產的素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		68
	type	食品
	code	honey
	name	蜂蜜
	info	中東特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	25%
@@ITEM
	no		69
	type	調味
	code	sugar
	name	砂糖
	info	中東特產的調味料
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	25%
@@ITEM
	no		70
	type	紡織
	code	carpet
	name	絨毯
	info	中東特產的紡織品
	price	2500
	limit	400
	base	10/20
	plus	-1h
	pop	5h
	scale	箱
	point	180%
@@ITEM
	no		71
	type	紡織
	code	hemptext
	name	麻紡織品
	info	中東特產的紡織品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	120%
@@ITEM
	no		72
	type	工藝
	code	bicornis
	name	犀牛角
	info	中東特產的工藝品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	100%

@@ITEM
	no		73
	type	素材
	code	saltpeter
	name	硝石
	info	印度特產的素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		74
	type	素材
	code	sapphire
	name	藍寶石
	info	印度特產的素材
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	箱
	point	300%
@@ITEM
	no		75
	type	調味
	code	pepper
	name	胡椒
	info	印度特產的調味料
	price	2500
	limit	400
	base	10/20
	plus	-1h
	pop	200m
	scale	箱
	point	150%
@@ITEM
	no		76
	type	調味
	code	cinnamon
	name	肉桂
	info	印度特產的調味料
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	25%
@@ITEM
	no		77
	type	紡織
	code	cottonfab
	name	綿紡織品
	info	印度特產的紡織品
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		78
	type	紡織
	code	printing
	name	印花棉布
	info	印度特產的紡織品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	100%
@@ITEM
	no		79
	type	工藝
	code	tortoiseshell
	name	龜殼
	info	印度特產的工藝品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	100%

@@ITEM
	no		80
	type	素材
	code	pearl
	name	珍珠
	info	亞洲特產的素材
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	箱
	point	250%
@@ITEM
	no		81
	type	食品
	code	sake
	name	清酒
	info	亞洲特產的食品
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	桶
	point	250%
@@ITEM
	no		82
	type	食品
	code	greentea
	name	茶
	info	亞洲特產的食品
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		83
	type	紡織
	code	silkfab
	name	絹紡織品
	info	亞洲特產的紡織品
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	20h
	scale	箱
	point	750%
@@ITEM
	no		84
	type	工藝
	code	ukiyoe
	name	浮世繪
	info	亞洲特產的工藝品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	120%
@@ITEM
	no		85
	type	工藝
	code	lacquer
	name	漆器
	info	亞洲特產的工藝品
	price	4000
	limit	250
	base	10/20
	plus	-1h
	pop	8h
	scale	箱
	point	200%
@@ITEM
	no		86
	type	工藝
	code	katana
	name	刀
	info	亞洲特產的工藝品
	price	8000
	limit	120
	base	10/20
	plus	-1h
	pop	16h
	scale	箱
	point	400%

@@ITEM
	no		17
	type	素材
	code	silver
	name	銀
	info	新大陸特產的素材
	price	4000
	limit	250
	base	10/20
	plus	-1h
	pop	8h
	scale	箱
	point	200%
@@ITEM
	no		12
	type	素材
	code	emerald
	name	祖母綠
	info	新大陸特產的素材
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	20h
	scale	箱
	point	500%
@@ITEM
	no		13
	type	食品
	code	cacao
	name	可可
	info	新大陸特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	桶
	point	25%
@@ITEM
	no		14
	type	食品
	code	corn
	name	玉米
	info	新大陸特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	桶
	point	25%
@@ITEM
	no		38
	type	食品
	code	tamato
	name	番茄
	info	新大陸特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	桶
	point	25%
@@ITEM
	no		23
	type	食品
	code	tobacco
	name	香菸
	info	新大陸特產的食品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	150%
@@ITEM
	no		21
	type	食品
	code	pumpkin
	name	南瓜
	info	新大陸特產的食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	桶
	point	25%

@@ITEM
	no		5
	type	船舶
	code	ship-a
	name	單船桅小型船
	info	小規模帆船。
	price	20000
	limit	50
	base	5/10
	plus	-1h
	pop	32h
	scale	艘
	point	2h
@@ITEM
	no		6
	type	船舶
	code	ship-c
	name	英國式柯克帆船
	info	小規模帆船。
	price	40000
	limit	25
	base	5/10
	plus	-1h
	pop	72h
	scale	艘
	point	4h
@@ITEM
	no		7
	type	船舶
	code	ship-b
	name	中型加萊排槳帆船
	info	中規模漕船。
	price	60000
	limit	16
	base	5/10
	plus	-1h
	pop	108h
	scale	艘
	point	6h
@@ITEM
	no		8
	type	船舶
	code	ship-d
	name	中型卡拉維爾帆船
	info	中規模帆船。
	price	80000
	limit	12
	base	5/10
	plus	-1h
	pop	150h
	scale	艘
	point	8h
@@ITEM
	no		9
	type	船舶
	code	ship-e
	name	大型卡瑞克帆船
	info	大規模帆船。
	price	160000
	limit	10
	base	5/10
	plus	-1h
	pop	300h
	scale	艘
	point	16h
@@ITEM
	no		10
	type	船舶
	code	ship-f
	name	大型蓋倫帆船
	info	大規模帆船。
	price	320000
	limit	10
	base	5/10
	plus	-1h
	pop	600h
	scale	艘
	point	50h
@@ITEM
	no		11
	type	船舶
	code	ship-g
	name	加萊賽排槳帆船
	info	巨大漕船。
	price	480000
	limit	10
	base	5/10
	plus	-1h
	pop	900h
	scale	艘
	point	80h

@@ITEM
	no		15
	type	道具
	code	wood
	name	木材
	info	船的材料
	price	5000
	limit	100/100
	pop	10d
	plus	10m
	base	100/10000
	scale	束
	cost	100
@@ITEM
	no		16
	type	道具
	code	cloth
	name	帆布
	info	帆圖的材料
	price	3000
	limit	100/100
	pop	10d
	plus	10m
	base	100/10000
	scale	枚
	cost	100

@@ITEM
	no		2
	type	道具
	code	jobchange
	name	職業的秘密
	info	記載著各種工作內容的書
	price	25000
	limit	1/1
	pop	0
	base	10/200
	scale	冊
	plus	2h
	@@USE
		time	20m
		scale	回
		action	確認
		name	確認現在職業不足的狀況
		info	可以一目了然地看到目前哪些職業供不應求
		arg	nocount
		func	jobwant
	@@USE
		time	6h
		action	轉職
		scale	回
		arg		nocount
		name	成為造船屋
		info	轉職成造船屋
		param	1,26:27:28:29:30:31:32:33:34:35:36:37,0.2,shipb
		funcb	jobcheck
			need		1	造船指南書
			use		1	職業的秘密
		func	jobport
	@@USE
		time	6h
		action	轉職
		scale	回
		arg		nocount
		name	成為貿易商
		info	轉職成貿易商
		param	30,1:26:27:28:29:34:35:36:37,0.2,trader
		funcb	jobcheck
			use		1	職業的秘密
		func	jobport
	@@USE
		time	6h
		action	轉職
		scale	回
		arg		nocount
		name	成為冒險家
		info	轉職成冒險家
		param	26,1:30:31:32:33:34:35:36:37,0.2,explore
		funcb	jobcheck
			use		1	職業的秘密
		func	jobport
	@@USE
		time	6h
		action	轉職
		scale	回
		arg		nocount
		name	成為海盜
		info	轉職成海盜
		param	34,1:26:27:28:29:30:31:32:33,0.2,pirate
		funcb	jobcheck
			use		1	職業的秘密
		func	jobport
	@@USE
		time	6h
		action	轉職
		scale	回
		arg		nocount
		name	成為海軍司令
		info	轉職成海軍司令
		param	34,1:26:27:28:29:30:31:32:33,0.2,pros
		funcb	jobcheck
			use		1	職業的秘密
		func	jobport

@@ITEM
	no		3
	type	道具
	code	cm
	name	廣告包
	info	可以變得受歡迎，但也會失敗…
	price	100000
	limit	1/0.1
	pop	10d
	plus	5d
	base	10/50
	scale	包
	cost	10000
	@@use
		time	10h
		exp	10%
		scale	回
		action	進行廣告
		name	推出自己商店的廣告
		info	提高自己商店的人氣
		arg		nocount
			use		1	廣告包
		func	_local_
				my $up=int(500*(2-$DT->{rank}/5000));
				if ( rand(1000)<250 ) {
					$DT->{rank}-=$up;
					$DT->{rank}=1000 if $DT->{rank}<1000;
					my $ret="廣告適得其反：人氣降低了".int($up/100);
					WriteLog(0,$DT->{id},$ret);
					WriteLog(3,0,$DT->{shopname}."把廣告貼出來後得到了反效果");
					return $ret;
				}
				$DT->{rank}+=$up;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				my $ret="進行廣告宣傳後：人氣上升了".int($up/100)."%";
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."進行了廣告宣傳");
				return $ret;
			_local_
	@@use
		time	10h
		exp	0%
		name	推出他人商店的廣告
		info	提高他人商店的人氣
		arg		target|nocount
			use		1	廣告包
		func	_local_
				return '沒辦法指定自己的商店' if ($DT==$DTS);
				my $up=int(500*(2-$DTS->{rank}/5000));
				$DTS->{rank}+=$up;
				$DTS->{rank}=10000 if $DTS->{rank}>10000;
				my $ret="進行廣告宣傳後，".$DTS->{shopname}."的人氣上升了".int($up/100)."%";
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."對".$DTS->{shopname}."進行了廣告宣傳。");
				return $ret;
			_local_
	@@use
		time	16h
		exp	0%
		name	進行商會的廣告
		info	可以提升同商會所屬店鋪的人氣
		arg		nocount
			use		1	廣告包
		func	_local_
				return '沒有加入商會無法進行商會廣告' if !$DT->{guild};

				WriteLog(3,0,$DT->{shopname}."的商會「".$main::GUILD{$DT->{guild}}->[$GUILDIDX_name]."」進行了廣告宣傳");
				foreach my $DTS (@DT)
				{
				next if ($DTS->{guild} ne $DT->{guild});
				my $up=int(500*(2-$DTS->{rank}/5000));
				$DTS->{rank}+=$up;
				$DTS->{rank}=10000 if $DTS->{rank}>10000;
				my $ret="進行商會廣告後，".$DTS->{shopname}."的人氣上升了".int($up/100)."%";
				WriteLog(0,$DT->{id},$ret);
				}
				return '進行商會廣告';
			_local_
@@ITEM
	no		4
	type	道具
	code	edit-showcase
	name	展示架擴建拆卸工具
	info	展架擴建或拆除所需的一套工具。
	price	0
	limit	1/1
	pop	0
	plus	1d
	scale	組
	flag	noshowcase|norequest
	@@use
		time	1h
		scale	回
		action	施工
		price	10000
		name	將展示架改為1個
		info	將展示架改為1個
		arg		nocount		#★使用時の選択肢指定。
							#  nocount -> 使用回数選択なし
		param	1			#★独自関数用パラメータ
			use	1	展示架擴建拆卸工具
		func	_local_
			# ★展示架数変更
			#   param1 変更後の棚数
			my $oldcnt=$DT->{showcasecount};
			my $newcnt=$USE->{param1};
			$DT->{showcasecount}=$newcnt;
			
			if($oldcnt<$newcnt)
			{
				foreach ($oldcnt..$newcnt-1)
				{
					$DT->{showcase}[$_]=0;
					$DT->{price}[$_]=0;
				}
			}
			if($oldcnt>$newcnt)
			{
				splice(@{$DT->{showcase}},$newcnt);
				splice(@{$DT->{price}},$newcnt);
			}
			my $ret="展示架已經改成$DT->{showcasecount}個了";
			WriteLog(0,$DT->{id},$ret);
			WriteLog(3,0,$DT->{shopname}."的展示架已經變成$DT->{showcasecount}個了");
			
			return $ret;
		_local_
	@@use
		time	2h
		price	20000
		name	將展示架改為2個
		info	將展示架改為2個
		func	_local_1
		arg		nocount
		param	2
			use	1	展示架擴建拆卸工具
	@@use
		time	3h
		price	30000
		name	將展示架改為3個
		info	將展示架改為3個
		func	_local_1
		arg		nocount
		param	3
			use	1	展示架擴建拆卸工具
	@@use
		time	4h
		price	40000
		name	將展示架改為4個
		info	將展示架改為4個
		func	_local_1
		arg		nocount
		param	4
			use	1	展示架擴建拆卸工具
	@@use
		time	5h
		price	50000
		name	將展示架改為5個
		info	將展示架改為5個
		func	_local_1
		arg		nocount
		param	5
			use	1	展示架擴建拆卸工具
	@@use
		time	6h
		price	60000
		name	將展示架改為6個
		info	將展示架改為6個
		func	_local_1
		arg		nocount
		param	6
			use	1	展示架擴建拆卸工具
	@@use
		time	7h
		price	70000
		name	將展示架改為7個
		info	將展示架改為7個
		func	_local_1
		arg		nocount
		param	7
			use	1	展示架擴建拆卸工具
	@@use
		time	8h
		price	80000
		name	將展示架改為8個
		info	將展示架改為8個
		func	_local_1
		arg		nocount
		param	8
			use	1	展示架擴建拆卸工具
@@ITEM
	no		22
	type	道具
	code	book-help
	name	遇到困難時要讀的書
	info	也許這可以解決你的問題
	price	0
	limit	1/1
	pop	0
	plus	4h
	scale	本
	flag	noshowcase
	@@USE
		time	20m
		scale	回
		action	確認
		name	確認現在職業不足的狀況
		info	可以一目了然地看到目前哪些職業供不應求
		arg	nocount
		func	jobwant
	@@use
		time	40m
		scale	回
		action	買進
		price	1200
		name	市場上沒有麵包可以買的時候
		info	從特別的通路採購麵包（10箱為單位）
		okmsg	採購了麵包
			get		10	麵包
	@@use
		time	40m
		scale	回
		action	買進
		price	2400
		name	市場上沒有蘭姆酒可以買的時候
		info	從特別的通路採購蘭姆酒（10桶為單位）
		okmsg	採購了蘭姆酒
			get		10	蘭姆酒
	@@use
		time	40m
		scale	回
		action	雇用
		price	15000
		name	市場上沒有水手可以雇用的時候
		info	從特別通路雇用水手（10人為單位）
		okmsg	雇用了水手
			get		10	水手
	@@use
		time	10m
		scale	回
		action	販售
		name	金幣賣不掉又庫存很多的時候
		info	從特別的通路販售金幣
		okmsg	販售了金幣
			use		1	金幣
		func	_local_
			$DT->{money}+=8000 * $count;
			return "變賣金額：".GetMoneyString(8000 * $count);
		_local_
	@@use
		time	8h
		scale	回
		action	工作
		name	資金短缺的時候
		info	透過去工地當臨時工賺錢
		okmsg	努力工作得到了金幣
			get		2	金幣

@@ITEM
	no		24
	type	道具
	code	gift
	name	禮物卷
	info	得到你想要的！
	price	10000
	cost	10
	limit	10/0
	scale	枚
	@@USE
		time	20m
		scale	回
		action	獲得建議
		name	在兌換禮物卷之前
		info	向了解海洋的人尋求建議
		arg	nocount
		func	advice
			need		10	禮物卷
	@@USE
		time	20m
		scale	回
		action	確認
		name	確認現在職業不足的狀況
		info	可以一目了然地看到目前哪些職業供不應求
		arg	nocount
		func	jobwant
			need		10	禮物卷
	@@USE
		time	20m
		scale	回
		action	交換
		name	交換造船補給品
		info	成為造船屋的必需品
		okmsg	感謝您的使用
			use		10	禮物卷
			get		1	造船指南書
	@@USE
		time	20m
		scale	回
		action	交換
		name	交換貿易補給品
		info	成為貿易商的必需品
		okmsg	感謝您的使用
			use		10	禮物卷
			get		5	單船桅小型船
			get		20	金幣
			get		1	職業的秘密
			get		1	遇到困難時要讀的書
	@@USE
		time	20m
		scale	回
		action	交換
		name	交換冒險補給品
		info	成為冒險家的必需品
		okmsg	感謝您的使用
			use		10	禮物卷
			get		5	單船桅小型船
			get		20	金幣
			get		1	職業的秘密
			get		1	遇到困難時要讀的書
	@@USE
		time	20m
		scale	回
		action	交換
		name	交換海盜補給品
		info	成為海盜的必需品
		okmsg	感謝您的使用
			use		10	禮物卷
			get		5	單船桅小型船
			get		10	金幣
			get		1	職業的秘密
			get		1	遇到困難時要讀的書
	@@USE
		time	20m
		scale	回
		action	交換
		name	交換海軍補給品
		info	成為海軍司令的必需品
		okmsg	感謝您的使用
			use		10	禮物卷
			get		5	單船桅小型船
			get		10	金幣
			get		1	職業的秘密
			get		1	遇到困難時要讀的書

@@ITEM
	no		25
	type	道具
	code	slot
	name	抽獎卷
	info	可能會抽到稀有物品
	price	20000
	cost	100
	limit	10/1.2
	plus	-10h
	scale	枚
	pop	10d
	flag	noshowcase
	@@use
		time	20m
		scale	回
		action	抽獎
		name	嘗試抽獎
		info	中或不中都取決於你的運氣
		arg		nocount
		ngmsg	什麼都沒抽到…
			use		1	抽獎卷
			get		1	禮物卷		5%		抽到禮物卷了！
			get		1	廣告包		10%		抽到廣告包了！
			get		1	職業的秘密		5%		抽到職業的秘密了！
			get		1	看門狗			5%		抽到看門狗了！
			get		1	禁忌的快樂莓	10%		抽到禁忌的快樂莓了！
			get		1	麵包			5%		抽到麵包了！
			get		1	蘭姆酒			5%		抽到蘭姆酒了！

@@ITEM
	no		87
	type	道具
	code	defence-manbiki
	name	看門狗
	info	可以看門的高級血統犬
	price	500000
	cost	5000
	limit	1/0.5
	pop	1d
	plus	30m
	scale	隻
	flag	noshowcase|onlysend|human

@@ITEM
	no		88
	type	道具
	code	badgossip
	name	禁忌的快樂莓
	info	禁忌的果實有一股甜甜的香味
	price	50000
	cost	5000
	limit	1/1
	pop	0
	plus	1d
	scale	本
	@@use
		time	10h
		exp	20%
		exptime	8h
		scale	回
		price	50000
		scale	回
		action	開始進行
		price	0
		name	穆特的隱藏筆記本
		info	如果成功可以降低對方店舖的人氣，但也有可能會失敗…
		arg	target|nocount
			needpoint	20000
		func	_local_
			my $ret;
			if(rand(1000)<800 && !$DTS->{exp}{@@ITEMNO"廣告包"})
			{
				$DTS->{rank}-=int($DTS->{rank}/3);
				$ret='散佈'.$DTS->{shopname}.'謠言的作戰成功了。';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(2,0,$DTS->{shopname}.'因為謠言的關係人氣下降了。');
			}
			else
			{
				$DTS->{exp}{@@ITEMNO"廣告包"}-=100;
				$DTS->{exp}{@@ITEMNO"廣告包"}=0 if ($DTS->{exp}{@@ITEMNO"廣告包"} < 0);
				$DT->{rank}-=int($DT->{rank}/4);
				$ret='散佈'.$DTS->{shopname}.'謠言的作戰失敗了。';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."的策畫散佈".$DTS->{shopname}.'的謠言。');
			}
			return $ret;
			_local_
	@@use
		time	10h
		exp	25%
		exptime	8h
		scale	回
		action	入店行竊
		price	50000
		name	拉維君的偷竊之道
		info	就算追了那麼遠，也無濟於事…
			needpoint	20000
		func	stole
		arg		target|nocount


#------------------------------イベント
@@event
	start		10%
	basetime	5h
	plustime	5h
	code		happy
	startmsg	街上開始舉辦感謝祭了。
	endmsg		感謝祭已經結束了。
	info		街上因感謝祭而熱鬧非凡。
	func		_local_
		my $time=$main::TIMESPAN;
		$time=10*3600 if $time>10*3600; # 最大10%制限
		$time=int($time/36);
		
		foreach(@DT)
		{
			$_->{rank}+=int(rand($time));
			$_->{rank}=10000 if $_->{rank}>10000;
		}
		return 0;
	_local_

@@EVENT
	start		150%
	basetime	0h
	plustime	0h
	code		message
	info		消息
	startfunc	_local_
		my @message=(
		'哲學家「這個地球是由一個在下面伸出雙手的巨人支撐的。」',
		'宗教家「世界是由一隻500公里長的烏龜支撐的。」',
		'天文學家「大地的形狀必定會是個圓球。」',
		'冒險家「世界是圓的。如果從這裡往西走，那麼應該很快就會到達印度。」',
		'水手「如果往西走太遠，會從地上掉下來。」',
		'酒吧女郎「如果世界是圓的，另一邊的人就會倒下。」',
		'航海家「據說遠東有一個國家，一切都是金子做的。」',
		'航海家「據說在西邊的森林裡有一個基督的天堂。」',
		'水手「南角仙女用歌聲將船擊沉。」',
		'水手「注意發出無熱光源的船隻。那是一艘幽靈船。」',
		'冒險家「有時候，會有比船還大的章魚來襲擊並將船擊沉。」',
		);
		my $cnt=int(rand(scalar(@message)));
		return (0,$message[$cnt]);
	_local_


@@FUNCINIT
#職業が「冒險家」の場合、買い物に必要な時間を1/2にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if $DT->{job} eq 'explore';

@@FUNCITEM
######################################################################
# ★ジョブチェンジチェック
######################################################################
sub jobcheck
{
my($USE)=@_;
return 1 if ($DT->{job} eq $USE->{param4});
return 0;
}

######################################################################
# ★ジョブチェンジ
######################################################################
sub jobport
{
	$DT->{job}=$USE->{param4};
	WriteLog(3,0,$DT->{shopname}.'轉職成「'.$main::JOBTYPE{$USE->{param4}}.'」了。');
	main::RequireFile('inc-sea.cgi');

	my $ret;
	my $exp1=$DT->{exp}{$USE->{param1}};
	my $exp2=0;
	$ret.="拿著一本書，走向了轉職的神殿。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('阿姆扎','amza')."神官阿姆扎：<br>";
	$ret.="…嗯。想成為".$main::JOBTYPE{$USE->{param4}}."啊<br>";
	$ret.='全知全能的神啊！<br>就在此時此刻，讓<b>'.$DT->{shopname}."</b><br>";
	$ret.='在'.$main::JOBTYPE{$USE->{param4}}."的道路上前進吧！";
	$ret.="</td></tr></table><br>";
	$ret.="轉職成".$main::JOBTYPE{$USE->{param4}}."了。<br>";
	
	foreach my $exps (split(/:/,$USE->{param2}))
	{
		my $exp=$DT->{exp}{$exps};
		next if (!$DT->{item}[$exps-1] && !$exp);
		$exp2+=$exp;
		delete($DT->{exp}{$exps});
		main::DeleteSeaSub("$DT->{id}-abi$exps");
		main::DeleteSeaSub("$DT->{id}-exp$exps");
		my $msg='失去了'.$ITEM[$exps]->{name};
		if ($DT->{item}[$exps-1])
			{
			$DT->{item}[$exps-1]=0;
			$msg.="（手續費 ".GetMoneyString(50000)."）";
			$DT->{money}+=50000;
			}
		$msg.="。";
		WriteLog(0,$DT->{id},$msg);
		$ret.=$msg."<br>";
	}
	$exp2=int($exp2*$USE->{param3});
	$exp1+=$exp2;
	$exp1=1000 if $exp1>1000;
	$msg=$ITEM[$USE->{param1}]->{name}."的熟練度變成了 ".int($exp1/10)."%。";
	WriteLog(0,$DT->{id},$msg);
	$ret.=$msg."<br>";
	$DT->{exp}{$USE->{param1}}=$exp1;
	return $ret;
}

######################################################################
#★冒險艦隊の派遣
######################################################################
sub exploring
{
	my $itemno=$USE->{param1};	#派遣船
	my $data=$USE->{param2};	#派遣海域
	my $ability=$ship[$data+4];	#能力
	main::ReadSea($data);
	my @subdata;
	$subdata[0]=$main::NOW_TIME + 3600*11 + int(rand(7200));
	$subdata[1]=$data;

	# 生き残り判定
	if ($main::Pir * 12 > 100 + rand(1900 - $DT->{exp}{$itemno}))
		{
		$subdata[2]=1;	#海の藻屑
		}
		else
		{
		$subdata[2]=0;
		
		# 発見物判定
		if ($main::Civ + 20 < rand($ability) + int($DT->{exp}{$itemno} / 50))
			{
			$subdata[3]=1;
			$main::Civ+=int(rand(3) + 1);
			$main::Civ=100 if ($main::Civ > 100);
			}
		# 都市発見判定
		$subdata[4]=1 if (rand(100)+ ($main::Townnum * 12) < $ability + int($DT->{exp}{$itemno} / 50));
		}
	main::WriteSea($data);
	main::WriteSeaSub("$DT->{id}-exp$itemno",@subdata);
	my $ret;
	$ret.=qq|<IMG width="112" height="150" SRC="$main::IMAGE_URL/map/ship1.png"><br>|;
	my @AREA=("","歐洲","非洲","中東","印度","亞洲","新大陸");
	$ret.='向'.$AREA[$data]."派遣了冒險艦隊。";
	WriteLog(0,0,$DT->{shopname}."已經向".$AREA[$data]."派遣了冒險艦隊。");
	return $ret;
}

######################################################################
# ★冒險艦隊派遣前チェック
######################################################################
sub beforeexp
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣船
my $data=$USE->{param2};	#派遣海域
return 1 if ($DT->{job} ne 'explore');
return 1 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
if (!$ship[0])
	{
	main::RequireFile('inc-sea.cgi');
	@ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	}
return 1 if $ship[$data+4] < 1;
$USE->{info}.="<b>".$ship[$data+4]."</b>%";
$USE->{use}[0]->{no}=@@ITEMNO "麵包";
$USE->{use}[0]->{count}=$ship[11];
$USE->{use}[0]->{proba}=1000;
$USE->{use}[1]->{no}=@@ITEMNO "蘭姆酒";
$USE->{use}[1]->{count}=$ship[12];
$USE->{use}[1]->{proba}=1000;
$USE->{use}[2]->{no}=@@ITEMNO "水手";
$USE->{use}[2]->{count}=$ship[13];
$USE->{use}[2]->{proba}=1000;
return 0;
}

######################################################################
# ★派遣中のときだけ可
######################################################################
sub onlyexp
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣した船
return 0 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
return 1;
}

######################################################################
#★冒險艦隊の出迎え
######################################################################
sub meetexp
{
	my $itemno=$USE->{param1};	#派遣した船
	main::RequireFile('inc-sea.cgi');
	my @subdata=main::ReadSeaSub("$DT->{id}-exp$itemno");
	my @ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	my $seaman=$ship[13];		#水手
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;

	if ($main::NOW_TIME < $subdata[0])
		{
		$ret.="去了港口，但似乎還沒有艦隊返回的跡象。<br>";
		$ret.="讓我們再等一會兒吧。</tr></table>";
		return $ret;
		}
	main::DeleteSeaSub("$DT->{id}-exp$itemno");
	if ($subdata[2])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="已經是艦隊返回的時間了。<br>";
		$ret.="然而，無論等了多久，都看不到艦隊返航。<br><br>";
		$ret.="顯然是已經葬身大海了。<br>";
		$ret.="想知道他們是不是被海盜襲擊了呢・・・。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'的冒險艦隊葬身大海了。');
		return $ret;
		}
	$seaman=int($seaman * (70 + rand(30)) / 100);
	AddItem(@@ITEMNO "水手",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','exp','align="left" ')."<SPAN>提督</SPAN>：哦，我們剛剛抵達。<br>";
	$ret.="不只遇到颱風還遭到海盜的襲擊，<br>水手共 $seaman 人平安無事歸來。<br>";
	if ($subdata[3])
		{
		$ret.="在這次航行中，我們發現了一些罕見的事物。<br>";
		$ret.="已經寫成<SPAN>報告書</SPAN>了，請閱讀。<br>";
		AddItem((38 + $subdata[1]),1);
		}
		else
		{
		$ret.="在這次航行中，沒有發現任何罕見的事物。<br>";
		}
	if ($subdata[4])
		{
		$ret.="重要的是，我們<b>發現了新的陸地</b>。";
		$ret.="可以建造<SPAN>新的貿易城市</SPAN>了！<br>";
		AddItem((44 + $subdata[1]),1);
		}
		else
		{
		$ret.="在這次航行中，並沒有找到任何新的陸地。<br>";
		}
	$ret.="報告到此結束。直到開始下一次航海前讓我們休息一會兒吧。";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
#★発見物
######################################################################
sub disc
{
	my $no=$USE->{param1} - 1;
	my @DISCOVER=(
		[
		['錬金術','一種可以將任何東西變成黃金的技術。 只是沒有材料。',55],
		['米諾陶洛斯之斧','希臘牛頭人米諾陶洛斯使用的斧頭。手把的部分發出咆哮的聲音。',72],
		['法蘭克國王的軍刀','法蘭克國王使用的軍刀。鑲嵌著珠寶。',75],
		['猶大長袍','出賣基督的猶大所穿的衣服。會詛咒持有者。',65],
		['阿提拉的盔甲','阿提拉國王穿的盔甲。它很重，無法舉起。',65],
		['反向懷錶','指針逆時針走動的懷錶。會自己轉動，無需上緊發條。',75],
		['滅絕的十字架','基督在被釘十字架時使用的十字架。',60],
		['巨石陣','用石柱圍成一圈的遺跡。',60],
		],
		[
		['麒麟','全身散發出五色磷光的靈獸。有著牛的尾巴和馬的蹄子，腹部是黃色的。',90],
		['人草','生長在地面上的人形種族。',65],
		['只有眼睛的頭','頭部全是眼睛的人形種族。',70],
		['行走的山毛櫸','行走的山毛櫸樹。看見的話就會獲得好運。',75],
		['哈馬佩格的劍','古代王者之劍。由純金製成。',100],
		['邪惡的神像','供奉蛇形邪神的雕像。',60],
		['獅身人面像','半人半獅的怪物。喜歡解謎，會將解不開的人吃掉。',70],
		['維多利亞瀑布','一個巨大的瀑布湧入大地的裂縫中。',60],
		],
		[
		['薩拉丁的盔甲','古代國王的盔甲。設計簡樸，但能抵擋攻擊。',60],
		['天球儀','在圓形球體上描繪星空的藝術作品。',80],
		['克麗歐巴特拉的地毯','漂亮的繡花地毯。據說，一名絕世的美女被它所困擾。',100],
		['神燈精靈','一種寄宿在油燈裡的人形種族',75],
		['古蘭經','該地區人民所看的書。似乎記載著很重要的事情。',50],
		['蘇美粘土板','古人所寫。非常類似於我們的語言。',50],
		['布卷人','全身裹著布的人形種族。',60],
		['十字軍的寶劍','十字軍隊長在東征時使用的寶劍。',80],
		],
		[
		['象','一隻長著長鼻子的巨大靈獸。有厚實的身體和八隻腳。',80],
		['首長族','脖子長近一米的人形種族。',60],
		['食金蟲','以黃金為食的昆蟲。',60],
		['觔斗雲','可以載人飛行的雲。',75],
		['斯圖巴','一座巨大的石塔。裡面供奉著當地的神靈。',50],
		['莫喀爾的寶盾','古代王國流傳下來的傳說中的盾牌。以零散的藍寶石做為裝飾。',100],
		['勇者的彎刀','據說是古代英雄使用的彎刀。',80],
		['泰姬瑪哈陵','古代國王為祭祀女性而建造的巨大寺廟。',70],
		],
		[
		['算盤','該地區的民族遊戲玩具。藉由翻轉球來遊玩。',90],
		['妖刀村正','一把神奇的劍。支配持有者的思想，驅使他進行復仇。',70],
		['浦島太郎的寶箱','從海中樂園帶回來的寶物。附近似乎有一座龍宮城。',100],
		['切腹人','喜歡割自己肚子的人形種族。',75],
		['桃花源的地圖','記載著傳說的樂園位置的地圖，附近就是桃花源的所在。',100],
		['冬蟲夏草','半蟲半植物。冬天是蟲，但夏天時會變成草。',80],
		['高麗人蔘','治癒萬病的傳說中的人蔘。',80],
		['萬里長城','古代國王為防止外敵入侵而建造的城牆。',70],
		],
		[
		['金色的青蛙','一隻活生生的青蛙，但身體是金色的。',90],
		['挫折的遺跡','祭祀耶穌基督的遺跡，祭司王約翰臨終的地方，似乎是傳說中的聖地。',120],
		['黃金之河','一條流著黃金而不是水的河流。附近似乎有一個黃金國(El Dorado)。',100],
		['納斯卡線','畫在地上的一隻巨大鳥的圖畫。',75],
		['摩艾石像','巨大的人臉石像在海灘上一字排開。',100],
		['紋身的人','喜歡將臉和身體塗成藍色和紅色等顏色的人形種族。',75],
		['人魚','腰部以下是魚身的人形種族。',90],
		['空中遺跡','存在於空中的城市遺跡。居住的人民已經滅亡。',80],
		],
	);
	my @MYDIS=@{$DISCOVER[$no]};
	my $num=int(rand(scalar(@MYDIS))) + 0;
	my @msg=@{$MYDIS[$num]};
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="455"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/discover.png);" valign="top"><br><br>|;
	$no++;
	$num++;
	$ret.=qq|<IMG width="60" height="80" align="left" SRC="$main::IMAGE_URL/disc/$no-$num.png">|;
	$ret.="<SPAN>$msg[0]</SPAN><br><br>";
	$ret.="$msg[1]</tr></table>";
	$ret.="<br>做為獎勵，國王給了<b>".($msg[2])."</b>枚".main::GetTagImgItemType(51)."金幣。";
	AddItem(51,$msg[2]);
	return $ret;
}

######################################################################
#★都市建設
######################################################################
sub newtown
{
	my $data=$USE->{param1};	#派遣海域
	$name=$USE->{arg}->{message};
	main::RequireFile('inc-sea.cgi');
	main::ReadSea($data);
	my $ret;
	if ($main::Townnum > 9)
		{
		$ret.='令人驚訝的是，在這個新發現的城市中已經有設立了商館。<br>';
		$ret.='看來已經有人在此建立的商館。<br>';
		$ret.='是誰！誰先建的？';
		return $ret;
		}
	main::OutError('請輸入城市名稱。') if !$name;
	main::OutError('城市名稱使用了無法使用的文字。') if ($name =~ /([,:;\t\r\n<>&])/);
	my @TOWN=(
		[
		[@@ITEMNO "葡萄酒",20,10],
		[@@ITEMNO "起司",15,10],
		[@@ITEMNO "橄欖油",25,5],
		[@@ITEMNO "毛紡織品",10,15],
		[@@ITEMNO "彩色玻璃",20,10],
		[@@ITEMNO "雕塑",20,10],
		[@@ITEMNO "槍",15,10],
		],
		[
		[@@ITEMNO "金",10,5],
		[@@ITEMNO "鑽石",10,10],
		[@@ITEMNO "珊瑚",15,10],
		[@@ITEMNO "象牙",15,15],
		[@@ITEMNO "咖啡",10,10],
		[@@ITEMNO "鹽",20,10],
		[@@ITEMNO "羅望子",20,10],
		],
		[
		[@@ITEMNO "鐵礦石",10,10],
		[@@ITEMNO "硫磺",10,10],
		[@@ITEMNO "蜂蜜",15,10],
		[@@ITEMNO "砂糖",15,15],
		[@@ITEMNO "絨毯",8,7],
		[@@ITEMNO "麻紡織品",10,5],
		[@@ITEMNO "犀牛角",5,15],
		],
		[
		[@@ITEMNO "硝石",10,10],
		[@@ITEMNO "藍寶石",10,5],
		[@@ITEMNO "胡椒",1,4],
		[@@ITEMNO "肉桂",10,15],
		[@@ITEMNO "綿紡織品",15,10],
		[@@ITEMNO "印花棉布",10,10],
		[@@ITEMNO "龜殼",10,5],
		],
		[
		[@@ITEMNO "珍珠",10,10],
		[@@ITEMNO "清酒",10,10],
		[@@ITEMNO "茶",5,10],
		[@@ITEMNO "絹紡織品",5,15],
		[@@ITEMNO "浮世繪",10,5],
		[@@ITEMNO "漆器",5,15],
		[@@ITEMNO "刀",5,10],
		],
		[
		[@@ITEMNO "銀",5,10],
		[@@ITEMNO "祖母綠",5,10],
		[@@ITEMNO "可可",5,15],
		[@@ITEMNO "玉米",5,15],
		[@@ITEMNO "番茄",10,5],
		[@@ITEMNO "香菸",5,5],
		[@@ITEMNO "南瓜",5,10],
		],
	);
	$no=$data - 1;
	my @MYDIS=@{$TOWN[$no]};
	my $num=int(rand(scalar(@MYDIS))) + 0;
	my @msg=@{$MYDIS[$num]};
	my $price=int($ITEM[$msg[0]]->{price} * ($msg[1] + rand($msg[2])) / 100);
	my $life=$main::NOW_TIME + 86400*8 + int(rand(86400) * 4);
	foreach(1..$#main::SEA)
		{
		my @buf=split(',',$main::SEA[$_]);
		$life++ if $buf[0] == $life;
		main::OutError('已經有一座同名的城市。請使用其他名稱。') if $buf[1] eq $name;
		}
	push (@main::SEA,"$life,$name,$DT->{id},$msg[0],$price,0\n");
	$main::Civ+=int(rand(3));
	$main::Civ=100 if ($main::Civ > 100);
	$main::Pir+=int(rand(4));
	$main::Pir=100 if ($main::Pir > 100);
	main::WriteSea($data);
	$ret.=qq|<IMG width="255" height="153" SRC="$main::IMAGE_URL/map/trade.jpg"><br><br>|;
	$ret.='建立了商館。<br>都市「<b>'.$USE->{arg}->{message}.'</b>可以進行貿易了。';
	WriteLog(2,0,$DT->{shopname}.'發現了都市「'.$USE->{arg}->{message}.'」。');
	return $ret;
}

######################################################################
# ★貿易艦隊派遣前チェック
######################################################################
sub routesel
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣船
my $data=$USE->{param2};	#派遣海域
return 1 if ($DT->{job} ne 'trader');
return 1 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
if (!$ship[0])
	{
	main::RequireFile('inc-sea.cgi');
	@ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	}
return 1 if $ship[$data+4] < 1;
$USE->{info}.="<b>".$ship[$data+4]."</b>%";
main::ReadSea($data);
return 1 if $main::Townnum < 1;
$USE->{argselect}=';';
foreach(1..$main::Townnum)
	{
	my($date,$name,$other)=split(',',$main::SEA[$_],3);
	$USE->{argselect}.=$_.';'.$name.';';
	}
$USE->{use}[0]->{no}=@@ITEMNO "麵包";
$USE->{use}[0]->{count}=$ship[11];
$USE->{use}[0]->{proba}=1000;
$USE->{use}[1]->{no}=@@ITEMNO "蘭姆酒";
$USE->{use}[1]->{count}=$ship[12];
$USE->{use}[1]->{proba}=1000;
$USE->{use}[2]->{no}=@@ITEMNO "水手";
$USE->{use}[2]->{count}=$ship[13];
$USE->{use}[2]->{proba}=1000;
return 0;
}

######################################################################
#★貿易艦隊の派遣
######################################################################
sub route
{
	my $itemno=$USE->{param1};	#派遣した船
	my $data=$USE->{param2};	#派遣海域
	my $ability=int($ship[$data+4] / 2);	#積載量（ｘ万円相当）
	my $sel=$USE->{arg}->{select};

	#派遣数を増やす
	my @buf=split(',',$main::SEA[$sel]);
	main::OutError("「$buf[1]」的產品已經快沒有庫存了，無法進行派遣。<br>請變更派遣目的地。") if ($buf[0] < $main::NOW_TIME);
	$main::SEA[$sel]="$buf[0],$buf[1],$buf[2],$buf[3],$buf[4],".($buf[5] + 1)."\n";
	main::WriteSea($data);

	my @subdata;
	$subdata[0]=$main::NOW_TIME + 3600*11 + int(rand(7200));

	# 生き残り判定
	$subdata[1]=1 if ($main::Pir * 12 > 100 + rand(1900 - $DT->{exp}{$itemno}));

	#貿易量
	$subdata[2]=$buf[1];
	$subdata[3]=$buf[3];
	$subdata[4]=int($ITEM[$buf[3]]->{limit} * $ability / 100);
	$subdata[5]=$buf[4] * $subdata[4];

	# 発見者に利益発生
	if (defined($main::id2idx{$buf[2]}))
		{
		$DT[$main::id2idx{$buf[2]}]->{money}+=int($subdata[5] / 2);
		$DT[$main::id2idx{$buf[2]}]->{saletoday}+=int($subdata[5] / 2);
		}
	main::WriteSeaSub("$DT->{id}-exp$itemno",@subdata);
	my $ret;
	$ret.=qq|<IMG width="112" height="150" SRC="$main::IMAGE_URL/map/ship1.png"><br>|;
	$ret.="向「$buf[1]」派遣了貿易艦隊。";
	return $ret;
}

######################################################################
#★貿易艦隊の出迎え
######################################################################
sub meetrtp
{
	my $itemno=$USE->{param1};	#派遣した船
	main::RequireFile('inc-sea.cgi');
	my @subdata=main::ReadSeaSub("$DT->{id}-exp$itemno");
	my @ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	my $seaman=$ship[13];		#水手
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;

	if ($main::NOW_TIME < $subdata[0])
		{
		$ret.="去了港口，但似乎還沒有艦隊返回的跡象。<br>";
		$ret.="還是晚點再來吧</tr></table>";
		return $ret;
		}
	main::DeleteSeaSub("$DT->{id}-exp$itemno");
	if ($subdata[1])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="已經是艦隊返回的時間了。<br>";
		$ret.="然而，無論等了多久，都看不到艦隊返航。<br><br>";
		$ret.="顯然是已經葬身大海了。<br>";
		$ret.="想知道他們是不是被海盜襲擊了呢・・・。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'的貿易艦隊葬身大海了。');
		return $ret;
		}
	$seaman=int($seaman * (70 + rand(30)) / 100);
	AddItem(@@ITEMNO "水手",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','rtp','align="left" ')."<SPAN>提督</SPAN>：哦，我們剛剛抵達。<br>";
	$ret.="途中不只遇到颱風還遭到海盜的襲擊，<br>水手共 $seaman 人平安無事歸來。<br>";
	$ret.="本次的貿易，從都市「$subdata[2]」，<br>購買了";
	$ret.=main::GetTagImgItemType($subdata[3]).$ITEM[$subdata[3]]->{name}." ";
	$ret.=$subdata[4].$ITEM[$subdata[3]]->{scale}."。<br>";
	$ret.="收購的費用一共是".GetMoneyString($subdata[5])."。<br>";
	$DT->{money}-=$subdata[5];
	$DT->{paytoday}+=$subdata[5];
	AddItem($subdata[3],$subdata[4]);
	$ret.="以上是本次的報告";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
# ★武装艦隊派遣前チェック
######################################################################
sub nowpp
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣した船
my $data=$USE->{param2};	#派遣海域
if ($DT->{job} eq 'pirate') {$USE->{name}.="派遣掠奪";}
elsif ($DT->{job} eq 'pros') {$USE->{name}.="派遣偵察";}
else {return 0;}
return 1 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
if (!$ship[0])
	{
	main::RequireFile('inc-sea.cgi');
	@ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	}
return 1 if $ship[$data+4] < 1;
$USE->{info}.="<b>".$ship[$data+4]."</b>%";
$USE->{use}[0]->{no}=@@ITEMNO "麵包";
$USE->{use}[0]->{count}=$ship[11];
$USE->{use}[0]->{proba}=1000;
$USE->{use}[1]->{no}=@@ITEMNO "蘭姆酒";
$USE->{use}[1]->{count}=$ship[12];
$USE->{use}[1]->{proba}=1000;
$USE->{use}[2]->{no}=@@ITEMNO "水手";
$USE->{use}[2]->{count}=$ship[13];
$USE->{use}[2]->{proba}=1000;
return 0;
}

######################################################################
#★武装艦隊の派遣
######################################################################
sub attack
{
	my $itemno=$USE->{param1};	#派遣船
	my $data=$USE->{param2};	#派遣海域
	my $ability=$ship[$data+4];	#能力
	main::ReadSea($data);
	my @subdata;
	$subdata[0]=$main::NOW_TIME + 3600*11 + int(rand(7200));
	$subdata[1]=$data;
	my $ret;
	$ret.=qq|<IMG width="112" height="150" SRC="$main::IMAGE_URL/map/ship1.png"><br>|;
	my @AREA=("","歐洲","非洲","中東","印度","亞洲","新大陸");

	if ($DT->{job} eq 'pros')
	{
	# 海軍の処理
	# 生き残り判定
	if ($main::Pir * 6 > 100 + rand(1900 - $DT->{exp}{$itemno}))
		{
		$subdata[2]=1;	#海の藻屑
		}
		else
		{
		# 海盜出現率低下
		$main::Pir-=int(rand(5)) + 6;
		$main::Pir=0 if ($main::Pir < 0);
		# 海軍偵察率上昇
		$main::Pro+=int(rand(5)) + 4;
		$main::Pro=100 if ($main::Pro > 100);
		}
	$ret.='向'.$AREA[$data]."派遣了海軍";
	WriteLog(0,0,$DT->{shopname}."向".$AREA[$data]."派遣了海軍。");
	}
	else
	{
	# 海盜の処理
	# 生き残り判定
	if ($main::Pro * 16 > 100 + rand(1900 - $DT->{exp}{$itemno}))
		{
		$subdata[2]=1;	#海の藻屑
		}
		else
		{
		# 海盜出現率上昇
		$main::Pir+=int(rand(5)) + 4;
		$main::Pir=100 if ($main::Pir > 100);
		}
	$ret.='向'.$AREA[$data]."派遣了海盜船";
	WriteLog(2,0,$AREA[$data]."似乎有海盜出沒。");
	}
	if (!$subdata[2])
		{
		$subdata[2]=0;
		# 金幣
		$subdata[3]=int(($ability / 4) + ($DT->{exp}{$itemno} / 100) + rand(5));
		# 貿易品
		if ($main::Townnum > 0 && $main::Pir > rand(20))
			{
			my $sel=int(rand($main::Townnum)) + 1;
			my @buf=split(',',$main::SEA[$sel]);
			$subdata[4]=$buf[3];
			$subdata[5]=int($ITEM[$buf[3]]->{limit} * $ability / 200);
			}
		}
	main::WriteSea($data);
	main::WriteSeaSub("$DT->{id}-exp$itemno",@subdata);
	return $ret;
}

######################################################################
#★武装艦隊の出迎え
######################################################################
sub meetpp
{
	my $itemno=$USE->{param1};	#派遣した船
	main::RequireFile('inc-sea.cgi');
	my @subdata=main::ReadSeaSub("$DT->{id}-exp$itemno");
	my @ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	my $seaman=$ship[13];		#水手
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;

	if ($main::NOW_TIME < $subdata[0])
		{
		$ret.="去了港口，但似乎還沒有艦隊返回的跡象。<br>";
		$ret.="還是晚點再來吧</tr></table>";
		return $ret;
		}
	main::DeleteSeaSub("$DT->{id}-exp$itemno");
	if ($DT->{job} eq 'pros')
	{
	# 海軍の処理
	if ($subdata[2])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="已經是艦隊返回的時間了。<br>";
		$ret.="然而，無論等了多久，都看不到艦隊返航。<br><br>";
		$ret.="顯然是已經葬身大海了。<br>";
		$ret.="輸給海盜了嗎・・・。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'的海軍敗給了海盜，葬身大海。');
		return $ret;
		}
	$seaman=int($seaman * (40 + rand(30)) / 100);
	AddItem(@@ITEMNO "水手",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','pro','align="left" ')."<SPAN>提督</SPAN>：哦，我們剛剛抵達。<br>";
	$ret.="途中不只遇到颱風還遭到海盜的襲擊，<br>水手共 $seaman 人平安無事歸來。<br>";

	if ($subdata[3])
		{
		$ret.="這一次，我們找到並清理了一個海盜的營地。<br>";
		$ret.="沒收了".main::GetTagImgItemType(51)."金幣 $subdata[3]枚。<br>";
		AddItem(51,$subdata[3]);
		}
	if ($subdata[4])
		{
		$ret.="途中受到海盜船的攻擊，並擊敗了他們<br>";
		$ret.="沒收了".main::GetTagImgItemType($subdata[4]).$ITEM[$subdata[4]]->{name}." ";
		$ret.=$subdata[5].$ITEM[$subdata[4]]->{scale}."。<br>";
		AddItem($subdata[4],$subdata[5]);
		}
	$ret.="報告到此結束。很自豪能為公共安全做出貢獻。";
	$ret.="</tr></table>";
	return $ret;
	}
	# 海盜の処理
	if ($subdata[2])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="已經是艦隊返回的時間了。<br>";
		$ret.="然而，無論等了多久，都看不到艦隊返航。<br><br>";
		$ret.="顯然是已經葬身大海了。<br>";
		$ret.="輸給海軍了嗎・・・。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'的海盜船被海軍討伐了。');
		return $ret;
		}
	$seaman=int($seaman * (40 + rand(30)) / 100);
	AddItem(@@ITEMNO "水手",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','pir','align="left" ')."<SPAN>提督</SPAN>：嘿，我們回來啦。<br>";
	$ret.="途中不只遇到颱風還遭到海盜的襲擊，<br>水手共 $seaman 人平安無事歸來。<br>";

	if ($subdata[3])
		{
		$ret.="這一次，我們擊沉了四處遊蕩的冒險艦隊。<br>";
		$ret.="得到了".main::GetTagImgItemType(51)."金幣 $subdata[3]枚。<br>";
		AddItem(51,$subdata[3]);
		}
	if ($subdata[4])
		{
		$ret.="搶劫了途中經過的貿易艦隊<br>";
		$ret.="得到了".main::GetTagImgItemType($subdata[4]).$ITEM[$subdata[4]]->{name}." ";
		$ret.=$subdata[5].$ITEM[$subdata[4]]->{scale}."。<br>";
		AddItem($subdata[4],$subdata[5]);
		}
	$ret.="怎樣，我們幹得如何呢？這果然是海盜的醍醐味啊！";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
#★開始時のアドバイス
######################################################################
sub advice
{
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;
	$ret.=main::GetTagImgKao('海雷丁','bal','align="left" ')."<SPAN>海雷丁</SPAN>：想尋求咱的意見，真是好膽量。<br>";
	$ret.="聽好了，禮物卷交換什麼，是<BIG>非常重大的選擇</BIG>。<br>";
	$ret.="你的第一個生活將由此決定，所以現在找出什麼職業是有利的。<br><br>";
	$ret.="１．<BIG>造船</BIG>很適合初學者，但<b>同業</b>很多時會很難生存。<br>";
	$ret.="２．<BIG>貿易</BIG>，歐洲的<b>海盜出現率</b>太高的話會虧損。<br>";
	$ret.="３．<BIG>冒險</BIG>，歐洲的<b>海盜出現率</b>要低，<b>未開拓的區域</b>要高才好。<br>";
	$ret.="４．<BIG>海盜</BIG>，歐洲的<b>海軍偵察率</b>太高的話還是別幹的好。<br>";
	$ret.="５．<BIG>海軍</BIG>，歐洲的<b>海盜出現率</b>太低的話會虧損。<br>";
	$ret.="<br>知道了嗎？此外，不失敗的最大技巧是，去閱讀<SPAN>圖書館</SPAN>的資料吧。";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
#★職業不足・飽和状況
######################################################################
sub jobwant
{
	my %jobwant;
	my $sum;
	foreach my $DT(@DT)
		{
		next if !$DT->{job};
		$jobwant{$DT->{job}}++;
		$sum++;
		}
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top" align="center"><br><br>|;
	$ret.=$main::TB;

	my %jobneed=qw(shipb 10 explore 15 trader 55 pirate 10 pros 10);
	foreach("shipb","explore","trader","pirate","pros")
		{
		$ret.=$main::TR.$main::TDB.$main::JOBTYPE{$_};
		my $i=($sum) ? ($jobwant{$_} / $sum / $jobneed{$_} * 100 * 100) : 100;
		$ret.=$main::TD.main::GetMarketStatusGraph($i).$main::TRE;
		}
	$ret.="</tr></table></tr></table>";
	return $ret;
}

######################################################################
#★万引き
######################################################################
sub stole
{
	return '無法從自己店裡偷東西。偷竊失敗了。' if  ($DT->{id} eq $DTS->{id});
	my $ret="偷竊失敗了。賠償金".GetMoneyString(500000)."已經被扣留。";
	if($DTS->{item}[@@ITEMNO"看門狗"-1])
	{
		$DT->{rank}-=int($DT->{rank}/4);
		$DTS->{money}+=500000;
		$DTS->{saletoday}+=500000;
		$DT->{money}-=500000;
		$DT->{paytoday}+=500000;
		WriteLog(3,0,$DT->{shopname}."曾經向".$DTS->{shopname}."進行偷竊，但被看門狗捉到了。");
		WriteLog(3,0,$DT->{shopname}."向".$DTS->{shopname}."支付了賠償金".GetMoneyString(500000)."。");
		WriteLog(0,$DT->{id},$ret);
		return $ret;
	}
	if(rand(1000)>900)
	{
		$DTS->{money}+=500000;
		$DTS->{saletoday}+=500000;
		$DT->{money}-=500000;
		$DT->{paytoday}+=500000;
		$DT->{rank}-=int($DT->{rank}/4);
		WriteLog(3,0,$DT->{shopname}."曾經向".$DTS->{shopname}."進行偷竊但失敗了。");
		WriteLog(3,0,$DT->{shopname}."向".$DTS->{shopname}."支付了賠償金".GetMoneyString(500000)."。");
		WriteLog(0,$DT->{id},$ret);
		return $ret;
	}
	$ret="偷竊成功了";
	my $manbiki_count=0;
	foreach my $idx (0..$DTS->{showcasecount}-1)
	{
		my $itemno=$DTS->{showcase}[$idx];
		if($itemno)
		{
			my $cnt=int($DTS->{item}[$itemno-1]*3/4);
			$cnt=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$cnt>$ITEM[$itemno]->{limit};
			$DTS->{item}[$itemno-1]-=$cnt;
			$DT->{item}[$itemno-1]+=$cnt;
			$manbiki_count+=$cnt*$DTS->{price}[$idx];
		}
	}
	$main::STATE->{safety}=int($main::STATE->{safety} * 18 / 19);
	WriteLog(2,0,$DTS->{shopname}."被偷了總價大概".GetMoneyString($manbiki_count)."的損失") if $manbiki_count;
	WriteLog(2,0,'闖進'.$DTS->{shopname}."的小偷什麼都沒拿就逃走了。") if !$manbiki_count;
	WriteLog(0,$DT->{id},$ret);
	return $ret;
}


@@FUNCUPDATE
sub UpdateResetBefore #決算直前の処理(関数名固定)
{
	UpdateTodayPrize();
	
	sub UpdateTodayPrize
	{
		#賞品授与
		my @TOP123=(
			[
				['禁忌的快樂莓',	[[@@ITEMNO "禁忌的快樂莓", 1],			],],
				['看門狗',	[[@@ITEMNO "看門狗", 1],			],],
				['麵包',	[[@@ITEMNO "麵包", 400],			],],
				['蘭姆酒',	[[@@ITEMNO "蘭姆酒", 200],			],],
				['廣告包',	[[@@ITEMNO "廣告包", 1],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 5],			],],
				['抽獎卷',	[[@@ITEMNO "抽獎卷", 5],			],],
			],
			[
				['禁忌的快樂莓',	[[@@ITEMNO "禁忌的快樂莓", 1],			],],
				['麵包',	[[@@ITEMNO "麵包", 400],			],],
				['蘭姆酒',	[[@@ITEMNO "蘭姆酒", 200],			],],
				['廣告包',	[[@@ITEMNO "廣告包", 1],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 4],			],],
				['抽獎卷',	[[@@ITEMNO "抽獎卷", 4],			],],
			],
			[
				['職業的秘密',	[[@@ITEMNO "職業的秘密", 1],			],],
				['麵包',	[[@@ITEMNO "麵包", 200],			],],
				['蘭姆酒',	[[@@ITEMNO "蘭姆酒", 100],			],],
				['廣告包',	[[@@ITEMNO "廣告包", 1],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 3],			],],
				['抽獎卷',	[[@@ITEMNO "抽獎卷", 3],			],],
			],
			[
				['職業的秘密',	[[@@ITEMNO "職業的秘密", 1],			],],
				['麵包',	[[@@ITEMNO "麵包", 100],			],],
				['蘭姆酒',	[[@@ITEMNO "蘭姆酒", 50],			],],
				['禮物卷',	[[@@ITEMNO "禮物卷", 2],			],],
				['抽獎卷',	[[@@ITEMNO "抽獎卷", 2],			],],
			],
		);
		
		TopGetItem($DT[0],$TOP123[0],"本次優勝") if defined($DT[0]);
		TopGetItem($DT[1],$TOP123[1],"可惜第二名的") if defined($DT[1]);
		TopGetItem($DT[2],$TOP123[2],"勉強得名的") if defined($DT[2]);
	
		for(my $i=9; $i<$#DT; $i+=10)
		{
			TopGetItem($DT[$i],$TOP123[3],"作為特別獎".($i+1)."名的") if defined($DT[$i]);
		}
		
		sub TopGetItem
		{
			my($DT,$itemlist,$head)=@_;
			
			my @list=@{$itemlist};
			my @getitem=@{$list[int(rand($#list+1))]};
			
			my $msg=$head.$DT->{shopname}."收到".$getitem[0]."";
			WriteLog(0,0,0,$msg,1);
			foreach (@{$getitem[1]})
			{
				my @itemnocount=@{$_};
				
				my $cnt=AddItem($DT,$itemnocount[0],$itemnocount[1]);
				my $ITEM=$ITEM[$itemnocount[0]];
				WriteLog(0,$DT->{id},0,$head."作為".$ITEM->{name}."的獎品，獲得".$itemnocount[1].$ITEM->{scale},1);
				$cnt=$itemnocount[1]-$cnt;
				WriteLog(0,$DT->{id},0,"但是由於超過了最大持有數量，".$cnt.$ITEM->{scale}."被丟棄了",1) if $cnt;
			}
		}
	}
}

sub UpdateResetAfter #決算直後の処理(関数名固定)
{
	foreach my $DT (@DT)
		{
		$DT->{profitstock}=5000000 if ($DT->{profitstock} > 5000000);
		$DT->{profitstock}=-1000000 if ($DT->{profitstock} < -1000000);
		if ($DT->{money} > 50000000)
			{
			$DT->{money} -= int( ($DT->{money} - 20000000)/2 );
			$DT->{rank} += int( (10000 - $DT->{rank})/2 );
			$DT->{rank}=10000 if $DT->{rank}>10000;
			PushLog(2,0,$DT->{shopname}.'舉辦了慶祝活動。');
			}
		}
	main::RequireFile('inc-atlas.cgi');
}

@@FUNCNEW

# @@DEFINE Set NewShopMoney NewShopTime NewShopItem の処理
$DT->{money}=@@VALUE"NewShopMoney" if @@VALUE"NewShopMoney";
$DT->{time}=$NOW_TIME-eval(@@VALUE"NewShopTime") if @@VALUE"NewShopTime";
if(@@VALUE"NewShopItem")
{
	my %item=split /:/,@@VALUE"NewShopItem";
	while(my($key,$val)=each %item)
	{
		foreach my $item (@ITEM)
		{
			 $DT->{item}[$item->{no}-1]+=$val,last if $key eq $item->{code} or $key eq $item->{name};
		}
	}
}

# $DEFINE_FUNCNEW_NOLOG=1 を設定すると、システム側の最近の出来事新装開店メッセージを抑制します。
# $DEFINE_FUNCNEW_NOLOG=1;
# WriteLog(1,0,0,$DT->{shopname}."がエントリーしました",1);

# その他、新装開店時に独自の処理を追加できます。

@@FUNCSHOPIN

SetUserDataEx($DT,'_so_move_in',$NOW_TIME); # 移転時刻を記録
if($DT->{job} eq 'peddle')
{
	# 行商人(peddle)には移転消費時間の1/2を返還
	$DT->{_MoveTownTime}=int($DT->{_MoveTownTime}/2);
	EditTime($DT,$DT->{_MoveTownTime});
	WriteLog(0,$DT->{id},0,'轉移時間大概是'.GetTime2HMS($DT->{_MoveTownTime}).'會完成',1);
}
if(GetUserDataEx($DT,'_so_present_money'))
{
	WriteLog(0,$DT->{id},0,'原始轉移街道送了餞別禮，得到'.GetMoneyString(GetUserDataEx($DT,'_so_present_money')).'了',1);
	SetUserDataEx($DT,'_so_present_money','');
}

@@FUNCSHOPOUT

if(GetUserDataEx($DT,'_so_move_in'))
{
	my $present_money=int(($NOW_TIME-GetUserDataEx($DT,'_so_move_in'))/86400)*5000;
	EditMoney($DT,$present_money); # 滞在期間1日に付き\5000を餞別として資金へ
	SetUserDataEx($DT,'_so_present_money',$present_money);
	SetUserDataEx($DT,'_so_move_in',''); # $DT->{user}{_so_move_in} を削除
}

@@FUNCBUY
# package item です。
# 
# $item::BUY を利用できます。$item::BUY の構造はマニュアルの @@ITEM funcb をご覧ください。
# 商品毎の処理は @@ITEM funcb を利用してください。

if($BUY->{whole})
{
	if (rand(1000) > 990 && $BUY->{num} > 10)
	{
	$count=AddItemSub(@@ITEMNO"禮物卷",1,$BUY->{dt});
	WriteLog(0,$BUY->{dt}{id},'在市場的抽獎中得到禮物卷'.$count.'枚。');
	$main::ret.='<br>獲得了抽獎的禮物卷'.$count.'枚！';
	}
}

@@END #定義終了宣言(以降コメント扱い)

