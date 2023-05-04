from typing import Union, Any
from atri_react.Flex import Flex
from atri_react.Image import Image
from atri_react.Anchor import Anchor
from manifests.FramerText import FramerText
from atri_react.TextBox import TextBox
from manifests.FramerFlex import FramerFlex
from atri_react.Input import Input
from atri_react.Div import Div


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.Flex1 = state["Flex1"] if "Flex1" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.Flex3 = state["Flex3"] if "Flex3" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.FramerText2 = state["FramerText2"] if "FramerText2" in state else None
		self.FramerText3 = state["FramerText3"] if "FramerText3" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.FramerText4 = state["FramerText4"] if "FramerText4" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.FramerText5 = state["FramerText5"] if "FramerText5" in state else None
		self.Anchor5 = state["Anchor5"] if "Anchor5" in state else None
		self.FramerText6 = state["FramerText6"] if "FramerText6" in state else None
		self.Anchor6 = state["Anchor6"] if "Anchor6" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.TextBox1 = state["TextBox1"] if "TextBox1" in state else None
		self.Anchor7 = state["Anchor7"] if "Anchor7" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.Flex7 = state["Flex7"] if "Flex7" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.FramerFlex2 = state["FramerFlex2"] if "FramerFlex2" in state else None
		self.FramerFlex3 = state["FramerFlex3"] if "FramerFlex3" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.FramerFlex4 = state["FramerFlex4"] if "FramerFlex4" in state else None
		self.TextBox6 = state["TextBox6"] if "TextBox6" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.FramerFlex5 = state["FramerFlex5"] if "FramerFlex5" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.FramerFlex6 = state["FramerFlex6"] if "FramerFlex6" in state else None
		self.TextBox7 = state["TextBox7"] if "TextBox7" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.FramerFlex9 = state["FramerFlex9"] if "FramerFlex9" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.Image9 = state["Image9"] if "Image9" in state else None
		self.Image10 = state["Image10"] if "Image10" in state else None
		self.Image11 = state["Image11"] if "Image11" in state else None
		self.Image12 = state["Image12"] if "Image12" in state else None
		self.Image13 = state["Image13"] if "Image13" in state else None
		self.Image14 = state["Image14"] if "Image14" in state else None
		self.Image15 = state["Image15"] if "Image15" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.FramerFlex10 = state["FramerFlex10"] if "FramerFlex10" in state else None
		self.FramerFlex11 = state["FramerFlex11"] if "FramerFlex11" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.TextBox12 = state["TextBox12"] if "TextBox12" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.FramerFlex12 = state["FramerFlex12"] if "FramerFlex12" in state else None
		self.FramerFlex13 = state["FramerFlex13"] if "FramerFlex13" in state else None
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.FramerFlex14 = state["FramerFlex14"] if "FramerFlex14" in state else None
		self.FramerFlex15 = state["FramerFlex15"] if "FramerFlex15" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.FramerFlex16 = state["FramerFlex16"] if "FramerFlex16" in state else None
		self.FramerFlex17 = state["FramerFlex17"] if "FramerFlex17" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.FramerFlex18 = state["FramerFlex18"] if "FramerFlex18" in state else None
		self.Image17 = state["Image17"] if "Image17" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.FramerFlex19 = state["FramerFlex19"] if "FramerFlex19" in state else None
		self.Image18 = state["Image18"] if "Image18" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.Image19 = state["Image19"] if "Image19" in state else None
		self.FramerFlex20 = state["FramerFlex20"] if "FramerFlex20" in state else None
		self.Image20 = state["Image20"] if "Image20" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.FramerFlex21 = state["FramerFlex21"] if "FramerFlex21" in state else None
		self.Image21 = state["Image21"] if "Image21" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.FramerFlex22 = state["FramerFlex22"] if "FramerFlex22" in state else None
		self.Flex23 = state["Flex23"] if "Flex23" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.Image22 = state["Image22"] if "Image22" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.Image23 = state["Image23"] if "Image23" in state else None
		self.Image24 = state["Image24"] if "Image24" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.TextBox26 = state["TextBox26"] if "TextBox26" in state else None
		self.Image25 = state["Image25"] if "Image25" in state else None
		self.TextBox27 = state["TextBox27"] if "TextBox27" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.FramerFlex23 = state["FramerFlex23"] if "FramerFlex23" in state else None
		self.FramerFlex24 = state["FramerFlex24"] if "FramerFlex24" in state else None
		self.FramerFlex25 = state["FramerFlex25"] if "FramerFlex25" in state else None
		self.FramerFlex26 = state["FramerFlex26"] if "FramerFlex26" in state else None
		self.TextBox29 = state["TextBox29"] if "TextBox29" in state else None
		self.FramerFlex27 = state["FramerFlex27"] if "FramerFlex27" in state else None
		self.FramerFlex28 = state["FramerFlex28"] if "FramerFlex28" in state else None
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
		self.Flex25 = state["Flex25"] if "Flex25" in state else None
		self.FramerFlex29 = state["FramerFlex29"] if "FramerFlex29" in state else None
		self.Flex26 = state["Flex26"] if "Flex26" in state else None
		self.Image26 = state["Image26"] if "Image26" in state else None
		self.Flex27 = state["Flex27"] if "Flex27" in state else None
		self.Flex28 = state["Flex28"] if "Flex28" in state else None
		self.Flex29 = state["Flex29"] if "Flex29" in state else None
		self.Flex30 = state["Flex30"] if "Flex30" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.FramerFlex30 = state["FramerFlex30"] if "FramerFlex30" in state else None
		self.FramerFlex31 = state["FramerFlex31"] if "FramerFlex31" in state else None
		self.FramerFlex32 = state["FramerFlex32"] if "FramerFlex32" in state else None
		self.FramerFlex33 = state["FramerFlex33"] if "FramerFlex33" in state else None
		self.FramerFlex34 = state["FramerFlex34"] if "FramerFlex34" in state else None
		self.FramerFlex35 = state["FramerFlex35"] if "FramerFlex35" in state else None
		self.FramerFlex36 = state["FramerFlex36"] if "FramerFlex36" in state else None
		self.FramerFlex37 = state["FramerFlex37"] if "FramerFlex37" in state else None
		self.FramerFlex38 = state["FramerFlex38"] if "FramerFlex38" in state else None
		self.Image27 = state["Image27"] if "Image27" in state else None
		self.Flex34 = state["Flex34"] if "Flex34" in state else None
		self.Flex35 = state["Flex35"] if "Flex35" in state else None
		self.FramerFlex39 = state["FramerFlex39"] if "FramerFlex39" in state else None
		self.FramerFlex40 = state["FramerFlex40"] if "FramerFlex40" in state else None
		self.TextBox30 = state["TextBox30"] if "TextBox30" in state else None
		self.TextBox31 = state["TextBox31"] if "TextBox31" in state else None
		self.Flex36 = state["Flex36"] if "Flex36" in state else None
		self.Flex37 = state["Flex37"] if "Flex37" in state else None
		self.Flex38 = state["Flex38"] if "Flex38" in state else None
		self.Flex39 = state["Flex39"] if "Flex39" in state else None
		self.FramerFlex41 = state["FramerFlex41"] if "FramerFlex41" in state else None
		self.FramerFlex42 = state["FramerFlex42"] if "FramerFlex42" in state else None
		self.TextBox32 = state["TextBox32"] if "TextBox32" in state else None
		self.TextBox33 = state["TextBox33"] if "TextBox33" in state else None
		self.FramerFlex43 = state["FramerFlex43"] if "FramerFlex43" in state else None
		self.Image28 = state["Image28"] if "Image28" in state else None
		self.TextBox34 = state["TextBox34"] if "TextBox34" in state else None
		self.TextBox35 = state["TextBox35"] if "TextBox35" in state else None
		self.Image29 = state["Image29"] if "Image29" in state else None
		self.FramerFlex44 = state["FramerFlex44"] if "FramerFlex44" in state else None
		self.TextBox36 = state["TextBox36"] if "TextBox36" in state else None
		self.Image30 = state["Image30"] if "Image30" in state else None
		self.FramerFlex45 = state["FramerFlex45"] if "FramerFlex45" in state else None
		self.Image31 = state["Image31"] if "Image31" in state else None
		self.Image32 = state["Image32"] if "Image32" in state else None
		self.Image33 = state["Image33"] if "Image33" in state else None
		self.Flex40 = state["Flex40"] if "Flex40" in state else None
		self.Flex41 = state["Flex41"] if "Flex41" in state else None
		self.Flex42 = state["Flex42"] if "Flex42" in state else None
		self.Flex43 = state["Flex43"] if "Flex43" in state else None
		self.TextBox37 = state["TextBox37"] if "TextBox37" in state else None
		self.Flex44 = state["Flex44"] if "Flex44" in state else None
		self.Flex45 = state["Flex45"] if "Flex45" in state else None
		self.Flex46 = state["Flex46"] if "Flex46" in state else None
		self.TextBox40 = state["TextBox40"] if "TextBox40" in state else None
		self.TextBox41 = state["TextBox41"] if "TextBox41" in state else None
		self.FramerFlex48 = state["FramerFlex48"] if "FramerFlex48" in state else None
		self.FramerFlex49 = state["FramerFlex49"] if "FramerFlex49" in state else None
		self.Flex47 = state["Flex47"] if "Flex47" in state else None
		self.Flex48 = state["Flex48"] if "Flex48" in state else None
		self.Flex49 = state["Flex49"] if "Flex49" in state else None
		self.Flex50 = state["Flex50"] if "Flex50" in state else None
		self.TextBox42 = state["TextBox42"] if "TextBox42" in state else None
		self.Image34 = state["Image34"] if "Image34" in state else None
		self.FramerFlex50 = state["FramerFlex50"] if "FramerFlex50" in state else None
		self.Image35 = state["Image35"] if "Image35" in state else None
		self.TextBox43 = state["TextBox43"] if "TextBox43" in state else None
		self.FramerFlex51 = state["FramerFlex51"] if "FramerFlex51" in state else None
		self.Image36 = state["Image36"] if "Image36" in state else None
		self.TextBox44 = state["TextBox44"] if "TextBox44" in state else None
		self.FramerFlex52 = state["FramerFlex52"] if "FramerFlex52" in state else None
		self.Image37 = state["Image37"] if "Image37" in state else None
		self.TextBox45 = state["TextBox45"] if "TextBox45" in state else None
		self.FramerFlex53 = state["FramerFlex53"] if "FramerFlex53" in state else None
		self.Image38 = state["Image38"] if "Image38" in state else None
		self.TextBox46 = state["TextBox46"] if "TextBox46" in state else None
		self.FramerFlex54 = state["FramerFlex54"] if "FramerFlex54" in state else None
		self.Image39 = state["Image39"] if "Image39" in state else None
		self.TextBox47 = state["TextBox47"] if "TextBox47" in state else None
		self.FramerFlex55 = state["FramerFlex55"] if "FramerFlex55" in state else None
		self.Image40 = state["Image40"] if "Image40" in state else None
		self.TextBox48 = state["TextBox48"] if "TextBox48" in state else None
		self.FramerFlex56 = state["FramerFlex56"] if "FramerFlex56" in state else None
		self.Image41 = state["Image41"] if "Image41" in state else None
		self.TextBox49 = state["TextBox49"] if "TextBox49" in state else None
		self.FramerFlex57 = state["FramerFlex57"] if "FramerFlex57" in state else None
		self.Flex51 = state["Flex51"] if "Flex51" in state else None
		self.Flex52 = state["Flex52"] if "Flex52" in state else None
		self.Flex53 = state["Flex53"] if "Flex53" in state else None
		self.TextBox50 = state["TextBox50"] if "TextBox50" in state else None
		self.FramerFlex58 = state["FramerFlex58"] if "FramerFlex58" in state else None
		self.TextBox51 = state["TextBox51"] if "TextBox51" in state else None
		self.FramerFlex59 = state["FramerFlex59"] if "FramerFlex59" in state else None
		self.Flex54 = state["Flex54"] if "Flex54" in state else None
		self.FramerFlex63 = state["FramerFlex63"] if "FramerFlex63" in state else None
		self.Flex56 = state["Flex56"] if "Flex56" in state else None
		self.TextBox54 = state["TextBox54"] if "TextBox54" in state else None
		self.TextBox56 = state["TextBox56"] if "TextBox56" in state else None
		self.FramerFlex65 = state["FramerFlex65"] if "FramerFlex65" in state else None
		self.TextBox57 = state["TextBox57"] if "TextBox57" in state else None
		self.Flex57 = state["Flex57"] if "Flex57" in state else None
		self.FramerFlex66 = state["FramerFlex66"] if "FramerFlex66" in state else None
		self.TextBox59 = state["TextBox59"] if "TextBox59" in state else None
		self.Flex59 = state["Flex59"] if "Flex59" in state else None
		self.FramerFlex68 = state["FramerFlex68"] if "FramerFlex68" in state else None
		self.TextBox60 = state["TextBox60"] if "TextBox60" in state else None
		self.Flex60 = state["Flex60"] if "Flex60" in state else None
		self.FramerFlex69 = state["FramerFlex69"] if "FramerFlex69" in state else None
		self.Image43 = state["Image43"] if "Image43" in state else None
		self.Flex61 = state["Flex61"] if "Flex61" in state else None
		self.Flex62 = state["Flex62"] if "Flex62" in state else None
		self.Flex63 = state["Flex63"] if "Flex63" in state else None
		self.Flex64 = state["Flex64"] if "Flex64" in state else None
		self.Flex65 = state["Flex65"] if "Flex65" in state else None
		self.Flex66 = state["Flex66"] if "Flex66" in state else None
		self.Flex67 = state["Flex67"] if "Flex67" in state else None
		self.Flex101 = state["Flex101"] if "Flex101" in state else None
		self.Flex102 = state["Flex102"] if "Flex102" in state else None
		self.Flex103 = state["Flex103"] if "Flex103" in state else None
		self.Flex104 = state["Flex104"] if "Flex104" in state else None
		self.TextBox88 = state["TextBox88"] if "TextBox88" in state else None
		self.TextBox89 = state["TextBox89"] if "TextBox89" in state else None
		self.FramerFlex96 = state["FramerFlex96"] if "FramerFlex96" in state else None
		self.FramerFlex97 = state["FramerFlex97"] if "FramerFlex97" in state else None
		self.Flex105 = state["Flex105"] if "Flex105" in state else None
		self.TextBox90 = state["TextBox90"] if "TextBox90" in state else None
		self.TextBox91 = state["TextBox91"] if "TextBox91" in state else None
		self.FramerFlex98 = state["FramerFlex98"] if "FramerFlex98" in state else None
		self.FramerFlex99 = state["FramerFlex99"] if "FramerFlex99" in state else None
		self.Flex106 = state["Flex106"] if "Flex106" in state else None
		self.TextBox92 = state["TextBox92"] if "TextBox92" in state else None
		self.TextBox93 = state["TextBox93"] if "TextBox93" in state else None
		self.FramerFlex100 = state["FramerFlex100"] if "FramerFlex100" in state else None
		self.FramerFlex101 = state["FramerFlex101"] if "FramerFlex101" in state else None
		self.Flex107 = state["Flex107"] if "Flex107" in state else None
		self.TextBox94 = state["TextBox94"] if "TextBox94" in state else None
		self.Flex108 = state["Flex108"] if "Flex108" in state else None
		self.TextBox95 = state["TextBox95"] if "TextBox95" in state else None
		self.Input5 = state["Input5"] if "Input5" in state else None
		self.FramerFlex102 = state["FramerFlex102"] if "FramerFlex102" in state else None
		self.FramerFlex103 = state["FramerFlex103"] if "FramerFlex103" in state else None
		self.Flex109 = state["Flex109"] if "Flex109" in state else None
		self.Flex110 = state["Flex110"] if "Flex110" in state else None
		self.Flex111 = state["Flex111"] if "Flex111" in state else None
		self.TextBox102 = state["TextBox102"] if "TextBox102" in state else None
		self.Flex119 = state["Flex119"] if "Flex119" in state else None
		self.FramerFlex110 = state["FramerFlex110"] if "FramerFlex110" in state else None
		self.Input6 = state["Input6"] if "Input6" in state else None
		self.TextBox103 = state["TextBox103"] if "TextBox103" in state else None
		self.Flex120 = state["Flex120"] if "Flex120" in state else None
		self.FramerFlex111 = state["FramerFlex111"] if "FramerFlex111" in state else None
		self.Flex121 = state["Flex121"] if "Flex121" in state else None
		self.Flex122 = state["Flex122"] if "Flex122" in state else None
		self.TextBox104 = state["TextBox104"] if "TextBox104" in state else None
		self.TextBox105 = state["TextBox105"] if "TextBox105" in state else None
		self.FramerFlex112 = state["FramerFlex112"] if "FramerFlex112" in state else None
		self.FramerFlex113 = state["FramerFlex113"] if "FramerFlex113" in state else None
		self.Flex123 = state["Flex123"] if "Flex123" in state else None
		self.TextBox108 = state["TextBox108"] if "TextBox108" in state else None
		self.TextBox109 = state["TextBox109"] if "TextBox109" in state else None
		self.FramerFlex116 = state["FramerFlex116"] if "FramerFlex116" in state else None
		self.FramerFlex117 = state["FramerFlex117"] if "FramerFlex117" in state else None
		self.Flex125 = state["Flex125"] if "Flex125" in state else None
		self.Flex126 = state["Flex126"] if "Flex126" in state else None
		self.TextBox110 = state["TextBox110"] if "TextBox110" in state else None
		self.TextBox111 = state["TextBox111"] if "TextBox111" in state else None
		self.FramerFlex118 = state["FramerFlex118"] if "FramerFlex118" in state else None
		self.FramerFlex119 = state["FramerFlex119"] if "FramerFlex119" in state else None
		self.Flex127 = state["Flex127"] if "Flex127" in state else None
		self.Flex128 = state["Flex128"] if "Flex128" in state else None
		self.Flex130 = state["Flex130"] if "Flex130" in state else None
		self.Flex131 = state["Flex131"] if "Flex131" in state else None
		self.Flex132 = state["Flex132"] if "Flex132" in state else None
		self.Flex133 = state["Flex133"] if "Flex133" in state else None
		self.Flex134 = state["Flex134"] if "Flex134" in state else None
		self.TextBox114 = state["TextBox114"] if "TextBox114" in state else None
		self.FramerFlex122 = state["FramerFlex122"] if "FramerFlex122" in state else None
		self.TextBox115 = state["TextBox115"] if "TextBox115" in state else None
		self.FramerFlex123 = state["FramerFlex123"] if "FramerFlex123" in state else None
		self.TextBox116 = state["TextBox116"] if "TextBox116" in state else None
		self.Image44 = state["Image44"] if "Image44" in state else None
		self.FramerFlex124 = state["FramerFlex124"] if "FramerFlex124" in state else None
		self.Flex135 = state["Flex135"] if "Flex135" in state else None
		self.Flex136 = state["Flex136"] if "Flex136" in state else None
		self.Flex137 = state["Flex137"] if "Flex137" in state else None
		self.Flex138 = state["Flex138"] if "Flex138" in state else None
		self.Div2 = state["Div2"] if "Div2" in state else None
		self.Flex139 = state["Flex139"] if "Flex139" in state else None
		self.Image45 = state["Image45"] if "Image45" in state else None
		self.TextBox117 = state["TextBox117"] if "TextBox117" in state else None
		self.Flex140 = state["Flex140"] if "Flex140" in state else None
		self.Flex141 = state["Flex141"] if "Flex141" in state else None
		self.FramerFlex125 = state["FramerFlex125"] if "FramerFlex125" in state else None
		self.TextBox118 = state["TextBox118"] if "TextBox118" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.FramerFlex126 = state["FramerFlex126"] if "FramerFlex126" in state else None
		self.TextBox120 = state["TextBox120"] if "TextBox120" in state else None
		self.FramerFlex127 = state["FramerFlex127"] if "FramerFlex127" in state else None
		self.FramerFlex128 = state["FramerFlex128"] if "FramerFlex128" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.TextBox122 = state["TextBox122"] if "TextBox122" in state else None
		self.FramerFlex129 = state["FramerFlex129"] if "FramerFlex129" in state else None
		self.FramerFlex130 = state["FramerFlex130"] if "FramerFlex130" in state else None
		self.Anchor10 = state["Anchor10"] if "Anchor10" in state else None
		self.TextBox124 = state["TextBox124"] if "TextBox124" in state else None
		self.TextBox125 = state["TextBox125"] if "TextBox125" in state else None
		self.TextBox126 = state["TextBox126"] if "TextBox126" in state else None
		self.FramerText7 = state["FramerText7"] if "FramerText7" in state else None
		self.Anchor11 = state["Anchor11"] if "Anchor11" in state else None
		self.FramerText8 = state["FramerText8"] if "FramerText8" in state else None
		self.Anchor12 = state["Anchor12"] if "Anchor12" in state else None
		self.FramerText9 = state["FramerText9"] if "FramerText9" in state else None
		self.Anchor13 = state["Anchor13"] if "Anchor13" in state else None
		self.FramerText10 = state["FramerText10"] if "FramerText10" in state else None
		self.Anchor14 = state["Anchor14"] if "Anchor14" in state else None
		self.TextBox127 = state["TextBox127"] if "TextBox127" in state else None
		self.TextBox128 = state["TextBox128"] if "TextBox128" in state else None
		self.TextBox129 = state["TextBox129"] if "TextBox129" in state else None
		self.FramerFlex131 = state["FramerFlex131"] if "FramerFlex131" in state else None
		self.TextBox130 = state["TextBox130"] if "TextBox130" in state else None
		self.FramerFlex132 = state["FramerFlex132"] if "FramerFlex132" in state else None
		self.TextBox131 = state["TextBox131"] if "TextBox131" in state else None
		self.FramerFlex133 = state["FramerFlex133"] if "FramerFlex133" in state else None
		self.TextBox132 = state["TextBox132"] if "TextBox132" in state else None
		self.Anchor15 = state["Anchor15"] if "Anchor15" in state else None
		self.FramerFlex134 = state["FramerFlex134"] if "FramerFlex134" in state else None
		self.Anchor16 = state["Anchor16"] if "Anchor16" in state else None
		self.FramerFlex135 = state["FramerFlex135"] if "FramerFlex135" in state else None
		self.Anchor17 = state["Anchor17"] if "Anchor17" in state else None
		self.FramerFlex136 = state["FramerFlex136"] if "FramerFlex136" in state else None
		self.Flex142 = state["Flex142"] if "Flex142" in state else None
		self.Flex143 = state["Flex143"] if "Flex143" in state else None
		self.Flex144 = state["Flex144"] if "Flex144" in state else None
		self.Flex146 = state["Flex146"] if "Flex146" in state else None
		self.TextBox134 = state["TextBox134"] if "TextBox134" in state else None
		self.Anchor18 = state["Anchor18"] if "Anchor18" in state else None
		self.TextBox135 = state["TextBox135"] if "TextBox135" in state else None
		self.Image46 = state["Image46"] if "Image46" in state else None
		self.TextBox136 = state["TextBox136"] if "TextBox136" in state else None
		self.Anchor19 = state["Anchor19"] if "Anchor19" in state else None
		self.Anchor20 = state["Anchor20"] if "Anchor20" in state else None
		self.Anchor21 = state["Anchor21"] if "Anchor21" in state else None
		self.Anchor25 = state["Anchor25"] if "Anchor25" in state else None
		self.FramerFlex138 = state["FramerFlex138"] if "FramerFlex138" in state else None
		self.Image47 = state["Image47"] if "Image47" in state else None
		self.Image48 = state["Image48"] if "Image48" in state else None
		self.Image49 = state["Image49"] if "Image49" in state else None
		self.Image50 = state["Image50"] if "Image50" in state else None
		self.Image51 = state["Image51"] if "Image51" in state else None
		self.Image52 = state["Image52"] if "Image52" in state else None
		self.Image53 = state["Image53"] if "Image53" in state else None
		self.Image54 = state["Image54"] if "Image54" in state else None
		self.Image55 = state["Image55"] if "Image55" in state else None
		self.Image56 = state["Image56"] if "Image56" in state else None
		self.Flex148 = state["Flex148"] if "Flex148" in state else None
		self.Flex149 = state["Flex149"] if "Flex149" in state else None
		self.Image59 = state["Image59"] if "Image59" in state else None
		self.Flex150 = state["Flex150"] if "Flex150" in state else None
		self.Flex151 = state["Flex151"] if "Flex151" in state else None
		self.Flex153 = state["Flex153"] if "Flex153" in state else None
		self.Image60 = state["Image60"] if "Image60" in state else None
		self.FramerFlex140 = state["FramerFlex140"] if "FramerFlex140" in state else None
		self.TextBox137 = state["TextBox137"] if "TextBox137" in state else None
		self.Flex154 = state["Flex154"] if "Flex154" in state else None
		self.Flex155 = state["Flex155"] if "Flex155" in state else None
		self.TextBox139 = state["TextBox139"] if "TextBox139" in state else None
		self.TextBox140 = state["TextBox140"] if "TextBox140" in state else None
		self.Flex156 = state["Flex156"] if "Flex156" in state else None
		self.Flex157 = state["Flex157"] if "Flex157" in state else None
		self.Flex158 = state["Flex158"] if "Flex158" in state else None
		self.FramerFlex141 = state["FramerFlex141"] if "FramerFlex141" in state else None
		self.TextBox141 = state["TextBox141"] if "TextBox141" in state else None
		self.TextBox142 = state["TextBox142"] if "TextBox142" in state else None
		self.TextBox143 = state["TextBox143"] if "TextBox143" in state else None
		self.Flex159 = state["Flex159"] if "Flex159" in state else None
		self.TextBox144 = state["TextBox144"] if "TextBox144" in state else None
		self.TextBox145 = state["TextBox145"] if "TextBox145" in state else None
		self.Image62 = state["Image62"] if "Image62" in state else None
		self.FramerFlex142 = state["FramerFlex142"] if "FramerFlex142" in state else None
		self.Flex160 = state["Flex160"] if "Flex160" in state else None
		self.FramerFlex143 = state["FramerFlex143"] if "FramerFlex143" in state else None
		self.Flex161 = state["Flex161"] if "Flex161" in state else None
		self.Flex162 = state["Flex162"] if "Flex162" in state else None
		self.Flex163 = state["Flex163"] if "Flex163" in state else None
		self.Flex164 = state["Flex164"] if "Flex164" in state else None
		self.Flex165 = state["Flex165"] if "Flex165" in state else None
		self.Image63 = state["Image63"] if "Image63" in state else None
		self.Image64 = state["Image64"] if "Image64" in state else None
		self.Image65 = state["Image65"] if "Image65" in state else None
		self.Flex166 = state["Flex166"] if "Flex166" in state else None
		self.Flex167 = state["Flex167"] if "Flex167" in state else None
		self.TextBox146 = state["TextBox146"] if "TextBox146" in state else None
		self.TextBox147 = state["TextBox147"] if "TextBox147" in state else None
		self.Flex168 = state["Flex168"] if "Flex168" in state else None
		self.Flex169 = state["Flex169"] if "Flex169" in state else None
		self.TextBox148 = state["TextBox148"] if "TextBox148" in state else None
		self.TextBox149 = state["TextBox149"] if "TextBox149" in state else None
		self.Flex170 = state["Flex170"] if "Flex170" in state else None
		self.TextBox150 = state["TextBox150"] if "TextBox150" in state else None
		self.TextBox151 = state["TextBox151"] if "TextBox151" in state else None
		self.Image66 = state["Image66"] if "Image66" in state else None
		self.Image67 = state["Image67"] if "Image67" in state else None
		self.TextBox152 = state["TextBox152"] if "TextBox152" in state else None
		self.TextBox153 = state["TextBox153"] if "TextBox153" in state else None
		self.Image68 = state["Image68"] if "Image68" in state else None
		self.Flex171 = state["Flex171"] if "Flex171" in state else None
		self.Flex172 = state["Flex172"] if "Flex172" in state else None
		self.Flex173 = state["Flex173"] if "Flex173" in state else None
		self.Flex174 = state["Flex174"] if "Flex174" in state else None
		self.Flex175 = state["Flex175"] if "Flex175" in state else None
		self.Flex176 = state["Flex176"] if "Flex176" in state else None
		self.Flex177 = state["Flex177"] if "Flex177" in state else None
		self.Image69 = state["Image69"] if "Image69" in state else None
		self.Image70 = state["Image70"] if "Image70" in state else None
		self.FramerFlex144 = state["FramerFlex144"] if "FramerFlex144" in state else None
		self.FramerFlex145 = state["FramerFlex145"] if "FramerFlex145" in state else None
		self.FramerFlex146 = state["FramerFlex146"] if "FramerFlex146" in state else None
		self.FramerFlex147 = state["FramerFlex147"] if "FramerFlex147" in state else None
		self.FramerFlex148 = state["FramerFlex148"] if "FramerFlex148" in state else None
		self.FramerFlex149 = state["FramerFlex149"] if "FramerFlex149" in state else None
		self.FramerFlex150 = state["FramerFlex150"] if "FramerFlex150" in state else None
		self.FramerFlex151 = state["FramerFlex151"] if "FramerFlex151" in state else None
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}
  
	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		if hasattr(self, self.event_alias):
			comp = getattr(self, self.event_alias)
			setattr(comp, callback_name, True)
		self.event_repeating = event["repeating"]
  
	
	@property
	def Flex1(self):
		self._getter_access_tracker["Flex1"] = {}
		return self._Flex1
	@Flex1.setter
	def Flex1(self, new_state):
		self._setter_access_tracker["Flex1"] = {}
		self._Flex1 = Flex(new_state)

	@property
	def Flex2(self):
		self._getter_access_tracker["Flex2"] = {}
		return self._Flex2
	@Flex2.setter
	def Flex2(self, new_state):
		self._setter_access_tracker["Flex2"] = {}
		self._Flex2 = Flex(new_state)

	@property
	def Flex3(self):
		self._getter_access_tracker["Flex3"] = {}
		return self._Flex3
	@Flex3.setter
	def Flex3(self, new_state):
		self._setter_access_tracker["Flex3"] = {}
		self._Flex3 = Flex(new_state)

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

	@property
	def Anchor2(self):
		self._getter_access_tracker["Anchor2"] = {}
		return self._Anchor2
	@Anchor2.setter
	def Anchor2(self, new_state):
		self._setter_access_tracker["Anchor2"] = {}
		self._Anchor2 = Anchor(new_state)

	@property
	def FramerText2(self):
		self._getter_access_tracker["FramerText2"] = {}
		return self._FramerText2
	@FramerText2.setter
	def FramerText2(self, new_state):
		self._setter_access_tracker["FramerText2"] = {}
		self._FramerText2 = FramerText(new_state)

	@property
	def FramerText3(self):
		self._getter_access_tracker["FramerText3"] = {}
		return self._FramerText3
	@FramerText3.setter
	def FramerText3(self, new_state):
		self._setter_access_tracker["FramerText3"] = {}
		self._FramerText3 = FramerText(new_state)

	@property
	def Anchor3(self):
		self._getter_access_tracker["Anchor3"] = {}
		return self._Anchor3
	@Anchor3.setter
	def Anchor3(self, new_state):
		self._setter_access_tracker["Anchor3"] = {}
		self._Anchor3 = Anchor(new_state)

	@property
	def FramerText4(self):
		self._getter_access_tracker["FramerText4"] = {}
		return self._FramerText4
	@FramerText4.setter
	def FramerText4(self, new_state):
		self._setter_access_tracker["FramerText4"] = {}
		self._FramerText4 = FramerText(new_state)

	@property
	def Anchor4(self):
		self._getter_access_tracker["Anchor4"] = {}
		return self._Anchor4
	@Anchor4.setter
	def Anchor4(self, new_state):
		self._setter_access_tracker["Anchor4"] = {}
		self._Anchor4 = Anchor(new_state)

	@property
	def FramerText5(self):
		self._getter_access_tracker["FramerText5"] = {}
		return self._FramerText5
	@FramerText5.setter
	def FramerText5(self, new_state):
		self._setter_access_tracker["FramerText5"] = {}
		self._FramerText5 = FramerText(new_state)

	@property
	def Anchor5(self):
		self._getter_access_tracker["Anchor5"] = {}
		return self._Anchor5
	@Anchor5.setter
	def Anchor5(self, new_state):
		self._setter_access_tracker["Anchor5"] = {}
		self._Anchor5 = Anchor(new_state)

	@property
	def FramerText6(self):
		self._getter_access_tracker["FramerText6"] = {}
		return self._FramerText6
	@FramerText6.setter
	def FramerText6(self, new_state):
		self._setter_access_tracker["FramerText6"] = {}
		self._FramerText6 = FramerText(new_state)

	@property
	def Anchor6(self):
		self._getter_access_tracker["Anchor6"] = {}
		return self._Anchor6
	@Anchor6.setter
	def Anchor6(self, new_state):
		self._setter_access_tracker["Anchor6"] = {}
		self._Anchor6 = Anchor(new_state)

	@property
	def Flex4(self):
		self._getter_access_tracker["Flex4"] = {}
		return self._Flex4
	@Flex4.setter
	def Flex4(self, new_state):
		self._setter_access_tracker["Flex4"] = {}
		self._Flex4 = Flex(new_state)

	@property
	def Flex5(self):
		self._getter_access_tracker["Flex5"] = {}
		return self._Flex5
	@Flex5.setter
	def Flex5(self, new_state):
		self._setter_access_tracker["Flex5"] = {}
		self._Flex5 = Flex(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def TextBox1(self):
		self._getter_access_tracker["TextBox1"] = {}
		return self._TextBox1
	@TextBox1.setter
	def TextBox1(self, new_state):
		self._setter_access_tracker["TextBox1"] = {}
		self._TextBox1 = TextBox(new_state)

	@property
	def Anchor7(self):
		self._getter_access_tracker["Anchor7"] = {}
		return self._Anchor7
	@Anchor7.setter
	def Anchor7(self, new_state):
		self._setter_access_tracker["Anchor7"] = {}
		self._Anchor7 = Anchor(new_state)

	@property
	def Flex6(self):
		self._getter_access_tracker["Flex6"] = {}
		return self._Flex6
	@Flex6.setter
	def Flex6(self, new_state):
		self._setter_access_tracker["Flex6"] = {}
		self._Flex6 = Flex(new_state)

	@property
	def Flex7(self):
		self._getter_access_tracker["Flex7"] = {}
		return self._Flex7
	@Flex7.setter
	def Flex7(self, new_state):
		self._setter_access_tracker["Flex7"] = {}
		self._Flex7 = Flex(new_state)

	@property
	def TextBox2(self):
		self._getter_access_tracker["TextBox2"] = {}
		return self._TextBox2
	@TextBox2.setter
	def TextBox2(self, new_state):
		self._setter_access_tracker["TextBox2"] = {}
		self._TextBox2 = TextBox(new_state)

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def FramerFlex2(self):
		self._getter_access_tracker["FramerFlex2"] = {}
		return self._FramerFlex2
	@FramerFlex2.setter
	def FramerFlex2(self, new_state):
		self._setter_access_tracker["FramerFlex2"] = {}
		self._FramerFlex2 = FramerFlex(new_state)

	@property
	def FramerFlex3(self):
		self._getter_access_tracker["FramerFlex3"] = {}
		return self._FramerFlex3
	@FramerFlex3.setter
	def FramerFlex3(self, new_state):
		self._setter_access_tracker["FramerFlex3"] = {}
		self._FramerFlex3 = FramerFlex(new_state)

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		self._TextBox5 = TextBox(new_state)

	@property
	def FramerFlex4(self):
		self._getter_access_tracker["FramerFlex4"] = {}
		return self._FramerFlex4
	@FramerFlex4.setter
	def FramerFlex4(self, new_state):
		self._setter_access_tracker["FramerFlex4"] = {}
		self._FramerFlex4 = FramerFlex(new_state)

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		self._TextBox6 = TextBox(new_state)

	@property
	def Flex8(self):
		self._getter_access_tracker["Flex8"] = {}
		return self._Flex8
	@Flex8.setter
	def Flex8(self, new_state):
		self._setter_access_tracker["Flex8"] = {}
		self._Flex8 = Flex(new_state)

	@property
	def Flex9(self):
		self._getter_access_tracker["Flex9"] = {}
		return self._Flex9
	@Flex9.setter
	def Flex9(self, new_state):
		self._setter_access_tracker["Flex9"] = {}
		self._Flex9 = Flex(new_state)

	@property
	def FramerFlex5(self):
		self._getter_access_tracker["FramerFlex5"] = {}
		return self._FramerFlex5
	@FramerFlex5.setter
	def FramerFlex5(self, new_state):
		self._setter_access_tracker["FramerFlex5"] = {}
		self._FramerFlex5 = FramerFlex(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def FramerFlex6(self):
		self._getter_access_tracker["FramerFlex6"] = {}
		return self._FramerFlex6
	@FramerFlex6.setter
	def FramerFlex6(self, new_state):
		self._setter_access_tracker["FramerFlex6"] = {}
		self._FramerFlex6 = FramerFlex(new_state)

	@property
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		self._TextBox7 = TextBox(new_state)

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		self._TextBox8 = TextBox(new_state)

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def Flex10(self):
		self._getter_access_tracker["Flex10"] = {}
		return self._Flex10
	@Flex10.setter
	def Flex10(self, new_state):
		self._setter_access_tracker["Flex10"] = {}
		self._Flex10 = Flex(new_state)

	@property
	def FramerFlex9(self):
		self._getter_access_tracker["FramerFlex9"] = {}
		return self._FramerFlex9
	@FramerFlex9.setter
	def FramerFlex9(self, new_state):
		self._setter_access_tracker["FramerFlex9"] = {}
		self._FramerFlex9 = FramerFlex(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		self._Image9 = Image(new_state)

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		self._Image10 = Image(new_state)

	@property
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		self._Image11 = Image(new_state)

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		self._Image12 = Image(new_state)

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		self._Image13 = Image(new_state)

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		self._Image14 = Image(new_state)

	@property
	def Image15(self):
		self._getter_access_tracker["Image15"] = {}
		return self._Image15
	@Image15.setter
	def Image15(self, new_state):
		self._setter_access_tracker["Image15"] = {}
		self._Image15 = Image(new_state)

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		self._TextBox10 = TextBox(new_state)

	@property
	def Flex11(self):
		self._getter_access_tracker["Flex11"] = {}
		return self._Flex11
	@Flex11.setter
	def Flex11(self, new_state):
		self._setter_access_tracker["Flex11"] = {}
		self._Flex11 = Flex(new_state)

	@property
	def Flex12(self):
		self._getter_access_tracker["Flex12"] = {}
		return self._Flex12
	@Flex12.setter
	def Flex12(self, new_state):
		self._setter_access_tracker["Flex12"] = {}
		self._Flex12 = Flex(new_state)

	@property
	def Flex13(self):
		self._getter_access_tracker["Flex13"] = {}
		return self._Flex13
	@Flex13.setter
	def Flex13(self, new_state):
		self._setter_access_tracker["Flex13"] = {}
		self._Flex13 = Flex(new_state)

	@property
	def FramerFlex10(self):
		self._getter_access_tracker["FramerFlex10"] = {}
		return self._FramerFlex10
	@FramerFlex10.setter
	def FramerFlex10(self, new_state):
		self._setter_access_tracker["FramerFlex10"] = {}
		self._FramerFlex10 = FramerFlex(new_state)

	@property
	def FramerFlex11(self):
		self._getter_access_tracker["FramerFlex11"] = {}
		return self._FramerFlex11
	@FramerFlex11.setter
	def FramerFlex11(self, new_state):
		self._setter_access_tracker["FramerFlex11"] = {}
		self._FramerFlex11 = FramerFlex(new_state)

	@property
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		self._TextBox11 = TextBox(new_state)

	@property
	def TextBox12(self):
		self._getter_access_tracker["TextBox12"] = {}
		return self._TextBox12
	@TextBox12.setter
	def TextBox12(self, new_state):
		self._setter_access_tracker["TextBox12"] = {}
		self._TextBox12 = TextBox(new_state)

	@property
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

	@property
	def TextBox15(self):
		self._getter_access_tracker["TextBox15"] = {}
		return self._TextBox15
	@TextBox15.setter
	def TextBox15(self, new_state):
		self._setter_access_tracker["TextBox15"] = {}
		self._TextBox15 = TextBox(new_state)

	@property
	def FramerFlex12(self):
		self._getter_access_tracker["FramerFlex12"] = {}
		return self._FramerFlex12
	@FramerFlex12.setter
	def FramerFlex12(self, new_state):
		self._setter_access_tracker["FramerFlex12"] = {}
		self._FramerFlex12 = FramerFlex(new_state)

	@property
	def FramerFlex13(self):
		self._getter_access_tracker["FramerFlex13"] = {}
		return self._FramerFlex13
	@FramerFlex13.setter
	def FramerFlex13(self, new_state):
		self._setter_access_tracker["FramerFlex13"] = {}
		self._FramerFlex13 = FramerFlex(new_state)

	@property
	def Flex14(self):
		self._getter_access_tracker["Flex14"] = {}
		return self._Flex14
	@Flex14.setter
	def Flex14(self, new_state):
		self._setter_access_tracker["Flex14"] = {}
		self._Flex14 = Flex(new_state)

	@property
	def Flex15(self):
		self._getter_access_tracker["Flex15"] = {}
		return self._Flex15
	@Flex15.setter
	def Flex15(self, new_state):
		self._setter_access_tracker["Flex15"] = {}
		self._Flex15 = Flex(new_state)

	@property
	def Flex16(self):
		self._getter_access_tracker["Flex16"] = {}
		return self._Flex16
	@Flex16.setter
	def Flex16(self, new_state):
		self._setter_access_tracker["Flex16"] = {}
		self._Flex16 = Flex(new_state)

	@property
	def FramerFlex14(self):
		self._getter_access_tracker["FramerFlex14"] = {}
		return self._FramerFlex14
	@FramerFlex14.setter
	def FramerFlex14(self, new_state):
		self._setter_access_tracker["FramerFlex14"] = {}
		self._FramerFlex14 = FramerFlex(new_state)

	@property
	def FramerFlex15(self):
		self._getter_access_tracker["FramerFlex15"] = {}
		return self._FramerFlex15
	@FramerFlex15.setter
	def FramerFlex15(self, new_state):
		self._setter_access_tracker["FramerFlex15"] = {}
		self._FramerFlex15 = FramerFlex(new_state)

	@property
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		self._Flex17 = Flex(new_state)

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		self._Flex18 = Flex(new_state)

	@property
	def TextBox16(self):
		self._getter_access_tracker["TextBox16"] = {}
		return self._TextBox16
	@TextBox16.setter
	def TextBox16(self, new_state):
		self._setter_access_tracker["TextBox16"] = {}
		self._TextBox16 = TextBox(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def FramerFlex16(self):
		self._getter_access_tracker["FramerFlex16"] = {}
		return self._FramerFlex16
	@FramerFlex16.setter
	def FramerFlex16(self, new_state):
		self._setter_access_tracker["FramerFlex16"] = {}
		self._FramerFlex16 = FramerFlex(new_state)

	@property
	def FramerFlex17(self):
		self._getter_access_tracker["FramerFlex17"] = {}
		return self._FramerFlex17
	@FramerFlex17.setter
	def FramerFlex17(self, new_state):
		self._setter_access_tracker["FramerFlex17"] = {}
		self._FramerFlex17 = FramerFlex(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

	@property
	def FramerFlex18(self):
		self._getter_access_tracker["FramerFlex18"] = {}
		return self._FramerFlex18
	@FramerFlex18.setter
	def FramerFlex18(self, new_state):
		self._setter_access_tracker["FramerFlex18"] = {}
		self._FramerFlex18 = FramerFlex(new_state)

	@property
	def Image17(self):
		self._getter_access_tracker["Image17"] = {}
		return self._Image17
	@Image17.setter
	def Image17(self, new_state):
		self._setter_access_tracker["Image17"] = {}
		self._Image17 = Image(new_state)

	@property
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		self._Flex20 = Flex(new_state)

	@property
	def Flex21(self):
		self._getter_access_tracker["Flex21"] = {}
		return self._Flex21
	@Flex21.setter
	def Flex21(self, new_state):
		self._setter_access_tracker["Flex21"] = {}
		self._Flex21 = Flex(new_state)

	@property
	def Flex22(self):
		self._getter_access_tracker["Flex22"] = {}
		return self._Flex22
	@Flex22.setter
	def Flex22(self, new_state):
		self._setter_access_tracker["Flex22"] = {}
		self._Flex22 = Flex(new_state)

	@property
	def FramerFlex19(self):
		self._getter_access_tracker["FramerFlex19"] = {}
		return self._FramerFlex19
	@FramerFlex19.setter
	def FramerFlex19(self, new_state):
		self._setter_access_tracker["FramerFlex19"] = {}
		self._FramerFlex19 = FramerFlex(new_state)

	@property
	def Image18(self):
		self._getter_access_tracker["Image18"] = {}
		return self._Image18
	@Image18.setter
	def Image18(self, new_state):
		self._setter_access_tracker["Image18"] = {}
		self._Image18 = Image(new_state)

	@property
	def TextBox19(self):
		self._getter_access_tracker["TextBox19"] = {}
		return self._TextBox19
	@TextBox19.setter
	def TextBox19(self, new_state):
		self._setter_access_tracker["TextBox19"] = {}
		self._TextBox19 = TextBox(new_state)

	@property
	def TextBox20(self):
		self._getter_access_tracker["TextBox20"] = {}
		return self._TextBox20
	@TextBox20.setter
	def TextBox20(self, new_state):
		self._setter_access_tracker["TextBox20"] = {}
		self._TextBox20 = TextBox(new_state)

	@property
	def Image19(self):
		self._getter_access_tracker["Image19"] = {}
		return self._Image19
	@Image19.setter
	def Image19(self, new_state):
		self._setter_access_tracker["Image19"] = {}
		self._Image19 = Image(new_state)

	@property
	def FramerFlex20(self):
		self._getter_access_tracker["FramerFlex20"] = {}
		return self._FramerFlex20
	@FramerFlex20.setter
	def FramerFlex20(self, new_state):
		self._setter_access_tracker["FramerFlex20"] = {}
		self._FramerFlex20 = FramerFlex(new_state)

	@property
	def Image20(self):
		self._getter_access_tracker["Image20"] = {}
		return self._Image20
	@Image20.setter
	def Image20(self, new_state):
		self._setter_access_tracker["Image20"] = {}
		self._Image20 = Image(new_state)

	@property
	def TextBox21(self):
		self._getter_access_tracker["TextBox21"] = {}
		return self._TextBox21
	@TextBox21.setter
	def TextBox21(self, new_state):
		self._setter_access_tracker["TextBox21"] = {}
		self._TextBox21 = TextBox(new_state)

	@property
	def FramerFlex21(self):
		self._getter_access_tracker["FramerFlex21"] = {}
		return self._FramerFlex21
	@FramerFlex21.setter
	def FramerFlex21(self, new_state):
		self._setter_access_tracker["FramerFlex21"] = {}
		self._FramerFlex21 = FramerFlex(new_state)

	@property
	def Image21(self):
		self._getter_access_tracker["Image21"] = {}
		return self._Image21
	@Image21.setter
	def Image21(self, new_state):
		self._setter_access_tracker["Image21"] = {}
		self._Image21 = Image(new_state)

	@property
	def TextBox22(self):
		self._getter_access_tracker["TextBox22"] = {}
		return self._TextBox22
	@TextBox22.setter
	def TextBox22(self, new_state):
		self._setter_access_tracker["TextBox22"] = {}
		self._TextBox22 = TextBox(new_state)

	@property
	def FramerFlex22(self):
		self._getter_access_tracker["FramerFlex22"] = {}
		return self._FramerFlex22
	@FramerFlex22.setter
	def FramerFlex22(self, new_state):
		self._setter_access_tracker["FramerFlex22"] = {}
		self._FramerFlex22 = FramerFlex(new_state)

	@property
	def Flex23(self):
		self._getter_access_tracker["Flex23"] = {}
		return self._Flex23
	@Flex23.setter
	def Flex23(self, new_state):
		self._setter_access_tracker["Flex23"] = {}
		self._Flex23 = Flex(new_state)

	@property
	def TextBox23(self):
		self._getter_access_tracker["TextBox23"] = {}
		return self._TextBox23
	@TextBox23.setter
	def TextBox23(self, new_state):
		self._setter_access_tracker["TextBox23"] = {}
		self._TextBox23 = TextBox(new_state)

	@property
	def Image22(self):
		self._getter_access_tracker["Image22"] = {}
		return self._Image22
	@Image22.setter
	def Image22(self, new_state):
		self._setter_access_tracker["Image22"] = {}
		self._Image22 = Image(new_state)

	@property
	def TextBox24(self):
		self._getter_access_tracker["TextBox24"] = {}
		return self._TextBox24
	@TextBox24.setter
	def TextBox24(self, new_state):
		self._setter_access_tracker["TextBox24"] = {}
		self._TextBox24 = TextBox(new_state)

	@property
	def Image23(self):
		self._getter_access_tracker["Image23"] = {}
		return self._Image23
	@Image23.setter
	def Image23(self, new_state):
		self._setter_access_tracker["Image23"] = {}
		self._Image23 = Image(new_state)

	@property
	def Image24(self):
		self._getter_access_tracker["Image24"] = {}
		return self._Image24
	@Image24.setter
	def Image24(self, new_state):
		self._setter_access_tracker["Image24"] = {}
		self._Image24 = Image(new_state)

	@property
	def TextBox25(self):
		self._getter_access_tracker["TextBox25"] = {}
		return self._TextBox25
	@TextBox25.setter
	def TextBox25(self, new_state):
		self._setter_access_tracker["TextBox25"] = {}
		self._TextBox25 = TextBox(new_state)

	@property
	def TextBox26(self):
		self._getter_access_tracker["TextBox26"] = {}
		return self._TextBox26
	@TextBox26.setter
	def TextBox26(self, new_state):
		self._setter_access_tracker["TextBox26"] = {}
		self._TextBox26 = TextBox(new_state)

	@property
	def Image25(self):
		self._getter_access_tracker["Image25"] = {}
		return self._Image25
	@Image25.setter
	def Image25(self, new_state):
		self._setter_access_tracker["Image25"] = {}
		self._Image25 = Image(new_state)

	@property
	def TextBox27(self):
		self._getter_access_tracker["TextBox27"] = {}
		return self._TextBox27
	@TextBox27.setter
	def TextBox27(self, new_state):
		self._setter_access_tracker["TextBox27"] = {}
		self._TextBox27 = TextBox(new_state)

	@property
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		self._TextBox28 = TextBox(new_state)

	@property
	def FramerFlex23(self):
		self._getter_access_tracker["FramerFlex23"] = {}
		return self._FramerFlex23
	@FramerFlex23.setter
	def FramerFlex23(self, new_state):
		self._setter_access_tracker["FramerFlex23"] = {}
		self._FramerFlex23 = FramerFlex(new_state)

	@property
	def FramerFlex24(self):
		self._getter_access_tracker["FramerFlex24"] = {}
		return self._FramerFlex24
	@FramerFlex24.setter
	def FramerFlex24(self, new_state):
		self._setter_access_tracker["FramerFlex24"] = {}
		self._FramerFlex24 = FramerFlex(new_state)

	@property
	def FramerFlex25(self):
		self._getter_access_tracker["FramerFlex25"] = {}
		return self._FramerFlex25
	@FramerFlex25.setter
	def FramerFlex25(self, new_state):
		self._setter_access_tracker["FramerFlex25"] = {}
		self._FramerFlex25 = FramerFlex(new_state)

	@property
	def FramerFlex26(self):
		self._getter_access_tracker["FramerFlex26"] = {}
		return self._FramerFlex26
	@FramerFlex26.setter
	def FramerFlex26(self, new_state):
		self._setter_access_tracker["FramerFlex26"] = {}
		self._FramerFlex26 = FramerFlex(new_state)

	@property
	def TextBox29(self):
		self._getter_access_tracker["TextBox29"] = {}
		return self._TextBox29
	@TextBox29.setter
	def TextBox29(self, new_state):
		self._setter_access_tracker["TextBox29"] = {}
		self._TextBox29 = TextBox(new_state)

	@property
	def FramerFlex27(self):
		self._getter_access_tracker["FramerFlex27"] = {}
		return self._FramerFlex27
	@FramerFlex27.setter
	def FramerFlex27(self, new_state):
		self._setter_access_tracker["FramerFlex27"] = {}
		self._FramerFlex27 = FramerFlex(new_state)

	@property
	def FramerFlex28(self):
		self._getter_access_tracker["FramerFlex28"] = {}
		return self._FramerFlex28
	@FramerFlex28.setter
	def FramerFlex28(self, new_state):
		self._setter_access_tracker["FramerFlex28"] = {}
		self._FramerFlex28 = FramerFlex(new_state)

	@property
	def Flex24(self):
		self._getter_access_tracker["Flex24"] = {}
		return self._Flex24
	@Flex24.setter
	def Flex24(self, new_state):
		self._setter_access_tracker["Flex24"] = {}
		self._Flex24 = Flex(new_state)

	@property
	def Flex25(self):
		self._getter_access_tracker["Flex25"] = {}
		return self._Flex25
	@Flex25.setter
	def Flex25(self, new_state):
		self._setter_access_tracker["Flex25"] = {}
		self._Flex25 = Flex(new_state)

	@property
	def FramerFlex29(self):
		self._getter_access_tracker["FramerFlex29"] = {}
		return self._FramerFlex29
	@FramerFlex29.setter
	def FramerFlex29(self, new_state):
		self._setter_access_tracker["FramerFlex29"] = {}
		self._FramerFlex29 = FramerFlex(new_state)

	@property
	def Flex26(self):
		self._getter_access_tracker["Flex26"] = {}
		return self._Flex26
	@Flex26.setter
	def Flex26(self, new_state):
		self._setter_access_tracker["Flex26"] = {}
		self._Flex26 = Flex(new_state)

	@property
	def Image26(self):
		self._getter_access_tracker["Image26"] = {}
		return self._Image26
	@Image26.setter
	def Image26(self, new_state):
		self._setter_access_tracker["Image26"] = {}
		self._Image26 = Image(new_state)

	@property
	def Flex27(self):
		self._getter_access_tracker["Flex27"] = {}
		return self._Flex27
	@Flex27.setter
	def Flex27(self, new_state):
		self._setter_access_tracker["Flex27"] = {}
		self._Flex27 = Flex(new_state)

	@property
	def Flex28(self):
		self._getter_access_tracker["Flex28"] = {}
		return self._Flex28
	@Flex28.setter
	def Flex28(self, new_state):
		self._setter_access_tracker["Flex28"] = {}
		self._Flex28 = Flex(new_state)

	@property
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		self._Flex29 = Flex(new_state)

	@property
	def Flex30(self):
		self._getter_access_tracker["Flex30"] = {}
		return self._Flex30
	@Flex30.setter
	def Flex30(self, new_state):
		self._setter_access_tracker["Flex30"] = {}
		self._Flex30 = Flex(new_state)

	@property
	def Flex31(self):
		self._getter_access_tracker["Flex31"] = {}
		return self._Flex31
	@Flex31.setter
	def Flex31(self, new_state):
		self._setter_access_tracker["Flex31"] = {}
		self._Flex31 = Flex(new_state)

	@property
	def Flex32(self):
		self._getter_access_tracker["Flex32"] = {}
		return self._Flex32
	@Flex32.setter
	def Flex32(self, new_state):
		self._setter_access_tracker["Flex32"] = {}
		self._Flex32 = Flex(new_state)

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		self._Flex33 = Flex(new_state)

	@property
	def FramerFlex30(self):
		self._getter_access_tracker["FramerFlex30"] = {}
		return self._FramerFlex30
	@FramerFlex30.setter
	def FramerFlex30(self, new_state):
		self._setter_access_tracker["FramerFlex30"] = {}
		self._FramerFlex30 = FramerFlex(new_state)

	@property
	def FramerFlex31(self):
		self._getter_access_tracker["FramerFlex31"] = {}
		return self._FramerFlex31
	@FramerFlex31.setter
	def FramerFlex31(self, new_state):
		self._setter_access_tracker["FramerFlex31"] = {}
		self._FramerFlex31 = FramerFlex(new_state)

	@property
	def FramerFlex32(self):
		self._getter_access_tracker["FramerFlex32"] = {}
		return self._FramerFlex32
	@FramerFlex32.setter
	def FramerFlex32(self, new_state):
		self._setter_access_tracker["FramerFlex32"] = {}
		self._FramerFlex32 = FramerFlex(new_state)

	@property
	def FramerFlex33(self):
		self._getter_access_tracker["FramerFlex33"] = {}
		return self._FramerFlex33
	@FramerFlex33.setter
	def FramerFlex33(self, new_state):
		self._setter_access_tracker["FramerFlex33"] = {}
		self._FramerFlex33 = FramerFlex(new_state)

	@property
	def FramerFlex34(self):
		self._getter_access_tracker["FramerFlex34"] = {}
		return self._FramerFlex34
	@FramerFlex34.setter
	def FramerFlex34(self, new_state):
		self._setter_access_tracker["FramerFlex34"] = {}
		self._FramerFlex34 = FramerFlex(new_state)

	@property
	def FramerFlex35(self):
		self._getter_access_tracker["FramerFlex35"] = {}
		return self._FramerFlex35
	@FramerFlex35.setter
	def FramerFlex35(self, new_state):
		self._setter_access_tracker["FramerFlex35"] = {}
		self._FramerFlex35 = FramerFlex(new_state)

	@property
	def FramerFlex36(self):
		self._getter_access_tracker["FramerFlex36"] = {}
		return self._FramerFlex36
	@FramerFlex36.setter
	def FramerFlex36(self, new_state):
		self._setter_access_tracker["FramerFlex36"] = {}
		self._FramerFlex36 = FramerFlex(new_state)

	@property
	def FramerFlex37(self):
		self._getter_access_tracker["FramerFlex37"] = {}
		return self._FramerFlex37
	@FramerFlex37.setter
	def FramerFlex37(self, new_state):
		self._setter_access_tracker["FramerFlex37"] = {}
		self._FramerFlex37 = FramerFlex(new_state)

	@property
	def FramerFlex38(self):
		self._getter_access_tracker["FramerFlex38"] = {}
		return self._FramerFlex38
	@FramerFlex38.setter
	def FramerFlex38(self, new_state):
		self._setter_access_tracker["FramerFlex38"] = {}
		self._FramerFlex38 = FramerFlex(new_state)

	@property
	def Image27(self):
		self._getter_access_tracker["Image27"] = {}
		return self._Image27
	@Image27.setter
	def Image27(self, new_state):
		self._setter_access_tracker["Image27"] = {}
		self._Image27 = Image(new_state)

	@property
	def Flex34(self):
		self._getter_access_tracker["Flex34"] = {}
		return self._Flex34
	@Flex34.setter
	def Flex34(self, new_state):
		self._setter_access_tracker["Flex34"] = {}
		self._Flex34 = Flex(new_state)

	@property
	def Flex35(self):
		self._getter_access_tracker["Flex35"] = {}
		return self._Flex35
	@Flex35.setter
	def Flex35(self, new_state):
		self._setter_access_tracker["Flex35"] = {}
		self._Flex35 = Flex(new_state)

	@property
	def FramerFlex39(self):
		self._getter_access_tracker["FramerFlex39"] = {}
		return self._FramerFlex39
	@FramerFlex39.setter
	def FramerFlex39(self, new_state):
		self._setter_access_tracker["FramerFlex39"] = {}
		self._FramerFlex39 = FramerFlex(new_state)

	@property
	def FramerFlex40(self):
		self._getter_access_tracker["FramerFlex40"] = {}
		return self._FramerFlex40
	@FramerFlex40.setter
	def FramerFlex40(self, new_state):
		self._setter_access_tracker["FramerFlex40"] = {}
		self._FramerFlex40 = FramerFlex(new_state)

	@property
	def TextBox30(self):
		self._getter_access_tracker["TextBox30"] = {}
		return self._TextBox30
	@TextBox30.setter
	def TextBox30(self, new_state):
		self._setter_access_tracker["TextBox30"] = {}
		self._TextBox30 = TextBox(new_state)

	@property
	def TextBox31(self):
		self._getter_access_tracker["TextBox31"] = {}
		return self._TextBox31
	@TextBox31.setter
	def TextBox31(self, new_state):
		self._setter_access_tracker["TextBox31"] = {}
		self._TextBox31 = TextBox(new_state)

	@property
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		self._Flex36 = Flex(new_state)

	@property
	def Flex37(self):
		self._getter_access_tracker["Flex37"] = {}
		return self._Flex37
	@Flex37.setter
	def Flex37(self, new_state):
		self._setter_access_tracker["Flex37"] = {}
		self._Flex37 = Flex(new_state)

	@property
	def Flex38(self):
		self._getter_access_tracker["Flex38"] = {}
		return self._Flex38
	@Flex38.setter
	def Flex38(self, new_state):
		self._setter_access_tracker["Flex38"] = {}
		self._Flex38 = Flex(new_state)

	@property
	def Flex39(self):
		self._getter_access_tracker["Flex39"] = {}
		return self._Flex39
	@Flex39.setter
	def Flex39(self, new_state):
		self._setter_access_tracker["Flex39"] = {}
		self._Flex39 = Flex(new_state)

	@property
	def FramerFlex41(self):
		self._getter_access_tracker["FramerFlex41"] = {}
		return self._FramerFlex41
	@FramerFlex41.setter
	def FramerFlex41(self, new_state):
		self._setter_access_tracker["FramerFlex41"] = {}
		self._FramerFlex41 = FramerFlex(new_state)

	@property
	def FramerFlex42(self):
		self._getter_access_tracker["FramerFlex42"] = {}
		return self._FramerFlex42
	@FramerFlex42.setter
	def FramerFlex42(self, new_state):
		self._setter_access_tracker["FramerFlex42"] = {}
		self._FramerFlex42 = FramerFlex(new_state)

	@property
	def TextBox32(self):
		self._getter_access_tracker["TextBox32"] = {}
		return self._TextBox32
	@TextBox32.setter
	def TextBox32(self, new_state):
		self._setter_access_tracker["TextBox32"] = {}
		self._TextBox32 = TextBox(new_state)

	@property
	def TextBox33(self):
		self._getter_access_tracker["TextBox33"] = {}
		return self._TextBox33
	@TextBox33.setter
	def TextBox33(self, new_state):
		self._setter_access_tracker["TextBox33"] = {}
		self._TextBox33 = TextBox(new_state)

	@property
	def FramerFlex43(self):
		self._getter_access_tracker["FramerFlex43"] = {}
		return self._FramerFlex43
	@FramerFlex43.setter
	def FramerFlex43(self, new_state):
		self._setter_access_tracker["FramerFlex43"] = {}
		self._FramerFlex43 = FramerFlex(new_state)

	@property
	def Image28(self):
		self._getter_access_tracker["Image28"] = {}
		return self._Image28
	@Image28.setter
	def Image28(self, new_state):
		self._setter_access_tracker["Image28"] = {}
		self._Image28 = Image(new_state)

	@property
	def TextBox34(self):
		self._getter_access_tracker["TextBox34"] = {}
		return self._TextBox34
	@TextBox34.setter
	def TextBox34(self, new_state):
		self._setter_access_tracker["TextBox34"] = {}
		self._TextBox34 = TextBox(new_state)

	@property
	def TextBox35(self):
		self._getter_access_tracker["TextBox35"] = {}
		return self._TextBox35
	@TextBox35.setter
	def TextBox35(self, new_state):
		self._setter_access_tracker["TextBox35"] = {}
		self._TextBox35 = TextBox(new_state)

	@property
	def Image29(self):
		self._getter_access_tracker["Image29"] = {}
		return self._Image29
	@Image29.setter
	def Image29(self, new_state):
		self._setter_access_tracker["Image29"] = {}
		self._Image29 = Image(new_state)

	@property
	def FramerFlex44(self):
		self._getter_access_tracker["FramerFlex44"] = {}
		return self._FramerFlex44
	@FramerFlex44.setter
	def FramerFlex44(self, new_state):
		self._setter_access_tracker["FramerFlex44"] = {}
		self._FramerFlex44 = FramerFlex(new_state)

	@property
	def TextBox36(self):
		self._getter_access_tracker["TextBox36"] = {}
		return self._TextBox36
	@TextBox36.setter
	def TextBox36(self, new_state):
		self._setter_access_tracker["TextBox36"] = {}
		self._TextBox36 = TextBox(new_state)

	@property
	def Image30(self):
		self._getter_access_tracker["Image30"] = {}
		return self._Image30
	@Image30.setter
	def Image30(self, new_state):
		self._setter_access_tracker["Image30"] = {}
		self._Image30 = Image(new_state)

	@property
	def FramerFlex45(self):
		self._getter_access_tracker["FramerFlex45"] = {}
		return self._FramerFlex45
	@FramerFlex45.setter
	def FramerFlex45(self, new_state):
		self._setter_access_tracker["FramerFlex45"] = {}
		self._FramerFlex45 = FramerFlex(new_state)

	@property
	def Image31(self):
		self._getter_access_tracker["Image31"] = {}
		return self._Image31
	@Image31.setter
	def Image31(self, new_state):
		self._setter_access_tracker["Image31"] = {}
		self._Image31 = Image(new_state)

	@property
	def Image32(self):
		self._getter_access_tracker["Image32"] = {}
		return self._Image32
	@Image32.setter
	def Image32(self, new_state):
		self._setter_access_tracker["Image32"] = {}
		self._Image32 = Image(new_state)

	@property
	def Image33(self):
		self._getter_access_tracker["Image33"] = {}
		return self._Image33
	@Image33.setter
	def Image33(self, new_state):
		self._setter_access_tracker["Image33"] = {}
		self._Image33 = Image(new_state)

	@property
	def Flex40(self):
		self._getter_access_tracker["Flex40"] = {}
		return self._Flex40
	@Flex40.setter
	def Flex40(self, new_state):
		self._setter_access_tracker["Flex40"] = {}
		self._Flex40 = Flex(new_state)

	@property
	def Flex41(self):
		self._getter_access_tracker["Flex41"] = {}
		return self._Flex41
	@Flex41.setter
	def Flex41(self, new_state):
		self._setter_access_tracker["Flex41"] = {}
		self._Flex41 = Flex(new_state)

	@property
	def Flex42(self):
		self._getter_access_tracker["Flex42"] = {}
		return self._Flex42
	@Flex42.setter
	def Flex42(self, new_state):
		self._setter_access_tracker["Flex42"] = {}
		self._Flex42 = Flex(new_state)

	@property
	def Flex43(self):
		self._getter_access_tracker["Flex43"] = {}
		return self._Flex43
	@Flex43.setter
	def Flex43(self, new_state):
		self._setter_access_tracker["Flex43"] = {}
		self._Flex43 = Flex(new_state)

	@property
	def TextBox37(self):
		self._getter_access_tracker["TextBox37"] = {}
		return self._TextBox37
	@TextBox37.setter
	def TextBox37(self, new_state):
		self._setter_access_tracker["TextBox37"] = {}
		self._TextBox37 = TextBox(new_state)

	@property
	def Flex44(self):
		self._getter_access_tracker["Flex44"] = {}
		return self._Flex44
	@Flex44.setter
	def Flex44(self, new_state):
		self._setter_access_tracker["Flex44"] = {}
		self._Flex44 = Flex(new_state)

	@property
	def Flex45(self):
		self._getter_access_tracker["Flex45"] = {}
		return self._Flex45
	@Flex45.setter
	def Flex45(self, new_state):
		self._setter_access_tracker["Flex45"] = {}
		self._Flex45 = Flex(new_state)

	@property
	def Flex46(self):
		self._getter_access_tracker["Flex46"] = {}
		return self._Flex46
	@Flex46.setter
	def Flex46(self, new_state):
		self._setter_access_tracker["Flex46"] = {}
		self._Flex46 = Flex(new_state)

	@property
	def TextBox40(self):
		self._getter_access_tracker["TextBox40"] = {}
		return self._TextBox40
	@TextBox40.setter
	def TextBox40(self, new_state):
		self._setter_access_tracker["TextBox40"] = {}
		self._TextBox40 = TextBox(new_state)

	@property
	def TextBox41(self):
		self._getter_access_tracker["TextBox41"] = {}
		return self._TextBox41
	@TextBox41.setter
	def TextBox41(self, new_state):
		self._setter_access_tracker["TextBox41"] = {}
		self._TextBox41 = TextBox(new_state)

	@property
	def FramerFlex48(self):
		self._getter_access_tracker["FramerFlex48"] = {}
		return self._FramerFlex48
	@FramerFlex48.setter
	def FramerFlex48(self, new_state):
		self._setter_access_tracker["FramerFlex48"] = {}
		self._FramerFlex48 = FramerFlex(new_state)

	@property
	def FramerFlex49(self):
		self._getter_access_tracker["FramerFlex49"] = {}
		return self._FramerFlex49
	@FramerFlex49.setter
	def FramerFlex49(self, new_state):
		self._setter_access_tracker["FramerFlex49"] = {}
		self._FramerFlex49 = FramerFlex(new_state)

	@property
	def Flex47(self):
		self._getter_access_tracker["Flex47"] = {}
		return self._Flex47
	@Flex47.setter
	def Flex47(self, new_state):
		self._setter_access_tracker["Flex47"] = {}
		self._Flex47 = Flex(new_state)

	@property
	def Flex48(self):
		self._getter_access_tracker["Flex48"] = {}
		return self._Flex48
	@Flex48.setter
	def Flex48(self, new_state):
		self._setter_access_tracker["Flex48"] = {}
		self._Flex48 = Flex(new_state)

	@property
	def Flex49(self):
		self._getter_access_tracker["Flex49"] = {}
		return self._Flex49
	@Flex49.setter
	def Flex49(self, new_state):
		self._setter_access_tracker["Flex49"] = {}
		self._Flex49 = Flex(new_state)

	@property
	def Flex50(self):
		self._getter_access_tracker["Flex50"] = {}
		return self._Flex50
	@Flex50.setter
	def Flex50(self, new_state):
		self._setter_access_tracker["Flex50"] = {}
		self._Flex50 = Flex(new_state)

	@property
	def TextBox42(self):
		self._getter_access_tracker["TextBox42"] = {}
		return self._TextBox42
	@TextBox42.setter
	def TextBox42(self, new_state):
		self._setter_access_tracker["TextBox42"] = {}
		self._TextBox42 = TextBox(new_state)

	@property
	def Image34(self):
		self._getter_access_tracker["Image34"] = {}
		return self._Image34
	@Image34.setter
	def Image34(self, new_state):
		self._setter_access_tracker["Image34"] = {}
		self._Image34 = Image(new_state)

	@property
	def FramerFlex50(self):
		self._getter_access_tracker["FramerFlex50"] = {}
		return self._FramerFlex50
	@FramerFlex50.setter
	def FramerFlex50(self, new_state):
		self._setter_access_tracker["FramerFlex50"] = {}
		self._FramerFlex50 = FramerFlex(new_state)

	@property
	def Image35(self):
		self._getter_access_tracker["Image35"] = {}
		return self._Image35
	@Image35.setter
	def Image35(self, new_state):
		self._setter_access_tracker["Image35"] = {}
		self._Image35 = Image(new_state)

	@property
	def TextBox43(self):
		self._getter_access_tracker["TextBox43"] = {}
		return self._TextBox43
	@TextBox43.setter
	def TextBox43(self, new_state):
		self._setter_access_tracker["TextBox43"] = {}
		self._TextBox43 = TextBox(new_state)

	@property
	def FramerFlex51(self):
		self._getter_access_tracker["FramerFlex51"] = {}
		return self._FramerFlex51
	@FramerFlex51.setter
	def FramerFlex51(self, new_state):
		self._setter_access_tracker["FramerFlex51"] = {}
		self._FramerFlex51 = FramerFlex(new_state)

	@property
	def Image36(self):
		self._getter_access_tracker["Image36"] = {}
		return self._Image36
	@Image36.setter
	def Image36(self, new_state):
		self._setter_access_tracker["Image36"] = {}
		self._Image36 = Image(new_state)

	@property
	def TextBox44(self):
		self._getter_access_tracker["TextBox44"] = {}
		return self._TextBox44
	@TextBox44.setter
	def TextBox44(self, new_state):
		self._setter_access_tracker["TextBox44"] = {}
		self._TextBox44 = TextBox(new_state)

	@property
	def FramerFlex52(self):
		self._getter_access_tracker["FramerFlex52"] = {}
		return self._FramerFlex52
	@FramerFlex52.setter
	def FramerFlex52(self, new_state):
		self._setter_access_tracker["FramerFlex52"] = {}
		self._FramerFlex52 = FramerFlex(new_state)

	@property
	def Image37(self):
		self._getter_access_tracker["Image37"] = {}
		return self._Image37
	@Image37.setter
	def Image37(self, new_state):
		self._setter_access_tracker["Image37"] = {}
		self._Image37 = Image(new_state)

	@property
	def TextBox45(self):
		self._getter_access_tracker["TextBox45"] = {}
		return self._TextBox45
	@TextBox45.setter
	def TextBox45(self, new_state):
		self._setter_access_tracker["TextBox45"] = {}
		self._TextBox45 = TextBox(new_state)

	@property
	def FramerFlex53(self):
		self._getter_access_tracker["FramerFlex53"] = {}
		return self._FramerFlex53
	@FramerFlex53.setter
	def FramerFlex53(self, new_state):
		self._setter_access_tracker["FramerFlex53"] = {}
		self._FramerFlex53 = FramerFlex(new_state)

	@property
	def Image38(self):
		self._getter_access_tracker["Image38"] = {}
		return self._Image38
	@Image38.setter
	def Image38(self, new_state):
		self._setter_access_tracker["Image38"] = {}
		self._Image38 = Image(new_state)

	@property
	def TextBox46(self):
		self._getter_access_tracker["TextBox46"] = {}
		return self._TextBox46
	@TextBox46.setter
	def TextBox46(self, new_state):
		self._setter_access_tracker["TextBox46"] = {}
		self._TextBox46 = TextBox(new_state)

	@property
	def FramerFlex54(self):
		self._getter_access_tracker["FramerFlex54"] = {}
		return self._FramerFlex54
	@FramerFlex54.setter
	def FramerFlex54(self, new_state):
		self._setter_access_tracker["FramerFlex54"] = {}
		self._FramerFlex54 = FramerFlex(new_state)

	@property
	def Image39(self):
		self._getter_access_tracker["Image39"] = {}
		return self._Image39
	@Image39.setter
	def Image39(self, new_state):
		self._setter_access_tracker["Image39"] = {}
		self._Image39 = Image(new_state)

	@property
	def TextBox47(self):
		self._getter_access_tracker["TextBox47"] = {}
		return self._TextBox47
	@TextBox47.setter
	def TextBox47(self, new_state):
		self._setter_access_tracker["TextBox47"] = {}
		self._TextBox47 = TextBox(new_state)

	@property
	def FramerFlex55(self):
		self._getter_access_tracker["FramerFlex55"] = {}
		return self._FramerFlex55
	@FramerFlex55.setter
	def FramerFlex55(self, new_state):
		self._setter_access_tracker["FramerFlex55"] = {}
		self._FramerFlex55 = FramerFlex(new_state)

	@property
	def Image40(self):
		self._getter_access_tracker["Image40"] = {}
		return self._Image40
	@Image40.setter
	def Image40(self, new_state):
		self._setter_access_tracker["Image40"] = {}
		self._Image40 = Image(new_state)

	@property
	def TextBox48(self):
		self._getter_access_tracker["TextBox48"] = {}
		return self._TextBox48
	@TextBox48.setter
	def TextBox48(self, new_state):
		self._setter_access_tracker["TextBox48"] = {}
		self._TextBox48 = TextBox(new_state)

	@property
	def FramerFlex56(self):
		self._getter_access_tracker["FramerFlex56"] = {}
		return self._FramerFlex56
	@FramerFlex56.setter
	def FramerFlex56(self, new_state):
		self._setter_access_tracker["FramerFlex56"] = {}
		self._FramerFlex56 = FramerFlex(new_state)

	@property
	def Image41(self):
		self._getter_access_tracker["Image41"] = {}
		return self._Image41
	@Image41.setter
	def Image41(self, new_state):
		self._setter_access_tracker["Image41"] = {}
		self._Image41 = Image(new_state)

	@property
	def TextBox49(self):
		self._getter_access_tracker["TextBox49"] = {}
		return self._TextBox49
	@TextBox49.setter
	def TextBox49(self, new_state):
		self._setter_access_tracker["TextBox49"] = {}
		self._TextBox49 = TextBox(new_state)

	@property
	def FramerFlex57(self):
		self._getter_access_tracker["FramerFlex57"] = {}
		return self._FramerFlex57
	@FramerFlex57.setter
	def FramerFlex57(self, new_state):
		self._setter_access_tracker["FramerFlex57"] = {}
		self._FramerFlex57 = FramerFlex(new_state)

	@property
	def Flex51(self):
		self._getter_access_tracker["Flex51"] = {}
		return self._Flex51
	@Flex51.setter
	def Flex51(self, new_state):
		self._setter_access_tracker["Flex51"] = {}
		self._Flex51 = Flex(new_state)

	@property
	def Flex52(self):
		self._getter_access_tracker["Flex52"] = {}
		return self._Flex52
	@Flex52.setter
	def Flex52(self, new_state):
		self._setter_access_tracker["Flex52"] = {}
		self._Flex52 = Flex(new_state)

	@property
	def Flex53(self):
		self._getter_access_tracker["Flex53"] = {}
		return self._Flex53
	@Flex53.setter
	def Flex53(self, new_state):
		self._setter_access_tracker["Flex53"] = {}
		self._Flex53 = Flex(new_state)

	@property
	def TextBox50(self):
		self._getter_access_tracker["TextBox50"] = {}
		return self._TextBox50
	@TextBox50.setter
	def TextBox50(self, new_state):
		self._setter_access_tracker["TextBox50"] = {}
		self._TextBox50 = TextBox(new_state)

	@property
	def FramerFlex58(self):
		self._getter_access_tracker["FramerFlex58"] = {}
		return self._FramerFlex58
	@FramerFlex58.setter
	def FramerFlex58(self, new_state):
		self._setter_access_tracker["FramerFlex58"] = {}
		self._FramerFlex58 = FramerFlex(new_state)

	@property
	def TextBox51(self):
		self._getter_access_tracker["TextBox51"] = {}
		return self._TextBox51
	@TextBox51.setter
	def TextBox51(self, new_state):
		self._setter_access_tracker["TextBox51"] = {}
		self._TextBox51 = TextBox(new_state)

	@property
	def FramerFlex59(self):
		self._getter_access_tracker["FramerFlex59"] = {}
		return self._FramerFlex59
	@FramerFlex59.setter
	def FramerFlex59(self, new_state):
		self._setter_access_tracker["FramerFlex59"] = {}
		self._FramerFlex59 = FramerFlex(new_state)

	@property
	def Flex54(self):
		self._getter_access_tracker["Flex54"] = {}
		return self._Flex54
	@Flex54.setter
	def Flex54(self, new_state):
		self._setter_access_tracker["Flex54"] = {}
		self._Flex54 = Flex(new_state)

	@property
	def FramerFlex63(self):
		self._getter_access_tracker["FramerFlex63"] = {}
		return self._FramerFlex63
	@FramerFlex63.setter
	def FramerFlex63(self, new_state):
		self._setter_access_tracker["FramerFlex63"] = {}
		self._FramerFlex63 = FramerFlex(new_state)

	@property
	def Flex56(self):
		self._getter_access_tracker["Flex56"] = {}
		return self._Flex56
	@Flex56.setter
	def Flex56(self, new_state):
		self._setter_access_tracker["Flex56"] = {}
		self._Flex56 = Flex(new_state)

	@property
	def TextBox54(self):
		self._getter_access_tracker["TextBox54"] = {}
		return self._TextBox54
	@TextBox54.setter
	def TextBox54(self, new_state):
		self._setter_access_tracker["TextBox54"] = {}
		self._TextBox54 = TextBox(new_state)

	@property
	def TextBox56(self):
		self._getter_access_tracker["TextBox56"] = {}
		return self._TextBox56
	@TextBox56.setter
	def TextBox56(self, new_state):
		self._setter_access_tracker["TextBox56"] = {}
		self._TextBox56 = TextBox(new_state)

	@property
	def FramerFlex65(self):
		self._getter_access_tracker["FramerFlex65"] = {}
		return self._FramerFlex65
	@FramerFlex65.setter
	def FramerFlex65(self, new_state):
		self._setter_access_tracker["FramerFlex65"] = {}
		self._FramerFlex65 = FramerFlex(new_state)

	@property
	def TextBox57(self):
		self._getter_access_tracker["TextBox57"] = {}
		return self._TextBox57
	@TextBox57.setter
	def TextBox57(self, new_state):
		self._setter_access_tracker["TextBox57"] = {}
		self._TextBox57 = TextBox(new_state)

	@property
	def Flex57(self):
		self._getter_access_tracker["Flex57"] = {}
		return self._Flex57
	@Flex57.setter
	def Flex57(self, new_state):
		self._setter_access_tracker["Flex57"] = {}
		self._Flex57 = Flex(new_state)

	@property
	def FramerFlex66(self):
		self._getter_access_tracker["FramerFlex66"] = {}
		return self._FramerFlex66
	@FramerFlex66.setter
	def FramerFlex66(self, new_state):
		self._setter_access_tracker["FramerFlex66"] = {}
		self._FramerFlex66 = FramerFlex(new_state)

	@property
	def TextBox59(self):
		self._getter_access_tracker["TextBox59"] = {}
		return self._TextBox59
	@TextBox59.setter
	def TextBox59(self, new_state):
		self._setter_access_tracker["TextBox59"] = {}
		self._TextBox59 = TextBox(new_state)

	@property
	def Flex59(self):
		self._getter_access_tracker["Flex59"] = {}
		return self._Flex59
	@Flex59.setter
	def Flex59(self, new_state):
		self._setter_access_tracker["Flex59"] = {}
		self._Flex59 = Flex(new_state)

	@property
	def FramerFlex68(self):
		self._getter_access_tracker["FramerFlex68"] = {}
		return self._FramerFlex68
	@FramerFlex68.setter
	def FramerFlex68(self, new_state):
		self._setter_access_tracker["FramerFlex68"] = {}
		self._FramerFlex68 = FramerFlex(new_state)

	@property
	def TextBox60(self):
		self._getter_access_tracker["TextBox60"] = {}
		return self._TextBox60
	@TextBox60.setter
	def TextBox60(self, new_state):
		self._setter_access_tracker["TextBox60"] = {}
		self._TextBox60 = TextBox(new_state)

	@property
	def Flex60(self):
		self._getter_access_tracker["Flex60"] = {}
		return self._Flex60
	@Flex60.setter
	def Flex60(self, new_state):
		self._setter_access_tracker["Flex60"] = {}
		self._Flex60 = Flex(new_state)

	@property
	def FramerFlex69(self):
		self._getter_access_tracker["FramerFlex69"] = {}
		return self._FramerFlex69
	@FramerFlex69.setter
	def FramerFlex69(self, new_state):
		self._setter_access_tracker["FramerFlex69"] = {}
		self._FramerFlex69 = FramerFlex(new_state)

	@property
	def Image43(self):
		self._getter_access_tracker["Image43"] = {}
		return self._Image43
	@Image43.setter
	def Image43(self, new_state):
		self._setter_access_tracker["Image43"] = {}
		self._Image43 = Image(new_state)

	@property
	def Flex61(self):
		self._getter_access_tracker["Flex61"] = {}
		return self._Flex61
	@Flex61.setter
	def Flex61(self, new_state):
		self._setter_access_tracker["Flex61"] = {}
		self._Flex61 = Flex(new_state)

	@property
	def Flex62(self):
		self._getter_access_tracker["Flex62"] = {}
		return self._Flex62
	@Flex62.setter
	def Flex62(self, new_state):
		self._setter_access_tracker["Flex62"] = {}
		self._Flex62 = Flex(new_state)

	@property
	def Flex63(self):
		self._getter_access_tracker["Flex63"] = {}
		return self._Flex63
	@Flex63.setter
	def Flex63(self, new_state):
		self._setter_access_tracker["Flex63"] = {}
		self._Flex63 = Flex(new_state)

	@property
	def Flex64(self):
		self._getter_access_tracker["Flex64"] = {}
		return self._Flex64
	@Flex64.setter
	def Flex64(self, new_state):
		self._setter_access_tracker["Flex64"] = {}
		self._Flex64 = Flex(new_state)

	@property
	def Flex65(self):
		self._getter_access_tracker["Flex65"] = {}
		return self._Flex65
	@Flex65.setter
	def Flex65(self, new_state):
		self._setter_access_tracker["Flex65"] = {}
		self._Flex65 = Flex(new_state)

	@property
	def Flex66(self):
		self._getter_access_tracker["Flex66"] = {}
		return self._Flex66
	@Flex66.setter
	def Flex66(self, new_state):
		self._setter_access_tracker["Flex66"] = {}
		self._Flex66 = Flex(new_state)

	@property
	def Flex67(self):
		self._getter_access_tracker["Flex67"] = {}
		return self._Flex67
	@Flex67.setter
	def Flex67(self, new_state):
		self._setter_access_tracker["Flex67"] = {}
		self._Flex67 = Flex(new_state)

	@property
	def Flex101(self):
		self._getter_access_tracker["Flex101"] = {}
		return self._Flex101
	@Flex101.setter
	def Flex101(self, new_state):
		self._setter_access_tracker["Flex101"] = {}
		self._Flex101 = Flex(new_state)

	@property
	def Flex102(self):
		self._getter_access_tracker["Flex102"] = {}
		return self._Flex102
	@Flex102.setter
	def Flex102(self, new_state):
		self._setter_access_tracker["Flex102"] = {}
		self._Flex102 = Flex(new_state)

	@property
	def Flex103(self):
		self._getter_access_tracker["Flex103"] = {}
		return self._Flex103
	@Flex103.setter
	def Flex103(self, new_state):
		self._setter_access_tracker["Flex103"] = {}
		self._Flex103 = Flex(new_state)

	@property
	def Flex104(self):
		self._getter_access_tracker["Flex104"] = {}
		return self._Flex104
	@Flex104.setter
	def Flex104(self, new_state):
		self._setter_access_tracker["Flex104"] = {}
		self._Flex104 = Flex(new_state)

	@property
	def TextBox88(self):
		self._getter_access_tracker["TextBox88"] = {}
		return self._TextBox88
	@TextBox88.setter
	def TextBox88(self, new_state):
		self._setter_access_tracker["TextBox88"] = {}
		self._TextBox88 = TextBox(new_state)

	@property
	def TextBox89(self):
		self._getter_access_tracker["TextBox89"] = {}
		return self._TextBox89
	@TextBox89.setter
	def TextBox89(self, new_state):
		self._setter_access_tracker["TextBox89"] = {}
		self._TextBox89 = TextBox(new_state)

	@property
	def FramerFlex96(self):
		self._getter_access_tracker["FramerFlex96"] = {}
		return self._FramerFlex96
	@FramerFlex96.setter
	def FramerFlex96(self, new_state):
		self._setter_access_tracker["FramerFlex96"] = {}
		self._FramerFlex96 = FramerFlex(new_state)

	@property
	def FramerFlex97(self):
		self._getter_access_tracker["FramerFlex97"] = {}
		return self._FramerFlex97
	@FramerFlex97.setter
	def FramerFlex97(self, new_state):
		self._setter_access_tracker["FramerFlex97"] = {}
		self._FramerFlex97 = FramerFlex(new_state)

	@property
	def Flex105(self):
		self._getter_access_tracker["Flex105"] = {}
		return self._Flex105
	@Flex105.setter
	def Flex105(self, new_state):
		self._setter_access_tracker["Flex105"] = {}
		self._Flex105 = Flex(new_state)

	@property
	def TextBox90(self):
		self._getter_access_tracker["TextBox90"] = {}
		return self._TextBox90
	@TextBox90.setter
	def TextBox90(self, new_state):
		self._setter_access_tracker["TextBox90"] = {}
		self._TextBox90 = TextBox(new_state)

	@property
	def TextBox91(self):
		self._getter_access_tracker["TextBox91"] = {}
		return self._TextBox91
	@TextBox91.setter
	def TextBox91(self, new_state):
		self._setter_access_tracker["TextBox91"] = {}
		self._TextBox91 = TextBox(new_state)

	@property
	def FramerFlex98(self):
		self._getter_access_tracker["FramerFlex98"] = {}
		return self._FramerFlex98
	@FramerFlex98.setter
	def FramerFlex98(self, new_state):
		self._setter_access_tracker["FramerFlex98"] = {}
		self._FramerFlex98 = FramerFlex(new_state)

	@property
	def FramerFlex99(self):
		self._getter_access_tracker["FramerFlex99"] = {}
		return self._FramerFlex99
	@FramerFlex99.setter
	def FramerFlex99(self, new_state):
		self._setter_access_tracker["FramerFlex99"] = {}
		self._FramerFlex99 = FramerFlex(new_state)

	@property
	def Flex106(self):
		self._getter_access_tracker["Flex106"] = {}
		return self._Flex106
	@Flex106.setter
	def Flex106(self, new_state):
		self._setter_access_tracker["Flex106"] = {}
		self._Flex106 = Flex(new_state)

	@property
	def TextBox92(self):
		self._getter_access_tracker["TextBox92"] = {}
		return self._TextBox92
	@TextBox92.setter
	def TextBox92(self, new_state):
		self._setter_access_tracker["TextBox92"] = {}
		self._TextBox92 = TextBox(new_state)

	@property
	def TextBox93(self):
		self._getter_access_tracker["TextBox93"] = {}
		return self._TextBox93
	@TextBox93.setter
	def TextBox93(self, new_state):
		self._setter_access_tracker["TextBox93"] = {}
		self._TextBox93 = TextBox(new_state)

	@property
	def FramerFlex100(self):
		self._getter_access_tracker["FramerFlex100"] = {}
		return self._FramerFlex100
	@FramerFlex100.setter
	def FramerFlex100(self, new_state):
		self._setter_access_tracker["FramerFlex100"] = {}
		self._FramerFlex100 = FramerFlex(new_state)

	@property
	def FramerFlex101(self):
		self._getter_access_tracker["FramerFlex101"] = {}
		return self._FramerFlex101
	@FramerFlex101.setter
	def FramerFlex101(self, new_state):
		self._setter_access_tracker["FramerFlex101"] = {}
		self._FramerFlex101 = FramerFlex(new_state)

	@property
	def Flex107(self):
		self._getter_access_tracker["Flex107"] = {}
		return self._Flex107
	@Flex107.setter
	def Flex107(self, new_state):
		self._setter_access_tracker["Flex107"] = {}
		self._Flex107 = Flex(new_state)

	@property
	def TextBox94(self):
		self._getter_access_tracker["TextBox94"] = {}
		return self._TextBox94
	@TextBox94.setter
	def TextBox94(self, new_state):
		self._setter_access_tracker["TextBox94"] = {}
		self._TextBox94 = TextBox(new_state)

	@property
	def Flex108(self):
		self._getter_access_tracker["Flex108"] = {}
		return self._Flex108
	@Flex108.setter
	def Flex108(self, new_state):
		self._setter_access_tracker["Flex108"] = {}
		self._Flex108 = Flex(new_state)

	@property
	def TextBox95(self):
		self._getter_access_tracker["TextBox95"] = {}
		return self._TextBox95
	@TextBox95.setter
	def TextBox95(self, new_state):
		self._setter_access_tracker["TextBox95"] = {}
		self._TextBox95 = TextBox(new_state)

	@property
	def Input5(self):
		self._getter_access_tracker["Input5"] = {}
		return self._Input5
	@Input5.setter
	def Input5(self, new_state):
		self._setter_access_tracker["Input5"] = {}
		self._Input5 = Input(new_state)

	@property
	def FramerFlex102(self):
		self._getter_access_tracker["FramerFlex102"] = {}
		return self._FramerFlex102
	@FramerFlex102.setter
	def FramerFlex102(self, new_state):
		self._setter_access_tracker["FramerFlex102"] = {}
		self._FramerFlex102 = FramerFlex(new_state)

	@property
	def FramerFlex103(self):
		self._getter_access_tracker["FramerFlex103"] = {}
		return self._FramerFlex103
	@FramerFlex103.setter
	def FramerFlex103(self, new_state):
		self._setter_access_tracker["FramerFlex103"] = {}
		self._FramerFlex103 = FramerFlex(new_state)

	@property
	def Flex109(self):
		self._getter_access_tracker["Flex109"] = {}
		return self._Flex109
	@Flex109.setter
	def Flex109(self, new_state):
		self._setter_access_tracker["Flex109"] = {}
		self._Flex109 = Flex(new_state)

	@property
	def Flex110(self):
		self._getter_access_tracker["Flex110"] = {}
		return self._Flex110
	@Flex110.setter
	def Flex110(self, new_state):
		self._setter_access_tracker["Flex110"] = {}
		self._Flex110 = Flex(new_state)

	@property
	def Flex111(self):
		self._getter_access_tracker["Flex111"] = {}
		return self._Flex111
	@Flex111.setter
	def Flex111(self, new_state):
		self._setter_access_tracker["Flex111"] = {}
		self._Flex111 = Flex(new_state)

	@property
	def TextBox102(self):
		self._getter_access_tracker["TextBox102"] = {}
		return self._TextBox102
	@TextBox102.setter
	def TextBox102(self, new_state):
		self._setter_access_tracker["TextBox102"] = {}
		self._TextBox102 = TextBox(new_state)

	@property
	def Flex119(self):
		self._getter_access_tracker["Flex119"] = {}
		return self._Flex119
	@Flex119.setter
	def Flex119(self, new_state):
		self._setter_access_tracker["Flex119"] = {}
		self._Flex119 = Flex(new_state)

	@property
	def FramerFlex110(self):
		self._getter_access_tracker["FramerFlex110"] = {}
		return self._FramerFlex110
	@FramerFlex110.setter
	def FramerFlex110(self, new_state):
		self._setter_access_tracker["FramerFlex110"] = {}
		self._FramerFlex110 = FramerFlex(new_state)

	@property
	def Input6(self):
		self._getter_access_tracker["Input6"] = {}
		return self._Input6
	@Input6.setter
	def Input6(self, new_state):
		self._setter_access_tracker["Input6"] = {}
		self._Input6 = Input(new_state)

	@property
	def TextBox103(self):
		self._getter_access_tracker["TextBox103"] = {}
		return self._TextBox103
	@TextBox103.setter
	def TextBox103(self, new_state):
		self._setter_access_tracker["TextBox103"] = {}
		self._TextBox103 = TextBox(new_state)

	@property
	def Flex120(self):
		self._getter_access_tracker["Flex120"] = {}
		return self._Flex120
	@Flex120.setter
	def Flex120(self, new_state):
		self._setter_access_tracker["Flex120"] = {}
		self._Flex120 = Flex(new_state)

	@property
	def FramerFlex111(self):
		self._getter_access_tracker["FramerFlex111"] = {}
		return self._FramerFlex111
	@FramerFlex111.setter
	def FramerFlex111(self, new_state):
		self._setter_access_tracker["FramerFlex111"] = {}
		self._FramerFlex111 = FramerFlex(new_state)

	@property
	def Flex121(self):
		self._getter_access_tracker["Flex121"] = {}
		return self._Flex121
	@Flex121.setter
	def Flex121(self, new_state):
		self._setter_access_tracker["Flex121"] = {}
		self._Flex121 = Flex(new_state)

	@property
	def Flex122(self):
		self._getter_access_tracker["Flex122"] = {}
		return self._Flex122
	@Flex122.setter
	def Flex122(self, new_state):
		self._setter_access_tracker["Flex122"] = {}
		self._Flex122 = Flex(new_state)

	@property
	def TextBox104(self):
		self._getter_access_tracker["TextBox104"] = {}
		return self._TextBox104
	@TextBox104.setter
	def TextBox104(self, new_state):
		self._setter_access_tracker["TextBox104"] = {}
		self._TextBox104 = TextBox(new_state)

	@property
	def TextBox105(self):
		self._getter_access_tracker["TextBox105"] = {}
		return self._TextBox105
	@TextBox105.setter
	def TextBox105(self, new_state):
		self._setter_access_tracker["TextBox105"] = {}
		self._TextBox105 = TextBox(new_state)

	@property
	def FramerFlex112(self):
		self._getter_access_tracker["FramerFlex112"] = {}
		return self._FramerFlex112
	@FramerFlex112.setter
	def FramerFlex112(self, new_state):
		self._setter_access_tracker["FramerFlex112"] = {}
		self._FramerFlex112 = FramerFlex(new_state)

	@property
	def FramerFlex113(self):
		self._getter_access_tracker["FramerFlex113"] = {}
		return self._FramerFlex113
	@FramerFlex113.setter
	def FramerFlex113(self, new_state):
		self._setter_access_tracker["FramerFlex113"] = {}
		self._FramerFlex113 = FramerFlex(new_state)

	@property
	def Flex123(self):
		self._getter_access_tracker["Flex123"] = {}
		return self._Flex123
	@Flex123.setter
	def Flex123(self, new_state):
		self._setter_access_tracker["Flex123"] = {}
		self._Flex123 = Flex(new_state)

	@property
	def TextBox108(self):
		self._getter_access_tracker["TextBox108"] = {}
		return self._TextBox108
	@TextBox108.setter
	def TextBox108(self, new_state):
		self._setter_access_tracker["TextBox108"] = {}
		self._TextBox108 = TextBox(new_state)

	@property
	def TextBox109(self):
		self._getter_access_tracker["TextBox109"] = {}
		return self._TextBox109
	@TextBox109.setter
	def TextBox109(self, new_state):
		self._setter_access_tracker["TextBox109"] = {}
		self._TextBox109 = TextBox(new_state)

	@property
	def FramerFlex116(self):
		self._getter_access_tracker["FramerFlex116"] = {}
		return self._FramerFlex116
	@FramerFlex116.setter
	def FramerFlex116(self, new_state):
		self._setter_access_tracker["FramerFlex116"] = {}
		self._FramerFlex116 = FramerFlex(new_state)

	@property
	def FramerFlex117(self):
		self._getter_access_tracker["FramerFlex117"] = {}
		return self._FramerFlex117
	@FramerFlex117.setter
	def FramerFlex117(self, new_state):
		self._setter_access_tracker["FramerFlex117"] = {}
		self._FramerFlex117 = FramerFlex(new_state)

	@property
	def Flex125(self):
		self._getter_access_tracker["Flex125"] = {}
		return self._Flex125
	@Flex125.setter
	def Flex125(self, new_state):
		self._setter_access_tracker["Flex125"] = {}
		self._Flex125 = Flex(new_state)

	@property
	def Flex126(self):
		self._getter_access_tracker["Flex126"] = {}
		return self._Flex126
	@Flex126.setter
	def Flex126(self, new_state):
		self._setter_access_tracker["Flex126"] = {}
		self._Flex126 = Flex(new_state)

	@property
	def TextBox110(self):
		self._getter_access_tracker["TextBox110"] = {}
		return self._TextBox110
	@TextBox110.setter
	def TextBox110(self, new_state):
		self._setter_access_tracker["TextBox110"] = {}
		self._TextBox110 = TextBox(new_state)

	@property
	def TextBox111(self):
		self._getter_access_tracker["TextBox111"] = {}
		return self._TextBox111
	@TextBox111.setter
	def TextBox111(self, new_state):
		self._setter_access_tracker["TextBox111"] = {}
		self._TextBox111 = TextBox(new_state)

	@property
	def FramerFlex118(self):
		self._getter_access_tracker["FramerFlex118"] = {}
		return self._FramerFlex118
	@FramerFlex118.setter
	def FramerFlex118(self, new_state):
		self._setter_access_tracker["FramerFlex118"] = {}
		self._FramerFlex118 = FramerFlex(new_state)

	@property
	def FramerFlex119(self):
		self._getter_access_tracker["FramerFlex119"] = {}
		return self._FramerFlex119
	@FramerFlex119.setter
	def FramerFlex119(self, new_state):
		self._setter_access_tracker["FramerFlex119"] = {}
		self._FramerFlex119 = FramerFlex(new_state)

	@property
	def Flex127(self):
		self._getter_access_tracker["Flex127"] = {}
		return self._Flex127
	@Flex127.setter
	def Flex127(self, new_state):
		self._setter_access_tracker["Flex127"] = {}
		self._Flex127 = Flex(new_state)

	@property
	def Flex128(self):
		self._getter_access_tracker["Flex128"] = {}
		return self._Flex128
	@Flex128.setter
	def Flex128(self, new_state):
		self._setter_access_tracker["Flex128"] = {}
		self._Flex128 = Flex(new_state)

	@property
	def Flex130(self):
		self._getter_access_tracker["Flex130"] = {}
		return self._Flex130
	@Flex130.setter
	def Flex130(self, new_state):
		self._setter_access_tracker["Flex130"] = {}
		self._Flex130 = Flex(new_state)

	@property
	def Flex131(self):
		self._getter_access_tracker["Flex131"] = {}
		return self._Flex131
	@Flex131.setter
	def Flex131(self, new_state):
		self._setter_access_tracker["Flex131"] = {}
		self._Flex131 = Flex(new_state)

	@property
	def Flex132(self):
		self._getter_access_tracker["Flex132"] = {}
		return self._Flex132
	@Flex132.setter
	def Flex132(self, new_state):
		self._setter_access_tracker["Flex132"] = {}
		self._Flex132 = Flex(new_state)

	@property
	def Flex133(self):
		self._getter_access_tracker["Flex133"] = {}
		return self._Flex133
	@Flex133.setter
	def Flex133(self, new_state):
		self._setter_access_tracker["Flex133"] = {}
		self._Flex133 = Flex(new_state)

	@property
	def Flex134(self):
		self._getter_access_tracker["Flex134"] = {}
		return self._Flex134
	@Flex134.setter
	def Flex134(self, new_state):
		self._setter_access_tracker["Flex134"] = {}
		self._Flex134 = Flex(new_state)

	@property
	def TextBox114(self):
		self._getter_access_tracker["TextBox114"] = {}
		return self._TextBox114
	@TextBox114.setter
	def TextBox114(self, new_state):
		self._setter_access_tracker["TextBox114"] = {}
		self._TextBox114 = TextBox(new_state)

	@property
	def FramerFlex122(self):
		self._getter_access_tracker["FramerFlex122"] = {}
		return self._FramerFlex122
	@FramerFlex122.setter
	def FramerFlex122(self, new_state):
		self._setter_access_tracker["FramerFlex122"] = {}
		self._FramerFlex122 = FramerFlex(new_state)

	@property
	def TextBox115(self):
		self._getter_access_tracker["TextBox115"] = {}
		return self._TextBox115
	@TextBox115.setter
	def TextBox115(self, new_state):
		self._setter_access_tracker["TextBox115"] = {}
		self._TextBox115 = TextBox(new_state)

	@property
	def FramerFlex123(self):
		self._getter_access_tracker["FramerFlex123"] = {}
		return self._FramerFlex123
	@FramerFlex123.setter
	def FramerFlex123(self, new_state):
		self._setter_access_tracker["FramerFlex123"] = {}
		self._FramerFlex123 = FramerFlex(new_state)

	@property
	def TextBox116(self):
		self._getter_access_tracker["TextBox116"] = {}
		return self._TextBox116
	@TextBox116.setter
	def TextBox116(self, new_state):
		self._setter_access_tracker["TextBox116"] = {}
		self._TextBox116 = TextBox(new_state)

	@property
	def Image44(self):
		self._getter_access_tracker["Image44"] = {}
		return self._Image44
	@Image44.setter
	def Image44(self, new_state):
		self._setter_access_tracker["Image44"] = {}
		self._Image44 = Image(new_state)

	@property
	def FramerFlex124(self):
		self._getter_access_tracker["FramerFlex124"] = {}
		return self._FramerFlex124
	@FramerFlex124.setter
	def FramerFlex124(self, new_state):
		self._setter_access_tracker["FramerFlex124"] = {}
		self._FramerFlex124 = FramerFlex(new_state)

	@property
	def Flex135(self):
		self._getter_access_tracker["Flex135"] = {}
		return self._Flex135
	@Flex135.setter
	def Flex135(self, new_state):
		self._setter_access_tracker["Flex135"] = {}
		self._Flex135 = Flex(new_state)

	@property
	def Flex136(self):
		self._getter_access_tracker["Flex136"] = {}
		return self._Flex136
	@Flex136.setter
	def Flex136(self, new_state):
		self._setter_access_tracker["Flex136"] = {}
		self._Flex136 = Flex(new_state)

	@property
	def Flex137(self):
		self._getter_access_tracker["Flex137"] = {}
		return self._Flex137
	@Flex137.setter
	def Flex137(self, new_state):
		self._setter_access_tracker["Flex137"] = {}
		self._Flex137 = Flex(new_state)

	@property
	def Flex138(self):
		self._getter_access_tracker["Flex138"] = {}
		return self._Flex138
	@Flex138.setter
	def Flex138(self, new_state):
		self._setter_access_tracker["Flex138"] = {}
		self._Flex138 = Flex(new_state)

	@property
	def Div2(self):
		self._getter_access_tracker["Div2"] = {}
		return self._Div2
	@Div2.setter
	def Div2(self, new_state):
		self._setter_access_tracker["Div2"] = {}
		self._Div2 = Div(new_state)

	@property
	def Flex139(self):
		self._getter_access_tracker["Flex139"] = {}
		return self._Flex139
	@Flex139.setter
	def Flex139(self, new_state):
		self._setter_access_tracker["Flex139"] = {}
		self._Flex139 = Flex(new_state)

	@property
	def Image45(self):
		self._getter_access_tracker["Image45"] = {}
		return self._Image45
	@Image45.setter
	def Image45(self, new_state):
		self._setter_access_tracker["Image45"] = {}
		self._Image45 = Image(new_state)

	@property
	def TextBox117(self):
		self._getter_access_tracker["TextBox117"] = {}
		return self._TextBox117
	@TextBox117.setter
	def TextBox117(self, new_state):
		self._setter_access_tracker["TextBox117"] = {}
		self._TextBox117 = TextBox(new_state)

	@property
	def Flex140(self):
		self._getter_access_tracker["Flex140"] = {}
		return self._Flex140
	@Flex140.setter
	def Flex140(self, new_state):
		self._setter_access_tracker["Flex140"] = {}
		self._Flex140 = Flex(new_state)

	@property
	def Flex141(self):
		self._getter_access_tracker["Flex141"] = {}
		return self._Flex141
	@Flex141.setter
	def Flex141(self, new_state):
		self._setter_access_tracker["Flex141"] = {}
		self._Flex141 = Flex(new_state)

	@property
	def FramerFlex125(self):
		self._getter_access_tracker["FramerFlex125"] = {}
		return self._FramerFlex125
	@FramerFlex125.setter
	def FramerFlex125(self, new_state):
		self._setter_access_tracker["FramerFlex125"] = {}
		self._FramerFlex125 = FramerFlex(new_state)

	@property
	def TextBox118(self):
		self._getter_access_tracker["TextBox118"] = {}
		return self._TextBox118
	@TextBox118.setter
	def TextBox118(self, new_state):
		self._setter_access_tracker["TextBox118"] = {}
		self._TextBox118 = TextBox(new_state)

	@property
	def Anchor8(self):
		self._getter_access_tracker["Anchor8"] = {}
		return self._Anchor8
	@Anchor8.setter
	def Anchor8(self, new_state):
		self._setter_access_tracker["Anchor8"] = {}
		self._Anchor8 = Anchor(new_state)

	@property
	def FramerFlex126(self):
		self._getter_access_tracker["FramerFlex126"] = {}
		return self._FramerFlex126
	@FramerFlex126.setter
	def FramerFlex126(self, new_state):
		self._setter_access_tracker["FramerFlex126"] = {}
		self._FramerFlex126 = FramerFlex(new_state)

	@property
	def TextBox120(self):
		self._getter_access_tracker["TextBox120"] = {}
		return self._TextBox120
	@TextBox120.setter
	def TextBox120(self, new_state):
		self._setter_access_tracker["TextBox120"] = {}
		self._TextBox120 = TextBox(new_state)

	@property
	def FramerFlex127(self):
		self._getter_access_tracker["FramerFlex127"] = {}
		return self._FramerFlex127
	@FramerFlex127.setter
	def FramerFlex127(self, new_state):
		self._setter_access_tracker["FramerFlex127"] = {}
		self._FramerFlex127 = FramerFlex(new_state)

	@property
	def FramerFlex128(self):
		self._getter_access_tracker["FramerFlex128"] = {}
		return self._FramerFlex128
	@FramerFlex128.setter
	def FramerFlex128(self, new_state):
		self._setter_access_tracker["FramerFlex128"] = {}
		self._FramerFlex128 = FramerFlex(new_state)

	@property
	def Anchor9(self):
		self._getter_access_tracker["Anchor9"] = {}
		return self._Anchor9
	@Anchor9.setter
	def Anchor9(self, new_state):
		self._setter_access_tracker["Anchor9"] = {}
		self._Anchor9 = Anchor(new_state)

	@property
	def TextBox122(self):
		self._getter_access_tracker["TextBox122"] = {}
		return self._TextBox122
	@TextBox122.setter
	def TextBox122(self, new_state):
		self._setter_access_tracker["TextBox122"] = {}
		self._TextBox122 = TextBox(new_state)

	@property
	def FramerFlex129(self):
		self._getter_access_tracker["FramerFlex129"] = {}
		return self._FramerFlex129
	@FramerFlex129.setter
	def FramerFlex129(self, new_state):
		self._setter_access_tracker["FramerFlex129"] = {}
		self._FramerFlex129 = FramerFlex(new_state)

	@property
	def FramerFlex130(self):
		self._getter_access_tracker["FramerFlex130"] = {}
		return self._FramerFlex130
	@FramerFlex130.setter
	def FramerFlex130(self, new_state):
		self._setter_access_tracker["FramerFlex130"] = {}
		self._FramerFlex130 = FramerFlex(new_state)

	@property
	def Anchor10(self):
		self._getter_access_tracker["Anchor10"] = {}
		return self._Anchor10
	@Anchor10.setter
	def Anchor10(self, new_state):
		self._setter_access_tracker["Anchor10"] = {}
		self._Anchor10 = Anchor(new_state)

	@property
	def TextBox124(self):
		self._getter_access_tracker["TextBox124"] = {}
		return self._TextBox124
	@TextBox124.setter
	def TextBox124(self, new_state):
		self._setter_access_tracker["TextBox124"] = {}
		self._TextBox124 = TextBox(new_state)

	@property
	def TextBox125(self):
		self._getter_access_tracker["TextBox125"] = {}
		return self._TextBox125
	@TextBox125.setter
	def TextBox125(self, new_state):
		self._setter_access_tracker["TextBox125"] = {}
		self._TextBox125 = TextBox(new_state)

	@property
	def TextBox126(self):
		self._getter_access_tracker["TextBox126"] = {}
		return self._TextBox126
	@TextBox126.setter
	def TextBox126(self, new_state):
		self._setter_access_tracker["TextBox126"] = {}
		self._TextBox126 = TextBox(new_state)

	@property
	def FramerText7(self):
		self._getter_access_tracker["FramerText7"] = {}
		return self._FramerText7
	@FramerText7.setter
	def FramerText7(self, new_state):
		self._setter_access_tracker["FramerText7"] = {}
		self._FramerText7 = FramerText(new_state)

	@property
	def Anchor11(self):
		self._getter_access_tracker["Anchor11"] = {}
		return self._Anchor11
	@Anchor11.setter
	def Anchor11(self, new_state):
		self._setter_access_tracker["Anchor11"] = {}
		self._Anchor11 = Anchor(new_state)

	@property
	def FramerText8(self):
		self._getter_access_tracker["FramerText8"] = {}
		return self._FramerText8
	@FramerText8.setter
	def FramerText8(self, new_state):
		self._setter_access_tracker["FramerText8"] = {}
		self._FramerText8 = FramerText(new_state)

	@property
	def Anchor12(self):
		self._getter_access_tracker["Anchor12"] = {}
		return self._Anchor12
	@Anchor12.setter
	def Anchor12(self, new_state):
		self._setter_access_tracker["Anchor12"] = {}
		self._Anchor12 = Anchor(new_state)

	@property
	def FramerText9(self):
		self._getter_access_tracker["FramerText9"] = {}
		return self._FramerText9
	@FramerText9.setter
	def FramerText9(self, new_state):
		self._setter_access_tracker["FramerText9"] = {}
		self._FramerText9 = FramerText(new_state)

	@property
	def Anchor13(self):
		self._getter_access_tracker["Anchor13"] = {}
		return self._Anchor13
	@Anchor13.setter
	def Anchor13(self, new_state):
		self._setter_access_tracker["Anchor13"] = {}
		self._Anchor13 = Anchor(new_state)

	@property
	def FramerText10(self):
		self._getter_access_tracker["FramerText10"] = {}
		return self._FramerText10
	@FramerText10.setter
	def FramerText10(self, new_state):
		self._setter_access_tracker["FramerText10"] = {}
		self._FramerText10 = FramerText(new_state)

	@property
	def Anchor14(self):
		self._getter_access_tracker["Anchor14"] = {}
		return self._Anchor14
	@Anchor14.setter
	def Anchor14(self, new_state):
		self._setter_access_tracker["Anchor14"] = {}
		self._Anchor14 = Anchor(new_state)

	@property
	def TextBox127(self):
		self._getter_access_tracker["TextBox127"] = {}
		return self._TextBox127
	@TextBox127.setter
	def TextBox127(self, new_state):
		self._setter_access_tracker["TextBox127"] = {}
		self._TextBox127 = TextBox(new_state)

	@property
	def TextBox128(self):
		self._getter_access_tracker["TextBox128"] = {}
		return self._TextBox128
	@TextBox128.setter
	def TextBox128(self, new_state):
		self._setter_access_tracker["TextBox128"] = {}
		self._TextBox128 = TextBox(new_state)

	@property
	def TextBox129(self):
		self._getter_access_tracker["TextBox129"] = {}
		return self._TextBox129
	@TextBox129.setter
	def TextBox129(self, new_state):
		self._setter_access_tracker["TextBox129"] = {}
		self._TextBox129 = TextBox(new_state)

	@property
	def FramerFlex131(self):
		self._getter_access_tracker["FramerFlex131"] = {}
		return self._FramerFlex131
	@FramerFlex131.setter
	def FramerFlex131(self, new_state):
		self._setter_access_tracker["FramerFlex131"] = {}
		self._FramerFlex131 = FramerFlex(new_state)

	@property
	def TextBox130(self):
		self._getter_access_tracker["TextBox130"] = {}
		return self._TextBox130
	@TextBox130.setter
	def TextBox130(self, new_state):
		self._setter_access_tracker["TextBox130"] = {}
		self._TextBox130 = TextBox(new_state)

	@property
	def FramerFlex132(self):
		self._getter_access_tracker["FramerFlex132"] = {}
		return self._FramerFlex132
	@FramerFlex132.setter
	def FramerFlex132(self, new_state):
		self._setter_access_tracker["FramerFlex132"] = {}
		self._FramerFlex132 = FramerFlex(new_state)

	@property
	def TextBox131(self):
		self._getter_access_tracker["TextBox131"] = {}
		return self._TextBox131
	@TextBox131.setter
	def TextBox131(self, new_state):
		self._setter_access_tracker["TextBox131"] = {}
		self._TextBox131 = TextBox(new_state)

	@property
	def FramerFlex133(self):
		self._getter_access_tracker["FramerFlex133"] = {}
		return self._FramerFlex133
	@FramerFlex133.setter
	def FramerFlex133(self, new_state):
		self._setter_access_tracker["FramerFlex133"] = {}
		self._FramerFlex133 = FramerFlex(new_state)

	@property
	def TextBox132(self):
		self._getter_access_tracker["TextBox132"] = {}
		return self._TextBox132
	@TextBox132.setter
	def TextBox132(self, new_state):
		self._setter_access_tracker["TextBox132"] = {}
		self._TextBox132 = TextBox(new_state)

	@property
	def Anchor15(self):
		self._getter_access_tracker["Anchor15"] = {}
		return self._Anchor15
	@Anchor15.setter
	def Anchor15(self, new_state):
		self._setter_access_tracker["Anchor15"] = {}
		self._Anchor15 = Anchor(new_state)

	@property
	def FramerFlex134(self):
		self._getter_access_tracker["FramerFlex134"] = {}
		return self._FramerFlex134
	@FramerFlex134.setter
	def FramerFlex134(self, new_state):
		self._setter_access_tracker["FramerFlex134"] = {}
		self._FramerFlex134 = FramerFlex(new_state)

	@property
	def Anchor16(self):
		self._getter_access_tracker["Anchor16"] = {}
		return self._Anchor16
	@Anchor16.setter
	def Anchor16(self, new_state):
		self._setter_access_tracker["Anchor16"] = {}
		self._Anchor16 = Anchor(new_state)

	@property
	def FramerFlex135(self):
		self._getter_access_tracker["FramerFlex135"] = {}
		return self._FramerFlex135
	@FramerFlex135.setter
	def FramerFlex135(self, new_state):
		self._setter_access_tracker["FramerFlex135"] = {}
		self._FramerFlex135 = FramerFlex(new_state)

	@property
	def Anchor17(self):
		self._getter_access_tracker["Anchor17"] = {}
		return self._Anchor17
	@Anchor17.setter
	def Anchor17(self, new_state):
		self._setter_access_tracker["Anchor17"] = {}
		self._Anchor17 = Anchor(new_state)

	@property
	def FramerFlex136(self):
		self._getter_access_tracker["FramerFlex136"] = {}
		return self._FramerFlex136
	@FramerFlex136.setter
	def FramerFlex136(self, new_state):
		self._setter_access_tracker["FramerFlex136"] = {}
		self._FramerFlex136 = FramerFlex(new_state)

	@property
	def Flex142(self):
		self._getter_access_tracker["Flex142"] = {}
		return self._Flex142
	@Flex142.setter
	def Flex142(self, new_state):
		self._setter_access_tracker["Flex142"] = {}
		self._Flex142 = Flex(new_state)

	@property
	def Flex143(self):
		self._getter_access_tracker["Flex143"] = {}
		return self._Flex143
	@Flex143.setter
	def Flex143(self, new_state):
		self._setter_access_tracker["Flex143"] = {}
		self._Flex143 = Flex(new_state)

	@property
	def Flex144(self):
		self._getter_access_tracker["Flex144"] = {}
		return self._Flex144
	@Flex144.setter
	def Flex144(self, new_state):
		self._setter_access_tracker["Flex144"] = {}
		self._Flex144 = Flex(new_state)

	@property
	def Flex146(self):
		self._getter_access_tracker["Flex146"] = {}
		return self._Flex146
	@Flex146.setter
	def Flex146(self, new_state):
		self._setter_access_tracker["Flex146"] = {}
		self._Flex146 = Flex(new_state)

	@property
	def TextBox134(self):
		self._getter_access_tracker["TextBox134"] = {}
		return self._TextBox134
	@TextBox134.setter
	def TextBox134(self, new_state):
		self._setter_access_tracker["TextBox134"] = {}
		self._TextBox134 = TextBox(new_state)

	@property
	def Anchor18(self):
		self._getter_access_tracker["Anchor18"] = {}
		return self._Anchor18
	@Anchor18.setter
	def Anchor18(self, new_state):
		self._setter_access_tracker["Anchor18"] = {}
		self._Anchor18 = Anchor(new_state)

	@property
	def TextBox135(self):
		self._getter_access_tracker["TextBox135"] = {}
		return self._TextBox135
	@TextBox135.setter
	def TextBox135(self, new_state):
		self._setter_access_tracker["TextBox135"] = {}
		self._TextBox135 = TextBox(new_state)

	@property
	def Image46(self):
		self._getter_access_tracker["Image46"] = {}
		return self._Image46
	@Image46.setter
	def Image46(self, new_state):
		self._setter_access_tracker["Image46"] = {}
		self._Image46 = Image(new_state)

	@property
	def TextBox136(self):
		self._getter_access_tracker["TextBox136"] = {}
		return self._TextBox136
	@TextBox136.setter
	def TextBox136(self, new_state):
		self._setter_access_tracker["TextBox136"] = {}
		self._TextBox136 = TextBox(new_state)

	@property
	def Anchor19(self):
		self._getter_access_tracker["Anchor19"] = {}
		return self._Anchor19
	@Anchor19.setter
	def Anchor19(self, new_state):
		self._setter_access_tracker["Anchor19"] = {}
		self._Anchor19 = Anchor(new_state)

	@property
	def Anchor20(self):
		self._getter_access_tracker["Anchor20"] = {}
		return self._Anchor20
	@Anchor20.setter
	def Anchor20(self, new_state):
		self._setter_access_tracker["Anchor20"] = {}
		self._Anchor20 = Anchor(new_state)

	@property
	def Anchor21(self):
		self._getter_access_tracker["Anchor21"] = {}
		return self._Anchor21
	@Anchor21.setter
	def Anchor21(self, new_state):
		self._setter_access_tracker["Anchor21"] = {}
		self._Anchor21 = Anchor(new_state)

	@property
	def Anchor25(self):
		self._getter_access_tracker["Anchor25"] = {}
		return self._Anchor25
	@Anchor25.setter
	def Anchor25(self, new_state):
		self._setter_access_tracker["Anchor25"] = {}
		self._Anchor25 = Anchor(new_state)

	@property
	def FramerFlex138(self):
		self._getter_access_tracker["FramerFlex138"] = {}
		return self._FramerFlex138
	@FramerFlex138.setter
	def FramerFlex138(self, new_state):
		self._setter_access_tracker["FramerFlex138"] = {}
		self._FramerFlex138 = FramerFlex(new_state)

	@property
	def Image47(self):
		self._getter_access_tracker["Image47"] = {}
		return self._Image47
	@Image47.setter
	def Image47(self, new_state):
		self._setter_access_tracker["Image47"] = {}
		self._Image47 = Image(new_state)

	@property
	def Image48(self):
		self._getter_access_tracker["Image48"] = {}
		return self._Image48
	@Image48.setter
	def Image48(self, new_state):
		self._setter_access_tracker["Image48"] = {}
		self._Image48 = Image(new_state)

	@property
	def Image49(self):
		self._getter_access_tracker["Image49"] = {}
		return self._Image49
	@Image49.setter
	def Image49(self, new_state):
		self._setter_access_tracker["Image49"] = {}
		self._Image49 = Image(new_state)

	@property
	def Image50(self):
		self._getter_access_tracker["Image50"] = {}
		return self._Image50
	@Image50.setter
	def Image50(self, new_state):
		self._setter_access_tracker["Image50"] = {}
		self._Image50 = Image(new_state)

	@property
	def Image51(self):
		self._getter_access_tracker["Image51"] = {}
		return self._Image51
	@Image51.setter
	def Image51(self, new_state):
		self._setter_access_tracker["Image51"] = {}
		self._Image51 = Image(new_state)

	@property
	def Image52(self):
		self._getter_access_tracker["Image52"] = {}
		return self._Image52
	@Image52.setter
	def Image52(self, new_state):
		self._setter_access_tracker["Image52"] = {}
		self._Image52 = Image(new_state)

	@property
	def Image53(self):
		self._getter_access_tracker["Image53"] = {}
		return self._Image53
	@Image53.setter
	def Image53(self, new_state):
		self._setter_access_tracker["Image53"] = {}
		self._Image53 = Image(new_state)

	@property
	def Image54(self):
		self._getter_access_tracker["Image54"] = {}
		return self._Image54
	@Image54.setter
	def Image54(self, new_state):
		self._setter_access_tracker["Image54"] = {}
		self._Image54 = Image(new_state)

	@property
	def Image55(self):
		self._getter_access_tracker["Image55"] = {}
		return self._Image55
	@Image55.setter
	def Image55(self, new_state):
		self._setter_access_tracker["Image55"] = {}
		self._Image55 = Image(new_state)

	@property
	def Image56(self):
		self._getter_access_tracker["Image56"] = {}
		return self._Image56
	@Image56.setter
	def Image56(self, new_state):
		self._setter_access_tracker["Image56"] = {}
		self._Image56 = Image(new_state)

	@property
	def Flex148(self):
		self._getter_access_tracker["Flex148"] = {}
		return self._Flex148
	@Flex148.setter
	def Flex148(self, new_state):
		self._setter_access_tracker["Flex148"] = {}
		self._Flex148 = Flex(new_state)

	@property
	def Flex149(self):
		self._getter_access_tracker["Flex149"] = {}
		return self._Flex149
	@Flex149.setter
	def Flex149(self, new_state):
		self._setter_access_tracker["Flex149"] = {}
		self._Flex149 = Flex(new_state)

	@property
	def Image59(self):
		self._getter_access_tracker["Image59"] = {}
		return self._Image59
	@Image59.setter
	def Image59(self, new_state):
		self._setter_access_tracker["Image59"] = {}
		self._Image59 = Image(new_state)

	@property
	def Flex150(self):
		self._getter_access_tracker["Flex150"] = {}
		return self._Flex150
	@Flex150.setter
	def Flex150(self, new_state):
		self._setter_access_tracker["Flex150"] = {}
		self._Flex150 = Flex(new_state)

	@property
	def Flex151(self):
		self._getter_access_tracker["Flex151"] = {}
		return self._Flex151
	@Flex151.setter
	def Flex151(self, new_state):
		self._setter_access_tracker["Flex151"] = {}
		self._Flex151 = Flex(new_state)

	@property
	def Flex153(self):
		self._getter_access_tracker["Flex153"] = {}
		return self._Flex153
	@Flex153.setter
	def Flex153(self, new_state):
		self._setter_access_tracker["Flex153"] = {}
		self._Flex153 = Flex(new_state)

	@property
	def Image60(self):
		self._getter_access_tracker["Image60"] = {}
		return self._Image60
	@Image60.setter
	def Image60(self, new_state):
		self._setter_access_tracker["Image60"] = {}
		self._Image60 = Image(new_state)

	@property
	def FramerFlex140(self):
		self._getter_access_tracker["FramerFlex140"] = {}
		return self._FramerFlex140
	@FramerFlex140.setter
	def FramerFlex140(self, new_state):
		self._setter_access_tracker["FramerFlex140"] = {}
		self._FramerFlex140 = FramerFlex(new_state)

	@property
	def TextBox137(self):
		self._getter_access_tracker["TextBox137"] = {}
		return self._TextBox137
	@TextBox137.setter
	def TextBox137(self, new_state):
		self._setter_access_tracker["TextBox137"] = {}
		self._TextBox137 = TextBox(new_state)

	@property
	def Flex154(self):
		self._getter_access_tracker["Flex154"] = {}
		return self._Flex154
	@Flex154.setter
	def Flex154(self, new_state):
		self._setter_access_tracker["Flex154"] = {}
		self._Flex154 = Flex(new_state)

	@property
	def Flex155(self):
		self._getter_access_tracker["Flex155"] = {}
		return self._Flex155
	@Flex155.setter
	def Flex155(self, new_state):
		self._setter_access_tracker["Flex155"] = {}
		self._Flex155 = Flex(new_state)

	@property
	def TextBox139(self):
		self._getter_access_tracker["TextBox139"] = {}
		return self._TextBox139
	@TextBox139.setter
	def TextBox139(self, new_state):
		self._setter_access_tracker["TextBox139"] = {}
		self._TextBox139 = TextBox(new_state)

	@property
	def TextBox140(self):
		self._getter_access_tracker["TextBox140"] = {}
		return self._TextBox140
	@TextBox140.setter
	def TextBox140(self, new_state):
		self._setter_access_tracker["TextBox140"] = {}
		self._TextBox140 = TextBox(new_state)

	@property
	def Flex156(self):
		self._getter_access_tracker["Flex156"] = {}
		return self._Flex156
	@Flex156.setter
	def Flex156(self, new_state):
		self._setter_access_tracker["Flex156"] = {}
		self._Flex156 = Flex(new_state)

	@property
	def Flex157(self):
		self._getter_access_tracker["Flex157"] = {}
		return self._Flex157
	@Flex157.setter
	def Flex157(self, new_state):
		self._setter_access_tracker["Flex157"] = {}
		self._Flex157 = Flex(new_state)

	@property
	def Flex158(self):
		self._getter_access_tracker["Flex158"] = {}
		return self._Flex158
	@Flex158.setter
	def Flex158(self, new_state):
		self._setter_access_tracker["Flex158"] = {}
		self._Flex158 = Flex(new_state)

	@property
	def FramerFlex141(self):
		self._getter_access_tracker["FramerFlex141"] = {}
		return self._FramerFlex141
	@FramerFlex141.setter
	def FramerFlex141(self, new_state):
		self._setter_access_tracker["FramerFlex141"] = {}
		self._FramerFlex141 = FramerFlex(new_state)

	@property
	def TextBox141(self):
		self._getter_access_tracker["TextBox141"] = {}
		return self._TextBox141
	@TextBox141.setter
	def TextBox141(self, new_state):
		self._setter_access_tracker["TextBox141"] = {}
		self._TextBox141 = TextBox(new_state)

	@property
	def TextBox142(self):
		self._getter_access_tracker["TextBox142"] = {}
		return self._TextBox142
	@TextBox142.setter
	def TextBox142(self, new_state):
		self._setter_access_tracker["TextBox142"] = {}
		self._TextBox142 = TextBox(new_state)

	@property
	def TextBox143(self):
		self._getter_access_tracker["TextBox143"] = {}
		return self._TextBox143
	@TextBox143.setter
	def TextBox143(self, new_state):
		self._setter_access_tracker["TextBox143"] = {}
		self._TextBox143 = TextBox(new_state)

	@property
	def Flex159(self):
		self._getter_access_tracker["Flex159"] = {}
		return self._Flex159
	@Flex159.setter
	def Flex159(self, new_state):
		self._setter_access_tracker["Flex159"] = {}
		self._Flex159 = Flex(new_state)

	@property
	def TextBox144(self):
		self._getter_access_tracker["TextBox144"] = {}
		return self._TextBox144
	@TextBox144.setter
	def TextBox144(self, new_state):
		self._setter_access_tracker["TextBox144"] = {}
		self._TextBox144 = TextBox(new_state)

	@property
	def TextBox145(self):
		self._getter_access_tracker["TextBox145"] = {}
		return self._TextBox145
	@TextBox145.setter
	def TextBox145(self, new_state):
		self._setter_access_tracker["TextBox145"] = {}
		self._TextBox145 = TextBox(new_state)

	@property
	def Image62(self):
		self._getter_access_tracker["Image62"] = {}
		return self._Image62
	@Image62.setter
	def Image62(self, new_state):
		self._setter_access_tracker["Image62"] = {}
		self._Image62 = Image(new_state)

	@property
	def FramerFlex142(self):
		self._getter_access_tracker["FramerFlex142"] = {}
		return self._FramerFlex142
	@FramerFlex142.setter
	def FramerFlex142(self, new_state):
		self._setter_access_tracker["FramerFlex142"] = {}
		self._FramerFlex142 = FramerFlex(new_state)

	@property
	def Flex160(self):
		self._getter_access_tracker["Flex160"] = {}
		return self._Flex160
	@Flex160.setter
	def Flex160(self, new_state):
		self._setter_access_tracker["Flex160"] = {}
		self._Flex160 = Flex(new_state)

	@property
	def FramerFlex143(self):
		self._getter_access_tracker["FramerFlex143"] = {}
		return self._FramerFlex143
	@FramerFlex143.setter
	def FramerFlex143(self, new_state):
		self._setter_access_tracker["FramerFlex143"] = {}
		self._FramerFlex143 = FramerFlex(new_state)

	@property
	def Flex161(self):
		self._getter_access_tracker["Flex161"] = {}
		return self._Flex161
	@Flex161.setter
	def Flex161(self, new_state):
		self._setter_access_tracker["Flex161"] = {}
		self._Flex161 = Flex(new_state)

	@property
	def Flex162(self):
		self._getter_access_tracker["Flex162"] = {}
		return self._Flex162
	@Flex162.setter
	def Flex162(self, new_state):
		self._setter_access_tracker["Flex162"] = {}
		self._Flex162 = Flex(new_state)

	@property
	def Flex163(self):
		self._getter_access_tracker["Flex163"] = {}
		return self._Flex163
	@Flex163.setter
	def Flex163(self, new_state):
		self._setter_access_tracker["Flex163"] = {}
		self._Flex163 = Flex(new_state)

	@property
	def Flex164(self):
		self._getter_access_tracker["Flex164"] = {}
		return self._Flex164
	@Flex164.setter
	def Flex164(self, new_state):
		self._setter_access_tracker["Flex164"] = {}
		self._Flex164 = Flex(new_state)

	@property
	def Flex165(self):
		self._getter_access_tracker["Flex165"] = {}
		return self._Flex165
	@Flex165.setter
	def Flex165(self, new_state):
		self._setter_access_tracker["Flex165"] = {}
		self._Flex165 = Flex(new_state)

	@property
	def Image63(self):
		self._getter_access_tracker["Image63"] = {}
		return self._Image63
	@Image63.setter
	def Image63(self, new_state):
		self._setter_access_tracker["Image63"] = {}
		self._Image63 = Image(new_state)

	@property
	def Image64(self):
		self._getter_access_tracker["Image64"] = {}
		return self._Image64
	@Image64.setter
	def Image64(self, new_state):
		self._setter_access_tracker["Image64"] = {}
		self._Image64 = Image(new_state)

	@property
	def Image65(self):
		self._getter_access_tracker["Image65"] = {}
		return self._Image65
	@Image65.setter
	def Image65(self, new_state):
		self._setter_access_tracker["Image65"] = {}
		self._Image65 = Image(new_state)

	@property
	def Flex166(self):
		self._getter_access_tracker["Flex166"] = {}
		return self._Flex166
	@Flex166.setter
	def Flex166(self, new_state):
		self._setter_access_tracker["Flex166"] = {}
		self._Flex166 = Flex(new_state)

	@property
	def Flex167(self):
		self._getter_access_tracker["Flex167"] = {}
		return self._Flex167
	@Flex167.setter
	def Flex167(self, new_state):
		self._setter_access_tracker["Flex167"] = {}
		self._Flex167 = Flex(new_state)

	@property
	def TextBox146(self):
		self._getter_access_tracker["TextBox146"] = {}
		return self._TextBox146
	@TextBox146.setter
	def TextBox146(self, new_state):
		self._setter_access_tracker["TextBox146"] = {}
		self._TextBox146 = TextBox(new_state)

	@property
	def TextBox147(self):
		self._getter_access_tracker["TextBox147"] = {}
		return self._TextBox147
	@TextBox147.setter
	def TextBox147(self, new_state):
		self._setter_access_tracker["TextBox147"] = {}
		self._TextBox147 = TextBox(new_state)

	@property
	def Flex168(self):
		self._getter_access_tracker["Flex168"] = {}
		return self._Flex168
	@Flex168.setter
	def Flex168(self, new_state):
		self._setter_access_tracker["Flex168"] = {}
		self._Flex168 = Flex(new_state)

	@property
	def Flex169(self):
		self._getter_access_tracker["Flex169"] = {}
		return self._Flex169
	@Flex169.setter
	def Flex169(self, new_state):
		self._setter_access_tracker["Flex169"] = {}
		self._Flex169 = Flex(new_state)

	@property
	def TextBox148(self):
		self._getter_access_tracker["TextBox148"] = {}
		return self._TextBox148
	@TextBox148.setter
	def TextBox148(self, new_state):
		self._setter_access_tracker["TextBox148"] = {}
		self._TextBox148 = TextBox(new_state)

	@property
	def TextBox149(self):
		self._getter_access_tracker["TextBox149"] = {}
		return self._TextBox149
	@TextBox149.setter
	def TextBox149(self, new_state):
		self._setter_access_tracker["TextBox149"] = {}
		self._TextBox149 = TextBox(new_state)

	@property
	def Flex170(self):
		self._getter_access_tracker["Flex170"] = {}
		return self._Flex170
	@Flex170.setter
	def Flex170(self, new_state):
		self._setter_access_tracker["Flex170"] = {}
		self._Flex170 = Flex(new_state)

	@property
	def TextBox150(self):
		self._getter_access_tracker["TextBox150"] = {}
		return self._TextBox150
	@TextBox150.setter
	def TextBox150(self, new_state):
		self._setter_access_tracker["TextBox150"] = {}
		self._TextBox150 = TextBox(new_state)

	@property
	def TextBox151(self):
		self._getter_access_tracker["TextBox151"] = {}
		return self._TextBox151
	@TextBox151.setter
	def TextBox151(self, new_state):
		self._setter_access_tracker["TextBox151"] = {}
		self._TextBox151 = TextBox(new_state)

	@property
	def Image66(self):
		self._getter_access_tracker["Image66"] = {}
		return self._Image66
	@Image66.setter
	def Image66(self, new_state):
		self._setter_access_tracker["Image66"] = {}
		self._Image66 = Image(new_state)

	@property
	def Image67(self):
		self._getter_access_tracker["Image67"] = {}
		return self._Image67
	@Image67.setter
	def Image67(self, new_state):
		self._setter_access_tracker["Image67"] = {}
		self._Image67 = Image(new_state)

	@property
	def TextBox152(self):
		self._getter_access_tracker["TextBox152"] = {}
		return self._TextBox152
	@TextBox152.setter
	def TextBox152(self, new_state):
		self._setter_access_tracker["TextBox152"] = {}
		self._TextBox152 = TextBox(new_state)

	@property
	def TextBox153(self):
		self._getter_access_tracker["TextBox153"] = {}
		return self._TextBox153
	@TextBox153.setter
	def TextBox153(self, new_state):
		self._setter_access_tracker["TextBox153"] = {}
		self._TextBox153 = TextBox(new_state)

	@property
	def Image68(self):
		self._getter_access_tracker["Image68"] = {}
		return self._Image68
	@Image68.setter
	def Image68(self, new_state):
		self._setter_access_tracker["Image68"] = {}
		self._Image68 = Image(new_state)

	@property
	def Flex171(self):
		self._getter_access_tracker["Flex171"] = {}
		return self._Flex171
	@Flex171.setter
	def Flex171(self, new_state):
		self._setter_access_tracker["Flex171"] = {}
		self._Flex171 = Flex(new_state)

	@property
	def Flex172(self):
		self._getter_access_tracker["Flex172"] = {}
		return self._Flex172
	@Flex172.setter
	def Flex172(self, new_state):
		self._setter_access_tracker["Flex172"] = {}
		self._Flex172 = Flex(new_state)

	@property
	def Flex173(self):
		self._getter_access_tracker["Flex173"] = {}
		return self._Flex173
	@Flex173.setter
	def Flex173(self, new_state):
		self._setter_access_tracker["Flex173"] = {}
		self._Flex173 = Flex(new_state)

	@property
	def Flex174(self):
		self._getter_access_tracker["Flex174"] = {}
		return self._Flex174
	@Flex174.setter
	def Flex174(self, new_state):
		self._setter_access_tracker["Flex174"] = {}
		self._Flex174 = Flex(new_state)

	@property
	def Flex175(self):
		self._getter_access_tracker["Flex175"] = {}
		return self._Flex175
	@Flex175.setter
	def Flex175(self, new_state):
		self._setter_access_tracker["Flex175"] = {}
		self._Flex175 = Flex(new_state)

	@property
	def Flex176(self):
		self._getter_access_tracker["Flex176"] = {}
		return self._Flex176
	@Flex176.setter
	def Flex176(self, new_state):
		self._setter_access_tracker["Flex176"] = {}
		self._Flex176 = Flex(new_state)

	@property
	def Flex177(self):
		self._getter_access_tracker["Flex177"] = {}
		return self._Flex177
	@Flex177.setter
	def Flex177(self, new_state):
		self._setter_access_tracker["Flex177"] = {}
		self._Flex177 = Flex(new_state)

	@property
	def Image69(self):
		self._getter_access_tracker["Image69"] = {}
		return self._Image69
	@Image69.setter
	def Image69(self, new_state):
		self._setter_access_tracker["Image69"] = {}
		self._Image69 = Image(new_state)

	@property
	def Image70(self):
		self._getter_access_tracker["Image70"] = {}
		return self._Image70
	@Image70.setter
	def Image70(self, new_state):
		self._setter_access_tracker["Image70"] = {}
		self._Image70 = Image(new_state)

	@property
	def FramerFlex144(self):
		self._getter_access_tracker["FramerFlex144"] = {}
		return self._FramerFlex144
	@FramerFlex144.setter
	def FramerFlex144(self, new_state):
		self._setter_access_tracker["FramerFlex144"] = {}
		self._FramerFlex144 = FramerFlex(new_state)

	@property
	def FramerFlex145(self):
		self._getter_access_tracker["FramerFlex145"] = {}
		return self._FramerFlex145
	@FramerFlex145.setter
	def FramerFlex145(self, new_state):
		self._setter_access_tracker["FramerFlex145"] = {}
		self._FramerFlex145 = FramerFlex(new_state)

	@property
	def FramerFlex146(self):
		self._getter_access_tracker["FramerFlex146"] = {}
		return self._FramerFlex146
	@FramerFlex146.setter
	def FramerFlex146(self, new_state):
		self._setter_access_tracker["FramerFlex146"] = {}
		self._FramerFlex146 = FramerFlex(new_state)

	@property
	def FramerFlex147(self):
		self._getter_access_tracker["FramerFlex147"] = {}
		return self._FramerFlex147
	@FramerFlex147.setter
	def FramerFlex147(self, new_state):
		self._setter_access_tracker["FramerFlex147"] = {}
		self._FramerFlex147 = FramerFlex(new_state)

	@property
	def FramerFlex148(self):
		self._getter_access_tracker["FramerFlex148"] = {}
		return self._FramerFlex148
	@FramerFlex148.setter
	def FramerFlex148(self, new_state):
		self._setter_access_tracker["FramerFlex148"] = {}
		self._FramerFlex148 = FramerFlex(new_state)

	@property
	def FramerFlex149(self):
		self._getter_access_tracker["FramerFlex149"] = {}
		return self._FramerFlex149
	@FramerFlex149.setter
	def FramerFlex149(self, new_state):
		self._setter_access_tracker["FramerFlex149"] = {}
		self._FramerFlex149 = FramerFlex(new_state)

	@property
	def FramerFlex150(self):
		self._getter_access_tracker["FramerFlex150"] = {}
		return self._FramerFlex150
	@FramerFlex150.setter
	def FramerFlex150(self, new_state):
		self._setter_access_tracker["FramerFlex150"] = {}
		self._FramerFlex150 = FramerFlex(new_state)

	@property
	def FramerFlex151(self):
		self._getter_access_tracker["FramerFlex151"] = {}
		return self._FramerFlex151
	@FramerFlex151.setter
	def FramerFlex151(self, new_state):
		self._setter_access_tracker["FramerFlex151"] = {}
		self._FramerFlex151 = FramerFlex(new_state)
  
	def _to_json_fields(self):
		return {
			"Flex1": self._Flex1,
			"Flex2": self._Flex2,
			"Flex3": self._Flex3,
			"Image1": self._Image1,
			"Anchor2": self._Anchor2,
			"FramerText2": self._FramerText2,
			"FramerText3": self._FramerText3,
			"Anchor3": self._Anchor3,
			"FramerText4": self._FramerText4,
			"Anchor4": self._Anchor4,
			"FramerText5": self._FramerText5,
			"Anchor5": self._Anchor5,
			"FramerText6": self._FramerText6,
			"Anchor6": self._Anchor6,
			"Flex4": self._Flex4,
			"Flex5": self._Flex5,
			"Image2": self._Image2,
			"TextBox1": self._TextBox1,
			"Anchor7": self._Anchor7,
			"Flex6": self._Flex6,
			"Flex7": self._Flex7,
			"TextBox2": self._TextBox2,
			"TextBox4": self._TextBox4,
			"FramerFlex2": self._FramerFlex2,
			"FramerFlex3": self._FramerFlex3,
			"TextBox5": self._TextBox5,
			"FramerFlex4": self._FramerFlex4,
			"TextBox6": self._TextBox6,
			"Flex8": self._Flex8,
			"Flex9": self._Flex9,
			"FramerFlex5": self._FramerFlex5,
			"Image3": self._Image3,
			"FramerFlex6": self._FramerFlex6,
			"TextBox7": self._TextBox7,
			"TextBox8": self._TextBox8,
			"Image5": self._Image5,
			"Flex10": self._Flex10,
			"FramerFlex9": self._FramerFlex9,
			"Image6": self._Image6,
			"Image7": self._Image7,
			"Image8": self._Image8,
			"Image9": self._Image9,
			"Image10": self._Image10,
			"Image11": self._Image11,
			"Image12": self._Image12,
			"Image13": self._Image13,
			"Image14": self._Image14,
			"Image15": self._Image15,
			"TextBox10": self._TextBox10,
			"Flex11": self._Flex11,
			"Flex12": self._Flex12,
			"Flex13": self._Flex13,
			"FramerFlex10": self._FramerFlex10,
			"FramerFlex11": self._FramerFlex11,
			"TextBox11": self._TextBox11,
			"TextBox12": self._TextBox12,
			"TextBox13": self._TextBox13,
			"TextBox14": self._TextBox14,
			"TextBox15": self._TextBox15,
			"FramerFlex12": self._FramerFlex12,
			"FramerFlex13": self._FramerFlex13,
			"Flex14": self._Flex14,
			"Flex15": self._Flex15,
			"Flex16": self._Flex16,
			"FramerFlex14": self._FramerFlex14,
			"FramerFlex15": self._FramerFlex15,
			"Flex17": self._Flex17,
			"Flex18": self._Flex18,
			"TextBox16": self._TextBox16,
			"TextBox17": self._TextBox17,
			"TextBox18": self._TextBox18,
			"FramerFlex16": self._FramerFlex16,
			"FramerFlex17": self._FramerFlex17,
			"Flex19": self._Flex19,
			"FramerFlex18": self._FramerFlex18,
			"Image17": self._Image17,
			"Flex20": self._Flex20,
			"Flex21": self._Flex21,
			"Flex22": self._Flex22,
			"FramerFlex19": self._FramerFlex19,
			"Image18": self._Image18,
			"TextBox19": self._TextBox19,
			"TextBox20": self._TextBox20,
			"Image19": self._Image19,
			"FramerFlex20": self._FramerFlex20,
			"Image20": self._Image20,
			"TextBox21": self._TextBox21,
			"FramerFlex21": self._FramerFlex21,
			"Image21": self._Image21,
			"TextBox22": self._TextBox22,
			"FramerFlex22": self._FramerFlex22,
			"Flex23": self._Flex23,
			"TextBox23": self._TextBox23,
			"Image22": self._Image22,
			"TextBox24": self._TextBox24,
			"Image23": self._Image23,
			"Image24": self._Image24,
			"TextBox25": self._TextBox25,
			"TextBox26": self._TextBox26,
			"Image25": self._Image25,
			"TextBox27": self._TextBox27,
			"TextBox28": self._TextBox28,
			"FramerFlex23": self._FramerFlex23,
			"FramerFlex24": self._FramerFlex24,
			"FramerFlex25": self._FramerFlex25,
			"FramerFlex26": self._FramerFlex26,
			"TextBox29": self._TextBox29,
			"FramerFlex27": self._FramerFlex27,
			"FramerFlex28": self._FramerFlex28,
			"Flex24": self._Flex24,
			"Flex25": self._Flex25,
			"FramerFlex29": self._FramerFlex29,
			"Flex26": self._Flex26,
			"Image26": self._Image26,
			"Flex27": self._Flex27,
			"Flex28": self._Flex28,
			"Flex29": self._Flex29,
			"Flex30": self._Flex30,
			"Flex31": self._Flex31,
			"Flex32": self._Flex32,
			"Flex33": self._Flex33,
			"FramerFlex30": self._FramerFlex30,
			"FramerFlex31": self._FramerFlex31,
			"FramerFlex32": self._FramerFlex32,
			"FramerFlex33": self._FramerFlex33,
			"FramerFlex34": self._FramerFlex34,
			"FramerFlex35": self._FramerFlex35,
			"FramerFlex36": self._FramerFlex36,
			"FramerFlex37": self._FramerFlex37,
			"FramerFlex38": self._FramerFlex38,
			"Image27": self._Image27,
			"Flex34": self._Flex34,
			"Flex35": self._Flex35,
			"FramerFlex39": self._FramerFlex39,
			"FramerFlex40": self._FramerFlex40,
			"TextBox30": self._TextBox30,
			"TextBox31": self._TextBox31,
			"Flex36": self._Flex36,
			"Flex37": self._Flex37,
			"Flex38": self._Flex38,
			"Flex39": self._Flex39,
			"FramerFlex41": self._FramerFlex41,
			"FramerFlex42": self._FramerFlex42,
			"TextBox32": self._TextBox32,
			"TextBox33": self._TextBox33,
			"FramerFlex43": self._FramerFlex43,
			"Image28": self._Image28,
			"TextBox34": self._TextBox34,
			"TextBox35": self._TextBox35,
			"Image29": self._Image29,
			"FramerFlex44": self._FramerFlex44,
			"TextBox36": self._TextBox36,
			"Image30": self._Image30,
			"FramerFlex45": self._FramerFlex45,
			"Image31": self._Image31,
			"Image32": self._Image32,
			"Image33": self._Image33,
			"Flex40": self._Flex40,
			"Flex41": self._Flex41,
			"Flex42": self._Flex42,
			"Flex43": self._Flex43,
			"TextBox37": self._TextBox37,
			"Flex44": self._Flex44,
			"Flex45": self._Flex45,
			"Flex46": self._Flex46,
			"TextBox40": self._TextBox40,
			"TextBox41": self._TextBox41,
			"FramerFlex48": self._FramerFlex48,
			"FramerFlex49": self._FramerFlex49,
			"Flex47": self._Flex47,
			"Flex48": self._Flex48,
			"Flex49": self._Flex49,
			"Flex50": self._Flex50,
			"TextBox42": self._TextBox42,
			"Image34": self._Image34,
			"FramerFlex50": self._FramerFlex50,
			"Image35": self._Image35,
			"TextBox43": self._TextBox43,
			"FramerFlex51": self._FramerFlex51,
			"Image36": self._Image36,
			"TextBox44": self._TextBox44,
			"FramerFlex52": self._FramerFlex52,
			"Image37": self._Image37,
			"TextBox45": self._TextBox45,
			"FramerFlex53": self._FramerFlex53,
			"Image38": self._Image38,
			"TextBox46": self._TextBox46,
			"FramerFlex54": self._FramerFlex54,
			"Image39": self._Image39,
			"TextBox47": self._TextBox47,
			"FramerFlex55": self._FramerFlex55,
			"Image40": self._Image40,
			"TextBox48": self._TextBox48,
			"FramerFlex56": self._FramerFlex56,
			"Image41": self._Image41,
			"TextBox49": self._TextBox49,
			"FramerFlex57": self._FramerFlex57,
			"Flex51": self._Flex51,
			"Flex52": self._Flex52,
			"Flex53": self._Flex53,
			"TextBox50": self._TextBox50,
			"FramerFlex58": self._FramerFlex58,
			"TextBox51": self._TextBox51,
			"FramerFlex59": self._FramerFlex59,
			"Flex54": self._Flex54,
			"FramerFlex63": self._FramerFlex63,
			"Flex56": self._Flex56,
			"TextBox54": self._TextBox54,
			"TextBox56": self._TextBox56,
			"FramerFlex65": self._FramerFlex65,
			"TextBox57": self._TextBox57,
			"Flex57": self._Flex57,
			"FramerFlex66": self._FramerFlex66,
			"TextBox59": self._TextBox59,
			"Flex59": self._Flex59,
			"FramerFlex68": self._FramerFlex68,
			"TextBox60": self._TextBox60,
			"Flex60": self._Flex60,
			"FramerFlex69": self._FramerFlex69,
			"Image43": self._Image43,
			"Flex61": self._Flex61,
			"Flex62": self._Flex62,
			"Flex63": self._Flex63,
			"Flex64": self._Flex64,
			"Flex65": self._Flex65,
			"Flex66": self._Flex66,
			"Flex67": self._Flex67,
			"Flex101": self._Flex101,
			"Flex102": self._Flex102,
			"Flex103": self._Flex103,
			"Flex104": self._Flex104,
			"TextBox88": self._TextBox88,
			"TextBox89": self._TextBox89,
			"FramerFlex96": self._FramerFlex96,
			"FramerFlex97": self._FramerFlex97,
			"Flex105": self._Flex105,
			"TextBox90": self._TextBox90,
			"TextBox91": self._TextBox91,
			"FramerFlex98": self._FramerFlex98,
			"FramerFlex99": self._FramerFlex99,
			"Flex106": self._Flex106,
			"TextBox92": self._TextBox92,
			"TextBox93": self._TextBox93,
			"FramerFlex100": self._FramerFlex100,
			"FramerFlex101": self._FramerFlex101,
			"Flex107": self._Flex107,
			"TextBox94": self._TextBox94,
			"Flex108": self._Flex108,
			"TextBox95": self._TextBox95,
			"Input5": self._Input5,
			"FramerFlex102": self._FramerFlex102,
			"FramerFlex103": self._FramerFlex103,
			"Flex109": self._Flex109,
			"Flex110": self._Flex110,
			"Flex111": self._Flex111,
			"TextBox102": self._TextBox102,
			"Flex119": self._Flex119,
			"FramerFlex110": self._FramerFlex110,
			"Input6": self._Input6,
			"TextBox103": self._TextBox103,
			"Flex120": self._Flex120,
			"FramerFlex111": self._FramerFlex111,
			"Flex121": self._Flex121,
			"Flex122": self._Flex122,
			"TextBox104": self._TextBox104,
			"TextBox105": self._TextBox105,
			"FramerFlex112": self._FramerFlex112,
			"FramerFlex113": self._FramerFlex113,
			"Flex123": self._Flex123,
			"TextBox108": self._TextBox108,
			"TextBox109": self._TextBox109,
			"FramerFlex116": self._FramerFlex116,
			"FramerFlex117": self._FramerFlex117,
			"Flex125": self._Flex125,
			"Flex126": self._Flex126,
			"TextBox110": self._TextBox110,
			"TextBox111": self._TextBox111,
			"FramerFlex118": self._FramerFlex118,
			"FramerFlex119": self._FramerFlex119,
			"Flex127": self._Flex127,
			"Flex128": self._Flex128,
			"Flex130": self._Flex130,
			"Flex131": self._Flex131,
			"Flex132": self._Flex132,
			"Flex133": self._Flex133,
			"Flex134": self._Flex134,
			"TextBox114": self._TextBox114,
			"FramerFlex122": self._FramerFlex122,
			"TextBox115": self._TextBox115,
			"FramerFlex123": self._FramerFlex123,
			"TextBox116": self._TextBox116,
			"Image44": self._Image44,
			"FramerFlex124": self._FramerFlex124,
			"Flex135": self._Flex135,
			"Flex136": self._Flex136,
			"Flex137": self._Flex137,
			"Flex138": self._Flex138,
			"Div2": self._Div2,
			"Flex139": self._Flex139,
			"Image45": self._Image45,
			"TextBox117": self._TextBox117,
			"Flex140": self._Flex140,
			"Flex141": self._Flex141,
			"FramerFlex125": self._FramerFlex125,
			"TextBox118": self._TextBox118,
			"Anchor8": self._Anchor8,
			"FramerFlex126": self._FramerFlex126,
			"TextBox120": self._TextBox120,
			"FramerFlex127": self._FramerFlex127,
			"FramerFlex128": self._FramerFlex128,
			"Anchor9": self._Anchor9,
			"TextBox122": self._TextBox122,
			"FramerFlex129": self._FramerFlex129,
			"FramerFlex130": self._FramerFlex130,
			"Anchor10": self._Anchor10,
			"TextBox124": self._TextBox124,
			"TextBox125": self._TextBox125,
			"TextBox126": self._TextBox126,
			"FramerText7": self._FramerText7,
			"Anchor11": self._Anchor11,
			"FramerText8": self._FramerText8,
			"Anchor12": self._Anchor12,
			"FramerText9": self._FramerText9,
			"Anchor13": self._Anchor13,
			"FramerText10": self._FramerText10,
			"Anchor14": self._Anchor14,
			"TextBox127": self._TextBox127,
			"TextBox128": self._TextBox128,
			"TextBox129": self._TextBox129,
			"FramerFlex131": self._FramerFlex131,
			"TextBox130": self._TextBox130,
			"FramerFlex132": self._FramerFlex132,
			"TextBox131": self._TextBox131,
			"FramerFlex133": self._FramerFlex133,
			"TextBox132": self._TextBox132,
			"Anchor15": self._Anchor15,
			"FramerFlex134": self._FramerFlex134,
			"Anchor16": self._Anchor16,
			"FramerFlex135": self._FramerFlex135,
			"Anchor17": self._Anchor17,
			"FramerFlex136": self._FramerFlex136,
			"Flex142": self._Flex142,
			"Flex143": self._Flex143,
			"Flex144": self._Flex144,
			"Flex146": self._Flex146,
			"TextBox134": self._TextBox134,
			"Anchor18": self._Anchor18,
			"TextBox135": self._TextBox135,
			"Image46": self._Image46,
			"TextBox136": self._TextBox136,
			"Anchor19": self._Anchor19,
			"Anchor20": self._Anchor20,
			"Anchor21": self._Anchor21,
			"Anchor25": self._Anchor25,
			"FramerFlex138": self._FramerFlex138,
			"Image47": self._Image47,
			"Image48": self._Image48,
			"Image49": self._Image49,
			"Image50": self._Image50,
			"Image51": self._Image51,
			"Image52": self._Image52,
			"Image53": self._Image53,
			"Image54": self._Image54,
			"Image55": self._Image55,
			"Image56": self._Image56,
			"Flex148": self._Flex148,
			"Flex149": self._Flex149,
			"Image59": self._Image59,
			"Flex150": self._Flex150,
			"Flex151": self._Flex151,
			"Flex153": self._Flex153,
			"Image60": self._Image60,
			"FramerFlex140": self._FramerFlex140,
			"TextBox137": self._TextBox137,
			"Flex154": self._Flex154,
			"Flex155": self._Flex155,
			"TextBox139": self._TextBox139,
			"TextBox140": self._TextBox140,
			"Flex156": self._Flex156,
			"Flex157": self._Flex157,
			"Flex158": self._Flex158,
			"FramerFlex141": self._FramerFlex141,
			"TextBox141": self._TextBox141,
			"TextBox142": self._TextBox142,
			"TextBox143": self._TextBox143,
			"Flex159": self._Flex159,
			"TextBox144": self._TextBox144,
			"TextBox145": self._TextBox145,
			"Image62": self._Image62,
			"FramerFlex142": self._FramerFlex142,
			"Flex160": self._Flex160,
			"FramerFlex143": self._FramerFlex143,
			"Flex161": self._Flex161,
			"Flex162": self._Flex162,
			"Flex163": self._Flex163,
			"Flex164": self._Flex164,
			"Flex165": self._Flex165,
			"Image63": self._Image63,
			"Image64": self._Image64,
			"Image65": self._Image65,
			"Flex166": self._Flex166,
			"Flex167": self._Flex167,
			"TextBox146": self._TextBox146,
			"TextBox147": self._TextBox147,
			"Flex168": self._Flex168,
			"Flex169": self._Flex169,
			"TextBox148": self._TextBox148,
			"TextBox149": self._TextBox149,
			"Flex170": self._Flex170,
			"TextBox150": self._TextBox150,
			"TextBox151": self._TextBox151,
			"Image66": self._Image66,
			"Image67": self._Image67,
			"TextBox152": self._TextBox152,
			"TextBox153": self._TextBox153,
			"Image68": self._Image68,
			"Flex171": self._Flex171,
			"Flex172": self._Flex172,
			"Flex173": self._Flex173,
			"Flex174": self._Flex174,
			"Flex175": self._Flex175,
			"Flex176": self._Flex176,
			"Flex177": self._Flex177,
			"Image69": self._Image69,
			"Image70": self._Image70,
			"FramerFlex144": self._FramerFlex144,
			"FramerFlex145": self._FramerFlex145,
			"FramerFlex146": self._FramerFlex146,
			"FramerFlex147": self._FramerFlex147,
			"FramerFlex148": self._FramerFlex148,
			"FramerFlex149": self._FramerFlex149,
			"FramerFlex150": self._FramerFlex150,
			"FramerFlex151": self._FramerFlex151
			}
  