# darkest

空格是可选的，妈的

# effect.darkest

任何.target "target" .riposte 1都必须有.riposte_validate false或true 不然加载崩溃

任何.skill_instant true 必须 .target "performer"

非应用buff的应用顺序：["skill_instant"="apply_with_result">skill>"">"queue"] ,skill 上排序

应用buff的应用顺序：["skill_instant">skill>"apply_with_result">"">"queue" ,skill 上排序

skill_instant会在结果preview上显示应用buff后的效果，但buff在skill之后就终止

valid_modes不能为空-阿比盖尔mod

-skipvalidation steam自带的参数

# rarities.trinkets.json

可能出现定义Ainsert_beforeB 在定义B前 详见NKCC_ The Festival of Light and Death和日落群岛 会导致出现这个饰品的时候崩溃
