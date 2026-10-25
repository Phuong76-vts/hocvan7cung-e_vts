# Ghép du-lieu.json vào mau.html để tạo index.html (một file, chạy offline).
import json, pathlib, sys
here = pathlib.Path(__file__).resolve().parent
d = json.loads((here/'du-lieu.json').read_text(encoding='utf-8'))
html = (here/'mau.html').read_text(encoding='utf-8')
assert '/*DATA*/' in html
data = json.dumps(d, ensure_ascii=False, separators=(',',':')).replace('</','<\\/')
out = here/(sys.argv[1] if len(sys.argv)>1 else 'index.html')
out.write_text(html.replace('/*DATA*/', data), encoding='utf-8')
print('Đã tạo', out, out.stat().st_size//1024, 'KB')
