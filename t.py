import base64
import json
import requests

GITHUB_TOKEN = "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"
REPO_NAME = "truongphp/Gamevui"
BRANCH = "data"
FILE_PATH = "thu_vien.json"

# 23 tài khoản cần chèn
DATA_CAN_BAN = [
  {"name": "Khách_034226", "email": "nick136960@yahoo.com", "password": "TnBuib4ZL9@", "dns_link": "https://apple.nextdns.io/?profile=1fa4b5", "pid": "1fa4b5", "doh_link": "https://dns.nextdns.io/1fa4b5", "ip": "118.68.108.195", "created_at": "2026-11-03 03:42:26"},
  {"name": "nthw_08", "email": "alpha28101@outlook.com", "password": "TdCCYSGEO9@", "dns_link": "https://apple.nextdns.io/?profile=f55988", "pid": "f55988", "doh_link": "https://dns.nextdns.io/f55988", "ip": "2405:4802:18ab:c40::/64", "created_at": "2026-11-03 03:37:02"},
  {"name": "phong", "email": "long540845@yahoo.com", "password": "TJeDuMIsF9@", "dns_link": "https://apple.nextdns.io/?profile=927c51", "pid": "927c51", "doh_link": "https://dns.nextdns.io/927c51", "ip": "2a09:bac3:d329:2e1e::/64", "created_at": "2026-11-03 03:29:14"},
  {"name": "nmquan1610", "email": "alpha122219@gmail.com", "password": "T2hNa55pp9@", "dns_link": "https://apple.nextdns.io/?profile=aceb76", "pid": "aceb76", "doh_link": "https://dns.nextdns.io/aceb76", "ip": "2a09:bac2:d32b:263c::/64", "created_at": "2026-11-03 03:27:45"},
  {"name": "Nam", "email": "long917942@gmail.com", "password": "TBn0lqsjl9@", "dns_link": "https://apple.nextdns.io/?profile=5cfd23", "pid": "5cfd23", "doh_link": "https://dns.nextdns.io/5cfd23", "ip": "2405:4802:4981:abf0::/64", "created_at": "2026-11-03 03:18:18"},
  {"name": "h", "email": "tuan303738@gmail.com", "password": "TpGPVx7WA9@", "dns_link": "https://apple.nextdns.io/?profile=23cbff", "pid": "23cbff", "doh_link": "https://dns.nextdns.io/23cbff", "ip": "2a09:bac2:d34d:16d2::/64", "created_at": "2026-11-03 03:17:46"},
  {"name": "cn.cuowg", "email": "khoa943731@yahoo.com", "password": "TrGIFzSh89@", "dns_link": "https://apple.nextdns.io/?profile=577713", "pid": "577713", "doh_link": "https://dns.nextdns.io/577713", "ip": "2a09:bac3:d365:e6::/64", "created_at": "2026-11-03 03:16:06"},
  {"name": "Băng", "email": "minh449725@outlook.com", "password": "TTsPNm6xJ9@", "dns_link": "https://apple.nextdns.io/?profile=577546", "pid": "577546", "doh_link": "https://dns.nextdns.io/577546", "ip": "2a09:bac2:d356:16dc::/64", "created_at": "2026-11-03 03:04:48"},
  {"name": "Khách_025923", "email": "ryan852430@outlook.com", "password": "T85zrZcfi9@", "dns_link": "https://apple.nextdns.io/?profile=ceed8f", "pid": "ceed8f", "doh_link": "https://dns.nextdns.io/ceed8f", "ip": "2a09:bac2:d317:30c8::/64", "created_at": "2026-11-03 02:59:23"},
  {"name": "hoan", "email": "nam507512@icloud.com", "password": "TF2sQlZ9b9@", "dns_link": "https://apple.nextdns.io/?profile=7eca9a", "pid": "7eca9a", "doh_link": "https://dns.nextdns.io/7eca9a", "ip": "27.72.72.85", "created_at": "2026-11-03 02:53:17"},
  {"name": "Khách_025115", "email": "truong301617@outlook.com", "password": "Tj1NlaLq09@", "dns_link": "https://apple.nextdns.io/?profile=9376a1", "pid": "9376a1", "doh_link": "https://dns.nextdns.io/9376a1", "ip": "2401:d800:5141:5291::/64", "created_at": "2026-11-03 02:51:16"},
  {"name": "Tuyen", "email": "nick599408@outlook.com", "password": "T7MmqP1Hr9@", "dns_link": "https://apple.nextdns.io/?profile=f67932", "pid": "f67932", "doh_link": "https://dns.nextdns.io/f67932", "ip": "2401:d800:23d2:810::/64", "created_at": "2026-11-03 02:51:02"},
  {"name": "Đông", "email": "minh53872@yahoo.com", "password": "Tm7TeXUGR9@", "dns_link": "https://apple.nextdns.io/?profile=1ef771", "pid": "1ef771", "doh_link": "https://dns.nextdns.io/1ef771", "ip": "42.118.25.158", "created_at": "2026-11-03 02:46:03"},
  {"name": "https://locket.cam/coqhnad", "email": "david452066@yahoo.com", "password": "TB476DhU09@", "dns_link": "https://apple.nextdns.io/?profile=5a2478", "pid": "5a2478", "doh_link": "https://dns.nextdns.io/5a2478", "ip": "2a09:bac2:d355:15f::/64", "created_at": "2026-11-03 02:29:12"},
  {"name": "Thắng", "email": "khoa57739@icloud.com", "password": "T0FmwQUut9@", "dns_link": "https://apple.nextdns.io/?profile=797f35", "pid": "797f35", "doh_link": "https://dns.nextdns.io/797f35", "ip": "2a09:bac3:d4c5:2e1e::/64", "created_at": "2026-11-03 02:24:11"},
  {"name": "Đức", "email": "daniel554676@outlook.com", "password": "TY3KtNPry9@", "dns_link": "https://apple.nextdns.io/?profile=544ded", "pid": "544ded", "doh_link": "https://dns.nextdns.io/544ded", "ip": "2a09:bac3:d4c3:263c::/64", "created_at": "2026-11-03 02:21:02"},
  {"name": "Bảo", "email": "ryan745086@gmail.com", "password": "TNcIssdfA9@", "dns_link": "https://apple.nextdns.io/?profile=3f5e1d", "pid": "3f5e1d", "doh_link": "https://dns.nextdns.io/3f5e1d", "ip": "2a09:bac3:d351:2e1e::/64", "created_at": "2026-11-03 02:14:38"},
  {"name": "khôi", "email": "david896164@gmail.com", "password": "TsLOOKHZy9@", "dns_link": "https://apple.nextdns.io/?profile=5a5ed4", "pid": "5a5ed4", "doh_link": "https://dns.nextdns.io/5a5ed4", "ip": "14.168.17.66", "created_at": "2026-11-03 02:09:29"},
  {"name": "HPN", "email": "khoa391660@gmail.com", "password": "ThgrquRrG9@", "dns_link": "https://apple.nextdns.io/?profile=c22bdb", "pid": "c22bdb", "doh_link": "https://dns.nextdns.io/c22bdb", "ip": "2a09:bac2:d4c4:263c::/64", "created_at": "2026-11-03 01:51:32"},
  {"name": "duy", "email": "david753298@gmail.com", "password": "T035Kg6M79@", "dns_link": "https://apple.nextdns.io/?profile=a8f34c", "pid": "a8f34c", "doh_link": "https://dns.nextdns.io/a8f34c", "ip": "2a09:bac2:d314:16d2::/64", "created_at": "2026-11-03 01:50:00"},
  {"name": "HPN", "email": "daniel324089@gmail.com", "password": "Tm5IDYV9f9@", "dns_link": "https://apple.nextdns.io/?profile=dc6d5e", "pid": "dc6d5e", "doh_link": "https://dns.nextdns.io/dc6d5e", "ip": "2402:800:61c7:3f63::/64", "created_at": "2026-11-03 01:48:04"},
  {"name": "Đăng", "email": "long880871@icloud.com", "password": "THEmooiW29@", "dns_link": "https://apple.nextdns.io/?profile=f39e84", "pid": "f39e84", "doh_link": "https://dns.nextdns.io/f39e84", "ip": "113.185.41.152", "created_at": "2026-11-03 01:47:27"},
  {"name": "khải", "email": "daniel863346@outlook.com", "password": "T2MhaXs309@", "dns_link": "https://apple.nextdns.io/?profile=45d7ba", "pid": "45d7ba", "doh_link": "https://dns.nextdns.io/45d7ba", "ip": "2401:d800:590c:ac2d::/64", "created_at": "2026-11-03 01:47:19"}
]

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# 1. Tải dữ liệu live từ GitHub
url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}?ref={BRANCH}"
res = requests.get(url, headers=headers)
file_info = res.json()
sha = file_info["sha"]
live_data = json.loads(base64.b64decode(file_info["content"]).decode("utf-8"))

# 2. Tự động tính STT tiếp theo
existing_pids = {item["pid"] for item in live_data if "pid" in item}
current_stt = max([item.get("stt", 0) for item in live_data], default=0)

added = 0
for row in DATA_CAN_BAN:
    if row["pid"] not in existing_pids:
        current_stt += 1
        item = {"stt": current_stt}
        item.update(row)
        live_data.append(item)
        existing_pids.add(row["pid"])
        added += 1

# 3. Đẩy lên GitHub
payload = {
    "message": f"Chèn {added} tài khoản mới",
    "content": base64.b64encode(json.dumps(live_data, ensure_ascii=False, indent=2).encode("utf-8")).decode("utf-8"),
    "sha": sha,
    "branch": BRANCH
}

resp = requests.put(url, headers=headers, json=payload)
if resp.status_code in [200, 201]:
    print(f"✅ ĐÃ BẮN THÀNH CÔNG {added} TÀI KHOẢN VÀO THƯ VIỆN!")
    print(f"Tổng tài khoản hiện tại: {len(live_data)}")
else:
    print("❌ Thất bại:", resp.text)
