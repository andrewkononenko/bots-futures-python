import json
from cryptorg import Api
from jproperties import Properties

configs = Properties()
with open('secrets.properties', 'rb') as config_file:
    configs.load(config_file)

cryptorg = Api(configs.get("Key").data, configs.get("Secret").data);

""" First arg must be an array of parrams """
""" Second arg must be an array of attributes """

# bots = cryptorg.botList();
# bots_dict = json.loads(bots);
# for bot in bots_dict["data"]:
#     if bot["title"] == "Speculation":
#         bot_id = bot["id"]
#
# if bot_id is None:
#     print("No bot found by name Speculation");
#     exit()

params = {'botId': '409994', 'pairTitle': 'USDT-' + 'TRX'}
attrs = {}

print(cryptorg.updateBot(params, attrs));