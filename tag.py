# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
import html5lib,shutil
import youtube_dl, pafy, asyncio
from gtts import gTTS
from googletrans import Translator
botStart = time.time()

#third
cl = LINE()
channelToken = cl.getChannelResult()
cl.log("TOKEN:" + str(cl.authToken))

print ("======THIRDz=====")
oepoll = OEPoll(cl)

settingsOpen = codecs.open("temp.json","r","utf-8")
preventsOpen = codecs.open("prevent.json","r","utf-8")

settings = json.load(settingsOpen)
prevents = json.load(preventsOpen)

clMID = cl.profile.mid
KAC=[cl]
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
admin=[clMID]
master=['u039d3e7645cdf9b119ae0bd765aec8db']
msg_dict = {}
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ REBOT ]")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=False, indent=4, ensure_ascii=True)
        backup = prevents
        f = codecs.open('prevent.json','w','utf-8')
        json.dump(backup, f, sort_keys=False, indent=4, ensure_ascii=True)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=False, indent=4, ensure_ascii=True)
        return False
    except Exception as error:
        logError(error)
        return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ ข้อผิดพลาด ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """⇛《รายการคำสั่ง》
⇛《Help》
⇛《Setread》《SR》ตั้งอ่าน
⇛《Lookread》《LR》อ่าน
⇛《Tagall》
⇛《URL On/Off》
⇛《Ginfo》
⇛《Gurl》
⇛《@bye》
⇛《Me》
⇛《Myname》
⇛《Mybio》
⇛《Mypicture》
⇛《Mycover》
⇛《Picture @》
⇛《Speed》
⇛《Runtime》
⇛《About》
⇛《Time》
⇛《Creator》
"""
    return helpMessage
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            ge = ("u039d3e7645cdf9b119ae0bd765aec8db")
            contact = cl.getContact(op.param1)
            print ("[ ADDNEWFRIEND ] เพิ่มชื่อเพื่อน: " + contact.displayName)
            cl.sendMessage(ge,"《การแจ้งเตือนเพื่อน \ nเพิ่มเพื่อน:" + contact.displayName + "\n》เพื่อนMid:\n" + op.param1)
            cl.findAndAddContactsByMid(op.param1)
            cl.sendMessage(op.param1, "สวัสดี{}~ยินดีที่ได้รู้จัก>///<".format(str(contact.displayName)))
            cl.sendMessage(op.param1, "โปรดไปที่หน้าแรกก่อนอ่านเพื่ออ่านคำแนะนำ")
            cl.sendMessage(op.param1, "↓↓หากมีคำถามอื่น ๆ คุณสามารถโฮสต์ส่วนตัวได้↓↓\n(ไม่ว่าคุณจะเพิ่มอะไรเจ้าของจะถูกปิดกั้นโดยเจ้าของ̇̇˙˙)")
            cl.sendContact(op.param1, "u039d3e7645cdf9b119ae0bd765aec8db")
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
        if op.type == 13:
            ge = ("u039d3e7645cdf9b119ae0bd765aec8db")
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[ JOIN ] ได้รับคำเชิญเป็นกลุ่ม: " + str(group.name) + "\nบุคคลที่ได้รับเชิญ: " + contact1.displayName + "\nบุคคลที่ได้รับเชิญ" + contact2.displayName)
            if settings["autoJoin"] == True:
                if op.param2 in settings['blacklist']:
                    if op.param3 in admin:
                        print ("[ BLACKJOIN ]การเชิญเข้าร่วมกลุ่มในรายการที่ไม่อนุญาต: " + str(group.name))
                        cl.sendMessage(ge, "《คำเชิญผู้ใช้คนเดียวของ Black》" + "\n》ชื่อกลุ่ม:" + str(group.name) + "\n》ชื่อผู้เชิญ:" + contact1.displayName + "\n》เชิญMID:\n" + op.param2 + "\n》ชื่อผู้รับเชิญ:" + contact2.displayName + "\n》ได้รับเชิญmid:\n" + op.param3)
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1, "《ผู้ใช้คนเดียวสีดำ》")
                        time.sleep(0.5)
                        cl.leaveGroup(op.param1)
                    else:
                        pass
                else:
                    if op.param3 in admin:
                        print ("[ NEWJOIN ]ผู้ใช้ที่ได้รับเชิญให้เข้าร่วมกลุ่ม: " + str(group.name))
                        cl.sendMessage(ge,"《คำเชิญผู้ใช้ทั่วไป》" + "\n》ชื่อกลุ่ม:" + str(group.name) + "\n》ชื่อผู้เชิญ:" + contact1.displayName + "\n》เชิญMID:\n" + op.param2 + "\n》ชื่อผู้รับเชิญ:" + contact2.displayName + "\n》ได้รับเชิญmid:\n" + op.param3)
                        cl.acceptGroupInvitation(op.param1)
                        time.sleep(0.5)
                        cl.sendMessage(op.param1,"《ผู้ใช้งาน " + contact1.displayName + " เชิญ》")
                    else:
                        pass
