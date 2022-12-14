use utf8;
# アイテム詳細表示 2005/01/06 由來

$NOMENU=1;
Turn();
DataRead();
CheckUserPass();

$itemno=$Q{no};
$showcase=$Q{sc};
CheckItemNo($itemno);

RequireFile('inc-html-ownerinfo.cgi');

GetMarketStatus();

$disp.="<BIG>●".l('倉庫')."</BIG><br><br>";

my $ITEM=$ITEM[$itemno];
$disp.= GetTagImgItemType($itemno,0,2).$ITEM->{name};
$disp.= GetTagImgItemType(0,$ITEM[$itemno]->{type})."<br><br>";

$disp.=$TB;
$disp.="$TR$TDB".l('在庫')."$TD$DT->{item}[$itemno-1] $ITEM->{scale}$TRE";
$disp.="$TR$TDB".l('標準価格')."$TD".GetMoneyString($ITEM->{price}).$TRE;
$disp.="$TR$TDB".l('維持費')."$TD".GetMoneyString($ITEM->{cost}).$TRE;
$disp.="$TR$TDB".l('説明')."$TD$ITEM->{info}$TRE";

unless ($ITEM->{flag}=~/s/) {	# 陳列不可
	if($ITEM->{marketprice})
	{
	$disp.="$TR$TDB".l('相場')."$TD".GetMoneyString($ITEM->{marketprice}).$TRE;
	$disp.="$TR$TDB".l('最安値')."$TD".GetMoneyString($ITEM->{marketpricelow}).$TRE;
	$disp.="$TR$TDB".l('最高値')."$TD".GetMoneyString($ITEM->{marketpricehigh}).$TRE;
	}
	else
	{
	$disp.="$TR$TDB".l('相場')."$TD".l("販売店舗なし")."$TRE";
	}
	$disp.="$TR$TDB".l('需供')."$TD".GetMarketStatusGraph($ITEM->{uppoint})."$TRE";
}
$disp.=$TBE;

if($ITEM->{flag}=~/s/)
	{
	$disp.="<hr width=500 noshade size=1>";
	$disp.='※'.l('%1を販売することはできません',$ITEM[$itemno]->{name}).'<br>';
	}
	else
	{
	$disp.="※".l('この商品は陳列しても売れません')."<br>" if ( $ITEM->{popular}==0);
	$disp.="※".l('この商品は陳列してもほとんど売れません')."<br>" if ( $ITEM->{popular} > 800000);
	$disp.="<hr width=500 noshade size=1>";
	RequireFile('inc-item-show.cgi');
	}

$disp.="<hr width=500 noshade size=1>";
if($ITEM->{flag}=~/t/)
	{
	$disp.='※'.l('%1を%2することはできません',$ITEM[$itemno]->{name},($ITEM->{flag}=~/h/)? l("解雇") : l("破棄")).'<br>';
	}
	else
	{
	RequireFile('inc-item-throw.cgi');
	}

$disp.="<hr width=500 noshade size=1>";
$itemcode=GetPath($ITEM_DIR,"use",$ITEM[$itemno]->{code});
if($itemcode ne '' && -e $itemcode)
{
	my $ITEM=$ITEM[$itemno];
	@item::DT=@DT;
	$item::DT=$DT;
	@item::ITEM=@ITEM;
	$item::ITEM=$ITEM;
	RequireFile('inc-item.cgi');
	require $itemcode;
	@USE=GetUseItemList();

	if($USE[0]->{name} ne '')
	{
	foreach my $USE (@USE)
		{
	$disp.="●";
	$disp.=qq|<a href="action.cgi?key=item-m&item=$itemno&no=$USE->{no}&$USERPASSURL&bk=$Q{bk}">| if $USE->{useok};
	$disp.=($USE->{useok} || $USE->{dispok}) ? $USE->{name} : l("？？？？？？？？");
	$disp.="</a>" if $USE->{useok};
	$disp.="<br>";
		}
	}
}
OutSkin();
1;
