# This Python file uses the following encoding: utf-8
from enum import Enum, auto
class gametoken(Enum):
    GIVE_ROLES = auto()
    ENTER_NIGHT = auto() 

class role_wrapper:
    def __init__(self,*,name,aura,team,description):
        self.team = team
        self.aura = aura
        self.description = description
        self.name = name
class teams:
    VILLAGE = auto()
    WEREWOLF = auto()
    THIRD_PARTY = auto()

class auras:
    GOOD = auto()
    BAD = auto()
    UNKNOWN = auto()
class roles(Enum):
    狼王 = role_wrapper(name = "狼王",aura = auras.BAD,team=teams.WEREWOLF,description='''被殺死時,可以帶多一個人(除左被毒)\n只可以喺自己發言階段自爆''')
    白狼王 = role_wrapper(name = "白狼王",aura = auras.BAD,team=teams.WEREWOLF,description='''在白天死亡,可以帶多一個人\n可以喺任何人發言階段自爆\n只限自爆先可以帶人\n''')
    黑狼王 = role_wrapper(name = "黑狼王",aura = auras.BAD,team=teams.WEREWOLF,description='''喺夜晚死亡,可以帶多一個人(唔怕女巫毒殺)\n唔可以自爆''')
    雪狼 = role_wrapper(name = "雪狼",aura = auras.GOOD,team=teams.WEREWOLF,description='''被查驗嘅時候,會顯示好人''')
    惡靈騎士 = role_wrapper(name = "惡靈騎士",aura = auras.BAD,team=teams.WEREWOLF,description='''唔會死喺夜晚''')
    驅魔屠夫 = role_wrapper(name = "驅魔屠夫",aura = auras.BAD,team=teams.WEREWOLF,description='''唔會死喺日頭\n(免死投票只限一次)''')
    狼美人 = role_wrapper(name = "狼美人",aura = auras.BAD,team=teams.WEREWOLF,description='''可以禁用一個角色嘅技能(每晚)(時限一晚)''')
    石像鬼 = role_wrapper(name = "石像鬼",aura = auras.BAD,team=teams.WEREWOLF,description='''唔會同同伴相認\n可以查驗一個人嘅真實身份''')
    血月師徒 = role_wrapper(name = "血月師徒",aura = auras.BAD,team=teams.WEREWOLF,description='''可以喺任何發言階段自爆\n自爆嘅時候,直接入血月\n血月-只有狼人可以殺人,其他神職人員全部禁用技能''')
    魅魔 = role_wrapper(name = "魅魔",aura = auras.BAD,team=teams.WEREWOLF,description='''可以迷惑一個人\n如果魅魔死,被迷惑嘅人會殉情(每一個回合重新選擇一個)''')
    惡魔 = role_wrapper(name = "惡魔",aura = auras.BAD,team=teams.WEREWOLF,description='''可以知道狼人殺死嘅人是否神職,可以相認\n(全神用唔到)\n\n全神局可以知道殺死嘅人嘅真實身份,唔可以同隊友相認''')
    睡狼 = role_wrapper(name = "睡狼",aura = auras.BAD,team=teams.WEREWOLF,description='''佢唔知狼人係邊個\n狼人們知道佢''')
    狐仙 = role_wrapper(name = "狐仙",aura = auras.BAD,team=teams.WEREWOLF,description='''可以選擇一個人,如果白天被投票所殺\n可以喺投票者內選擇殺多一個\n例如狐仙選擇1號,而1被234投死,狐仙可以喺234揀一個殺''')
    電光人 = role_wrapper(name = "電光人",aura = auras.BAD,team=teams.WEREWOLF,description='''所以投電光人嘅人都會被封技能\n(包括狼人)''')
    綁匪 = role_wrapper(name = "綁匪",aura = auras.BAD,team=teams.WEREWOLF,description='''可以選擇一個人作為人質\n當綁匪被查身份時,佢會撕票''')
    豺狼 = role_wrapper(name ="豺狼",aura = auras.BAD,team=teams.WEREWOLF,description='''可以將一個人嘅身份變成狼人(每晚一次)\n開局嘅時候得豺狼一個''')
    狼巫婆 = role_wrapper(name = "狼巫婆",aura = auras.BAD,team=teams.WEREWOLF,description='''死後會干擾下一回合嘅查驗結果''')
    黑蝙蝠 = role_wrapper(aura = auras.BAD,team=teams.WEREWOLF,description='''可以用兩次盾\n盾嘅功能係如果神職人員用技能喺你身上,會令到佢嘅技能用係自己身上(魔術師優先度高啲)\n例如你比盾A,當A比人查嘅時候,會顯示查人果個身份\n如果女巫毒A,女巫死''')
    混沌惡魔 = role_wrapper(name = "混沌惡魔",aura = auras.BAD,team=teams.WEREWOLF,description='''邪惡陣營嘅魔術師\n可以交換兩個人嘅死亡結果\n例如搞完一大輪野之後,白天A死咗,如果佢將A同B交換,咁就係B死,包括投票階段都會交換''')
    河豚 = role_wrapper(name = "河豚",aura = auras.BAD,team=teams.WEREWOLF,description='''當河豚被投票所殺時,會發到技能,佢會殺曬個輪投河豚嘅人''')
    勾魂使者 = role_wrapper(name = "勾魂使者",aura = auras.BAD,team=teams.WEREWOLF,description='''死後可以封左右兩位技能''')
    狼兄 = role_wrapper(name = "狼兄",aura = auras.BAD,team=teams.WEREWOLF,description='''首夜,狼兄和狼弟優先睜眼確認彼此身份。\n狼弟閉眼後,狼兄再與其他狼人玩家一同睜眼執行狼刀,而狼弟不入狼窩。\n狼人和狼弟同刀(選擇擊殺同一名玩家)則女巫解藥和守衛守護不能救活被殺的玩家；\n由於狼弟不知道其餘狼隊友的身份,覺醒夜有可能殺死狼隊友；\n若狼兄後於其餘狼人玩家被淘汰,覺醒夜當晚狼弟仍然只有覺醒刀,不會因此提前執行狼刀,狼隊視為空刀。''')
    狼弟 = role_wrapper(name = "狼弟",aura = auras.BAD,team=teams.WEREWOLF,description='''首夜,狼兄和狼弟優先睜眼確認彼此身份。\n狼弟閉眼後,狼兄再與其他狼人玩家一同睜眼執行狼刀,而狼弟不入狼窩。\n•狼弟-狼兄被淘汰前,狼弟被預言家查驗為好人。\n•狼弟-狼兄被淘汰後的第一個晚上,狼弟覺醒,單獨睜眼額外擊殺一人,覺醒刀必須執行,不能選擇空刀。\n•狼弟-覺醒的狼弟被預言家查驗為狼人。狼弟在覺醒夜之後的下一個晚上起入狼窩(覺醒當夜仍未入狼窩),與其餘狼人玩家一同睜眼執行狼刀。\n\n狼人和狼弟同刀(選擇擊殺同一名玩家)則女巫解藥和守衛守護不能救活被殺的玩家；\n由於狼弟不知道其餘狼隊友的身份,覺醒夜有可能殺死狼隊友；\n若狼兄後於其餘狼人玩家被淘汰,覺醒夜當晚狼弟仍然只有覺醒刀,不會因此提前執行狼刀,狼隊視為空刀。''')
    約束者 = role_wrapper(name = "約束者",aura = auras.BAD, team=teams.WEREWOLF, description='''可以鎖一個人\n唔同狼隊見面\n鎖鏈-受到傷害×2\n如果有(2個盾/2個救/1個盾+1個救)係可以救番''')
    天狗 = role_wrapper(name = "天狗", aura = auras.BAD, team = teams.WEREWOLF, description='''與你投票相同嘅人,全部被封技能\n如果你投A,喺夜晚其他投A嘅人技能被封''')
    半天狗 = role_wrapper(name = "半天狗", aura= auras.BAD, team = teams.WEREWOLF, description='''揀1個與你投票相同嘅人,被封技能\n如果(你、B、C、D)投A,喺夜晚你可以喺B、C、D揀一個,被封技能''')
    預言家 = role_wrapper(name = "預言家", aura= auras.GOOD, teams = teams.VILLAGE, description='''可以查一個人嘅身份係好定壞''')
    通靈師 = role_wrapper(name = "通靈師", aura= auras.GOOD, teams = teams.VILLAGE, description='''可以知道一個人嘅真實職業\n(石像鬼在場,先可以用)''')
    熊 = role_wrapper(name = "熊",aura = auras.GOOD, team = teams.VILLAGE, description='''每次天光MC都要講“熊有叫or熊無叫"\n“熊有叫"代表熊(左右/上下)個兩位有狼\n“熊無叫"代表熊(左右/上下)個兩位無狼''')
    睇相佬 = role_wrapper(name = "睇相佬", aura = auras.GOOD, team = teams.VILLAGE, description='''可以選擇坐位連著3個人查驗（淨係會話俾你聽有狼or無狼（喺嗰3個人內）\n-如果無狼，睇相佬就會無技能\n-一定要查到有狼先可以繼續用技能''')
    騎士 = role_wrapper(name = "騎士", aura = auras.GOOD, team = teams.VILLAGE, description='''喺發言階段可以同人決鬥''')
    午夜騎士 = role_wrapper(name = "午夜騎士", aura = auras.GOOD, team = teams.VILLAGE, description='''會同你所投票嘅人決鬥喺夜晚\n（小心投票）''')
    狩魔人 = role_wrapper(name = "狩魔人", aura = auras.GOOD, team= teams.VILLAGE, description='''喺夜晚可以選擇一人決鬥\n唔怕毒藥''')
    