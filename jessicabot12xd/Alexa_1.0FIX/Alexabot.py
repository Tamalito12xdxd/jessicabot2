import os
import random
from os import system
import urllib
system("pip install --upgrade  amino.fix")
system("pip install gtts")
system("pip install requests")
import aminofix as amino
import time
from gtts import gTTS
import requests
from uuid import uuid4
client=amino.Client()
os.system("clear")
print("\t\033[1;32m JESSICA  \033[1;36m Comunidad bot \n\n   Iniciando bot \n \n")
email="Multicuenta225xdxd@hotmail.com"
password="Muerte"

client.login(email=email,password=password)

cid="1138677"
cidy=1138677

adm=[]
self=client.socket
def generate_transaction_id(self):
        return str(uuid4())
transaction=generate_transaction_id(self)

admx=["http://aminoapps.com/p/Rad"]

client.join_community(cid)
for i in admx:
	try:
		w=client.get_from_code(i).objectId
		adm.append(w)
	except:
		print("Invalid link")
subclient=amino.SubClient(comId=cid,profile=client.profile)
msg="""🌻⃟꙲꙰ཱྀ༆̸̳ꇙ𝗶𝗴𝗮𝗻 𝗹𝗮𝘀 𝗿𝗲𝗴𝗹𝗮𝘀♥︎︫୭𖤐
1.ɴᴏ ꜱᴘᴀᴍ
2.ʀᴇꜱᴘᴇᴛᴀʀ ᴀ ʟᴏꜱ ʟɪᴅᴇʀᴇꜱ ʏ ᴄᴜʀᴀᴅᴏʀᴇꜱ, ᴀʟ ɪɢᴜᴀʟ Qᴜᴇ ʟᴏꜱ ᴀɴꜰɪᴛʀɪᴏɴᴇꜱ ᴅᴇ ʟᴏꜱ ᴄʜᴀᴛꜱ
3.ᴄᴀᴅᴀ ᴄʜᴀᴛ ᴛɪᴇɴᴇ ʀᴇɢʟᴀꜱ ᴇꜱᴛᴀʙʟᴇᴄɪᴅᴀꜱ ᴀꜱɪ Qᴜᴇ ʀᴇꜱᴘᴇᴛᴀ ᴄᴀᴅᴀ ᴜɴᴀ ᴅᴇ ᴇʟʟᴀꜱ
4.ᴅɪᴠɪᴇʀᴛᴇᴛᴇ ᴇɴ ᴛᴏᴅᴏ, ʏ ʀᴇᴄᴜᴇʀᴅᴀ, ᴛᴀᴋᴜᴍɪ ᴇꜱ ꜱᴇxʏ"""
print("Bot joined community")
subclient=amino.SubClient(comId=cid,profile=client.profile)
print("Joining All chatrooms")
subclient=amino.SubClient(comId=cid,profile=client.profile)
print("Alexa 1.0 Ready")
l=[]
lis = ["Es cierto",
    "Es decididamente así",
    "Sin duda",
    "Sí definitivamente",
    "Puedes confiar en ello",
    "Como yo lo veo, sí",
    "Más probable",
    "Perspectivas buena",
    "Sí",
    "Las señales apuntan a que sí",
    "Respuesta confusa, intenta otra vez",
    "Pregunta de nuevo más tarde",
    "Mejor no decirte ahora",
    "No se puede predecir ahora",
    "Concéntrate y pregunta otra vez",
    "No cuentes con eso",
    "Mi respuesta es no",
    "Mis fuentes dicen que no",
    "Perspectivas no tan buenas",
    "Muy dudoso",
    "Si", 
    "No", 
    "Probablemente", 
    "100 %",
    "no estoy seguro",
    "Mi madre es princess",
    "Mi padre es Takumi",
    "Quiero cogerte",
    "Quiero que me des un beso"]

@client.event("on_group_member_join")
def on_group_member_join(data):
	if data.comId==cidy:
		try:
			x=data.message.author.icon
			response=requests.get(f"{x}")
			file=open("sample.png","wb")
			file.write(response.content)
			file.close()
			img=open("sample.png","rb")
			subclient.send_message(chatId=data.message.chatId,message=f"""
[C]━━━━━━━━━━━━━━━
[c]Welcome <${data.message.author.nickname}$>
[C]━━━━━━━━━━━━━━━
{msg}
[C]━━━━━━━━━━━━━━━""",embedId=data.message.author.userId,embedTitle=data.message.author.nickname,embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}",embedImage=img,mentionUserIds=[data.message.author.userId])
			print(f"\nwelcomed {data.message.author.nickname} to gc ")
		except Exception as e:
			print(e)
				
