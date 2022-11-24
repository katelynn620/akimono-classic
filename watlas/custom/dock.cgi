use utf8;
# ドック 2004/02/28 由來
# ワールドアトラス版

Lock() if ($Q{mode});	# できるだけ早くロック。
DataRead();
CheckUserPass();

$disp.=GetMenuTag('dock',	'['.l('第一船団').']')
	.GetMenuTag('dock',	'['.l('第二船団').']','&plus=1')
	.GetMenuTag('dock',	'['.l('第三船団').']','&plus=2')
	.GetMenuTag('dock',	'['.l('第四船団').']','&plus=3');
$disp.="<hr width=500 noshade size=1>";
$disp.="<BIG>●".l('ドック')."</BIG><br><br>";

my %itemnum=qw(explore 26 trader 30 pirate 34 pros 34);
if (!$itemnum{$DT->{job}})
	{
	$disp.=l("ドックを利用するには，関係する職業に就く必要があります。");
	OutSkin();
	exit;
	}
$Q{ship}=($itemnum{$DT->{job}}+$Q{plus});
my @AREA=("",l("欧州"),l("アフリカ"),l("中近東"),l("インド"),l("アジア"),l("新大陸"));
$disp.=GetTagImgItemType($Q{ship}).$ITEM[$Q{ship}]->{name}."<br><br>";

undef @subdata;
@subdata=ReadShipSub($DT->{id}."-abi".$Q{ship});
RequireFile('inc-dock.cgi') if ($Q{mode});

$disp.="$TB$TR$TDB".l('編成')."<td colspan=6>";
foreach(0..4)
	{
	next if !$subdata[$_];
	$disp.=GetTagImgItemType($subdata[$_]);
	$DT->{item}[$subdata[$_]-1]++;
	}
$disp.="$TRE$TR$TDB".l('海域適性');
foreach(0..5)
	{
	$disp.="$TD<SPAN>".$AREA[$_+1]."</SPAN>：".($subdata[$_+5] + 0)." %";
	}
$disp.="$TRE$TR$TDB派遣条件";
$disp.="<td colspan=2>".GetTagImgItemType(18)."<SPAN>".l('パン')."</SPAN>：".l("%1食",($subdata[11] + 0));
$disp.="<td colspan=2>".GetTagImgItemType(19)."<SPAN>".l('ラム酒')."</SPAN>：".l("%1樽",($subdata[12] + 0));
$disp.="<td colspan=2>".GetTagImgItemType(20)."<SPAN>".l('水夫')."</SPAN>：".l("%1人",($subdata[13] + 0));
$disp.=$TRE.$TBE;

$disp.="<hr width=500 noshade size=1>";
$disp.="<BIG>●".l('船団の編成')."</BIG><br><br>";

my $shipform;
foreach my $num(5..11)
	{
	my $amt=$DT->{item}[$num-1];
	next if !$amt;
	$amt=5 if $amt > 5;
	$shipform.=$TR;
	$shipform.=$TD.GetTagImgItemType($num).$ITEM[$num]->{name}.$TD;
	foreach my $cnt(1..$amt)
		{
		$shipform.='<input type=checkbox name="'.$num.'_'.$cnt.'" value="1"> ';
		}
	$shipform.=$TRE;
	}

if (!$shipform)
	{
	$disp.=l("船を持っていないため，船団を編成できません。");
	}
	else
	{
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=plus VALUE="$Q{plus}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="make">
$TB
$shipform
$TR<td colspan=2>${\l('最大 5つまで選択できます。')}<br>
${\l('何も選択しないと船団を解体します。')}$TRE
$TBE
<br><INPUT TYPE=SUBMIT VALUE="${\l('船団を編成する')}">
</FORM>
STR
	}

OutSkin();
1;


sub ReadShipSub
{
	my($file)=@_;
	my $filename=GetPath($SUBDATA_DIR,$file);
	open(IN,"<:encoding(UTF-8)",$filename) or return;
	read(IN,my $buf,-s $filename);
	close(IN);
	my @buf=split(',',$buf);
	return @buf;
}


