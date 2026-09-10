from pathlib import Path

p = Path('src/components/Header.tsx')
s = p.read_text(encoding='utf-8-sig')
s = s.replace('className="h-8 md:h-10 shrink-0"', 'className="h-11 sm:h-12 md:h-10 lg:h-11 shrink-0"')
p.write_text(s, encoding='utf-8')
