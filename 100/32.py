# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re
pattern = r'http://(?:.*?\w)'
text = "88http://www.bai667du99.com55"

ll = re.findall(pattern,text)
print(ll)