import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# We extract everything between <!-- ADMIN LOGIN MODAL --> and the next component (<!-- EVENT DETAIL PANEL -->)
# This guarantees we pick up the absolute final closing </div>.
m = re.search(r'(<!-- ADMIN LOGIN MODAL -->.*?(?=<!-- EVENT DETAIL PANEL -->))', idx, re.DOTALL)
if not m:
    print('Failed to safely extract the login modal from index.html')
    exit(1)

login_code = m.group(1).rstrip() # rstrip to control exactly where spacing starts

pages_dir = 'pages'
success_count = 0
for p in os.listdir(pages_dir):
    if not p.endswith('.html'): continue
    path = os.path.join(pages_dir, p)
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Switch the logo path to be relative to pages/
    local_login_code = login_code.replace('src="rccg-for-web.png"', 'src="../rccg-for-web.png"')
    
    # Overwrite the damaged modal
    # We look for the start, and stop perfectly before the next block
    new_con = re.sub(r'<!-- ADMIN LOGIN MODAL -->.*?(?=<!-- (?:VIDEO MODAL|EVENT DETAIL PANEL|Navigation) -->)', local_login_code + '\n\n    ', content, flags=re.DOTALL)
    
    if new_con != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_con)
        success_count += 1
        print(f'Repaired {p}')
        
print(f'All {success_count} pages successfully processed and restored.')
