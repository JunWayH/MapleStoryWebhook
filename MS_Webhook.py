from dhooks import Webhook, Embed, File
import MS_Official
import sys

class MSWEBHOOK():
    def __init__(self):
        try:
            self.hook = Webhook('https://discordapp.com/api/webhooks/{id}/{token}')
            self.thook = Webhook('https://discordapp.com/api/webhooks/{id}/{token}')
        except ValueError as e:
            print(e)
            print('Webhook link need modify!!')
            exit()
        if MS_Official.Is_updated():
            exit()
        self.anno_dict, self.bottom_image = MS_Official.get_official_announcement()

    def send_to_discord(self):
        self.hook.send(embed=self.tune_embed_message())

    def send_to_discord_for_test(self):
        self.thook.send(embed=self.tune_embed_message())

    def tune_embed_message(self):
        embed = Embed(
            description='不定期更新! :poop:',
            color=0x1e0f3,
            timestamp='now'  # sets the timestamp to current time
            )
        
        image0 = 'https://i.imgur.com/rdm3W9t.png'
        image1 = 'https://tw.beanfun.com/maplestory/image/Board/category/72.gif'

        embed.set_author(name='近期活動公告', icon_url=image0)
        for ele in self.anno_dict.keys():
            embed.add_field(name=ele, value=self.anno_dict[ele])
        #embed.set_footer(text='Here is my footer text', icon_url=image1)
        
        embed.set_thumbnail(image1)
        embed.set_image(self.bottom_image)
        return embed


if __name__ == "__main__":
    MSW = MSWEBHOOK()
    if len(sys.argv)<2:
        MSW.send_to_discord()
    else:
        if sys.argv[1] == 't':
            MSW.send_to_discord_for_test()
        else:
            print('Wrong arg!!')
    