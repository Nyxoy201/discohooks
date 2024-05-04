import requests
import base64

class Webhook:
    def __init__(self, webhook_urls):
        self.webhook_urls = webhook_urls

    def send(self, content=None, embed=None):
        payload = {}
        if content:
            payload['content'] = content
        if embed:
            payload['embeds'] = [embed.to_dict()]
        for webhook_url in self.webhook_urls:
            response = requests.post(webhook_url, json=payload)
            if response.status_code != 204:
                print(f"Failed to send message to {webhook_url}: {response.text}")
            else:
                pass

    def delete(self):
        for webhook_url in self.webhook_urls:
            response = requests.delete(webhook_url)
            if response.status_code == 204:
                pass
            else:
                print(f"Failed to delete webhook {webhook_url}: {response.text}")

    def customize(self, name=None, avatar=None):
        payload = {}
        if name:
            payload['name'] = name
        if avatar:
            image_data = requests.get(avatar).content
            avatar_base64 = base64.b64encode(image_data).decode('utf-8')
            payload['avatar'] = f"data:image/jpeg;base64,{avatar_base64}"
        for webhook_url in self.webhook_urls:
            response = requests.patch(webhook_url, json=payload)
            if response.status_code == 200:
                pass
            else:
                print(f"Failed to customize webhook {webhook_url}: {response.text}")

    def info(self, args=None):
        infos = []
        for webhook_url in self.webhook_urls:
            response = requests.get(webhook_url)
            if response.status_code == 200:
                info = response.json()
                if args:
                    info = {arg: info[arg] for arg in args if arg in info}
                infos.append(info)
            else:
                print(f"Failed to get webhook info from {webhook_url}: {response.text}")
        return infos


    def send_file(self, file_path):
        for webhook_url in self.webhook_urls:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(webhook_url, files=files)
                if response.status_code != 200:
                    print(f"Échec d'envoi du fichier à {webhook_url}: {response.text}")
                else:
                    pass

class Embed:
    def __init__(self, title=None, description=None, color=None):
        self.title = title
        self.description = description
        self.color = color
        self.fields = []
        self.thumbnail = None
        self.image = None
        self.footer = None

    def add_field(self, name, value, inline=False):
        self.fields.append({'name': name, 'value': value, 'inline': inline})

    def set_thumbnail(self, url):
        self.thumbnail = {'url': url}

    def set_image(self, url):
        self.image = {'url': url}

    def set_footer(self, text, icon_url=None):
        self.footer = {'text': text, 'icon_url': icon_url}

    def to_dict(self):
        embed_dict = {
            'title': self.title,
            'description': self.description,
            'color': self.color,
            'fields': self.fields
        }
        if self.thumbnail:
            embed_dict['thumbnail'] = self.thumbnail
        if self.image:
            embed_dict['image'] = self.image
        if self.footer:
            embed_dict['footer'] = self.footer
        return embed_dict
