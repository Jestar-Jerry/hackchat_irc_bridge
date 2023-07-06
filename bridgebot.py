#!/mnt/disk/webpython/bin/python3

import ircbot
import hackchat
import _thread

irchost = "127.0.0.1"
ircport = 6668
ircchannel = "#en"
ircbotnick = "beidgetohackchati2p"
ircbotpass = ""
ircbotnickpass = ""


hcnick = "bridge"
hcchannel = "irc.ilita.i2p(en)"

ircbot = ircbot.bot_irc()
hcbot = hackchat.HackChat(hcnick,hcchannel)

# solve irc message

def irc_msg_slove(res):
    if "PRIVMSG" in res.split(" "):
        nick=res.split(":")[1].split("!")[0]
        msg=res.split(":",2)[2]
        print("irc>"+nick + " " + msg)
        return nick + ":" + msg

def irc_to_hc():
    # connect to the irc
    ircbot.connect_irc(irchost,ircport,ircbotnick,ircbotpass,ircbotnickpass)
                                                                         # respond to ping once before ircbot
    r = ircbot.response_irc()
    ircbot.join(ircchannel)

    # loop
    while True :
        r_irc = ircbot.response_irc()
        ircmsg=irc_msg_slove(r_irc)
        if ircmsg != None:
            hcbot.send_message(ircmsg)

def hc_to_irc(hcbot,msg,nick):
    print("hc>"+nick + " " + msg)
    ircbot.send_irc(ircchannel,nick+":"+msg)

if __name__ == "__main__":
    hcbot.on_message+=[hc_to_irc]
    hcbot.daemon()
    _thread.start_new_thread(irc_to_hc,())
