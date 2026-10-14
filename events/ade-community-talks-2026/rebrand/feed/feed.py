import re, os
import os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'
BASE='''
html, body { height: 1350px; }
.page { padding: 76px 64px 60px; }
.logos { bottom: 60px; padding-top: 22px; }
.lgroup { gap: 12px; }
.g1 { width: 640px; height: 640px; top: -240px; }
.g2 { bottom: -260px; }
'''
pages = {
 '00-invite-nusantara.html': ('00-invite.html', '''
.blank { height: 170px; margin-top: 30px; }
.facts > div { padding: 22px 0 24px; }
.date, .time, .venue { font-size: 30px; }
.who { line-height: 1.9; }
''', [('font-size:196px;line-height:.88','font-size:176px;line-height:.88'),
      ('class="lead" style="margin-top:48px"','class="lead" style="margin-top:30px"'),
      ('class="facts" style="margin-top:40px"','class="facts" style="margin-top:30px"'),
      ('class="label who" style="margin-top:34px"','class="label who" style="margin-top:24px"')]),
 '01-lineup-nusantara.html': ('01-lineup.html', '''
.grid { column-gap: 20px; row-gap: 20px; }
.grid .card { width: calc((100% - 40px) / 3); }
.card .ph { height: 196px; }
.card .nm { margin-top: 12px; font-size: 20px; }
.card .org { margin-top: 5px; font-size: 12px; }
.facts > div { padding: 18px 0 20px; }
.date, .time, .venue { font-size: 27px; }
.venue small { margin-top: 6px; font-size: 12px; }
.facts .v { margin-top: 8px; }
''', [('font-size:112px;line-height:.9;margin-top:20px','font-size:96px;line-height:.9;margin-top:16px'),
      ('font-size:64px;line-height:1;margin-top:14px','font-size:56px;line-height:1;margin-top:12px'),
      ('class="lead" style="margin-top:20px;font-size:28px"','class="lead" style="margin-top:16px;font-size:26px"'),
      ('class="facts" style="margin-top:44px"','class="facts" style="margin-top:32px"'),
      ('style="margin-top:38px;margin-bottom:20px">Speakers','style="margin-top:24px;margin-bottom:14px">Speakers')]),
 '02-topics-nusantara.html': ('02-topics.html', '''
.topic { padding: 26px 0 28px; grid-template-columns: 80px 1fr; }
.topic .no { padding-top: 6px; }
.topic .t { font-size: 30px; }
.topic .q { font-size: 24px; line-height: 1.35; margin-top: 8px; }
''', [('font-size:104px;line-height:.92;margin-top:0','font-size:96px;line-height:.92;margin-top:0'),
      ('class="lead" style="margin-top:22px"','class="lead" style="margin-top:14px;font-size:23px"'),
      ('style="margin-top:40px;border-top','style="margin-top:26px;border-top')]),
 '03-scene-amsterdam-nusantara.html': ('03-why.html', '''
.body { font-size: 34px; }
''', [('font-size:92px;line-height:.94','font-size:92px;line-height:.94'),
      ('class="body" style="margin-top:44px"','class="body" style="margin-top:36px"'),
      ('font-size:44px;font-weight:800;margin-top:60px','font-size:44px;font-weight:800;margin-top:56px')]),
 '04-days-amsterdam-B.html': ('04-days.html', '''
.body { font-size: 34px; }
''', [('font-size:86px;line-height:.96;margin-top:20px','font-size:86px;line-height:.96;margin-top:0'),
      ('class="body" style="margin-top:56px"','class="body" style="margin-top:40px"'),
      ('height:30px;vertical-align:-2px','height:30px;vertical-align:-3px'),
      ('font-size:44px;font-weight:800;margin-top:64px','font-size:44px;font-weight:800;margin-top:56px'),
      ('bottom:96px;padding-top:30px','bottom:60px;padding-top:24px')]),
}
for src,(dst,css,reps) in pages.items():
    s=open(R+src).read()
    s=s.replace('href="../modern.css"','href="../../modern.css"').replace('"../img/','"../../img/').replace('"../../../assets/','"../../../../assets/')
    for a,b in reps:
        assert s.count(a)==1,(src,a)
        s=s.replace(a,b)
    s=s.replace('</style></head>', BASE+css+'</style></head>',1)
    open(R+'feed/'+dst,'w').write(s)
print('ok')
