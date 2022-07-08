import pymysql
from game_dicobot.pt import token
import discord , asyncio
import random as r

client = discord.Client()

member = [] # 게임하기 리스트 

#학습하기는 딕션너리로 처리할거 
#학습 아웃풋  # 수정 , 삭제 , 학습 , 읽기 (@학습하기 리스트 출력 )
studydic = {}

###############################################################
#db설정 mysql 



###############################################################

# 봇이 접속하면 아래의 함수 실행 
@client.event
async def on_ready():
    print(f'{client.user} online!')
    
    
@client.event
async def on_message(message): # 채팅명령어 
    if message.author == client.user:
        return
    #봇의 모든 명령어 출력     
    if message.content == (";명령어"):
        embed = discord.Embed(title= "명령어 모음")
        embed.add_field(name="컨텐츠용 명령어" , value= ";게임참가, ;게임나가기, ;러시안룰렛 " , inline=False)
        embed.add_field(name="학교관련 명령어" , value= ";학식/학교이름(패치예정)" , inline=False)
        embed.add_field(name="학습하기 도움말" , value=";학습하기/내가 해줄 말/내가 들을 말 , ;학습하기수정/내가 해줄 말/내가 들을 말 , ;학습하기제거/내가 해줄 말 " , inline=False)
        await message.channel.send(embed=embed)

###################################################################################################
    #러시안 롤렛
    if message.content == ";러시안룰렛":
        set_member = set(member) #중복이 되면 안됨으로 Set형을 써서 리스트를 만듬 그걸가지고 롤렛을 돌리는 거임 
        set_member = list(set_member)
        if member == []:
            await message.channel.send("알림 : 멤버 리스트가 비어있습니다.")
        else: 
            if message.author.name in set_member:
               r.shuffle(set_member)
               r.shuffle(member)
               await message.channel.send("이번에 걸린 사람은 ???????")
               await message.channel.send("3")
               await message.channel.send("2")
               await message.channel.send("1")
               await message.channel.send("!!!!!!!!!")
               await message.channel.send(set_member[0])
            else:
                await message.channel.send("먼저 @게임참가 를 해주세요")
    

    #학습하기 
    mslst = list(message.content.split("/"))
    if len(mslst) == 3 :
        if mslst[0] == ";학습하기":
           studydic[str(mslst[1])] = str(mslst[2])
           mslst = []
           await message.channel.send('단어장이 추가되었습니다.')
        elif mslst[0] == ";학습하기수정": # 학습하기 수정 
            studydic[str(mslst[1])] = str(mslst[2])
            mslst = []
            await message.channel.send("단어장이 수정되었습니다.")
        else:
            await message.channel.send("@학습하기 명령어에 오류가 있습니다 ")
            await message.channel.send("@학습하기/내가 해줄 말/내가 들을 말 ")
    elif len(mslst) == 2 :
        if mslst[0] == ";학습하기제거": # 학습하기 제거 
            studydic.pop(str(mslst[1]))
            mslst = []
            
            await message.channel.send("단어_삭제가 완료되었습니다.")
    #학습한거 토대로 말하는 것 
    if message.content in list(studydic.keys()):
        await message.channel.send(studydic[message.content])


    #게임 참가
    if message.content == (";게임참가"): # 게임 참가 
        name = message.author.name
        member.append(name)
        await message.channel.send(name +'님이 게임에 참가했습니다.')
    if message.content == ";게임나가기": # 게임 나가기 
        if message.author.name in member:
            name = message.author.name
            member.remove(name)
            await message.channel.send(name +'님이 게임에서 나갔습니다.')
        else:
            await message.channel.send("참가도 안했는데 뭘 나가요.....")

########################################################################################
### 학교관련 명령어 
    #@학식/학교이름 

    # 이건 사이트로 가는게 아니라 바로 뜨게끔 연구하기
        
########################################################################################
    #리스트 확인 
    if message.content == ";리스트확인":
        set_member = set(member) 
        set_member = list(set_member)
        
        await message.channel.send("게임 리스트 :") 
        await message.channel.send(set_member)
        await message.channel.send("봇 단어장 : ")
        await message.channel.send(studydic)

    #얘도 그냥 테스트용 
    if message.content == "ping":
        await message.channel.send("pong")

    #############################################################################################

    
 
   

#실행 
client.run(token)


