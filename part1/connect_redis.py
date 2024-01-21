import redis
from redis_lru import RedisLRU
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# ----- Redis local -----

redis_user = config.get('RED', 'user')
redis_pass = config.get('RED', 'password')
redis_port = config.get('RED', 'port')
redis_server = config.get('RED', 'server')
redis_db = config.get('RED', 'db_name')

# ----- redis  CLOUD -----

# redis_user = config.get('RED_CLOUD', 'user')
# redis_pass = config.get('RED_CLOUD', 'password')
# redis_port = config.get('RED_CLOUD', 'port')
# redis_server = config.get('RED_CLOUD', 'server')
# redis_db = config.get('RED_CLOUD', 'db_name')

# ----- redis inline -----
# redis_user = None
# redis_pass = None
# redis_port = 6369
# redis_server = "localhost"
# redis_db = 0


# ----- redis connect -----
redis_client = redis.Redis(
    host=redis_server,
    port=redis_port,
    db=redis_db,
    username=redis_user,
    password=redis_pass
    )

cache = RedisLRU(redis_client)