@client.event("on_group_member_leave")
def on_group_member_leave(data):
	if data.comId==cidy:
		try:
			subclient.send_message(chatId=data.message.chatId,message="""[CI]ɴᴏ ᴠᴜᴇʟᴠᴀꜱ ᴘᴜᴛᴏ, ɴᴏ ᴍᴇɴᴛɪʀᴀ, ᴄᴜɪᴅᴀᴛᴇ ᴍᴜᴄʜᴏ ʏ ᴠᴜᴇʟᴠᴇ ᴘʀᴏɴᴛᴏ♥""")
			print(f"Someone left the gc")
		except Exception as e:
			print(e)

@client.event("on_text_message")
def on_text_message(data):
	if data.comId==cidy:
		ex=data.message.content
		cd=ex.split(' ')
		x=cd[0]
		c=cd[1:]
		adx=[]
		for w in cd:
			adx.append(w)
		print(adx)
		if ex:
			for i in adx:
				if len(i)<=50:
					if i[:23]=="http://aminoapps.com/p/" or i[:23]=="http://aminoapps.com/c/":
						fok=client.get_from_code(i)
						cidx=fok.path[1:fok.path.index("/")]
						if cidx!=cid:
							try:
								subclient.delete_message(chatId=data.message.chatId,messageId=data.message.messageId,asStaff=True)
								s=subclient.get_chat_thread(data.message.chatId).title
								subclient.start_chat(userId=adm,message=f"ndc://x{cid}/user/profile/{data.message.author.userId} was advertisng in {s}")
								
								subclient.send_message(chatId=data.message.chatId,message=f"<${data.message.author.nickname} don't advertise here")
								print("spotted advertiser")
							except Exception as e:
								print(e)
			if x.lower()=="!info" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="[ci]ʜᴏʟᴀ, ꜱᴏʏ ᴊᴇꜱꜱɪᴄᴀ, ᴜɴ ʙᴏᴛ ᴄʀᴇᴀᴅᴏ ᴘᴏʀ 🆃̶꯭𝗔᎒𝗞𝗨̸̸̈꒷͟𝗠̤𝗜̶ ᯥ, ᴘᴀʀᴀ ᴘᴏᴅᴇʀ ᴠᴇʀ ᴍɪꜱ ᴄᴏᴍᴀɴᴅᴏꜱ ᴇꜱᴄʀɪʙᴇ !ʜᴇʟᴘ")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!global":
				try:
					for i in c:
						mention = subclient.get_message_info(chatId=data.message.chatId, messageId=data.message.messageId).mentionUserIds
						for user in mention:
							h=subclient.get_user_info(userId=str(user)).nickname
							AID=client.get_user_info(userId=str(user)).aminoId
							d=client.get_from_code(i).objectId
							subclient.send_message(chatId=data.message.chatId,message="https://aminoapps.com/u/"+str(AID),embedTitle="Global Id",embedContent=f"{h}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!clear":
				if x.lower() not in l:
					try:
						for i in c:
							d=int(i)
							a=subclient.get_chat_messages(chatId=data.message.chatId,size=d)
							for i in a.messageId:
								subclient.delete_message(chatId=data.message.chatId,messageId=i,asStaff=True,reason="clear")
							subclient.send_message(chatId=data.message.chatId,message=f"Listo, acabo de borrar {d} sucios")
					except:
						subclient.send_message(chatId=data.message.chatId,message="[ci]ɴᴏ ᴘᴜᴇᴅᴏ ᴜᴛɪʟɪᴢᴀʀ ᴇꜱᴛᴇ ᴄᴏᴍᴀɴᴅᴏ ᴘᴏʀ Qᴜᴇ ɴᴏ ᴛᴇɴɢᴏ ʟɪᴅᴇʀ ᴏ ᴄᴜʀᴀᴅᴏʀ")
				else:
					subclient.send_message(chatId=data.message.chatId,message="Clear command is locked")
			if x.lower()=="!llock" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"Comando bloqueado{l}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!lock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.append(i)
							subclient.send_message(chatId=data.message.chatId,message=f"Unlocked {i} command")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Este comando solo es accesible para el administrador")
					except Exception as e:
						print(e)
			if x.lower()=="!unlock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.remove(i)
							subclient.send_message(chatId=data.message.chatId,message=f"Unlocked {i} command")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Este comando solo es accesible para el administrador")
					except Exception as e:
						print(e)
			if x.lower()=="!say":
				if x.lower() not in l:
					if c==[]:
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"{data.message.author.nickname}, ¡No puedo hablar a menos que escribas algo después de decir!")
						except:
							pass
					else:
						try:
							t=''
							lx='en'
							for i in c:
								t=t+i
							out=gTTS(text=t,lang="es",tld='co.in',slow=False)
							out.save("audio.mp3")
							with open("audio.mp3","rb") as f:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
							f.close()
							print(f"Info requested by {data.message.author.nickname}")
						except Exception as e:
							print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="say command is locked")
					except:
						pass
			if x.lower()=="!join":
				if c==[]:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"{data.message.author.nickname}, tienes que pegar el enlace después de unirte")
					except:
						pass
				else:
					try:
						for i in c:
							try:
								d=client.get_from_code(i).objectId
								subclient.join_chat(chatId=d)
								subclient.send_message(chatId=data.message.chatId,message="Listo, entre papi")
							except Exception as e:
								print(e)
						print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
			if x.lower()=="!vc" and c==[]:
				try:
					subclient.invite_to_vc(userId=data.message.author.userId,chatId=data.message.chatId)
					print(f"Invited {data.message.author.nickname} to vc")
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]No tengo identificación de co/anfitrión/anfitrión/personal para invitarte a vc, <$@{data.message.author.nickname}$>")
			if x.lower()=="!inviteall" and c==[]:
				if x.lower() not in l:
					try:
						h=subclient.get_all_users(start=0,size=1000).profile.userId
						m=len(h)
						for u in h:
							try:
								subclient.invite_to_chat(userId=u,chatId=data.message.chatId)
							except Exception as e:
								print(e)
								pass
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]Listo, invite {m} usuarios en total")
						print(f"invited {data.message.author.nickname} to vc")
					except Exception as e:
						print(e)
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]No tengo identificación de co/anfitrión/anfitrión/personal para invitarte a vc, <$@{data.message.author.nickname}$>")
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Inviteall command is locked")
					except:
						pass
			if x.lower()=="!pm" and c==[]:
				if x.lower() not in l:
					try:
						subclient.start_chat(userId=data.message.author.userId,message="[CI]Hola soy jessica, ¿podemos ser amigos? !")
						subclient.send_message(chatId=data.message.chatId,message=f"Check your pm <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
						print(f"invite {data.message.author.nickname} to pm")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"Pm command is locked <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="!startvc" and c==[]:
				if x.lower() not in l:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Okey papi, te llamare en 5 segundos, preparate")
						time.sleep(5)
						client.start_vc(comId=cid,chatId=data.message.chatId,joinType=1)
						#subclient.send_message(chatId=data.message.chatId,message=f"Vc started")
						print(f"VC started")
					except Exception as e:
						print(e)
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"[ic]No tengo identificación de co/anfitrión/anfitrión/personal para invitarte a vc, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"Start command is locked <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="!endlive" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="Okey papi, iniciare el live en 5 segundos")
					time.sleep(5)
					client.end_vc(comId=cid,chatId=data.message.chatId,joinType=2)
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]No tengo identificación de co/anfitrión/anfitrión/personal para invitarte a vc, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
			if x.lower()=="!online" and c==[]:
				if x.lower() not in l:
					try:
						o=""
						q=subclient.get_online_users(start=0,size=1000)
						for uid in q.profile.nickname:
							o=o+uid+"\n"
						subclient.send_message(chatId=data.message.chatId,message=f"""[c]Usuarios traviesos en linea
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
						print("done")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Members command is locked")
					except:
						pass

			if x.lower()=="!buenosdias" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"[ci]Buenos dias hermoso, ten un excelente dia, suerte en todo guapo <3<${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!seguir" and c==[]:
				try:
					subclient.follow(userId=data.message.author.userId)
					subclient.send_message(chatId=data.message.chatId,message=f"[c]mmm ya que, te comence a seguir pero no me gusta que no me dejen decidir :) <${data.message.author.nickname}$> ",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!buenasnoches" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"[ci]buenas noches, gracias por tu trabajo en el dia de hoy, espero que no vuelvas a molestarme hijo de tu ptm nwn <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!love":
				try:
					for i in c:
						msg = i + " null null "
						msg = msg.split(" ")
						msg[2] = msg[1]
						msg[1] = msg[0]
						subclient.send_message(chatId=data.message.chatId, message=f"""[c]-----------------
[c]Match ❤️  {random.randint(0,100)}%
[c]---------------""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!danza" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""
(_＼ヽ
　 ＼＼ .Λ＿Λ.
　　 ＼(　ˇωˇ)　
　　　 >　⌒ヽ
　　　/ 　 へ＼
　　 /　　/　＼＼
　　 ﾚ　ノ　　 ヽ_つ
　　/　/
　 /　/|
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
`ノ ) 　 Lﾉ
(_／""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!help" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c] J E S S I C A  Comandos
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
!join                       !global
!say                        !pm
!buenasnoches      !horadefiesta
!startvc                 !chocolate
!buenasdias          !leader
!playlist                 !inviteall
!llock                       !clear
!play                       !buenasnoches
!endlive                 !meme
!pm          !info        !vc
!chocolate             !nombre
!profilepic              !danza
!joke                       !oye
!seguir                    !coin     !clear
!online                    !lock
!love                       !gf      !unlock

[ci]J E S S I C A  TAKUMI
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!coin":
				try:
					for i in c:
						d=int(i)
						print(transaction)
						subclient.send_coins(coins=d, chatId=data.message.chatId, transactionId=transaction)
						subclient.send_message(chatId=data.message.chatId,message=f"Sent {d} coins to Host")
				except Exception as e:
					print(e)
			if x.lower()=="!buenasnoches" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"[ci]No molestes.. no mentira excelente noche mi amor <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!horadefiesta" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[ci]joder, claro que shiiii, fiesta toda la pinche nocheee, eres mi bebito fiu fiu""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!profilepic":
				try:
					t=''
					for i in c:
						t=t+i
						subclient.edit_profile(nickname=t)
						subclient.send_message(chatId=data.message.chatId,message=f"My name changed to {i}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!profilepic" and c==[]:
				try:
					info = subclient.get_message_info(chatId = data.message.chatId, messageId = data.message.messageId)
					reply_message = info.json['extensions']
					if reply_message:
						image = info.json['extensions']['replyMessage']['mediaValue']
						filename = image.split("/")[-1]
						filetype = image.split(".")[-1]
						urllib.request.urlretrieve(image, filename)
						with open(filename, 'rb') as fp:
							for i in range(1,8):
								try:
									subclient.edit_profile(icon=fp)
								except Exception as e:
									subclient.send_message(data.message.chatId, message="Profile pic changed",replyTo=data.message.messageId)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!playlist" and c==[]:
				try:
					files=os.listdir("music")
					o=""
					for f in files:
						o=o+f+"\n"
					subclient.send_message(chatId=data.message.chatId,message=f"""
[c]Descubre nuestra musica secreta 
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!gf" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[bi]eres soltero (づ｡◕‿‿◕｡)づ
[i]Estoy aquí para ti...""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!joke" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]No eres mi persona favorita""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!oye":
				try:
					subclient.send_message(chatId=data.message.chatId,message=str(random.choice(lis)),replyTo=data.message.messageId)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!play":
				if subclient.get_chat_thread(data.message.chatId).title!=None:
					mx=random.choice(os.listdir("music"))
					if x.lower() not in l:
						sounds=f"music/{mx}"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
								print(f"Info requested by {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message="command is locked")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="el comando solo funciona en pm, escriba /pm para que Jessica se una a pm")
					except:
						pass
			if x.lower()=="!meme":
				if subclient.get_chat_thread(data.message.chatId).title!=None:
					hx=random.choice(os.listdir("memes"))
					if x.lower() not in l:
						sounds=f"memes/{hx}"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="image")
								print(f"Info requested by {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message=" el comando está bloqueado")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="el comando solo funciona en pm, escriba !pm para que Jessica se una a pm")
					except:
						pass
			if x.lower()=="!leader" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="Ve y compruébalo tú mismo")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!aboutme" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[CI]Eres una buena persona, seguro que tendrás novia aquí, y si gustas podria ser yooo""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
     
     
			if x.lower()=="!chocolate" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""
╔╦╦
╠╬╬╬╣
╠╬╬╬╣ I ♥
╠╬╬╬╣ Chocolate
╚╩╩╩╝""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()