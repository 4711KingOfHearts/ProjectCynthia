import asyncio
import websockets
import requests
import json

class SDClient:

    wss = None
    uri = None
    login_uri = None
    username = None
    password = None

    @classmethod
    async def create(cls, username, password, uri):
        self = SDClient()
        self.username = username
        self.password = password
        self.uri = uri
        self.wss = await websockets.connect(self.uri)
        self.login_uri = "https://play.pokemonshowdown.com/action.php"

        return self

    async def login(self):
        client_id, challstr = await self._get_challstr()
        if self.password:
            response = requests.post(
                self.login_uri,
                data = {
                    'act' : 'login',
                    'name' : self.username,
                    'pass' : self.password,
                    'challstr' : "|".join([client_id, challstr])
                }
            )

        else:
            response = requests.post(
                self.login_uri,
                data = {
                    'act' : 'getassertion',
                    'name' : self.username,
                    'challstr' : "|".join([client_id, challstr])
                }
            )

        if response.status_code == 200:
            if self.password:
                response_json = json.loads(response.text[1:])
                assertion = response_json.get('assertion')
            else:
                assertion = response.text

            message = ["/trn " + self.username + ",0," + assertion]
            await self._send_message("", message)

#        else:
#            raise LoginError("Could not log-in")

    async def find_game(self, ladder, team):
#        message = [ "/utm {}".format(team) , "/search {}".format(ladder)]
#        await self._send_message('', message)
        message1 = ["/utm {}".format(team)]
        await self._send_message('', message1)
        message2 = ["/search {}".format(ladder)]
        await self._send_message('', message2)

    async def _get_challstr(self):
        while True:
            message = await self._receive_message()
            split_message = message.split('|')
            if split_message[1] == 'challstr':
                return split_message[2], split_message[3]

    async def _send_message(self, room, message_list):
        message = room + "|" + "|".join(message_list)
        await self.wss.send(message)

    async def _receive_message(self):
        message = await self.wss.recv()
        return message
