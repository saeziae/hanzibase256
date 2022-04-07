#!/usr/bin/env python3
import sys
TABLE='人十二又力九八七刀上大子小下工三口女山及才千土久亡寸川弓夕不中天太日方分五心水月化比公今手六反少文夫火元毛王友支片木引止父尺午牛氏井仁犬以可生出主用去民本外加四正由平代白立打北世必目市布石母未半示古史失功田皮令左句右玉冬兄永巨幼甘仙申在有地全年多自好行同成如老因向合各百西回次先名再安共光至交字米色式早列江衣存忙守充考血印肉危曲耳羊休伐竹吉伏刑朱仰舌宅宇寺兆我作利位走完形身改快花住志更究近何技告兵言低足角助防希村投弟良初均男判冷材君困否迎吹私忘序辛尾妙忍豆秀臣赤扶孝的和到事所法定明使物知表者命性果放官取育直治金受非油林空往易京服河若注英苦始念武例雨固夜免承依波居呼妹味松季枝宗招店幸妻抱虎姓典彼奉忠宙泣昔卒是要活面看前政度重相便建革美南界海思品指科保信省持神食首故草送音洋城客屋律施急星待春限室香退祖威洗昨秋厚追皆勇恨皇怒俗祝拾泉柔哀怨逆能家起高原展通特造流根料校席病笑除速害消破容修留致旅益素恩酒降案借射烈夏骨庭弱徒浪耕悟泰浮胸栽勉眠浴得都部著理第情常接基深望商球推族船密救停章野唱菜堂移混探盛欲雪惜授患宿崇祭就道等然量最期集喜落富答朝敢短善童散植登敬景遇街湖雄寒尊番勤悲晴暑新意想路解感福暗禁暖愁慈算精端察歌舞暴露里';
CONTENT="";
RESULT="";
if len(sys.argv) == 1:
    CONTENT=sys.stdin.readline().rstrip("\n");
    RESULT = bytes([TABLE.index(i) for i in CONTENT]);
    RESULT=RESULT.decode();
    sys.stdout.write(RESULT);
elif len(sys.argv) == 2:
    with open(sys.argv[1],"r") as f:
        CONTENT=f.read();
    RESULT = bytes([TABLE.index(i) for i in CONTENT]);
    with open(sys.argv[1]+".decoded","wb") as f:
        f.write(RESULT)
else:
    with open(sys.argv[1],"r") as f:
        CONTENT=f.read().hex();
    RESULT += TABLE[int(CONTENT[i:i+2],16)];
    with open(sys.argv[2],"wb") as f:
        f.write(RESULT)
