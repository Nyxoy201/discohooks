<div align="center">

# DiscoHooks 
</div>

## Projet Description 
DiscoHooks is a simple python library to use discord webhooks.

## Lib Features 
- Send Message To Webhook
- Send File To Webhook
- Send Embed To Webhook
- Delete Webhook
- Customize Webhook
- Get Webhook Informations
- Use multiple webhooks

## Installing
The requests library is required.

```
# Install Requests Lib
pip install reqests

#Install Discohooks Lib
pip install discohooks
```

## How To Use

### To use the library without embed :

First, import the library : 
```python
from discohooks import Webhook
```

1. **Send Message :**
```python
from discohooks import Webhook

hook = Webhook(["webhook_url_1", "webhook_url_2"])
# Even if you're using only one webhook, still use the [ ]

hook.send(content="Hello Word!")
```

2. **Delete Webhook :**
```python
from discohooks import Webhook

hook = Webhook(["webhook_url_1", "webhook_url_2"])
# Even if you're using only one webhook, still use the [ ]

hook.delete()
```

3. **Customize Webhook :**
```python
from discohooks import Webhook

hook = Webhook(["webhook_url_1", "webhook_url_2"])
# Even if you're using only one webhook, still use the [ ]

hook.customize(name="WEBHOOK_NAME", avatar="AVATAR_URL")
# If you want, you can choose to take only one of the two.
```

4. **Get Webhook Informations :**
```python
from discohooks import Webhook

hook = Webhook(["webhook_url_1", "webhook_url_2"])
# Even if you're using only one webhook, still use the [ ]

info = hook.info(["name", "id"])
print(info)
```
These are just two examples; here are all the retrievable pieces of information: 
`application_id, avatar, channel_id, guild_id, id, name, type, token, url`

5. **Send File :**
```python
from discohooks import Webhook

hook = Webhook(["webhook_url_1", "webhook_url_2"])
# Even if you're using only one webhook, still use the [ ]

hook.send_file("YOUR_FILE")
```


### To use the library witht embed :
First, import the library : 
```python
from discohooks import Webhook, Embed

embed = Embed(title='Title', description='Description', color=0xFF5733)
embed.add_field(name='Field 1', value='Value 1', inline=False)
embed.add_field(name='Field 2', value='Value 2', inline=True)
embed.set_thumbnail(url='https://example.com/thumbnail.jpg')
embed.set_image(url='https://example.com/image.jpg')
embed.set_footer(text='Footer text', icon_url='https://example.com/footer_icon.jpg')

hook.send(embed=embed)
# Here's everything you can put in your webhook's embed.
```

