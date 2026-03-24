import os

pages_dir = 'pages'
success_count = 0

for p in os.listdir(pages_dir):
    if not p.endswith('.html'): continue
    
    path = os.path.join(pages_dir, p)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The primary RCCG logo is strictly in the root directory. Subpages need the ../ prefix.
    # The login modal was already fixed in the previous script, but the nav and footer were missed.
    new_con = content.replace('src="rccg-for-web.png"', 'src="../rccg-for-web.png"')
    
    if new_con != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_con)
        success_count += 1
        print(f"Fixed logos in {p}")

print(f"Total pages updated with correct logo relative paths: {success_count}")
