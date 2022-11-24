use utf8;
# 商館 2005/01/06 由來
# ワールドアトラス版

DataRead();
CheckUserPass(1);
RequireFile('inc-sea.cgi');

$disp.=GetMenuTag('tradehouse',		'['.l('欧州').']')
	.GetMenuTag('tradehouse',	'['.l('アフリカ').']','&sea=2')
	.GetMenuTag('tradehouse',	'['.l('中近東').']','&sea=3')
	.GetMenuTag('tradehouse',	'['.l('インド').']','&sea=4')
	.GetMenuTag('tradehouse',	'['.l('アジア').']','&sea=5')
	.GetMenuTag('tradehouse',	'['.l('新大陸').']','&sea=6');
$disp.="<hr width=500 noshade size=1>";
$Q{sea}||=1;
ReadSea($Q{sea});
my @AREA=("",l("欧州"),l("アフリカ"),l("中近東"),l("インド"),l("アジア"),l("新大陸"));

$disp.="<BIG>●".l('商館')."</BIG><br><br>";

$disp.="$TB$TR$TDB".$AREA[$Q{sea}];
$disp.="$TD<SPAN>".l('未踏破領域')."</SPAN>：".(100 - $Civ)." %";
$disp.="$TD<SPAN>".l('海賊出現率')."</SPAN>：".($Pir + 0)." %";
$disp.="$TD<SPAN>".l('海軍偵察率')."</SPAN>：".($Pro + 0)." %";
$disp.=$TRE.$TBE;

$disp.=<<STR;
<br>
$TB$TR
$TDB${\l('都市名')}
$TDB${\l('発見者')}
$TDB${\l('産物')}
$TDB${\l('仕入値')}
$TDB${\l('産出量')}
$TDB${\l('航路')}
$TRE
STR

foreach(1..$#SEA)
	{
	my @buf=split(',',$main::SEA[$_]);
	next if !$buf[0];
	$disp.=$TR;
	$disp.=$TD.$buf[1];
	$disp.=defined($id2idx{$buf[2]}) ?'<td>'.$DT[$id2idx{$buf[2]}]->{shopname} : '<td>'.l('なし');
	$disp.=$TD.GetTagImgItemType($buf[3]).$ITEM[$buf[3]]->{name}."<br>";
	$disp.="<small>(".l('定価')." ".GetMoneyString($ITEM[$buf[3]]->{price}).")</small>";
	$disp.=$TD.GetMoneyString($buf[4])."<br>";
	$disp.="<small>(".l('定価の%1%',int($buf[4] / $ITEM[$buf[3]]->{price} * 100)).")</small>";
	$disp.=$TD.GetAmountMessage($buf[0]);
	$disp.=$TD."(".l('%1本',($buf[5] + 0)).")";
	$disp.=$TRE;
	}
	$disp.=$TBE;

OutSkin();
1;


sub GetAmountMessage
{
	my($rank)=@_;
	my $per=int(($rank - $NOW_TIME)/8640);
	$per=100 if $per > 100;
	$per=0 if $per < 0;
	my $i=l("品薄");
	$i=l("普通") if $per>=30;
	$i=l("豊富") if $per>=60;
	$i=l("底無") if $per>=80;
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/b.gif" width="|.(    $per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.=" ".$i;
	$bar.="</nobr><br>";
	
	return $bar;
}

