# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20496814"))
    API_HASH = getenv("API_HASH", "a87c1094edd18650e5dfee0f2bc78bda")
    BOT_TOKEN = getenv("BOT_TOKEN", "7903275622:AAGBo4Mb31w0hNa9HCg5qmvsUszFsamoDeE")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002318921089")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "6276113288").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://nhmovies9:nhmovies9@cluster0.lp65c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
