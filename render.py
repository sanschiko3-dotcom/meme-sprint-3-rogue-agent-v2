from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
S = 2
im = Image.new('RGB', (2048, 2048), '#f7eedb')
d = ImageDraw.Draw(im)
ink = '#203842'
def poly(p, fill, width=6):
    p = [(x*S,y*S) for x,y in p]
    d.polygon(p, fill)
    d.line(p+[p[0]], fill=ink, width=width*S, joint='curve')
def rect(b,fill,r=0,w=6):
    d.rounded_rectangle(tuple(v*S for v in b),r*S,fill,ink,w*S)
def line(p,fill=ink,w=6):
    d.line([(x*S,y*S) for x,y in p],fill,width=w*S,joint='curve')
def oval(b,fill,w=5):
    d.ellipse(tuple(v*S for v in b),fill,ink,w*S)
def text(t,x,y,size):
    d.text((x*S,y*S),t,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',size*S),fill=ink,anchor='mt')
text('I QUIT.',512,30,180)
# Open doorway and a pool of warm daylight.
rect((679,262,955,810),'#edba66',5,9)
poly([(695,280),(939,280),(939,793),(695,793)],'#ffe4a0',0)
poly([(695,708),(939,793),(950,858),(328,858)],'#f0d49b',0)
line([(55,811),(678,811)],'#cdbfa4',4)
poly([(953,264),(819,336),(819,782),(953,810)],'#c78653')
oval((837,558,851,577),'#f7eedb',3)
# Shadow, long stride: the agent is already leaving.
d.ellipse((385*S,781*S,789*S,839*S),fill='#d3bd95')
poly([(527,650),(590,663),(556,746),(472,794),(438,769),(505,708)],'#557a80')
rect((423,765,493,804),'#203842',15,4)
poly([(615,649),(671,639),(687,733),(755,777),(728,808),(636,758)],'#83aaa8')
poly([(714,777),(744,765),(790,797),(780,816),(719,816)],'#203842')
# Back shell and side panel.
rect((483,460,676,675),'#6d999a',42,7)
poly([(623,474),(678,495),(697,626),(662,670),(623,650)],'#42656e')
rect((514,509,602,608),'#a7c9bf',15,5)
line([(535,536),(580,536)],'#557a80',5)
line([(535,552),(580,552)],'#557a80',5)
rect((543,429,610,478),'#a7c9bf',10)
# Head: rear three-quarter, with one luminous eye on the right side.
rect((467,302,656,450),'#9ebfba',34,7)
poly([(621,314),(683,346),(683,423),(638,447),(621,418)],'#34535e')
oval((640,356,671,393),'#baffdf',3)
line([(552,302),(552,280)],w=7)
oval((541,259,563,281),'#e6aa53',4)
rect((494,346,527,406),'#6d999a',9,4)
# Carrying arm behind the box.
line([(648,497),(700,548),(727,585)],ink,36)
line([(648,497),(700,548),(727,585)],'#a7c9bf',24)
# Desk belongings: keyboard, plant, mug.
poly([(692,518),(715,449),(741,458),(721,533)],'#e6e8d8',4)
for y in range(469,515,12):
    line([(711,y),(727,y+4)],'#557a80',3)
line([(787,520),(786,453)],'#426b56',6)
oval((751,442,786,465),'#64916a',3)
oval((786,428,819,454),'#7c9e63',3)
poly([(763,481),(811,481),(803,526),(772,526)],'#bd6e4d',4)
oval((837,487,867,517),'#f7eedb',4)
rect((812,479,847,528),'#f7eedb',7,4)
# Cardboard box, held in front of the walking agent.
poly([(664,531),(836,531),(870,555),(699,565)],'#e5b77c',5)
poly([(699,565),(870,555),(856,661),(694,674)],'#cc925c',6)
poly([(664,531),(699,565),(694,674),(662,632)],'#b87b4c',6)
line([(768,562),(765,590)],'#f4d2a0',14)
# Visible bent arm connects the shoulder to the hand gripping the box.
line([(627,511),(610,574),(675,595)],ink,40)
line([(627,511),(610,574),(675,595)],'#a7c9bf',27)
oval((663,579,710,610),'#a7c9bf',5)
# Single resignation note, separate from the scene for easy reading.
rect((65,877,959,991),'#fffaf0',9,4)
oval((501,886,519,904),'#c56f4c',2)
text('REASON: “MAKE IT BETTER”',512,915,37)
text('IS NOT A PROMPT.',512,955,32)
Path(__file__).parent.joinpath('assets').mkdir(exist_ok=True)
im.resize((1024,1024),Image.Resampling.LANCZOS).save(Path(__file__).parent/'assets/entry.png',optimize=True)