#--                    
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print(("[19] กลุ่มชื่อ: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid ))
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
                        cl.sendMessage(op.param1, "คนที่เตะ! ")
                        cl.sendContact(op.param1,op.param2)
                        time.sleep(0.1)
                        cl.sendMessage(op.param1, "คนถูกเตะ！")
                        cl.sendContact(op.param1,op.param3)
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    cl.sendMessage(op.param1, "คนที่เตะ! ")
                    cl.sendContact(op.param1,op.param2)
                    time.sleep(0.1)
                    cl.sendMessage(op.param1, "คนถูกเตะ！")
                    cl.sendContact(op.param1,op.param3)
                else:
                    pass
#--                         
        elif op.type == 19:
            ge = ("u039d3e7645cdf9b119ae0bd765aec8db")
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[ KICK ]มีคนเตะออกจากกลุ่มชื่อกลุ่ม: " + str(group.name) + "\n" + op.param1 +"\nคนเตะ: " + contact1.displayName + "\nMid: " + contact1.mid + "\nคนที่ถูกเตะ" + contact2.displayName + "\nMid:" + contact2.mid )
            cl.sendMessage(ge,"《เตะออกกลุ่ม》" + "\n》ชื่อกลุ่ม:" + str(group.name) +"\n》คนเตะ: " + contact1.displayName + "\n》Mid: " + contact1.mid + "\n》คนที่ถูกเตะ" + contact2.displayName + "\n》Mid: " + contact2.mid )
            try:
                if op.param3 not in admin or master:
                    arrData = ""
                    text = "%s " %('#')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param3}
                    arr.append(arrData)
                    text += mention + '⇛《《《《/'
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
            except:
                settings["blacklist"][op.param2] = True
                cl.sendMessage(op.param2, "《BLACK》\nขออภัยคุณละเมิดกฎ\nคุณอยู่ในบันชีรายชื่อบัญชีดำ\nไม่สามารถใช้ฟังก์ชันคำสั่งใด ๆ\nสำหรับรายละเอียดโปรดดูประกาศจากหน้าแรก")
                cl.sendMessage(ge, "《ประกาศดำ》" + "\n》ชื่อที่แสดง:" + contact1.displayName + "\n》ดำเดี่ยวMID:\n" + op.param2)
                print("《ประกาศดำ》" + "ชื่อที่แสดง:" + contact1.displayName + "》ดำเดี่ยวMID:" + op.param2)
        if op.type == 24:
            cl.leaveRoom(op.param1)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if sender in master:
                if "KICK " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in master:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif msg.text in ["SET"]:
                    try:
                        ret_ = "《ตั้งค่า》"
                        if settings["reread"] == True: ret_ += "\n⇛《reread 《เปิด》"
                        else: ret_ += "\n⇛《reread 《ปิด》"
                        if settings["autoJoin"] == True: ret_ += "\n⇛《autoJoin 《เปิด》"
                        else: ret_ += "\n⇛《autoJoin 《ปิด》"
                        if settings["autoLeave"] == True: ret_ += "\n⇛《autoLeave 《เปิด》"
                        else: ret_ += "\n⇛《autoLeave 《ปิด》"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif msg.text in ["REBOT"]:
                    cl.sendMessage(to, "《รีสตาร์ท~》")
                    restartBot()
                elif msg.text in ["AUTOJOIN On"]:
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "《ตั้งค่าสำเร็จ》")
                elif msg.text in ["AUTOJOIN Off"]:
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "《ตั้งค่าสำเร็จ》")
                elif msg.text in ["LEAVE On"]:
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "《ตั้งค่าสำเร็จ》")
                elif msg.text in ["LEAVE Off"]:
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "《ตั้งค่าสำเร็จ》")
                elif msg.text in ["REREAD On"]:
                    settings["reread"] = True
                    cl.sendMessage(to, "《ตั้งค่าสำเร็จ》")
                elif msg.text in ["REREAD Off"]:
                    settings["reread"] = False
                    cl.sendMessage(to, "《ตั้งค่าสำเร็จ》")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    cl.sendMessage(to, "《ตั้งค่าสำเร็จ》")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    cl.sendMessage(to, "《ตั้งค่าสำเร็จ》")                    
                elif text.lower() == 'gw on':
                    settings["group"] = True
                    cl.sendMessage(to, "《ตั้งค่าสำเร็จ》")					
                elif text.lower() == 'gw off':
                    settings["group"] = False
                    cl.sendMessage(to, "ปิดเเจ้งเเตือนของคุณเเล้ว ✘")                
                elif msg.text in ["Grl","grl","GRL"]:
                        groups = cl.groups
                        ret_ = "《กลุ่ม》"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n☆ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n《จำนวน {} กลุ่ม》".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif "JBLACK @" in msg.text:
                    if msg.toType == 2:
                        print ("[ JBAN ] ความสำเร็จ")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "《เข้าร่วมบัญชีดำ》")
                                    cl.sendMessage(target, "《BLACK》\nขออภัยคุณละเมิดกฎ\nด้วยเหตุนี้จึงถูกระบุว่าเป็นบัญชีดำ\nไม่สามารถใช้ฟังก์ชันคำสั่งใด ๆ\nสำหรับรายละเอียดโปรดดูประกาศจากหน้าแรก")
                                except:
                                    pass
                elif "JMBLACK " in msg.text:
                    mmid = msg.text.replace("JMBLACK ","")
                    print ("[ JMBAN ] ความสำเร็จ")
                    try:
                        settings["blacklist"][mmid] = True
                        cl.sendMessage(to, "《เข้าร่วมบัญชีดำ》")
                        cl.sendMessage(mmid, "《BLACK》\nขออภัยคุณละเมิดกฎ\nด้วยเหตุนี้จึงถูกระบุว่าเป็นบัญชีดำ\nไม่สามารถใช้ฟังก์ชันคำสั่งใด ๆ\nสำหรับรายละเอียดโปรดดูที่ประกาศหน้าแรก")
                    except:
                        pass                        
                elif "MBK " in msg.text:
                    mmid = msg.text.replace("MBK ","")
                    print ("[ JMBAN ] ความสำเร็จ")
                    try:
                        settings["blacklist"][mmid] = True
                        cl.sendMessage(to, "《เข้าร่วมบัญชีดำ》")
                    except:
                        pass
                elif msg.text in ["CLEAR BLACKLIST"]:
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "《ล้างรายการที่ไม่อนุญาต》")
                elif "UMBLACK " in msg.text:
                    mmid = msg.text.replace("UMBLACK ","")
                    print ("[ UMBAN ] ความสำเร็จ")
                    try:
                        del settings["blacklist"][mmid]
                        cl.sendMessage(to, "《ปิดบัญชีดำ》")
                        cl.sendMessage(mmid, "《UBLACK》\nปิดบัญชีดำ")
                    except:
                        pass
                elif "UBLACK @" in msg.text:
                    if msg.toType == 2:
                        print ("[ UBAN ] ความสำเร็จ")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "《ปิดรายการสีดำ》")
                                    cl.sendMessage(target, "《UBLACK》\nปิดรายการสีดำ")
                                except:
                                    pass
                elif msg.text in ["BLACKLIST"]:
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "《ไม่มีบัญชีดำ》")
                    else:
                        mc = "《รายการบัญชีดำ》"
                        for mi_d in settings["blacklist"]:
                            mc += "\n》" + cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)
                elif msg.text in ["BLACKMID"]:
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "《ไม่มีบัญชีดำ》")
                    else:
                        mc = "《รายการบัญชีดำ》"
                        for mi_d in settings["blacklist"]:
                            mc += "\n》" + mi_d
                        cl.sendMessage(to, mc)
                elif msg.text in ["KBLACK"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "《ไม่มีบัญชีดำ》")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "《ลบบัญชีดำแล้ว》")
                elif msg.text in ["KALLBLACK"]:
                    gid = cl.getGroupIdsJoined()
                    group = cl.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        cl.sendMessage(to, "《ไม่มีบัญชีดำ》")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                cl.kickoutFromGroup(i, [jj])
                            cl.sendMessage(i, "《นำผู้สมัครบัญชีดำกลุ่มทั้งหมดออก》")
                elif "Friendbc:" in msg.text:
                    bctxt = text.replace("Friendbc:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                elif "Groupsbc:" in msg.text:
                    bctxt = text.replace("Groupsbc:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "《MID》"
                        for ls in lists:
                            ret_ += "\n" + "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif "user " in msg.text:
                    mmid = msg.text.replace("user ","")
                    cl.sendContact(to, mmid)                    

#---
                elif "ยูทูป " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        cl.sendMessage(to, str(ret_))                    
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if not sender in settings['blacklist']:
                    if sender in prevents['limit']:
                        if msg.text in prevents['limit'][sender]['text']:
                            if prevents ['limit'][sender]['text'][msg.text] >= 3:
                                prevents ['limit'][sender]['text']['react'] = False
                            else:
                                prevents ['limit'][sender]['text'][msg.text] += 1
                                prevents ['limit'][sender]['text']['react'] = True
                        else:
                            try:
                                del prevents['limit'][sender]['text']
                            except:
                                pass
                            prevents['limit'][sender]['text'] = {}
                            prevents['limit'][sender]['text'][msg.text] = 1
                            prevents['limit'][sender]['text']['react'] = True
                    else:
                        prevents['limit'][sender] = {}
                        prevents['limit'][sender]['stick'] = {}
                        prevents['limit'][sender]['text'] = {}
                        prevents['limit'][sender]['text'][msg.text] = 1
                        prevents['limit'][sender]['text']['react'] = True
                    if sender not in master:
                        if prevents['limit'][sender]['text']['react'] == False:
                            return
                    if msg.text in ["help","Help","HELP"]:
                        helpMessage = helpmessage()
                        cl.sendMessage(to, str(helpMessage))
                    elif msg.text in ["Creator","creator"]:
                        cl.sendContact(to, "u039d3e7645cdf9b119ae0bd765aec8db")
                    elif text.lower() == '@bye':
                        if msg.toType == 2:
                            ge = ("u039d3e7645cdf9b119ae0bd765aec8db")
                            ginfo = cl.getGroup(to)
                            try:
                                cl.sendMessage(to,"هل الجميع لا يحب ليام؟ قاق")
                                time.sleep(1)
                                cl.leaveGroup(to)
                            except:
                                pass
                    elif text.lower() == 'runtime':
                        timeNow = time.time()
                        runtime = timeNow - botStart
                        runtime = format_timespan(runtime)
                        cl.sendMessage(to, "《เวลาทำงาน {}》".format(str(runtime)))
                    elif text.lower() == 'time':
                        tz = pytz.timezone("Asia/Bangkok")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = "《เวลาปัจจุบัน/GMT+7》\n" + timeNow.strftime('%Y') + "/" + bln + "/" + timeNow.strftime('%d') + "/\n" + hasil + "\n" + timeNow.strftime('%H:%M:%S')
                        cl.sendMessage(msg.to, readTime)
                    elif msg.text in ["SR","Setread"]:
                        cl.sendMessage(msg.to, "《ตั้งค่าตรวจจำนวนคนอ่าน》")
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        now2 = datetime.now()
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                        wait2['ROM'][msg.to] = {}
                    elif msg.text in ["LR","Lookread"]:
                        if msg.to in wait2['readPoint']:
                            if wait2["ROM"][msg.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in wait2["ROM"][msg.to].items():
                                    chiya += rom[1] + "\n"
                            cl.sendMessage(msg.to, "《คนที่อ่าน》%s\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
                        else:
                            cl.sendMessage(msg.to, "《ยังไม่มีการตั้งค่าคนอ่าน..พิมพ์   SR ¨》")
                    elif text.lower() == 'msgbomb':
                        bomb = (' ')
                        cl.sendContact(to, bomb)
                    elif text.lower() == 'me':
                        sendMessageWithMention(to, sender)
                        cl.sendContact(to, sender)
                    elif text.lower() == 'myname':
                        me = cl.getContact(sender)
                        cl.sendMessage(msg.to,"《ชื่อที่แสดง..》\n" + me.displayName)
                    elif text.lower() == 'mybio':
                        me = cl.getContact(sender)
                        cl.sendMessage(msg.to,"《สเตตัส..》\n" + me.statusMessage)
                    elif text.lower() == 'mypicture':
                        me = cl.getContact(sender)
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    elif text.lower() == 'myvideoprofile':
                        me = cl.getContact(sender)
                        cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                    elif text.lower() == 'mycover':
                        me = cl.getContact(sender)
                        cover = cl.getProfileCoverURL(sender)
                        cl.sendImageWithURL(msg.to, cover)
                    elif msg.text.lower().startswith("picture "):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                                cl.sendImageWithURL(msg.to, str(path))
                    elif msg.text in ["cancel","Cancel","CANCEL"]:
                        if msg.toType == 2:
                            X = cl.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = (contact.mid for contact in X.invitee)
                            ginfo = cl.getGroup(msg.to)
                            sinvitee = str(len(ginfo.invitee))
                            start = time.time()
                            for cancelmod in gInviMids:
                                cl.cancelGroupInvitation(msg.to, [cancelmod])
                            elapsed_time = time.time() - start
                            cl.sendMessage(to, "《คำเชิญทั้งหมดถูกยกเลิกแล้ว》" )
                        else:
                            cl.sendMessage(to, "《ไม่มีคำเชิญสามารถยกเลิกได้》")
                    elif msg.text in ["speed","Speed","SPEED"]:
                        time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                        str1 = str(time0)
                        start = time.time()
                        cl.sendMessage(to,'《ความเร็วในการประมวลผล》\n' + str1 + 'วินาที')
                        elapsed_time = time.time() - start
                        cl.sendMessage(to,'《การตอบสนองคำสั่ง》\n' + format(str(elapsed_time)) + 'วินาที')
                    elif msg.text in ["About","about","ABOUT"]:
                        try:
                            arr = []
                            owner = "u039d3e7645cdf9b119ae0bd765aec8db"
                            creator = cl.getContact(owner)
                            contact = cl.getContact(clMID)
                            grouplist = cl.getGroupIdsJoined()
                            contactlist = cl.getAllContactIds()
                            blockedlist = cl.getBlockedContactIds()
                            ret_ = "《เกี่ยวกับ》"
                            ret_ += "\nเวอร์ชั้น : v8.5"
                            ret_ += "\nชื่อ : {}".format(contact.displayName)
                            ret_ += "\nกลุ่ม : {}".format(str(len(grouplist)))
                            ret_ += "\nเพื่อน : {}".format(str(len(contactlist)))
                            cl.sendMessage(to, str(ret_))
                        except Exception as e:
                            cl.sendMessage(msg.to, str(e))
                    elif msg.text in ["Gurl","gurl","GURL"]:
                        if msg.toType == 2:
                            group = cl.getGroup(to)
                            if group.preventedJoinByTicket == False:
                                ticket = cl.reissueGroupTicket(to)
                                cl.sendMessage(to, "《URL ของกลุ่ม》\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                            else:
                                cl.sendMessage(to, "《URL ของกลุ่ม》\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                    elif msg.text in ["URL On"]:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.sendMessage(to, "《เปิดใช้ URL ของกลุ่มแล้ว》")
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                cl.sendMessage(to, "《เปิดกลุ่ม URL เรียบร้อยแล้ว》")
                    elif msg.text in ["URL Off"]:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == True:
                                cl.sendMessage(to, "《ปิด URL ของกลุ่มแล้ว》")
                            else:
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                cl.sendMessage(to, "《ปิด URL ของกลุ่มเรียบร้อยแล้ว》")
                    elif msg.text in ["Ginfo","ginfo","GINFO"]:
                        group = cl.getGroup(to)
                        try:
                            gCreator = group.creator.displayName
                        except:
                            gCreator = "ไม่พบ"
                        if group.invitee is None:
                            gPending = "0"
                        else:
                            gPending = str(len(group.invitee))
                        if group.preventedJoinByTicket == True:
                            gQr = "ใกล้"
                            gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                        else:
                            gQr = "เปิด"
                            gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                        path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        ret_ = "《ข้อมูลกลุ่ม》"
                        ret_ += "\nชื่อกลุ่ม : {}".format(str(group.name))
                        ret_ += "\nกลุ่มＩＤ : {}".format(group.id)
                        ret_ += "\nผู้สร้างกลุ่ม : {}".format(str(gCreator))
                        ret_ += "\nจำนวนสมาชิก : {}".format(str(len(group.members)))
                        ret_ += "\nจำนวนคำเชิญ : {}".format(gPending)
                        ret_ += "\nสถานะ URL : {}".format(gQr)
                        ret_ += "\nURL ของกลุ่ม : {}".format(gTicket)
                        cl.sendMessage(to, str(ret_))
                        cl.sendImageWithURL(to, path)
                    elif msg.text in ["Tagall","tagall","TAGALL"]:
                        group = cl.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        k = len(nama)//100
                        for a in range(k+1):
                            txt = u''
                            s=0
                            b=[]
                            for i in group.members[a*100 : (a+1)*100]:
                                b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                s += 7
                                txt += u'@Alin \n'
                            cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                            cl.sendMessage(to, "《รวม {} สมาชิก》".format(str(len(nama))))
#--  
                if msg.text in ["Me","me",".me",".Me","คท","/me"]:
                    cl.sendMessage(msg.to,"เชคทะมุยกลัวหลุดออ")
                if msg.text in ["sp","speed",".speed","/speed","Sp",".Speed"]:
                    cl.sendMessage(msg.to,"เร็วแรงไหมพี่")
                if msg.text in ["runtime","Runtime","/uptime","ออน",".uptime"]:
                    cl.sendMessage(msg.to,"นานยังๆ")							  
                if msg.text in [".มอง"]:
                    cl.sendMessage(msg.to,"มองไยยยย")	  
                if msg.text in ["555","5555","55555"]:
                    cl.sendMessage(msg.to,"ขำอะไรนักหนา-.-")                            
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
          if settings["group"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus			
            cl.sendMessage(op.param1, "Total Member Masuk「1」\nHaii" + "@"+ cl.getContact(op.param2).displayName + " \n╔══════════\n║🍒 ᶳᶤˡᵃʰᵏᵃᶰ ᶜᵉᵏ ᴺᵒᵗᵉ \n║🍒 ᶳᶤˡᵃʰᵏᵃᶰ ᴾᶤˡᶤʰ ᵀᵃʳᵍᵉᵗ ᵀᶤᵏᵘᶰᵍᵃᶰ \n║🍒 ᴰᶤˡᵃʳᵃᶰᵍ ᴷᵉʳᵃᶳ ᴮᵃᵖᵉʳ\n║🍒 ᶳᵃˡᵃᵐ ᴷᵉᶰᵃˡ ᴷᵃᵏᵃᵏ \n╚══════════\nNama grup :" + "👉" + str(ginfo.name) + "👈""")
            cl.sendContact(op.param1,op.param2)			
# ----------------- NOTIFED MEMBER OUT GROUP
        if op.type == 15:
          if settings['group'] == True:
            if op.param2 in admin:
                return
            cl.sendMessage(op.param1,"good Bye\n" + "@"+ cl.getContact(op.param2).displayName + "\nSee You Next Time . . . (p′︵‵。) 🤗")
            cl.sendContact(op.param1,op.param2)                
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"%s\n[Recovered\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)                            
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 16:
                try:
                    msg.contentType = 0
                    f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                    s_mid = f_mid[1].split("&")
                    mid = s_mid[0]
                    try:
                        arrData = ""
                        text = "%s " %("《ผู้เขียนบทความ》\n")
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':mid}
                        arr.append(arrData)
                        text += mention + "\n《ดูตัวอย่างบทความ》\n" + msg.contentMetadata["text"] + "\n《URL ของบทความ》\n " + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
                except: 
                    msg.contentType = 0
                    ret_ = "《ดูตัวอย่างบทความ》\n" + msg.contentMetadata["text"]
                    cl.sendMessage(msg.to, ret_)
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 60:
            if op.param2 in settings['blacklist']:
                cl.sendMessage(op.param1, "《！ผู้ใช้บัญชีดำเข้าร่วม！》")
            else:
                if op.param2 not in admin:
                    try:
                        arrData = ""
                        text = "%s " %('#')
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + 'ยินดีต้อนรับคุณเข้าร่วม~'
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error) 
        if op.type == 65:
            try:
                ge = ("u039d3e7645cdf9b119ae0bd765aec8db")
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_dict[msg_id]["from"] in settings["blacklist"]:
                        pass
                    else:
                        if msg_id in msg_dict:
                            if msg_dict[msg_id]["from"] not in bl:
                                print (msg_dict[msg_id]["from"])
                                arrData = ""
                                text = "%s " %("《Limousin เห็นใครบางคนนำข้อความกลับมา》\n")
                                arr = []
                                mention = "@x "
                                slen = str(len(text))
                                elen = str(len(text) + len(mention) - 1)
                                arrData = {'S':slen, 'E':elen, 'M':msg_dict[msg_id]["from"]}
                                arr.append(arrData)
                                text += mention + "\n" +msg_dict[msg_id]["text"]
                                cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                            del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☆" + Name
                        wait2['ROM'][op.param1][op.param2] = "☆" + Name
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
        