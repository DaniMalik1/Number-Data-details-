# ENCRYPTED by PY-ENCODE
# Created by Dani Malik (DANi)
# Facebook : http://facebook.com/Dani Malik
# Github : http://github.com/Dani Malik

import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
