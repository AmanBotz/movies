import datetime
import pytz
from motor.motor_asyncio import AsyncIOMotorClient
from info import (
    IS_VERIFY, AUTH_CHANNEL, SHORTENER_WEBSITE3, SHORTENER_API3, THREE_VERIFY_GAP,
    LINK_MODE, FILE_CAPTION, TUTORIAL, TUTORIAL2, TUTORIAL3, DATABASE_NAME, DATABASE_URI,
    DATABASE_URI2, IMDB, IMDB_TEMPLATE, PROTECT_CONTENT, AUTO_DELETE, SPELL_CHECK, AUTO_FILTER,
    LOG_VR_CHANNEL, SHORTENER_WEBSITE, SHORTENER_API, SHORTENER_WEBSITE2, SHORTENER_API2, TWO_VERIFY_GAP
)

# Initialize the database client and select the database
client = AsyncIOMotorClient(DATABASE_URI)
mydb = client[DATABASE_NAME]

class Database:
    # Default settings
    default = {
        'spell_check': SPELL_CHECK,
        'auto_filter': AUTO_FILTER,
        'file_secure': PROTECT_CONTENT,
        'auto_delete': AUTO_DELETE,
        'template': IMDB_TEMPLATE,
        'caption': FILE_CAPTION,
        'tutorial': TUTORIAL,
        'tutorial_two': TUTORIAL2,
        'tutorial_three': TUTORIAL3,
        'shortner': SHORTENER_WEBSITE,
        'api': SHORTENER_API,
        'shortner_two': SHORTENER_WEBSITE2,
        'api_two': SHORTENER_API2,
        'log': LOG_VR_CHANNEL,
        'imdb': IMDB,
        'link': LINK_MODE,
        'is_verify': IS_VERIFY,
        'verify_time': TWO_VERIFY_GAP,
        'shortner_three': SHORTENER_WEBSITE3,
        'api_three': SHORTENER_API3,
        'fsub_id': AUTH_CHANNEL,
        'third_verify_time': THREE_VERIFY_GAP
    }

    def __init__(self):
        self.col = mydb.users
        self.grp = mydb.groups
        self.misc = mydb.misc
        self.verify_id = mydb.verify_id
        self.users = mydb.uersz
        self.req = mydb.requests

    # --- User and Group Helpers ---

    def new_user(self, id, name):
        return {
            "id": id,
            "name": name,
            "ban_status": {
                "is_banned": False,
                "ban_reason": ""
            }
        }

    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({"id": int(user_id)})

    # --- Chat Helpers ---

    def new_group(self, id, title):
        return {
            "id": id,
            "title": title,
            "chat_status": {
                "is_disabled": False,
                "reason": ""
            }
        }

    async def add_chat(self, chat, title):
        group = self.new_group(chat, title)
        await self.grp.insert_one(group)

    async def get_chat(self, chat):
        chat_obj = await self.grp.find_one({"id": int(chat)})
        return False if not chat_obj else chat_obj.get("chat_status")

    async def update_settings(self, id, settings):
        await self.grp.update_one({"id": int(id)}, {"$set": {"settings": settings}})

    async def total_chat_count(self):
        count = await self.grp.count_documents({})
        return count

    async def get_all_chats(self):
        return self.grp.find({})

    async def get_db_size(self):
        stats = await mydb.command("dbstats")
        return stats.get('dataSize')

    # --- Join Request Helpers ---

    async def find_join_req(self, id):
        return bool(await self.req.find_one({"id": id}))

    async def add_join_req(self, id):
        await self.req.insert_one({"id": id})

    async def del_join_req(self):
        await self.req.drop()

    async def get_banned(self):
        users_cursor = self.col.find({"ban_status.is_banned": True})
        chats_cursor = self.grp.find({"chat_status.is_disabled": True})
        b_chats = [chat["id"] async for chat in chats_cursor]
        b_users = [user["id"] async for user in users_cursor]
        return b_users, b_chats

    # --- Not-Copy Verification Helpers ---
    # This collection holds timestamps for different verification steps.
    
    async def get_notcopy_user(self, user_id):
        """Retrieve or create a document for verification timestamps."""
        user_id = int(user_id)
        user = await self.misc.find_one({"user_id": user_id})
        ist_timezone = pytz.timezone("Asia/Kolkata")
        if not user:
            # Initialize with default timestamps far in the past
            res = {
                "user_id": user_id,
                "last_verified": datetime.datetime(2020, 5, 17, 0, 0, 0, tzinfo=ist_timezone),
                "second_time_verified": datetime.datetime(2019, 5, 17, 0, 0, 0, tzinfo=ist_timezone),
                "third_time_verified": datetime.datetime(2018, 5, 17, 0, 0, 0, tzinfo=ist_timezone)
            }
            await self.misc.insert_one(res)
            return res
        return user

    async def update_notcopy_user(self, user_id, value: dict):
        user_id = int(user_id)
        myquery = {"user_id": user_id}
        newvalues = {"$set": value}
        return await self.misc.update_one(myquery, newvalues)

    # --- Verification Functions ---
    # The following functions now use a fixed 8-hour window for validity.

    async def is_user_verified(self, user_id):
        """
        First verification check using 'last_verified'.
        Returns True if the difference between now and 'last_verified' is less than 8 hours.
        """
        user = await self.get_notcopy_user(user_id)
        try:
            pastDate = user["last_verified"]
        except Exception:
            user = await self.get_notcopy_user(user_id)
            pastDate = user["last_verified"]

        ist_timezone = pytz.timezone("Asia/Kolkata")
        pastDate = pastDate.astimezone(ist_timezone)
        current_time = datetime.datetime.now(tz=ist_timezone)
        return (current_time - pastDate) < datetime.timedelta(hours=8)

    async def user_verified(self, user_id):
        """
        Second verification check using 'second_time_verified'.
        Returns True if the difference between now and 'second_time_verified' is less than 8 hours.
        """
        user = await self.get_notcopy_user(user_id)
        try:
            pastDate = user["second_time_verified"]
        except Exception:
            user = await self.get_notcopy_user(user_id)
            pastDate = user["second_time_verified"]

        ist_timezone = pytz.timezone("Asia/Kolkata")
        pastDate = pastDate.astimezone(ist_timezone)
        current_time = datetime.datetime.now(tz=ist_timezone)
        return (current_time - pastDate) < datetime.timedelta(hours=8)

    async def use_second_shortener(self, user_id, time=28800):
        """
        Determines if the user may proceed to use the second shortener.
        If the second verification timestamp is not set, it is initialized.
        Then, if the first verification (last_verified) has exceeded 8 hours,
        it checks if the second verification timestamp is older than the first.
        (Customize the business logic as per your exact requirements.)
        """
        user = await self.get_notcopy_user(user_id)
        ist_timezone = pytz.timezone("Asia/Kolkata")
        if not user.get("second_time_verified") or user["second_time_verified"] is None:
            await self.update_notcopy_user(user_id, {"second_time_verified": datetime.datetime.now(tz=ist_timezone)})
            user = await self.get_notcopy_user(user_id)
        if await self.is_user_verified(user_id):  # Assuming first verification is valid
            pastDate = user["last_verified"].astimezone(ist_timezone)
            current_time = datetime.datetime.now(tz=ist_timezone)
            time_difference = current_time - pastDate
            if time_difference >= datetime.timedelta(hours=8):
                second_time = user["second_time_verified"].astimezone(ist_timezone)
                # Business logic: allow second shortener only if the second verification is older than the first
                return second_time < pastDate
        return False

    async def use_third_shortener(self, user_id, time=28800):
        """
        Determines if the user may proceed to use the third shortener.
        If the third verification timestamp is not set, it is initialized.
        Then, if the second verification (second_time_verified) has exceeded 8 hours,
        it checks if the third verification timestamp is older than the second.
        """
        user = await self.get_notcopy_user(user_id)
        ist_timezone = pytz.timezone("Asia/Kolkata")
        if not user.get("third_time_verified") or user["third_time_verified"] is None:
            await self.update_notcopy_user(user_id, {"third_time_verified": datetime.datetime.now(tz=ist_timezone)})
            user = await self.get_notcopy_user(user_id)
        if await self.user_verified(user_id):  # Assuming second verification is valid
            pastDate = user["second_time_verified"].astimezone(ist_timezone)
            current_time = datetime.datetime.now(tz=ist_timezone)
            time_difference = current_time - pastDate
            if time_difference >= datetime.timedelta(hours=8):
                third_time = user["third_time_verified"].astimezone(ist_timezone)
                # Business logic: allow third shortener only if the third verification is older than the second
                return third_time < pastDate
        return False

    # --- Additional User Functions for Premium Access ---

    async def get_user(self, user_id):
        user_data = await self.users.find_one({"id": user_id})
        return user_data

    async def update_user(self, user_data):
        await self.users.update_one({"id": user_data["id"]}, {"$set": user_data}, upsert=True)

    async def has_premium_access(self, user_id):
        user_data = await self.get_user(user_id)
        if user_data:
            expiry_time = user_data.get("expiry_time")
            if expiry_time is None:
                return False
            elif isinstance(expiry_time, datetime.datetime) and datetime.datetime.now() <= expiry_time:
                return True
            else:
                await self.users.update_one({"id": user_id}, {"$set": {"expiry_time": None}})
        return False

    async def update_one(self, filter_query, update_data):
        try:
            result = await self.users.update_one(filter_query, update_data)
            return result.matched_count == 1
        except Exception as e:
            print(f"Error updating document: {e}")
            return False

    async def get_expired(self, current_time):
        expired_users = []
        cursor = self.users.find({"expiry_time": {"$lt": current_time}})
        async for user in cursor:
            expired_users.append(user)
        return expired_users

    async def remove_premium_access(self, user_id):
        return await self.update_one({"id": user_id}, {"$set": {"expiry_time": None}})

# Instantiate the Database object
db = Database()