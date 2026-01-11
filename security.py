# security.py

# IPs المسموحة (غيرها حسب جهازك)
ALLOWED_IPS = [
    "127.0.0.1",       # الجهاز نفسه
    "192.168.1.100"    # IP جهازك على الواي فاي
]

# مسارات مسموحة فقط
ALLOWED_PATHS = [
    "/",
    "/index.html"
]

# User-Agents ممنوعة
BLOCKED_AGENTS = [
    "python",
    "curl",
    "wget",
    "httpclient",
    "scanner"
]


def is_allowed(client_ip, path, user_agent):
    # تحقق من IP
    if client_ip not in ALLOWED_IPS:
        return False

    # تحقق من المسار
    if path not in ALLOWED_PATHS:
        return False

    # تحقق من User-Agent
    ua = user_agent.lower()
    for bad in BLOCKED_AGENTS:
        if bad in ua:
            return False

    return True