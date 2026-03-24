import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

m = re.search(r'(<!-- ADMIN LOGIN MODAL -->.*?</p>\s*</div>)', idx, re.DOTALL)
if not m:
    print('Failed to find login modal in index.html')
    exit(1)

login_code = m.group(1)

pages_dir = 'pages'
for p in os.listdir(pages_dir):
    if not p.endswith('.html'): continue
    path = os.path.join(pages_dir, p)
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # In sub pages it might be <!-- LOGIN DRAWER --> or <!-- ADMIN LOGIN MODAL -->
    # We strip out whichever overlays block contains 'toggleLogin()'
    # Wait, better regex: find "<!-- LOGIN DRAWER -->" OR "<!-- ADMIN LOGIN MODAL -->" up until the NEXT overlay which is usually <!-- VIDEO MODAL --> or <!-- EVENT DETAIL PANEL -->
    new_con = re.sub(r'<!-- (?:LOGIN DRAWER|ADMIN LOGIN MODAL) -->.*?(?=<!-- (?:VIDEO MODAL|EVENT DETAIL PANEL|Navigation) -->)', login_code + '\n\n    ', content, flags=re.DOTALL)
    
    # fix the image path just for the pages/ directory
    # the logo is 'rccg-for-web.png' but in pages/ it should be '../rccg-for-web.png'
    # Currently login_code relies on logo in index.html which is 'rccg-for-web.png'
    local_login_code = login_code.replace('src="rccg-for-web.png"', 'src="../rccg-for-web.png"')
    
    new_con = re.sub(r'<!-- (?:LOGIN DRAWER|ADMIN LOGIN MODAL) -->.*?(?=<!-- (?:VIDEO MODAL|EVENT DETAIL PANEL|Navigation) -->)', local_login_code + '\n\n    ', content, flags=re.DOTALL)
    
    if new_con != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_con)
        print(f'Updated {p}')
    else:
        print(f'No changes in {p} (or regex missed)')
